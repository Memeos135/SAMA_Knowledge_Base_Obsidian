"""
Assess PDF → .md / PNG conversion quality for SAMAKnowledgeBase.

Scores each PDF under scanner-sama-docs (or --pdf-dir) against corpus artifacts:
  - structural fidelity (page counts, density, routing)
  - text integrity (coverage, Arabic/bidi, tokens, garbage)
  - image quality (DPI proxy, dimensions)
  - near-duplicate MD pairs

Usage:
  python tools/assess_conversion.py
  python tools/assess_conversion.py --pdf-dir scanner-sama-docs
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import fitz
from PIL import Image

# ---------------------------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------------------------

# Project root (parent of tools/)
ROOT = Path(__file__).resolve().parent.parent
CORPUS_MD_DIR = ROOT / "corpus" / "markdown"
IMAGES_DIR = ROOT / "assets" / "page-images"
REPORTS_DIR = ROOT / "reports" / "conversion"
DEFAULT_PDF_DIR = ROOT / "scanner-sama-docs"

ARABIC_RE = re.compile(r"[\u0600-\u06FF]")
# Isolated Arabic letters / short fragments often appear when bidi/glyphs break
ISOLATED_AR_RE = re.compile(r"(?<!\S)[\u0600-\u06FF]{1,2}(?!\S)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# Circular / reference-like numbers seen in SAMA docs
CIRCULAR_RE = re.compile(
    r"(?:\(?\d{3,}(?:[./]\d+)*\)?|(?:Art(?:icle)?\.?\s*\d+|المادة\s*\d+))",
    re.IGNORECASE,
)
PAGE_HDR_RE = re.compile(r"^## Page (\d+)\s*$", re.MULTILINE)

# Heuristic thresholds
THIN_CHARS_PER_PAGE = 400          # below → suspicious for a "text" route
EMPTY_PAGE_CHARS = 20
COVERAGE_WARN = 0.85
COVERAGE_FAIL = 0.60
ARABIC_SHARE_WARN = 0.15           # if Arabic share high, check bidi
ISOLATED_AR_RATE_WARN = 0.08       # isolated short Arabic tokens / Arabic tokens
DPI_EXPECT = 72
DPI_OCR_TARGET = 200
A4_INCH = (8.27, 11.69)            # for DPI estimate from pixel size


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class PageStats:
    page: int
    chars: int
    empty: bool


@dataclass
class DocReport:
    stem: str
    pdf_path: str
    route: str  # md | images | missing
    artifact_path: str = ""
    pdf_pages: int = 0
    artifact_pages: int = 0
    page_count_match: bool = False
    pdf_text_chars: int = 0
    artifact_chars: int = 0
    coverage: float | None = None
    chars_per_page: float = 0.0
    empty_pages: int = 0
    thin: bool = False
    misrouted_suspect: bool = False
    arabic_share: float = 0.0
    isolated_arabic_rate: float = 0.0
    arabic_bidi_risk: str = "n/a"  # low | medium | high | n/a
    token_retention: float | None = None
    tokens_pdf: int = 0
    tokens_kept: int = 0
    garbage_ratio: float = 0.0
    image_count: int = 0
    image_median_dpi: float | None = None
    image_median_px: str = ""
    flags: list[str] = field(default_factory=list)
    grade: str = "N/A"
    score: float = 0.0
    page_stats: list[dict] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def stem_of_pdf(path: Path) -> str:
    return path.stem


def md_path_for(stem: str) -> Path | None:
    p = CORPUS_MD_DIR / f"{stem}.md"
    return p if p.exists() else None


def image_paths_for(stem: str) -> list[Path]:
    if not IMAGES_DIR.exists():
        return []
    # Exact stem_page_N.png only (avoid document* matching document2*)
    pages: dict[int, Path] = {}
    pattern = re.compile(rf"^{re.escape(stem)}_page_(\d+)\.png$", re.IGNORECASE)
    for p in IMAGES_DIR.iterdir():
        if not p.is_file():
            continue
        m = pattern.match(p.name)
        if m:
            pages[int(m.group(1))] = p
    return [pages[i] for i in sorted(pages)]


def parse_md_pages(text: str) -> list[tuple[int, str]]:
    matches = list(PAGE_HDR_RE.finditer(text))
    if not matches:
        body = text
        # strip leading H1
        body = re.sub(r"^# .*\n+", "", body, count=1)
        return [(1, body.strip())] if body.strip() else []
    pages: list[tuple[int, str]] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        pages.append((int(m.group(1)), text[start:end].strip()))
    return pages


def pdf_page_texts(doc: fitz.Document) -> list[str]:
    out = []
    for page in doc:
        out.append(page.get_text("text") or "")
    return out


def extract_tokens(text: str) -> set[str]:
    tokens: set[str] = set()
    for m in EMAIL_RE.finditer(text):
        tokens.add(m.group(0).lower())
    for m in CIRCULAR_RE.finditer(text):
        t = re.sub(r"\s+", " ", m.group(0)).strip().lower()
        if len(t) >= 3:
            tokens.add(t)
    # Stable English identifiers / codes
    for m in re.finditer(r"\b[A-Z]{2,}(?:[-_/][A-Z0-9]+){1,}\b", text):
        tokens.add(m.group(0).lower())
    return tokens


def arabic_metrics(text: str) -> tuple[float, float]:
    if not text:
        return 0.0, 0.0
    letters = re.findall(r"\S+", text)
    if not letters:
        return 0.0, 0.0
    ar_tokens = [t for t in letters if ARABIC_RE.search(t)]
    arabic_share = len(ar_tokens) / len(letters)
    if not ar_tokens:
        return 0.0, 0.0
    isolated = sum(1 for t in ar_tokens if ISOLATED_AR_RE.fullmatch(t))
    # also count very short Arabic words (1–2 letters) as risk signal
    short = sum(1 for t in ar_tokens if len(ARABIC_RE.findall(t)) <= 2 and len(t) <= 3)
    isolated_rate = max(isolated, short) / len(ar_tokens)
    return arabic_share, isolated_rate


def garbage_ratio(text: str) -> float:
    if not text.strip():
        return 0.0
    # Replacement chars, private-use, odd control-ish leftovers
    bad = len(re.findall(r"[\ufffd\u0000-\u0008\u000b\u000c\u000e-\u001f]", text))
    # Lone Latin letters sandwiched as noise in Arabic-heavy lines is hard; use
    # ratio of non-printable / weird symbols among non-space chars
    nons = re.sub(r"\s+", "", text)
    if not nons:
        return 0.0
    weird = len(re.findall(r"[^\w\u0600-\u06FF.,;:!?()\[\]{}\"'%/\\@#$&*+=<>|~`^-]", nons, re.UNICODE))
    return min(1.0, (bad + weird * 0.25) / len(nons))


def estimate_dpi(width_px: int, height_px: int, page_rect: fitz.Rect | None) -> float:
    if page_rect and page_rect.width > 0 and page_rect.height > 0:
        # PDF points: 72 pt = 1 inch
        w_in = page_rect.width / 72.0
        h_in = page_rect.height / 72.0
        if w_in > 0 and h_in > 0:
            return round((width_px / w_in + height_px / h_in) / 2.0, 1)
    # Assume A4 portrait fallback
    return round((width_px / A4_INCH[0] + height_px / A4_INCH[1]) / 2.0, 1)


def median(vals: list[float]) -> float | None:
    if not vals:
        return None
    s = sorted(vals)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def grade_from_score(score: float, route: str) -> str:
    if route == "missing":
        return "F"
    if score >= 0.85:
        return "A"
    if score >= 0.70:
        return "B"
    if score >= 0.55:
        return "C"
    if score >= 0.40:
        return "D"
    return "F"


# ---------------------------------------------------------------------------
# Per-document assessment
# ---------------------------------------------------------------------------

def assess_md(stem: str, pdf_path: Path, md_path: Path) -> DocReport:
    report = DocReport(
        stem=stem,
        pdf_path=str(pdf_path),
        route="md",
        artifact_path=str(md_path),
    )
    doc = fitz.open(pdf_path)
    try:
        pdf_texts = pdf_page_texts(doc)
        report.pdf_pages = len(pdf_texts)
        pdf_full = "\n".join(pdf_texts)
        report.pdf_text_chars = sum(len(t.strip()) for t in pdf_texts)

        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        pages = parse_md_pages(md_text)
        report.artifact_pages = len(pages)
        report.page_count_match = report.artifact_pages == report.pdf_pages
        if not report.page_count_match:
            report.flags.append(
                f"page_count_mismatch:pdf={report.pdf_pages},md={report.artifact_pages}"
            )

        page_stats: list[PageStats] = []
        art_chars = 0
        empty = 0
        for num, body in pages:
            c = len(body.strip())
            art_chars += c
            is_empty = c <= EMPTY_PAGE_CHARS
            if is_empty:
                empty += 1
            page_stats.append(PageStats(page=num, chars=c, empty=is_empty))
        report.artifact_chars = art_chars
        report.empty_pages = empty
        report.chars_per_page = art_chars / max(report.artifact_pages, 1)
        report.page_stats = [asdict(p) for p in page_stats]

        ocr_enriched = False
        if report.pdf_text_chars > 0:
            report.coverage = min(1.5, report.artifact_chars / report.pdf_text_chars)
            pdf_cpp = report.pdf_text_chars / max(report.pdf_pages, 1)
            # OCR/enrichment: PDF text layer thin but artifact dense -> not a coverage failure
            ocr_enriched = pdf_cpp < THIN_CHARS_PER_PAGE and report.chars_per_page >= THIN_CHARS_PER_PAGE
            if ocr_enriched:
                report.flags.append("ocr_enriched_vs_thin_pdf_text_layer")
                report.coverage = 1.0
            elif report.coverage < COVERAGE_FAIL:
                report.flags.append(f"coverage_fail:{report.coverage:.2f}")
            elif report.coverage < COVERAGE_WARN:
                report.flags.append(f"coverage_warn:{report.coverage:.2f}")
        else:
            report.coverage = None
            report.flags.append("pdf_has_no_text_layer")
            if report.chars_per_page >= THIN_CHARS_PER_PAGE:
                report.flags.append("ocr_or_manual_text_present")
                ocr_enriched = True
            else:
                report.misrouted_suspect = True

        report.thin = report.chars_per_page < THIN_CHARS_PER_PAGE
        if report.thin:
            report.flags.append(f"thin_text:{report.chars_per_page:.0f}_chars/page")
            pdf_cpp = report.pdf_text_chars / max(report.pdf_pages, 1)
            if pdf_cpp < THIN_CHARS_PER_PAGE:
                report.misrouted_suspect = True
                report.flags.append("misrouted_suspect:should_be_image_or_ocr")
        else:
            report.misrouted_suspect = False

        if empty:
            report.flags.append(f"empty_pages:{empty}")

        ar_share, iso_rate = arabic_metrics(md_text)
        report.arabic_share = round(ar_share, 3)
        report.isolated_arabic_rate = round(iso_rate, 3)
        if ar_share >= ARABIC_SHARE_WARN:
            if iso_rate >= 0.20 or (iso_rate >= ISOLATED_AR_RATE_WARN and ar_share > 0.3):
                report.arabic_bidi_risk = "high"
                report.flags.append(f"arabic_bidi_high:isolated_rate={iso_rate:.2f}")
            elif iso_rate >= ISOLATED_AR_RATE_WARN:
                report.arabic_bidi_risk = "medium"
                report.flags.append(f"arabic_bidi_medium:isolated_rate={iso_rate:.2f}")
            else:
                report.arabic_bidi_risk = "low"
        else:
            report.arabic_bidi_risk = "n/a"

        pdf_tokens = extract_tokens(pdf_full)
        md_tokens = extract_tokens(md_text)
        report.tokens_pdf = len(pdf_tokens)
        if pdf_tokens and not ocr_enriched:
            kept = pdf_tokens & md_tokens
            report.tokens_kept = len(kept)
            report.token_retention = len(kept) / len(pdf_tokens)
            if report.token_retention < 0.7:
                report.flags.append(f"token_retention_low:{report.token_retention:.2f}")
        elif ocr_enriched:
            report.token_retention = None
            report.tokens_kept = 0
            report.flags.append("token_retention_skipped_ocr_enriched")
        else:
            report.token_retention = None

        report.garbage_ratio = round(garbage_ratio(md_text), 4)
        if report.garbage_ratio > 0.05:
            report.flags.append(f"garbage_ratio:{report.garbage_ratio:.3f}")

        # Score (0-1)
        score = 1.0
        if not report.page_count_match:
            score -= 0.25
        if ocr_enriched:
            if report.chars_per_page < THIN_CHARS_PER_PAGE:
                score -= 0.25
        elif report.coverage is not None:
            if report.coverage < COVERAGE_FAIL:
                score -= 0.30
            elif report.coverage < COVERAGE_WARN:
                score -= 0.12
            if report.coverage > 1.15:
                score -= 0.05
        else:
            score -= 0.35
        if report.thin:
            score -= 0.15
        if report.misrouted_suspect:
            score -= 0.20
        if report.arabic_bidi_risk == "high":
            score -= 0.25
        elif report.arabic_bidi_risk == "medium":
            score -= 0.12
        if report.token_retention is not None and report.token_retention < 0.7:
            score -= 0.10
        if report.empty_pages:
            score -= min(0.15, 0.02 * report.empty_pages)
        if report.garbage_ratio > 0.05:
            score -= 0.08
        report.score = max(0.0, round(score, 3))
        report.grade = grade_from_score(report.score, report.route)
        return report
    finally:
        doc.close()


def assess_images(stem: str, pdf_path: Path, images: list[Path]) -> DocReport:
    report = DocReport(
        stem=stem,
        pdf_path=str(pdf_path),
        route="images",
        artifact_path=str(IMAGES_DIR),
        image_count=len(images),
    )
    doc = fitz.open(pdf_path)
    try:
        report.pdf_pages = doc.page_count
        pdf_texts = pdf_page_texts(doc)
        report.pdf_text_chars = sum(len(t.strip()) for t in pdf_texts)
        report.artifact_pages = len(images)
        report.page_count_match = report.artifact_pages == report.pdf_pages
        if not report.page_count_match:
            report.flags.append(
                f"page_count_mismatch:pdf={report.pdf_pages},png={report.artifact_pages}"
            )

        # If PDF actually has substantial text, images-only was the wrong route
        pdf_cpp = report.pdf_text_chars / max(report.pdf_pages, 1)
        if pdf_cpp >= THIN_CHARS_PER_PAGE:
            report.misrouted_suspect = True
            report.flags.append(
                f"misrouted_suspect:pdf_has_text_layer:{pdf_cpp:.0f}_chars/page"
            )

        dpis: list[float] = []
        sizes: list[tuple[int, int]] = []
        for i, img_path in enumerate(images):
            with Image.open(img_path) as im:
                w, h = im.size
            sizes.append((w, h))
            page_rect = doc[i].rect if i < doc.page_count else None
            dpis.append(estimate_dpi(w, h, page_rect))

        med_dpi = median(dpis)
        report.image_median_dpi = med_dpi
        if sizes:
            mw = int(median([float(s[0]) for s in sizes]) or 0)
            mh = int(median([float(s[1]) for s in sizes]) or 0)
            report.image_median_px = f"{mw}x{mh}"

        if med_dpi is not None:
            if med_dpi < 100:
                report.flags.append(f"low_dpi:{med_dpi:.0f}_(ocr_target_{DPI_OCR_TARGET})")
            elif med_dpi < DPI_OCR_TARGET:
                report.flags.append(f"dpi_ok_for_vision_weak_for_ocr:{med_dpi:.0f}")

        # Score
        score = 1.0
        if not report.page_count_match:
            score -= 0.30
        if report.misrouted_suspect:
            score -= 0.15
        if med_dpi is not None:
            if med_dpi < 90:
                score -= 0.20
            elif med_dpi < DPI_OCR_TARGET:
                score -= 0.08
        if report.image_count == 0:
            score = 0.0
        report.score = max(0.0, round(score, 3))
        report.grade = grade_from_score(report.score, report.route)
        # Image path has no MD text metrics
        report.coverage = None
        report.token_retention = None
        return report
    finally:
        doc.close()


def assess_missing(stem: str, pdf_path: Path) -> DocReport:
    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:
        return DocReport(
            stem=stem,
            pdf_path=str(pdf_path),
            route="missing",
            flags=[f"pdf_open_failed:{exc}"[:80]],
            grade="F",
            score=0.0,
        )
    try:
        pages = doc.page_count
        chars = sum(len((p.get_text("text") or "").strip()) for p in doc)
    finally:
        doc.close()
    return DocReport(
        stem=stem,
        pdf_path=str(pdf_path),
        route="missing",
        pdf_pages=pages,
        pdf_text_chars=chars,
        flags=["no_md_or_images_found"],
        grade="F",
        score=0.0,
    )


# ---------------------------------------------------------------------------
# Corpus-level: near-duplicates among MD outputs
# ---------------------------------------------------------------------------

def md_fingerprint(text: str) -> str:
    # Normalize whitespace for comparison
    norm = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha1(norm.encode("utf-8", errors="replace")).hexdigest()


def jaccard_shingles(a: str, b: str, k: int = 12) -> float:
    def shingles(s: str) -> set[str]:
        s = re.sub(r"\s+", " ", s).lower()
        if len(s) < k:
            return {s} if s else set()
        return {s[i : i + k] for i in range(len(s) - k + 1)}

    sa, sb = shingles(a), shingles(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def find_near_duplicates(md_files: list[Path], threshold: float = 0.90) -> list[dict]:
    texts = {p: p.read_text(encoding="utf-8", errors="replace") for p in md_files}
    pairs = []
    paths = list(texts)
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            sim = jaccard_shingles(texts[paths[i]], texts[paths[j]])
            identical = md_fingerprint(texts[paths[i]]) == md_fingerprint(texts[paths[j]])
            if identical or sim >= threshold:
                pairs.append(
                    {
                        "a": paths[i].name,
                        "b": paths[j].name,
                        "similarity": round(sim, 3),
                        "identical": identical,
                    }
                )
    return pairs


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def render_markdown(reports: list[DocReport], dupes: list[dict], pdf_dir: Path) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    by_grade = defaultdict(int)
    for r in reports:
        by_grade[r.grade] += 1
    avg = sum(r.score for r in reports) / max(len(reports), 1)
    md_n = sum(1 for r in reports if r.route == "md")
    img_n = sum(1 for r in reports if r.route == "images")
    miss_n = sum(1 for r in reports if r.route == "missing")
    flagged = [r for r in reports if r.flags]

    lines: list[str] = []
    lines.append("# Conversion Quality Assessment")
    lines.append("")
    lines.append(f"> Generated: {now}")
    lines.append(f"> PDF source: `{pdf_dir}`")
    lines.append(f"> Project root: `{ROOT}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| PDFs assessed | {len(reports)} |")
    lines.append(f"| Routed to `.md` | {md_n} |")
    lines.append(f"| Routed to `images/` | {img_n} |")
    lines.append(f"| Missing artifacts | {miss_n} |")
    lines.append(f"| Mean score | {avg:.3f} |")
    lines.append(
        f"| Grades | "
        + ", ".join(f"{g}:{by_grade[g]}" for g in ["A", "B", "C", "D", "F"] if by_grade[g])
        + " |"
    )
    lines.append(f"| Docs with flags | {len(flagged)} |")
    lines.append(f"| Near-duplicate MD pairs | {len(dupes)} |")
    lines.append("")

    lines.append("## Grade legend")
    lines.append("")
    lines.append("- **A** (>=0.85): structurally sound, good coverage")
    lines.append("- **B** (>=0.70): usable, minor issues")
    lines.append("- **C** (>=0.55): significant issues (thin text, mild Arabic breakage, DPI)")
    lines.append("- **D** (>=0.40): poor fidelity - re-extract recommended")
    lines.append("- **F** (<0.40): failed / missing / misrouted")
    lines.append("")

    lines.append("## Per-document scores")
    lines.append("")
    lines.append(
        "| Stem | Route | Grade | Score | PDF pp | Art pp | "
        "Coverage | chars/pp | Empty | AR bidi | Tokens | Flags |"
    )
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|")
    for r in sorted(reports, key=lambda x: (x.grade, -x.score, x.stem)):
        cov = f"{r.coverage:.2f}" if r.coverage is not None else "-"
        tok = (
            f"{r.token_retention:.2f}"
            if r.token_retention is not None
            else "-"
        )
        flags = "; ".join(r.flags) if r.flags else "-"
        if len(flags) > 80:
            flags = flags[:77] + "..."
        cpp = f"{r.chars_per_page:.0f}" if r.route == "md" else (
            f"dpi~{r.image_median_dpi:.0f}" if r.image_median_dpi else "-"
        )
        lines.append(
            f"| `{r.stem}` | {r.route} | **{r.grade}** | {r.score:.2f} | "
            f"{r.pdf_pages} | {r.artifact_pages} | {cov} | {cpp} | "
            f"{r.empty_pages} | {r.arabic_bidi_risk} | {tok} | {flags} |"
        )
    lines.append("")

    if dupes:
        lines.append("## Near-duplicate Markdown pairs")
        lines.append("")
        lines.append("| A | B | Similarity | Identical? |")
        lines.append("|---|---|---:|---|")
        for d in dupes:
            lines.append(
                f"| `{d['a']}` | `{d['b']}` | {d['similarity']:.3f} | "
                f"{'yes' if d['identical'] else 'no'} |"
            )
        lines.append("")

    lines.append("## Priority actions")
    lines.append("")
    clean_actions: list[str] = []
    for r in sorted(reports, key=lambda x: x.score):
        if r.route == "missing":
            clean_actions.append(f"**{r.stem}**: no artifact - convert to `.md` or images.")
        elif r.misrouted_suspect and r.route == "md":
            clean_actions.append(
                f"**{r.stem}**: thin/misrouted text extract - re-render PNG @200 DPI + OCR."
            )
        elif r.arabic_bidi_risk == "high":
            clean_actions.append(
                f"**{r.stem}**: Arabic bidi/glyph breakage - re-extract with bidi-aware text or OCR."
            )
        elif r.route == "images" and r.image_median_dpi and r.image_median_dpi < 100:
            clean_actions.append(
                f"**{r.stem}**: images ~{r.image_median_dpi:.0f} DPI - "
                f"re-render at {DPI_OCR_TARGET} DPI before OCR."
            )
        elif r.coverage is not None and r.coverage < COVERAGE_WARN:
            clean_actions.append(
                f"**{r.stem}**: coverage {r.coverage:.2f} - investigate dropped text."
            )
        elif r.empty_pages >= 3:
            clean_actions.append(
                f"**{r.stem}**: {r.empty_pages} empty pages - verify blanks vs extract failure."
            )
    for d in dupes:
        clean_actions.append(
            f"Near-duplicate: `{d['a']}` <-> `{d['b']}` (sim={d['similarity']:.2f}) - "
            "confirm intentional bilingual/version pair."
        )
    if not clean_actions:
        lines.append("- No critical actions; spot-check golden pages manually.")
    else:
        for i, a in enumerate(clean_actions, 1):
            lines.append(f"{i}. {a}")
    lines.append("")

    lines.append("## Method notes")
    lines.append("")
    lines.append(
        "- **Coverage** = artifact text chars / PDF `get_text()` chars "
        "(same extractor family as the original pipeline)."
    )
    lines.append(
        f"- **Thin text** = < {THIN_CHARS_PER_PAGE} chars/page on an MD-routed doc."
    )
    lines.append(
        "- **Arabic bidi risk** uses share of Arabic tokens and rate of "
        "very short/isolated Arabic fragments (proxy for reversed/broken extraction)."
    )
    lines.append(
        "- **Token retention** = emails, article refs, and code-like identifiers "
        "found in the PDF text layer that also appear in the `.md`."
    )
    lines.append(
        f"- **DPI** estimated from PNG pixel size / PDF page size in inches "
        f"(expected ~{DPI_EXPECT} for current renders)."
    )
    lines.append(
        "- This report does **not** replace a manual golden-page layout audit "
        "(tables, reading order)."
    )
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Assess PDF→MD/PNG conversion quality")
    ap.add_argument(
        "--pdf-dir",
        type=Path,
        default=DEFAULT_PDF_DIR,
        help=f"Directory of source PDFs (default: {DEFAULT_PDF_DIR})",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=REPORTS_DIR / "CONVERSION_QUALITY_REPORT.md",
        help="Markdown report output path",
    )
    ap.add_argument(
        "--json",
        type=Path,
        default=REPORTS_DIR / "conversion_quality.json",
        help="JSON report output path",
    )
    args = ap.parse_args()

    pdf_dir: Path = args.pdf_dir
    if not pdf_dir.is_dir():
        print(f"ERROR: PDF dir not found: {pdf_dir}", file=sys.stderr)
        return 1

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        print(f"ERROR: no PDFs in {pdf_dir}", file=sys.stderr)
        return 1

    reports: list[DocReport] = []
    for pdf in pdfs:
        stem = stem_of_pdf(pdf)
        md = md_path_for(stem)
        images = image_paths_for(stem)
        if md and images:
            # Prefer MD if both exist, but flag and note image DPI
            r = assess_md(stem, pdf, md)
            r.flags.append(f"also_has_images:{len(images)}")
            # Quick DPI sample from first image + page 0
            try:
                doc = fitz.open(pdf)
                with Image.open(images[0]) as im:
                    w, h = im.size
                dpi0 = estimate_dpi(w, h, doc[0].rect if doc.page_count else None)
                doc.close()
                r.image_median_dpi = dpi0
                r.image_count = len(images)
                if dpi0 < 100:
                    r.flags.append(f"low_dpi:{dpi0:.0f}")
                    r.score = max(0.0, round(r.score - 0.08, 3))
                    r.grade = grade_from_score(r.score, r.route)
                elif dpi0 < DPI_OCR_TARGET:
                    r.flags.append(f"dpi_below_ocr_target:{dpi0:.0f}")
            except Exception as exc:
                r.flags.append(f"dpi_check_failed:{exc}")
            reports.append(r)
        elif md:
            reports.append(assess_md(stem, pdf, md))
        elif images:
            reports.append(assess_images(stem, pdf, images))
        else:
            reports.append(assess_missing(stem, pdf))

    md_files = [CORPUS_MD_DIR / f"{r.stem}.md" for r in reports if r.route == "md"]
    md_files = [p for p in md_files if p.exists()]
    dupes = find_near_duplicates(md_files)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    md_report = render_markdown(reports, dupes, pdf_dir)
    args.out.write_text(md_report, encoding="utf-8")

    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "pdf_dir": str(pdf_dir),
        "root": str(ROOT),
        "documents": [asdict(r) for r in reports],
        "near_duplicates": dupes,
        "summary": {
            "count": len(reports),
            "mean_score": round(sum(r.score for r in reports) / max(len(reports), 1), 3),
            "grades": {
                g: sum(1 for r in reports if r.grade == g)
                for g in ["A", "B", "C", "D", "F"]
            },
        },
    }
    args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # Avoid Windows cp1252 console crashes on Unicode
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass
    summary = payload["summary"]
    print(f"Assessed {summary['count']} PDFs | mean_score={summary['mean_score']} | grades={summary['grades']}")
    print(f"Wrote {args.out}")
    print(f"Wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
