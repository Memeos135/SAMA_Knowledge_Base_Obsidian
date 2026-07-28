"""
Compare scanner-sama-docs PDFs against baseline + corpus.

Statuses:
  NEW       — stem/file not in baseline (or no baseline yet)
  UPDATED   — same stem, different SHA256 (or higher VER than baseline)
  UNCHANGED — same stem + SHA
  CORPUS_ONLY — in corpus but not in scanner-sama-docs (informational)
  FAILED    — listed in manifest as failed download (if present)

Replace policy: UPDATED means preprocess will archive old .md then overwrite.

Outputs:
  reports/rulebook/comparison.json
  reports/rulebook/comparison_report.md

Usage:
  python tools/rulebook_compare.py
  python tools/rulebook_compare.py --update-baseline   # after successful preprocess
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "scanner-sama-docs"
CORPUS_DIR = ROOT / "corpus" / "markdown"
OUT_DIR = ROOT / "reports" / "rulebook"
BASELINE_PATH = OUT_DIR / "baseline.json"
MANIFEST_PATH = OUT_DIR / "manifest.json"

STEM_RE = re.compile(r"(SAMA_(?:EN|AR)_(\d+)_VER(\d+)(?:_(\d+))?)", re.I)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_stem(name: str) -> Optional[dict]:
    m = STEM_RE.search(name)
    if not m:
        return None
    return {
        "stem": m.group(1).upper(),
        "doc_id": m.group(2),
        "ver": int(m.group(3)),
        "suffix": int(m.group(4)) if m.group(4) else 0,
    }


def inventory_docs(docs_dir: Path) -> Dict[str, dict]:
    inv: Dict[str, dict] = {}
    for p in sorted(docs_dir.glob("*.pdf")):
        meta = parse_stem(p.name)
        key = meta["stem"] if meta else p.stem
        inv[key] = {
            "key": key,
            "stem": meta["stem"] if meta else None,
            "filename": p.name,
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256_file(p),
            "size": p.stat().st_size,
            "doc_id": meta["doc_id"] if meta else None,
            "ver": meta["ver"] if meta else None,
            "suffix": meta["suffix"] if meta else None,
        }
    return inv


def inventory_corpus() -> Dict[str, str]:
    out: Dict[str, str] = {}
    for p in CORPUS_DIR.glob("*.md"):
        m = STEM_RE.search(p.stem)
        out[m.group(1).upper() if m else p.stem] = p.name
    return out


def load_baseline() -> Dict[str, dict]:
    if not BASELINE_PATH.exists():
        return {}
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return data.get("files") or {}


def save_baseline(inv: Dict[str, dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "docs_dir": str(DOCS_DIR.relative_to(ROOT)),
        "count": len(inv),
        "files": inv,
    }
    BASELINE_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def compare(inv: Dict[str, dict], baseline: Dict[str, dict], corpus: Dict[str, str]) -> List[dict]:
    items: List[dict] = []
    for key, cur in inv.items():
        prev = baseline.get(key)
        in_corpus = key in corpus or (cur.get("stem") in corpus if cur.get("stem") else False)
        if not prev:
            # First baseline empty → all NEW; also treat as NEW if never preprocessed
            status = "NEW"
            summary = "Not in baseline"
            if in_corpus and not baseline:
                # first run with existing corpus: still NEW-to-pipeline unless SHA tracked
                summary = "Not in baseline (may already exist in corpus — replace on preprocess)"
        elif prev.get("sha256") != cur["sha256"]:
            status = "UPDATED"
            summary = f"SHA changed ({prev.get('sha256', '')[:12]}… → {cur['sha256'][:12]}…)"
        else:
            status = "UNCHANGED"
            summary = "Same SHA as baseline"

        # version bump vs older stem of same doc_id in baseline
        if status == "NEW" and cur.get("doc_id") and baseline:
            older = [
                b
                for b in baseline.values()
                if b.get("doc_id") == cur["doc_id"]
                and b.get("stem")
                and b["stem"] != cur.get("stem")
            ]
            if older:
                status = "UPDATED"
                summary = f"New version of doc_id={cur['doc_id']} (replaces older stem)"

        items.append(
            {
                "status": status,
                "key": key,
                "stem": cur.get("stem"),
                "filename": cur["filename"],
                "sha256": cur["sha256"],
                "in_corpus": bool(in_corpus),
                "summary": summary,
                "path": cur["path"],
            }
        )

    for cstem in sorted(corpus.keys()):
        if cstem not in inv:
            items.append(
                {
                    "status": "CORPUS_ONLY",
                    "key": cstem,
                    "stem": cstem,
                    "filename": corpus[cstem],
                    "sha256": None,
                    "in_corpus": True,
                    "summary": "In corpus/markdown but not in scanner-sama-docs",
                    "path": f"corpus/markdown/{corpus[cstem]}",
                }
            )

    # manifest failures
    if MANIFEST_PATH.exists():
        try:
            man = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            for p in man.get("pdfs") or []:
                if p.get("action") == "failed":
                    items.append(
                        {
                            "status": "FAILED",
                            "key": p.get("file_id") or p.get("filename"),
                            "stem": p.get("stem"),
                            "filename": p.get("filename"),
                            "sha256": None,
                            "in_corpus": False,
                            "summary": p.get("error") or "download failed",
                            "path": p.get("pdf_url"),
                        }
                    )
        except Exception:
            pass

    order = {"UPDATED": 0, "NEW": 1, "FAILED": 2, "CORPUS_ONLY": 3, "UNCHANGED": 4}
    items.sort(key=lambda x: (order.get(x["status"], 9), x.get("key") or ""))
    return items


def write_report(items: List[dict], baseline_count: int) -> None:
    counts: Dict[str, int] = {}
    for it in items:
        counts[it["status"]] = counts.get(it["status"], 0) + 1

    to_preprocess = [it for it in items if it["status"] in ("NEW", "UPDATED")]

    lines = [
        "# Rulebook comparison report",
        "",
        f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> scanner-sama-docs PDFs vs baseline ({baseline_count} prior files)",
        "",
        "## Counts",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for k in ("NEW", "UPDATED", "UNCHANGED", "CORPUS_ONLY", "FAILED"):
        lines.append(f"| {k} | {counts.get(k, 0)} |")
    lines += [
        "",
        f"**To preprocess (NEW+UPDATED): {len(to_preprocess)}**",
        "",
        "## Changes (NEW / UPDATED)",
        "",
    ]
    if to_preprocess:
        lines.append("| Status | File | In corpus | Summary |")
        lines.append("|---|---|---|---|")
        for it in to_preprocess:
            lines.append(
                f"| {it['status']} | `{it.get('filename') or it.get('key')}` | "
                f"{it['in_corpus']} | {it['summary'][:80]} |"
            )
    else:
        lines.append("_None — monthly run can stop before preprocess/graphify._")
    lines.append("")

    failed = [it for it in items if it["status"] == "FAILED"]
    if failed:
        lines += ["## Failed acquisitions", ""]
        for it in failed:
            lines.append(f"- `{it.get('filename')}` — {it['summary']}")
        lines.append("")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "comparison_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "baseline_count": baseline_count,
        "counts": counts,
        "to_preprocess": to_preprocess,
        "items": items,
    }
    (OUT_DIR / "comparison.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--update-baseline", action="store_true", help="Write current inventory as baseline")
    ap.add_argument("--docs-dir", type=Path, default=DOCS_DIR)
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass

    if not args.docs_dir.exists():
        raise SystemExit(f"Missing docs dir: {args.docs_dir}")

    inv = inventory_docs(args.docs_dir)
    corpus = inventory_corpus()
    baseline = load_baseline()

    if args.update_baseline:
        save_baseline(inv)
        baseline = inv
        print(f"Baseline updated: {len(inv)} files → {BASELINE_PATH}", flush=True)

    items = compare(inv, baseline, corpus)
    write_report(items, len(baseline))
    n_prep = sum(1 for i in items if i["status"] in ("NEW", "UPDATED"))
    print(
        f"Compare done: NEW+UPDATED={n_prep} | report={OUT_DIR / 'comparison_report.md'}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
