"""
Orchestrate rulebook pipeline (scanner → acquire → compare → preprocess).

Graphify is intentionally NOT run here — do that manually in OpenCode; this
script prints the correct, cost-aware Graphify steps for the situation it found.

Monthly cost policy (encoded in graphify_instructions):
  scanner → acquire → compare
    - no NEW/UPDATED  -> STOP (no preprocess, no Graphify, no API cost)
    - changes         -> preprocess ONLY changed stems, then Graphify:
                           * small delta  -> incremental extract (no --force)
                           * large / consistency -> full --force rebuild
                         enrich WITHOUT --force (cached edges reused; pay only
                         for new/changed edges). Snapshot graphify-out before
                         replacing; promote the new graph only after success.

Modes:
  first    — scan + acquire + compare + preprocess all NEW/UPDATED (full build)
  monthly  — same, but stop early if nothing changed (incremental build)
  compare  — compare only
  preprocess — preprocess from existing comparison.json

Usage:
  python tools/rulebook_run.py --mode first
  python tools/rulebook_run.py --mode monthly
  python tools/rulebook_run.py --mode first --skip-scan --skip-acquire
  python tools/rulebook_run.py --mode preprocess --max 5
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parent.parent
OUT_RULEBOOK = ROOT / "reports" / "rulebook"
RUNS_DIR = ROOT / "reports" / "runs"
PY = sys.executable


def run_step(name: str, args: List[str], log_path: Path) -> int:
    print(f"\n===== {name} =====", flush=True)
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"\n===== {name} @ {datetime.now(timezone.utc).isoformat()} =====\n")
        log.write(" ".join(args) + "\n")
        proc = subprocess.Popen(
            args,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            sys.stdout.write(line)
            log.write(line)
        return proc.wait()


def graphify_instructions(changed: bool, n_changed: int = 0, first: bool = False) -> str:
    if not changed:
        return (
            "No NEW/UPDATED documents — SKIP Graphify this month "
            "(no extract, no enrichment, no API cost).\n"
        )
    delta = f"{n_changed} document(s)" if n_changed else "some documents"
    # First run = full build; monthly delta = incremental + non-force enrich.
    build = (
        "# FIRST / full rebuild — pay once for the whole corpus:\n"
        "graphify extract corpus --force --mode deep --backend claude --model claude-opus-4-8"
        if first else
        "# SMALL DELTA ({d} changed): prefer incremental (no --force) so graphify\n"
        "# serves unchanged docs from its own cache and only re-embeds changed ones:\n"
        "graphify extract corpus --mode deep --backend claude --model claude-opus-4-8\n"
        "#\n"
        "# Only if you want a GUARANTEED-consistent rebuild (or the delta is large),\n"
        "# pay for a full re-extract instead:\n"
        "#   graphify extract corpus --force --mode deep --backend claude --model claude-opus-4-8"
    ).format(d=delta)
    enrich = (
        "python tools\\enrich_graph_notes.py --force        # full: re-enrich everything"
        if first else
        "python tools\\enrich_graph_notes.py                 # DELTA: cached edges reused,\n"
        "#                                                   only NEW/CHANGED edges call the model\n"
        "#   (use --force ONLY when you deliberately did a full rebuild above)"
    )
    return f"""
================================================================================
GRAPHIFY (manual — run in OpenCode)  —  {delta} changed
================================================================================

# Prereqs (see README):
#   - 'graphify' must be on PATH (verify:  graphify --version)
#   - $env:ANTHROPIC_API_KEY must be set
$env:GRAPHIFY_VAULT_DIR    = "SAMA_Knowledge_Base_Obsidian"
$env:GRAPHIFY_ENRICH_MODEL = "claude-opus-4-8"

# --- ROBUSTNESS: never half-update the live graph ---------------------------
# Snapshot the current graph BEFORE rebuilding; promote the new one ONLY after
# a successful extract (leave last month's graphify-out intact until then).
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
if (Test-Path graphify-out) {{ Copy-Item graphify-out "archive\\graphify-snapshots\\graphify-out_$stamp" -Recurse }}

# --- 1) BUILD ---------------------------------------------------------------
{build}
# extract writes under the scanned path; promote to repo root ONLY after success:
Move-Item corpus\\graphify-out graphify-out -Force
graphify cluster-only . --backend claude --model claude-opus-4-8
graphify label . --backend claude --model claude-opus-4-8
graphify export obsidian --dir SAMA_Knowledge_Base_Obsidian

