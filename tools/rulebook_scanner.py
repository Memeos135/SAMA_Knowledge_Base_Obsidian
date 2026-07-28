"""
SAMA Rulebook tree scanner (rulebook.sama.gov.sa/en).

Recursively walks the left sidebar tree: visits each folder page, discovers
direct children via x-indent, repeats until every branch is expanded.

Outputs (reports/rulebook/):
  tree.json, tree.log, scan_summary.md

Usage:
  python tools/rulebook_scanner.py                  # full tree (structure only)
  python tools/rulebook_scanner.py --with-metadata  # also fetch PDF stems per leaf
  python tools/rulebook_scanner.py --max-nodes 50   # cap for testing
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "corpus" / "markdown"
PDF_DIR = Path(r"C:\Users\memeo\Downloads\SAMA_DOCS")
OUT_DIR = ROOT / "reports" / "rulebook"
BASE = "https://rulebook.sama.gov.sa"

STEM_RE = re.compile(r"(SAMA_(?:EN|AR)_\d+_VER\d+(?:_\d+)?)", re.I)
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")
DOC_NO_RE = re.compile(r"No:\s*([^\n|]+)", re.I)
STATUS_RE = re.compile(r"Status:\s*([^\n|]+)", re.I)

SKIP_HREFS = {
    "/en",
    "/en/search",
    "/en/view-revision-updates",
    "/en/terms-and-conditions",
}

# Page that exposes all top-level sector links at x=196 in the left nav.
ENTRY_PAGE = "/en/finance-sector-0"


@dataclass
class LeafRecord:
    tree_path: str
    title: str
    slug_url: str
    stem: Optional[str] = None
    document_no: Optional[str] = None
    status: Optional[str] = None
    render_lang: Optional[str] = None
    pdf_urls: List[str] = field(default_factory=list)
    acquisition_hints: List[str] = field(default_factory=list)
    in_local_corpus: bool = False
    in_local_pdf: bool = False
    error: Optional[str] = None


@dataclass
class TreeNode:
    title: str
    slug: str
    depth: int
    is_folder: bool = True
    children: List["TreeNode"] = field(default_factory=list)
    leaf: Optional[LeafRecord] = None


def load_local_stems() -> Tuple[Set[str], Set[str]]:
    corpus, pdfs = set(), set()
    for p in CORPUS_DIR.glob("*.md"):
        m = STEM_RE.search(p.stem)
        corpus.add(m.group(1).upper() if m else p.stem)
    if PDF_DIR.exists():
        for p in PDF_DIR.glob("*.pdf"):
            m = STEM_RE.search(p.stem)
            pdfs.add(m.group(1).upper() if m else p.stem)
    return corpus, pdfs


def detect_lang(text: str) -> str:
    if not text.strip():
        return "unknown"
    words = re.findall(r"\S+", text)
    ar = sum(1 for w in words if ARABIC_RE.search(w))
    if not words:
        return "unknown"
    r = ar / len(words)
    if r > 0.15:
        return "ar"
    if r > 0.02:
        return "mixed"
    return "en"


def abs_url(href: str) -> str:
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return BASE + href
    return BASE + "/" + href.lstrip("/")


def norm_slug(href: str) -> str:
    return href.split("?")[0].rstrip("/")


def should_skip(href: str) -> bool:
    slug = norm_slug(href)
    if slug in SKIP_HREFS:
        return True
    if not slug.startswith("/en/"):
        return True
    if "/entiresection/" in slug:
        return True
    return False


def collect_sidebar_links(page) -> List[dict]:
    return page.evaluate(
        """() => {
        const links = [];
        document.querySelectorAll('a[href]').forEach(a => {
            const r = a.getBoundingClientRect();
            if (r.left > 500 || r.top < 200 || r.top > 950) return;
            const t = (a.innerText || '').trim().replace(/\\s+/g, ' ');
            const h = a.getAttribute('href') || '';
            if (!t || t.length < 2) return;
            if (h.startsWith('javascript') || h === '#') return;
            if (h.includes('sama.gov.sa/en-US')) return;
            links.push({ x: Math.round(r.left), y: Math.round(r.top), href: h, title: t });
        });
        links.sort((a,b) => a.y - b.y || a.x - b.x);
        return links;
    }"""
    )


def parse_direct_children(links: List[dict], current_slug: str) -> List[dict]:
    """Direct sidebar children of current_slug (x-indent relative to active node)."""
    cur = norm_slug(current_slug)
    idx: Optional[int] = None
    px: Optional[int] = None
    for i, lk in enumerate(links):
        if norm_slug(lk["href"]) == cur:
            idx = i
            px = lk["x"]
    if idx is None or px is None:
        return []

    descendants: List[dict] = []
    for lk in links[idx + 1 :]:
        if lk["x"] <= px:
            break
        descendants.append(lk)
    if not descendants:
        return []

    min_x = min(lk["x"] for lk in descendants)
    return [lk for lk in descendants if lk["x"] == min_x]


def top_level_sectors(links: List[dict]) -> List[dict]:
    en = [lk for lk in links if lk["href"].startswith("/en/") and not should_skip(lk["href"])]
    if not en:
        return []
    min_x = min(lk["x"] for lk in en)
    return [lk for lk in en if lk["x"] == min_x]


def render_tree_log(node: TreeNode, lines: List[str], prefix: str = "") -> None:
    if node.depth >= 0:
        kind = "[folder]" if node.children else "[leaf]"
        line = f"{prefix}{kind} {node.title}"
        if node.slug:
            line += f"  ({node.slug})"
        if node.leaf:
            lr = node.leaf
            bits = []
            if lr.stem:
                bits.append(f"stem={lr.stem}")
            if lr.render_lang:
                bits.append(f"lang={lr.render_lang}")
            if lr.acquisition_hints:
                bits.append(f"acq={','.join(lr.acquisition_hints)}")
            if lr.in_local_corpus:
                bits.append("LOCAL_MD")
            if lr.in_local_pdf:
                bits.append("LOCAL_PDF")
            if lr.error:
                bits.append(f"ERR={lr.error[:60]}")
            if bits:
                line += " | " + " | ".join(bits)
        lines.append(line)
    child_prefix = prefix + "  "
    for ch in node.children:
        render_tree_log(ch, lines, child_prefix)


def tree_to_dict(node: TreeNode) -> dict:
    d = {
        "title": node.title,
        "slug": node.slug,
        "depth": node.depth,
        "is_folder": bool(node.children),
        "children": [tree_to_dict(c) for c in node.children],
    }
    if node.leaf:
        d["leaf"] = asdict(node.leaf)
    return d


def count_nodes(node: TreeNode) -> Tuple[int, int, int]:
    """Return (total, folders, leaves)."""
    if node.depth < 0:
        total = folders = leaves = 0
        for ch in node.children:
            t, f, l = count_nodes(ch)
            total += t
            folders += f
            leaves += l
        return total, folders, leaves
    if node.children:
        t = 1
        f = 1
        l = 0
        for ch in node.children:
            ct, cf, cl = count_nodes(ch)
            t += ct
            f += cf
            l += cl
        return t, f, l
    return 1, 0, 1


def walk_collect_leaves(node: TreeNode) -> List[LeafRecord]:
    leaves: List[LeafRecord] = []
    if node.depth >= 0 and not node.children and node.leaf:
        leaves.append(node.leaf)
    elif node.depth >= 0 and not node.children and not node.leaf:
        pass
    for ch in node.children:
        leaves.extend(walk_collect_leaves(ch))
    return leaves


def extract_regulation_page(page, leaf: LeafRecord) -> LeafRecord:
    try:
        page.wait_for_load_state("networkidle", timeout=12000)
    except Exception:
        pass
    page.wait_for_timeout(400)

    data = page.evaluate(
        """() => {
        const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
        const text = (main.innerText || '').slice(0, 12000);
        const pdfs = [];
        const hints = [];
        document.querySelectorAll('a[href], button').forEach(el => {
            const h = el.getAttribute('href') || '';
            const t = (el.innerText || '').trim().toLowerCase();
            if (h.includes('file_store') || h.endsWith('.pdf')) {
                pdfs.push({ href: h, text: (el.innerText||'').trim() });
            }
            if (t.includes('download') && t.includes('original') && t.includes('pdf')) hints.push('original_pdf');
            if (t.includes('print') && t.includes('pdf')) hints.push('print_pdf');
            if (t === 'entire section') hints.push('entire_section');
        });
        return { text, pdfs, hints };
    }"""
    )

    leaf.render_lang = detect_lang(data.get("text", ""))
    pdf_urls = []
    for p in data.get("pdfs", []):
        href = abs_url(p.get("href", ""))
        if "file_store" in href or href.endswith(".pdf"):
            pdf_urls.append(href)
    store = [u for u in pdf_urls if "rulebook.sama.gov.sa" in u and "file_store" in u]
    leaf.pdf_urls = list(dict.fromkeys(store or pdf_urls))

    hints = list(dict.fromkeys(data.get("hints", [])))
    if any("file_store" in u for u in leaf.pdf_urls):
        hints.insert(0, "store_pdf")
    leaf.acquisition_hints = hints or (["html_only"] if not leaf.pdf_urls else ["unknown"])

    text = data.get("text", "")
    m = DOC_NO_RE.search(text)
    if m:
        leaf.document_no = m.group(1).strip()[:60]
    m2 = STATUS_RE.search(text)
    if m2:
        leaf.status = m2.group(1).strip()[:40]

    for u in leaf.pdf_urls:
        sm = STEM_RE.search(u)
        if sm:
            leaf.stem = sm.group(1).upper()
            break
    return leaf


def mark_local(leaf: LeafRecord, corpus: Set[str], pdfs: Set[str]) -> None:
    if leaf.stem:
        leaf.in_local_corpus = leaf.stem in corpus
        leaf.in_local_pdf = leaf.stem in pdfs


def build_summary(
    root: TreeNode,
    leaves: List[LeafRecord],
    corpus: Set[str],
    elapsed: float,
    total_nodes: int,
    with_metadata: bool,
) -> str:
    stems = {l.stem for l in leaves if l.stem}
    new_stems = sorted(stems - corpus)
    corpus_missing = sorted(corpus - stems)

    lines = [
        "# Rulebook scan summary",
        "",
        f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Mode: {'tree + metadata' if with_metadata else 'tree structure only'}",
        f"> Elapsed: {elapsed:.1f}s",
        "",
        "## Counts",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Total nodes in tree | {total_nodes} |",
        f"| Leaf nodes (no children) | {sum(1 for _ in _iter_leaves(root))} |",
        f"| Metadata records | {len(leaves)} |",
        f"| With SAMA_EN/AR stem | {sum(1 for l in leaves if l.stem)} |",
        f"| In local corpus | {sum(1 for l in leaves if l.in_local_corpus)} |",
        f"| In local PDF dir | {sum(1 for l in leaves if l.in_local_pdf)} |",
        f"| New stems (in scan, not corpus) | {len(new_stems)} |",
        f"| Corpus stems not in scan | {len(corpus_missing)} |",
        "",
    ]

    if with_metadata:
        lines += ["## Acquisition methods", ""]
        acq: Dict[str, int] = {}
        for l in leaves:
            for h in l.acquisition_hints or ["none"]:
                acq[h] = acq.get(h, 0) + 1
        for k, v in sorted(acq.items(), key=lambda x: -x[1]):
            lines.append(f"- `{k}`: {v}")

        lines += ["", "## Render language", ""]
        lang: Dict[str, int] = {}
        for l in leaves:
            lang[l.render_lang or "unknown"] = lang.get(l.render_lang or "unknown", 0) + 1
        for k, v in sorted(lang.items(), key=lambda x: -x[1]):
            lines.append(f"- `{k}`: {v}")

        lines += ["", "## Matched local corpus (sample)", ""]
        matched = [l for l in leaves if l.in_local_corpus][:20]
        if matched:
            lines.append("| Stem | Title | PDF | Lang |")
            lines.append("|---|---|---|---|")
            for l in matched:
                stem_pdf = next((u for u in l.pdf_urls if l.stem and l.stem.split("_VER")[0] in u), None)
                pdf = stem_pdf.split("/")[-1] if stem_pdf else (l.pdf_urls[0].split("/")[-1] if l.pdf_urls else "-")
                lines.append(f"| `{l.stem}` | {l.title[:50]} | {pdf} | {l.render_lang} |")
        else:
            lines.append("_No stem matches (run with --with-metadata)._")

        lines += ["", "## New stems found (first 30)", ""]
        if new_stems:
            for s in new_stems[:30]:
                hit = next((l for l in leaves if l.stem == s), None)
                title = hit.title[:60] if hit else ""
                lines.append(f"- `{s}` — {title}")
        else:
            lines.append("_None._")

        lines += ["", "## Local corpus not seen (first 30)", ""]
        for s in corpus_missing[:30]:
            lines.append(f"- `{s}`")
    else:
        lines += [
            "_Stem/corpus diff requires `--with-metadata` (visits every leaf page)._",
            "",
        ]

    return "\n".join(lines) + "\n"


def _iter_leaves(node: TreeNode):
    if node.depth >= 0 and not node.children:
        yield node
    for ch in node.children:
        yield from _iter_leaves(ch)


def discover_tree(
    page,
    entry: str,
    max_nodes: int,
) -> Tuple[TreeNode, Dict[str, TreeNode], int]:
    """
    BFS-expand every sidebar branch. Returns (root, slug_index, pages_visited).
    """
    page.goto(abs_url(entry), wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    root = TreeNode(title="SAMA Rulebook (EN)", slug="", depth=-1, is_folder=True)
    by_slug: Dict[str, TreeNode] = {}

    links = collect_sidebar_links(page)
    sectors = top_level_sectors(links)
    if not sectors:
        raise RuntimeError(f"No top-level sectors found on {entry}")

    for lk in sectors:
        slug = norm_slug(lk["href"])
        node = TreeNode(title=lk["title"], slug=slug, depth=0, is_folder=True)
        root.children.append(node)
        by_slug[slug] = node

    queue: deque[str] = deque(by_slug.keys())
    expanded: Set[str] = set()
    pages_visited = 1

    while queue:
        slug = queue.popleft()
        if slug in expanded:
            continue
        if max_nodes > 0 and len(expanded) >= max_nodes:
            print(f"  [cap] reached --max-nodes {max_nodes}", flush=True)
            break

        expanded.add(slug)
        node = by_slug[slug]

        try:
            page.goto(abs_url(slug), wait_until="domcontentloaded")
            page.wait_for_timeout(1200)
            pages_visited += 1
        except Exception as exc:
            if node.leaf is None:
                node.leaf = LeafRecord(tree_path=slug, title=node.title, slug_url=abs_url(slug), error=str(exc)[:200])
            print(f"  ERR navigate {slug}: {exc}", flush=True)
            continue

        child_links = parse_direct_children(collect_sidebar_links(page), slug)
        seen_child: Set[str] = set()
        for lk in child_links:
            ch_slug = norm_slug(lk["href"])
            if should_skip(ch_slug) or ch_slug in seen_child:
                continue
            seen_child.add(ch_slug)

            if ch_slug not in by_slug:
                child = TreeNode(title=lk["title"], slug=ch_slug, depth=node.depth + 1, is_folder=True)
                by_slug[ch_slug] = child
                node.children.append(child)
                queue.append(ch_slug)
            elif ch_slug not in expanded:
                queue.append(ch_slug)

        if len(expanded) % 20 == 0:
            print(f"  expanded {len(expanded)} | queued {len(queue)} | indexed {len(by_slug)}", flush=True)

    # Mark leaves (nodes never got children attached)
    for n in by_slug.values():
        n.is_folder = bool(n.children)

    return root, by_slug, pages_visited


def attach_metadata(page, root: TreeNode, by_slug: Dict[str, TreeNode], corpus: Set[str], pdfs: Set[str]) -> List[LeafRecord]:
    """Visit every leaf node and extract PDF/stem metadata."""
    leaves_meta: List[LeafRecord] = []
    leaf_nodes = list(_iter_leaves(root))
    total = len(leaf_nodes)

    for i, node in enumerate(leaf_nodes, 1):
        path = node.slug
        leaf = LeafRecord(tree_path=path, title=node.title, slug_url=abs_url(node.slug))
        print(f"  meta [{i}/{total}] {node.title[:60]}", flush=True)
        try:
            page.goto(leaf.slug_url, wait_until="domcontentloaded")
            leaf = extract_regulation_page(page, leaf)
            mark_local(leaf, corpus, pdfs)
        except Exception as exc:
            leaf.error = str(exc)[:200]
        node.leaf = leaf
        leaves_meta.append(leaf)
        page.wait_for_timeout(200)

    return leaves_meta


def scan(
    entry: str,
    max_nodes: int,
    with_metadata: bool,
    headless: bool,
) -> int:
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    corpus, pdfs = load_local_stems()
    t0 = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.set_default_timeout(30000)

        print("Discovering full sidebar tree (recursive BFS)...", flush=True)
        root, by_slug, pages_visited = discover_tree(page, entry, max_nodes)

        total, folders, leaves = count_nodes(root)
        print(f"Tree: {total} nodes ({folders} folders, {leaves} leaves) | {pages_visited} pages loaded", flush=True)

        all_leaves: List[LeafRecord] = []
        if with_metadata:
            print(f"Fetching metadata for {leaves} leaf nodes...", flush=True)
            all_leaves = attach_metadata(page, root, by_slug, corpus, pdfs)

        browser.close()

    elapsed = time.time() - t0

    log_lines = [
        f"SAMA Rulebook — full tree scan — {datetime.now(timezone.utc).isoformat()}",
        f"Entry: {entry}",
        f"Nodes: {total} total | {folders} folders | {leaves} leaves",
        f"Pages visited (discovery): {pages_visited}",
        f"Metadata: {'yes' if with_metadata else 'no (use --with-metadata)'}",
        "",
    ]
    render_tree_log(root, log_lines)

    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "entry": entry,
        "total_nodes": total,
        "folder_nodes": folders,
        "leaf_nodes": leaves,
        "pages_visited": pages_visited,
        "with_metadata": with_metadata,
        "tree": tree_to_dict(root),
        "leaves": [asdict(l) for l in all_leaves],
        "slug_index": {s: {"title": n.title, "depth": n.depth, "children": len(n.children)} for s, n in by_slug.items()},
    }

    (OUT_DIR / "tree.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "tree.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    (OUT_DIR / "scan_summary.md").write_text(
        build_summary(root, all_leaves, corpus, elapsed, total, with_metadata), encoding="utf-8"
    )

    print(f"\nWrote reports/rulebook/tree.log ({total} nodes, {elapsed:.1f}s)", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Recursively scan SAMA Rulebook sidebar tree")
    ap.add_argument("--entry", default=ENTRY_PAGE, help=f"Entry page exposing top sectors (default: {ENTRY_PAGE})")
    ap.add_argument("--max-nodes", type=int, default=0, help="Cap nodes expanded (0=unlimited)")
    ap.add_argument("--with-metadata", action="store_true", help="Visit every leaf for PDF/stem metadata (slow)")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass
    return scan(args.entry, args.max_nodes, args.with_metadata, headless=not args.headed)


if __name__ == "__main__":
    raise SystemExit(main())
