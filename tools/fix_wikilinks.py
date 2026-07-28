"""
Repair broken Obsidian wikilinks in the Graphify vault.

Graphify exports note filenames with Windows-forbidden characters removed
(e.g. "AML/CTF Guide" -> "AMLCTF Guide.md"), but links written inside notes keep
the original text ("[[AML/CTF Guide]]"). Obsidian then (a) fails to resolve the
link and (b) for '/' treats it as a folder separator and shows a hollow phantom
node on the graph edge.

This script rewrites each broken link to the alias form:
    [[AML/CTF Guide]]            -> [[AMLCTF Guide|AML/CTF Guide]]
    [[Circular: X]]             -> [[Circular X|Circular: X]]
    [[real|Display]] (bad real) -> [[strippedreal|Display]]

It resolves targets against the actual .md files on disk, is idempotent, and
touches only link *text*. Safe to re-run after any `graphify export obsidian`.

Usage:
    python tools/fix_wikilinks.py            # apply
    python tools/fix_wikilinks.py --dry-run  # report only
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Vault location is configurable (env var) so this can repair a custom export dir
# such as `graphify export obsidian --dir SAMA_Knowledge_Base_Obsidian`.
VAULT = Path(os.environ.get("GRAPHIFY_VAULT_DIR", str(ROOT / "graphify-out" / "obsidian")))
FORBIDDEN = set('<>:"/\\|?*')

LINK_RE = re.compile(r"\[\[([^\]\|]+)(\|[^\]]+)?\]\]")


def strip_forbidden(name: str) -> str:
    """Match Graphify's filename rule: delete forbidden chars (no replacement)."""
    return "".join(c for c in name if c not in FORBIDDEN)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = ap.parse_args()

    if not VAULT.exists():
        raise SystemExit(f"Vault not found: {VAULT}")

    existing = {p.stem for p in VAULT.glob("*.md")}

    total_changes = 0
    files_changed = 0
    per_link: dict[str, int] = {}

    for md in VAULT.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        changed_in_file = 0

        def repl(m: re.Match) -> str:
            nonlocal changed_in_file
            target = m.group(1).strip()
            alias = m.group(2)  # includes leading '|' or None
            # already resolvable -> leave untouched (idempotent)
            if target in existing:
                return m.group(0)
            stripped = strip_forbidden(target)
            # only rewrite when the stripped name is a real note and something was stripped
            if stripped != target and stripped in existing:
                changed_in_file += 1
                key = f"[[{target}]]"
                per_link[key] = per_link.get(key, 0) + 1
                if alias:
                    # keep existing display alias, fix only the target
                    return f"[[{stripped}{alias}]]"
                # add original text as display alias
                return f"[[{stripped}|{target}]]"
            return m.group(0)

        new_text = LINK_RE.sub(repl, text)
        if changed_in_file:
            total_changes += changed_in_file
            files_changed += 1
            if not args.dry_run:
                md.write_text(new_text, encoding="utf-8")

    verb = "Would rewrite" if args.dry_run else "Rewrote"
    print(f"{verb} {total_changes} link(s) across {files_changed} file(s).")
    for link, c in sorted(per_link.items(), key=lambda x: -x[1]):
        print(f"   {c:2}  {link}")
    if args.dry_run:
        print("(dry run — no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