# --- 2) LINKS + ENRICHMENT --------------------------------------------------
python tools\\fix_wikilinks.py
{enrich}

# --- 3) QA ------------------------------------------------------------------
python tools\\audit_graph_quality.py
================================================================================
""".strip()


def load_to_preprocess() -> List[dict]:
    path = OUT_RULEBOOK / "comparison.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("to_preprocess") or []


def snapshot_run(run_dir: Path) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    for name in (
        "comparison.json",
        "comparison_report.md",
        "acquisition_report.md",
        "scan_summary.md",
        "downloaded_files.txt",
    ):
        src = OUT_RULEBOOK / name
        if src.exists():
            shutil.copy2(src, run_dir / name)
    conv = ROOT / "reports" / "conversion" / "preprocess_report.md"
    if conv.exists():
        shutil.copy2(conv, run_dir / "preprocess_report.md")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["first", "monthly", "compare", "preprocess"], required=True)
    ap.add_argument("--skip-scan", action="store_true")
    ap.add_argument("--skip-acquire", action="store_true")
    ap.add_argument("--skip-preprocess", action="store_true")
    ap.add_argument("--max", type=int, default=0, help="Cap preprocess PDFs (0=all)")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = RUNS_DIR / stamp
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "run.log"
    t0 = time.time()
    rc = 0

    print(f"Run dir: {run_dir}", flush=True)

    if args.mode in ("first", "monthly") and not args.skip_scan:
        code = run_step("scanner", [PY, "tools/rulebook_scanner.py"], log_path)
        if code != 0:
            print("Scanner failed — aborting.", flush=True)
            return code

    if args.mode in ("first", "monthly") and not args.skip_acquire:
        acq = [PY, "tools/rulebook_acquire.py"]
        if args.headed:
            acq.append("--headed")
        code = run_step("acquire", acq, log_path)
        # acquire may exit 1 on partial download failures; continue if PDFs exist
        if code != 0:
            print(f"Acquire exited {code} (continuing if docs exist)", flush=True)
            rc = code

    if args.mode in ("first", "monthly", "compare"):
        code = run_step("compare", [PY, "tools/rulebook_compare.py"], log_path)
        if code != 0:
            return code

    to_prep = load_to_preprocess()
    changed = len(to_prep) > 0

    if args.mode == "monthly" and not changed:
        print("\nMonthly: no NEW/UPDATED — skipping preprocess.", flush=True)
        snapshot_run(run_dir)
        (run_dir / "GRAPHIFY.txt").write_text(graphify_instructions(False), encoding="utf-8")
        print(graphify_instructions(False), flush=True)
        print(f"Elapsed: {time.time() - t0:.1f}s", flush=True)
        return rc

    if args.mode in ("first", "monthly", "preprocess") and not args.skip_preprocess:
        if not changed and args.mode != "preprocess":
            print("Nothing to preprocess.", flush=True)
        else:
            prep = [
                PY,
                "tools/preprocess_pdfs.py",
                "--from-plan",
                str(OUT_RULEBOOK / "comparison.json"),
            ]
            if args.max > 0:
                prep += ["--max", str(args.max)]
            # If compare empty but preprocess mode, process all scanner docs
            if args.mode == "preprocess" and not changed:
                prep = [PY, "tools/preprocess_pdfs.py", "--pdf-dir", str(ROOT / "scanner-sama-docs")]
                if args.max > 0:
                    prep += ["--max", str(args.max)]
            code = run_step("preprocess", prep, log_path)
            if code != 0:
                rc = code
            else:
                # Update baseline after successful preprocess
                run_step(
                    "update-baseline",
                    [PY, "tools/rulebook_compare.py", "--update-baseline"],
                    log_path,
                )
            # QA assess (non-fatal)
            assess = [
                PY,
                "tools/assess_conversion.py",
                "--pdf-dir",
                str(ROOT / "scanner-sama-docs"),
            ]
            run_step("assess", assess, log_path)

    snapshot_run(run_dir)
    instructions = graphify_instructions(
        changed or args.mode == "first",
        n_changed=len(to_prep),
        first=(args.mode == "first"),
    )
    (run_dir / "GRAPHIFY.txt").write_text(instructions + "\n", encoding="utf-8")
    print("\n" + instructions, flush=True)
    print(f"\nRun complete → {run_dir} | elapsed {time.time() - t0:.1f}s | exit={rc}", flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
