"""
SAMA Rulebook acquisition: manifest PDFs from tree slugs + circular indexes, download.

Policy:
  - Visit every tree slug; collect rulebook file_store PDFs on each page.
  - Visit circular index pages; follow main-content links to each circular; download its PDF.
  - If a downloadable PDF exists -> fetch it (any language). No PDF -> skip.
  - Output: scanner-sama-docs/ (deduped by stem or URL basename).

Outputs (reports/rulebook/):
  manifest.json, acquisition_plan.json, acquisition_report.md, downloaded_files.txt

Usage:
  python tools/rulebook_acquire.py                    # full manifest + fetch
  python tools/rulebook_acquire.py --manifest-only
  python tools/rulebook_acquire.py --fetch-only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
TREE_JSON = ROOT / "reports" / "rulebook" / "tree.json"
OUT_DIR = ROOT / "reports" / "rulebook"
DOCS_DIR = ROOT / "scanner-sama-docs"
CORPUS_DIR = ROOT / "corpus" / "markdown"
LEGACY_PDF_DIR = Path(r"C:\Users\memeo\Downloads\SAMA_DOCS")
BASE = "https://rulebook.sama.gov.sa"

STEM_RE = re.compile(r"(SAMA_(?:EN|AR)_\d+_VER\d+(?:_\d+)?)", re.I)
DOC_NO_RE = re.compile(r"No:\s*([^\n|]+)", re.I)
STATUS_RE = re.compile(r"Status:\s*([^\n|]+)", re.I)
USER_AGENT = "SAMA-KB-Rulebook-Acquire/1.0"

IN_FORCE_STATUSES = {"in-force", "in force"}


def is_in_force(status: Optional[str]) -> bool:
    if not status:
        return False
    normalized = status.strip().lower().split("\t")[0].split("  ")[0].strip()
    return normalized in IN_FORCE_STATUSES


def parse_status(text: str) -> Optional[str]:
    m = STATUS_RE.search(text)
    if not m:
        return None
    return m.group(1).strip()[:80]

SECTOR_NAV_SLUGS = {
    "/en/laws-and-implementing-regulations",
    "/en/all-financial-institutions",
    "/en/banking-sector-0",
    "/en/finance-sector-0",
    "/en/payment-systems-and-payment-services-providers",
    "/en/money-exchange-sector-0",
    "/en/credit-bureaus",
    "/en/regulatory-sandbox",
    "/en/sama-circulars",
}


@dataclass
class PdfRecord:
    file_id: str
    stem: Optional[str]
    pdf_url: str
    filename: str
    link_label: str = ""
    source_slug: str = ""
    source_title: str = ""
    tree_path: str = ""
    source_kind: str = "tree"
    document_no: Optional[str] = None
    status: Optional[str] = None
    local_path: Optional[str] = None
    sha256: Optional[str] = None
    action: str = "pending"
    error: Optional[str] = None


def abs_url(href: str) -> str:
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return BASE + href
    if href.startswith("en/"):
        return BASE + "/" + href
    return BASE + "/" + href.lstrip("/")


def norm_slug(href: str) -> str:
    return href.split("?")[0].rstrip("/")


def file_id_for(url: str, stem: Optional[str]) -> str:
    if stem:
        return stem.upper()
    name = urllib.parse.unquote(url.split("/")[-1].split("?")[0])
    clean = re.sub(r"[^\w.\-]+", "_", name)[:120]
    return clean or hashlib.sha256(url.encode()).hexdigest()[:16]


def filename_for(rec: PdfRecord) -> str:
    if rec.stem:
        return f"{rec.stem}.pdf"
    return rec.filename if rec.filename.lower().endswith(".pdf") else f"{rec.filename}.pdf"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_tree() -> Tuple[dict, Dict[str, str]]:
    data = json.loads(TREE_JSON.read_text(encoding="utf-8"))
    paths: Dict[str, str] = {}

    def walk(node: dict, prefix: str) -> None:
        slug = node.get("slug") or ""
        title = node.get("title") or ""
        path = f"{prefix} / {title}" if prefix else title
        if slug.startswith("/en/"):
            paths[slug] = path
        for ch in node.get("children") or []:
            walk(ch, path if slug else prefix)

    walk(data.get("tree") or {}, "")
    return data, paths


def collect_visit_slugs(tree_data: dict) -> List[Tuple[str, str]]:
    _, paths = load_tree()
    slug_index = tree_data.get("slug_index") or {}
    out: List[Tuple[str, str]] = []
    seen: Set[str] = set()
    for slug in sorted(slug_index.keys()):
        if not slug.startswith("/en/"):
            continue
        if slug in seen:
            continue
        seen.add(slug)
        meta = slug_index[slug]
        title = meta.get("title", slug)
        out.append((slug, paths.get(slug, title)))
    return out


def collect_circular_index_slugs(tree_data: dict) -> List[Tuple[str, str]]:
    _, paths = load_tree()
    slug_index = tree_data.get("slug_index") or {}
    out: List[Tuple[str, str]] = []
    for slug, meta in sorted(slug_index.items()):
        if not slug.startswith("/en/"):
            continue
        if meta.get("children", 0) != 0:
            continue
        if not slug.endswith("-circulars") and "circulars" not in slug.lower():
            continue
        title = meta.get("title", slug)
        out.append((slug, paths.get(slug, title)))
    return out


def pdfs_from_eval(
    data: dict,
    slug: str,
    tree_path: str,
    title: str,
    kind: str,
    require_in_force: bool = False,
) -> List[PdfRecord]:
    text = data.get("text", "")
    document_no = None
    status = parse_status(text)
    if require_in_force and not is_in_force(status):
        return []

    m = DOC_NO_RE.search(text)
    if m:
        document_no = m.group(1).strip()[:80]

    records: List[PdfRecord] = []
    seen_urls: Set[str] = set()
    for item in data.get("pdfs", []):
        url = abs_url(item.get("href", ""))
        if "file_store" not in url and "rulebook.sama.gov.sa" not in url:
            continue
        if url in seen_urls:
            continue
        seen_urls.add(url)
        stem_m = STEM_RE.search(url)
        stem = stem_m.group(1).upper() if stem_m else None
        basename = urllib.parse.unquote(url.split("/")[-1].split("?")[0])
        records.append(
            PdfRecord(
                file_id=file_id_for(url, stem),
                stem=stem,
                pdf_url=url,
                filename=basename,
                link_label=(item.get("text") or "")[:120],
                source_slug=slug,
                source_title=title,
                tree_path=tree_path,
                source_kind=kind,
                document_no=document_no,
                status=status,
            )
        )
    return records


def extract_page_pdfs(
    page,
    slug: str,
    tree_path: str,
    title: str,
    kind: str = "tree",
    require_in_force: bool = False,
) -> List[PdfRecord]:
    try:
        page.wait_for_load_state("domcontentloaded", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(500)

    data = page.evaluate(
        """() => {
        const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
        const text = (main.innerText || '').slice(0, 12000);
        const pdfs = [];
        document.querySelectorAll('a[href]').forEach(el => {
            const h = el.getAttribute('href') || '';
            const t = (el.innerText || '').trim();
            if (h.includes('file_store') && h.includes('.pdf')) {
                pdfs.push({ href: h, text: t });
            }
        });
        return { text, pdfs };
    }"""
    )
    return pdfs_from_eval(data, slug, tree_path, title, kind, require_in_force)


def extract_circular_links(page, index_slug: str) -> List[Tuple[str, str]]:
    index_slug = norm_slug(index_slug)
    rows = page.evaluate(
        """(indexSlug) => {
        const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
        const seen = new Set();
        const out = [];
        main.querySelectorAll('a[href]').forEach(a => {
            let h = a.getAttribute('href') || '';
            if (h.startsWith('en/')) h = '/' + h;
            if (!h.startsWith('/en/')) return;
            h = h.split('?')[0].replace(/\\/$/, '');
            const t = (a.innerText || '').trim().replace(/\\s+/g, ' ');
            if (!t || t.length < 3) return;
            if (h.includes('entiresection') || h.includes('file_store')) return;
            if (h.includes('/revisions/')) return;
            if (h === indexSlug) return;
            if (h.endsWith('-circulars')) return;
            if (!h.includes('/node/') && t.length < 10) return;
            if (seen.has(h)) return;
            seen.add(h);
            out.push({ href: h, title: t.slice(0, 200) });
        });
        return out;
    }""",
        index_slug,
    )
    out: List[Tuple[str, str]] = []
    for row in rows:
        slug = norm_slug(row["href"])
        if slug in SECTOR_NAV_SLUGS:
            continue
        out.append((slug, row["title"]))
    return out


def merge_records(by_id: Dict[str, PdfRecord], found: List[PdfRecord]) -> None:
    for rec in found:
        existing = by_id.get(rec.file_id)
        if not existing:
            by_id[rec.file_id] = rec
        elif not existing.tree_path and rec.tree_path:
            existing.tree_path = rec.tree_path


def build_manifest(max_pages: int, headless: bool) -> Tuple[List[PdfRecord], dict]:
    from playwright.sync_api import sync_playwright

    tree_data, _ = load_tree()
    visits = collect_visit_slugs(tree_data)
    circular_indexes = collect_circular_index_slugs(tree_data)
    if max_pages > 0:
        visits = visits[:max_pages]

    by_id: Dict[str, PdfRecord] = {}
    pages_scanned = 0
    pages_with_pdf = 0
    circular_pages = 0
    circular_with_pdf = 0
    circular_links_found = 0
    circular_skipped_not_in_force = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.set_default_timeout(30000)

        total = len(visits)
        for i, (slug, tree_path) in enumerate(visits, 1):
            title = tree_path.split(" / ")[-1] if tree_path else slug
            print(f"[tree {i}/{total}] {title[:70]}", flush=True)
            try:
                page.goto(abs_url(slug), wait_until="domcontentloaded")
                found = extract_page_pdfs(page, slug, tree_path, title, "tree")
                pages_scanned += 1
                if found:
                    pages_with_pdf += 1
                merge_records(by_id, found)
            except Exception as exc:
                print(f"  ERR {slug}: {exc}", flush=True)
            page.wait_for_timeout(200)

        print(f"\n=== Circular indexes ({len(circular_indexes)}) ===", flush=True)
        seen_circular_slugs: Set[str] = set()
        circular_targets: List[Tuple[str, str, str]] = []

        for idx, (index_slug, index_path) in enumerate(circular_indexes, 1):
            index_title = index_path.split(" / ")[-1] if index_path else index_slug
            print(f"[index {idx}/{len(circular_indexes)}] {index_title}", flush=True)
            try:
                page.goto(abs_url(index_slug), wait_until="domcontentloaded")
                page.wait_for_timeout(800)
                # Index page: discover links only (do not download index bundle PDFs).
                for cslug, ctitle in extract_circular_links(page, index_slug):
                    if cslug in seen_circular_slugs:
                        continue
                    seen_circular_slugs.add(cslug)
                    circular_links_found += 1
                    cpath = f"{index_path} / {ctitle}" if index_path else ctitle
                    circular_targets.append((cslug, cpath, ctitle))
            except Exception as exc:
                print(f"  ERR index {index_slug}: {exc}", flush=True)

        print(f"\n=== Circular pages ({len(circular_targets)}) ===", flush=True)
        for i, (cslug, cpath, ctitle) in enumerate(circular_targets, 1):
            if i % 25 == 0 or i == 1:
                print(f"[circular {i}/{len(circular_targets)}] {ctitle[:70]}", flush=True)
            try:
                page.goto(abs_url(cslug), wait_until="domcontentloaded")
                page.wait_for_timeout(400)
                data = page.evaluate(
                    """() => {
                    const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
                    const text = (main.innerText || '').slice(0, 12000);
                    const pdfs = [];
                    document.querySelectorAll('a[href]').forEach(el => {
                        const h = el.getAttribute('href') || '';
                        const t = (el.innerText || '').trim();
                        if (h.includes('file_store') && h.includes('.pdf')) {
                            pdfs.push({ href: h, text: t });
                        }
                    });
                    return { text, pdfs };
                }"""
                )
                status = parse_status(data.get("text", ""))
                circular_pages += 1
                if not is_in_force(status):
                    circular_skipped_not_in_force += 1
                    continue
                found = pdfs_from_eval(data, cslug, cpath, ctitle, "circular_page", require_in_force=False)
                if found:
                    circular_with_pdf += 1
                    merge_records(by_id, found)
            except Exception as exc:
                print(f"  ERR circular {cslug}: {exc}", flush=True)
            page.wait_for_timeout(150)

        browser.close()

    stats = {
        "pages_scanned": pages_scanned,
        "pages_with_pdf": pages_with_pdf,
        "unique_pdfs": len(by_id),
        "circular_indexes": len(circular_indexes),
        "circular_links_found": circular_links_found,
        "circular_pages_scanned": circular_pages,
        "circular_pages_with_pdf": circular_with_pdf,
        "circular_skipped_not_in_force": circular_skipped_not_in_force,
    }
    return list(by_id.values()), stats


def load_local_stems() -> Tuple[Set[str], Set[str]]:
    corpus, legacy = set(), set()
    for p in CORPUS_DIR.glob("*.md"):
        m = STEM_RE.search(p.stem)
        if m:
            corpus.add(m.group(1).upper())
    if LEGACY_PDF_DIR.exists():
        for p in LEGACY_PDF_DIR.glob("*.pdf"):
            m = STEM_RE.search(p.stem)
            if m:
                legacy.add(m.group(1).upper())
    return corpus, legacy


def plan_downloads(records: List[PdfRecord]) -> List[PdfRecord]:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for rec in records:
        dest = DOCS_DIR / filename_for(rec)
        rec.local_path = str(dest.relative_to(ROOT)).replace("\\", "/")
        rec.action = "download"
        if dest.exists():
            rec.sha256 = sha256_file(dest)
            rec.action = "skip_exists"
    return records


def safe_url(url: str) -> str:
    """Encode spaces/control chars in URL paths (rulebook occasionally has ' (1).pdf')."""
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parts.path, safe="/%:@")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def download_record(rec: PdfRecord, timeout: int = 120) -> PdfRecord:
    dest = DOCS_DIR / filename_for(rec)
    if rec.action == "skip_exists" and dest.exists():
        return rec
    url = safe_url(rec.pdf_url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        dest.write_bytes(data)
        rec.sha256 = hashlib.sha256(data).hexdigest()
        rec.action = "downloaded"
        rec.error = None
    except Exception as exc:
        rec.action = "failed"
        rec.error = str(exc)[:200]
    return rec


def fetch_all(records: List[PdfRecord]) -> List[PdfRecord]:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    to_get = [r for r in records if r.action in ("download", "pending")]
    total = len(to_get)
    for i, rec in enumerate(to_get, 1):
        print(f"fetch [{i}/{total}] {filename_for(rec)}", flush=True)
        download_record(rec)
        time.sleep(0.12)
    return records


def write_report(records: List[PdfRecord], stats: dict, elapsed: float) -> None:
    corpus, legacy = load_local_stems()
    downloaded = sorted([r for r in records if r.action == "downloaded"], key=lambda r: filename_for(r))
    failed = sorted([r for r in records if r.action == "failed"], key=lambda r: filename_for(r))
    skipped = [r for r in records if r.action == "skip_exists"]
    stems = {r.stem for r in records if r.stem}

    by_kind: Dict[str, int] = {}
    for r in records:
        by_kind[r.source_kind] = by_kind.get(r.source_kind, 0) + 1

    lines = [
        "# Rulebook acquisition report",
        "",
        f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Elapsed: {elapsed:.1f}s",
        f"> Output folder: `{DOCS_DIR.relative_to(ROOT).as_posix()}/`",
        "",
        "## Scan",
        "",
        f"- Tree pages scanned: {stats.get('pages_scanned', 0)}",
        f"- Circular index pages: {stats.get('circular_indexes', 0)}",
        f"- Circular detail pages: {stats.get('circular_pages_scanned', 0)}",
        f"- Circular links discovered: {stats.get('circular_links_found', 0)}",
        f"- Circular skipped (not In-Force): {stats.get('circular_skipped_not_in_force', 0)}",
        f"- Pages with ≥1 PDF: {stats.get('pages_with_pdf', 0)}",
        f"- Unique PDFs in manifest: {len(records)}",
        "",
        "## Fetch",
        "",
        f"- Downloaded this run: {len(downloaded)}",
        f"- Already on disk (skipped): {len(skipped)}",
        f"- Failed: {len(failed)}",
        "",
        "## vs local corpus",
        "",
        f"- Stems in manifest: {len(stems)}",
        f"- Also in corpus/markdown: {len(stems & corpus)}",
        f"- Also in legacy SAMA_DOCS: {len(stems & legacy)}",
        f"- New stems (not in corpus): {len(stems - corpus)}",
        "",
        "## By source kind",
        "",
    ]
    for k, v in sorted(by_kind.items()):
        lines.append(f"- `{k}`: {v}")
    lines.append("")

    lines += ["## All downloaded files (this run)", ""]
    if downloaded:
        for r in downloaded:
            lines.append(f"- `{filename_for(r)}` — {r.source_title[:70]} ({r.source_kind})")
    else:
        lines.append("_None this run._")
    lines.append("")

    all_on_disk = sorted(DOCS_DIR.glob("*.pdf"), key=lambda p: p.name.lower())
    lines += [f"## All PDFs on disk ({len(all_on_disk)} files)", ""]
    for p in all_on_disk:
        lines.append(f"- `{p.name}`")
    lines.append("")

    if failed:
        lines += ["## Failed downloads", ""]
        for r in failed:
            lines.append(f"- `{filename_for(r)}` — {r.error}")
        lines.append("")

    (OUT_DIR / "acquisition_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    all_on_disk = sorted(DOCS_DIR.glob("*.pdf"), key=lambda p: p.name.lower())
    file_lines = [f"# All PDFs in scanner-sama-docs — {len(all_on_disk)} files", ""]
    for p in all_on_disk:
        file_lines.append(p.name)
    (OUT_DIR / "downloaded_files.txt").write_text("\n".join(file_lines) + "\n", encoding="utf-8")


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def run_manifest(max_pages: int, headless: bool) -> Tuple[List[PdfRecord], dict]:
    if not TREE_JSON.exists():
        raise SystemExit(f"Missing {TREE_JSON} — run rulebook_scanner.py first.")
    records, stats = build_manifest(max_pages, headless)
    planned = plan_downloads(records)
    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "docs_dir": str(DOCS_DIR.relative_to(ROOT)),
        "stats": stats,
        "pdfs": [asdict(r) for r in planned],
    }
    save_json(OUT_DIR / "manifest.json", payload)
    save_json(
        OUT_DIR / "acquisition_plan.json",
        {
            "generated": payload["generated"],
            "to_download": [asdict(r) for r in planned if r.action == "download"],
            "skip_exists": [asdict(r) for r in planned if r.action == "skip_exists"],
        },
    )
    return planned, stats


def run_fetch_from_manifest() -> Tuple[List[PdfRecord], dict]:
    path = OUT_DIR / "manifest.json"
    if not path.exists():
        raise SystemExit(f"Missing {path} — run with --manifest-only first.")
    data = json.loads(path.read_text(encoding="utf-8"))
    records = [PdfRecord(**item) for item in data.get("pdfs", [])]
    stats = data.get("stats", {})
    planned = plan_downloads(records)
    fetch_all(planned)
    return planned, stats


def main() -> int:
    ap = argparse.ArgumentParser(description="SAMA Rulebook PDF acquisition")
    ap.add_argument("--manifest-only", action="store_true")
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--max-pages", type=int, default=0, help="Cap tree pages (0=all)")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    if args.fetch_only:
        records, stats = run_fetch_from_manifest()
    else:
        records, stats = run_manifest(args.max_pages, headless=not args.headed)
        if not args.manifest_only:
            fetch_all(records)

    elapsed = time.time() - t0
    save_json(
        OUT_DIR / "manifest.json",
        {
            "generated": datetime.now(timezone.utc).isoformat(),
            "docs_dir": str(DOCS_DIR.relative_to(ROOT)),
            "stats": stats,
            "pdfs": [asdict(r) for r in records],
        },
    )
    write_report(records, stats, elapsed)

    n_dl = sum(1 for r in records if r.action == "downloaded")
    n_skip = sum(1 for r in records if r.action == "skip_exists")
    n_fail = sum(1 for r in records if r.action == "failed")
    print(
        f"\nDone: {len(records)} PDFs in manifest | downloaded={n_dl} skip={n_skip} failed={n_fail} | {elapsed:.1f}s",
        flush=True,
    )
    print(f"Docs: {DOCS_DIR}", flush=True)
    print(f"Report: {OUT_DIR / 'acquisition_report.md'}", flush=True)
    print(f"File list: {OUT_DIR / 'downloaded_files.txt'}", flush=True)
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
