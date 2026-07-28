"""
Unified PDF → markdown preprocess for SAMAKnowledgeBase.

Replaces ad-hoc ingest_new_pdfs.py + fix_conversion.py.

Routing (automatic, no hard-coded stem lists):
  1. Bidi-aware text extract from PDF
  2. If thin (chars/page < threshold) OR high isolated-Arabic rate → OCR @ 200 DPI
  3. Else keep bidi text

On replace: archive existing corpus .md under archive/conversion-backup/.

Usage:
  python tools/preprocess_pdfs.py --pdf-dir scanner-sama-docs
  python tools/preprocess_pdfs.py --stems SAMA_EN_791_VER1 SAMA_EN_4725_VER1
  python tools/preprocess_pdfs.py --from-plan reports/rulebook/comparison.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set

import fitz
import pytesseract
from PIL import Image

try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
except ImportError:  # pragma: no cover
    reshape = None  # type: ignore
    get_display = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF_DIR = ROOT / "scanner-sama-docs"
CORPUS_MD = ROOT / "corpus" / "markdown"
IMAGES = ROOT / "assets" / "page-images"
BACKUP_DIR = ROOT / "archive" / "conversion-backup"
REPORTS_DIR = ROOT / "reports" / "conversion"
TESSDATA = Path(__file__).resolve().parent / "tessdata"
TESSERACT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
OCR_TMP = ROOT / "archive" / "ocr-tmp"

DPI = 200
OCR_LANG = "eng+ara"
THIN_CPP = 400
ISOLATED_AR_OCR = 0.12

STEM_RE = re.compile(r"(SAMA_(?:EN|AR)_\d+_VER\d+(?:_\d+)?)", re.I)
ARABIC_RE = re.compile(r"[\u0600-\u06FF]+")


def setup_tess() -> None:
    if not TESSERACT.exists():
        raise SystemExit(f"Tesseract missing: {TESSERACT}")
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT)
    if TESSDATA.exists():
        os.environ["TESSDATA_PREFIX"] = str(TESSDATA)


def backup_file(path: Path) -> Optional[Path]:
    if not path.exists():
        return None
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = BACKUP_DIR / f"{path.stem}.{stamp}{path.suffix}"
    shutil.copy2(path, dest)
    return dest


def fix_arabic_runs(text: str) -> str:
    if reshape is None or get_display is None:
        return text

    def _fix(m: re.Match) -> str:
        chunk = m.group(0)
        reversed_chunk = chunk[::-1]
        try:
            return get_display(reshape(reversed_chunk))
        except Exception:
            return reversed_chunk

    return ARABIC_RE.sub(_fix, text)


def extract_text_bidi(page: fitz.Page) -> str:
    blocks = page.get_text("blocks") or []
    text_blocks = [b for b in blocks if len(b) >= 5 and (b[4] or "").strip()]
    text_blocks.sort(key=lambda b: (round(b[1], 1), round(b[0], 1)))
    lines = []
    for b in text_blocks:
        t = (b[4] or "").replace("\x00", "").strip()
        if t:
            lines.append(fix_arabic_runs(t))
    return "\n".join(lines).strip()


def arabic_isolated_rate(text: str) -> float:
    tokens = re.findall(r"\S+", text)
    ar = [t for t in tokens if ARABIC_RE.search(t)]
    if not ar:
        return 0.0
    short = sum(1 for t in ar if len(ARABIC_RE.findall(t)) <= 2 and len(t) <= 3)
    return short / len(ar)


def sanitize_text(text: str) -> str:
    """Drop nulls and lone UTF-16 surrogates so UTF-8 write never crashes."""
    if not text:
        return ""
    return "".join(
        "\ufffd" if 0xD800 <= ord(ch) <= 0xDFFF else ch for ch in text.replace("\x00", "")
    )

def pages_to_md(fname: str, pages: List[str]) -> str:
    parts = [f"# {fname}", ""]
    for i, body in enumerate(pages, 1):
        parts += [f"## Page {i}", "", sanitize_text(body or ""), ""]
    return "\n".join(parts).rstrip() + "\n"


def write_md(stem: str, fname: str, pages: List[str]) -> Path:
    CORPUS_MD.mkdir(parents=True, exist_ok=True)
    out = CORPUS_MD / f"{stem}.md"
    backup_file(out)
    out.write_text(pages_to_md(fname, pages), encoding="utf-8", errors="replace")
    return out


def clear_stem_images(stem: str) -> None:
    if not IMAGES.exists():
        return
    pat = re.compile(rf"^{re.escape(stem)}_page_\d+\.png$", re.I)
    for p in list(IMAGES.iterdir()):
        if p.is_file() and pat.match(p.name):
            p.unlink()


def ocr_page(page: fitz.Page, img_path: Path) -> str:
    img_path.parent.mkdir(parents=True, exist_ok=True)
    pix = page.get_pixmap(dpi=DPI)
    pix.save(str(img_path))
    with Image.open(img_path) as im:
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        text = pytesseract.image_to_string(im, lang=OCR_LANG)
    return (text or "").strip()


def process_pdf(pdf: Path) -> dict:
    raw_stem = pdf.stem
    m = STEM_RE.search(raw_stem)
    stem = m.group(1).upper() if m else raw_stem
    try:
        doc = fitz.open(pdf)
    except Exception as exc:
        return {"stem": stem, "ok": False, "error": f"open_failed: {exc}"[:200]}
    try:
        bidi_pages = [extract_text_bidi(page) for page in doc]
        joined = "\n".join(bidi_pages)
        cpp = len(joined) / max(doc.page_count, 1)
        iso = arabic_isolated_rate(joined)
        use_ocr = cpp < THIN_CPP or iso >= ISOLATED_AR_OCR

        if use_ocr:
            print(
                f"[{stem}] OCR route (pages={doc.page_count}, cpp={cpp:.0f}, iso={iso:.2f})",
                flush=True,
            )
            clear_stem_images(stem)
            ocr_pages: List[str] = []
            for i, page in enumerate(doc, 1):
                print(f"  OCR {i}/{doc.page_count} ...", flush=True)
                ocr_pages.append(ocr_page(page, IMAGES / f"{stem}_page_{i}.png"))
            write_md(stem, pdf.name, ocr_pages)
            return {
                "stem": stem,
                "ok": True,
                "route": "ocr",
                "pages": doc.page_count,
                "md_chars": sum(len(p) for p in ocr_pages),
                "cpp_text": round(cpp, 1),
                "isolated_rate": round(iso, 3),
            }

        print(
            f"[{stem}] text/bidi route (pages={doc.page_count}, cpp={cpp:.0f}, iso={iso:.2f})",
            flush=True,
        )
        write_md(stem, pdf.name, bidi_pages)
        return {
            "stem": stem,
            "ok": True,
            "route": "bidi",
            "pages": doc.page_count,
            "md_chars": sum(len(p) for p in bidi_pages),
            "cpp_text": round(cpp, 1),
            "isolated_rate": round(iso, 3),
        }
    except Exception as exc:
        return {"stem": stem, "ok": False, "error": str(exc)[:200]}
    finally:
        doc.close()


def resolve_pdfs(pdf_dir: Path, stems: Optional[List[str]]) -> List[Path]:
    if stems:
        out: List[Path] = []
        for s in stems:
            stem = s.replace(".pdf", "")
            matches = list(pdf_dir.glob(f"{stem}.pdf"))
            if not matches:
                # allow non-SAMA filenames
                matches = list(pdf_dir.glob(stem)) if Path(stem).suffix else []
            if matches:
                out.extend(matches)
            else:
                print(f"[missing] {stem}.pdf in {pdf_dir}", flush=True)
        return out
    return sorted(pdf_dir.glob("*.pdf"))


def stems_from_plan(plan_path: Path) -> List[str]:
    data = json.loads(plan_path.read_text(encoding="utf-8"))
    items = data.get("items") or data.get("to_preprocess") or []
    out: List[str] = []
    for it in items:
        status = (it.get("status") or "").upper()
        if status in ("NEW", "UPDATED", "DOWNLOAD", "PENDING"):
            stem = it.get("stem") or it.get("file_id") or ""
            if stem:
                out.append(stem)
            elif it.get("filename"):
                out.append(Path(it["filename"]).stem)
    # also accept action queues
    for key in ("new", "updated", "to_preprocess"):
        for it in data.get(key) or []:
            if isinstance(it, str):
                out.append(it.replace(".pdf", ""))
            elif isinstance(it, dict):
                out.append((it.get("stem") or Path(it.get("filename", "")).stem).replace(".pdf", ""))
    # dedupe preserve order
    seen: Set[str] = set()
    uniq: List[str] = []
    for s in out:
        if s and s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def write_preprocess_report(results: List[dict], elapsed: float) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ok = sum(1 for r in results if r.get("ok"))
    lines = [
        "# Preprocess report",
        "",
        f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Elapsed: {elapsed:.1f}s",
        f"> OK: {ok}/{len(results)}",
        "",
        "| Stem | OK | Route | Pages | MD chars | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        notes = r.get("error") or f"cpp={r.get('cpp_text')}, iso={r.get('isolated_rate')}"
        lines.append(
            f"| `{r.get('stem')}` | {r.get('ok')} | {r.get('route', '-')} | "
            f"{r.get('pages', '-')} | {r.get('md_chars', '-')} | {notes} |"
        )
    lines.append("")
    out = REPORTS_DIR / "preprocess_report.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS_DIR / "preprocess_results.json").write_text(
        json.dumps(
            {
                "generated": datetime.now(timezone.utc).isoformat(),
                "ok": ok,
                "total": len(results),
                "results": results,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Unified PDF→MD preprocess")
    ap.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    ap.add_argument("--stems", nargs="*", default=None, help="Limit to these stems")
    ap.add_argument("--from-plan", type=Path, default=None, help="comparison.json / plan with NEW/UPDATED")
    ap.add_argument("--max", type=int, default=0, help="Cap PDFs processed (0=all)")
    ap.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip PDFs that already have corpus/markdown/<stem>.md",
    )
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass

    setup_tess()
    CORPUS_MD.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    stems = args.stems
    if args.from_plan:
        stems = stems_from_plan(args.from_plan)
        if not stems:
            print("No NEW/UPDATED stems in plan — nothing to preprocess.", flush=True)
            write_preprocess_report([], 0.0)
            return 0

    pdfs = resolve_pdfs(args.pdf_dir, stems)
    if args.skip_existing:
        kept = []
        for pdf in pdfs:
            m = STEM_RE.search(pdf.stem)
            stem = m.group(1).upper() if m else pdf.stem
            if (CORPUS_MD / f"{stem}.md").exists():
                print(f"[skip existing] {stem}.md", flush=True)
                continue
            kept.append(pdf)
        pdfs = kept
    if args.max > 0:
        pdfs = pdfs[: args.max]
    if not pdfs:
        print("No PDFs left to process.", flush=True)
        write_preprocess_report([], 0.0)
        return 0

    t0 = time.time()
    results: List[dict] = []
    for i, pdf in enumerate(pdfs, 1):
        print(f"\n=== [{i}/{len(pdfs)}] {pdf.name} ===", flush=True)
        results.append(process_pdf(pdf))

    elapsed = time.time() - t0
    report = write_preprocess_report(results, elapsed)
    ok = sum(1 for r in results if r.get("ok"))
    print(f"\nDone: {ok}/{len(results)} | report: {report}", flush=True)
    print(f"Corpus markdown count: {len(list(CORPUS_MD.glob('*.md')))}", flush=True)
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
