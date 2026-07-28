# SAMA Knowledge Base

Knowledge graph workspace for Saudi Central Bank (SAMA) regulatory PDFs → Markdown corpus → Graphify → Obsidian vault → legal/compliance enrichment.

## Layout

```
SAMAKnowledgeBase/
├── scanner-sama-docs/               # PDFs from rulebook.sama.gov.sa (staging)
├── corpus/markdown/                 # converted .md (Graphify ingest root)
├── assets/page-images/              # 200 DPI PNGs (OCR route; not Graphify-ingested)
├── tools/                           # scanner, acquire, compare, preprocess, enrich, audit
│   └── tessdata/                    # eng+ara for OCR
├── reports/
│   ├── rulebook/                    # tree, manifest, comparison, acquisition
│   ├── conversion/                  # preprocess + QA reports
│   ├── graph/                       # graph / enrichment audits
│   └── runs/YYYYMMDDTHHMMSSZ/       # per-run snapshots + GRAPHIFY.txt
├── archive/
│   ├── conversion-backup/           # previous .md on replace
│   └── graphify-snapshots/          # dated graphify-out backups
├── graphify-out/                    # live graph.json + reports + enrichment_cache.json
├── SAMA_Knowledge_Base_Obsidian/    # exported Obsidian vault (open THIS in Obsidian)
├── requirements.txt                 # Python dependencies
├── docs/SESSION.md                  # session / runbook
├── docs/agents/                     # Orchestrator → Legal → Mapper → Extractor → Reviewer → Formatter
├── .cursor/rules/
├── README.md
└── .opencode/
```

## Setup

```powershell
# 1) Python deps (project runtime: CPython 3.7)
python -m pip install -r requirements.txt
python -m playwright install chromium          # for the rulebook scanner

# 2) External binaries (not pip):
#    - graphify  -> must be on PATH  (verify: graphify --version)
#    - Tesseract OCR -> system install; language data eng+ara is in tools/tessdata/

# 3) Secrets / config (per shell session)
$env:ANTHROPIC_API_KEY     = "sk-ant-..."       # required for graphify + enrichment
$env:GRAPHIFY_VAULT_DIR    = "SAMA_Knowledge_Base_Obsidian"
$env:GRAPHIFY_ENRICH_MODEL = "claude-opus-4-8"
$env:TESSDATA_PREFIX       = "$PWD\tools\tessdata"
```

## Pipeline

```
scanner → acquire → compare → preprocess → (manual) graphify + enrich
```

| Mode | Behavior |
|---|---|
| **First** | Download all; preprocess all NEW/UPDATED; then Graphify in OpenCode |
| **Monthly** | Download; compare; preprocess **only** NEW/UPDATED; skip Graphify if none |

**Replace policy:** UPDATED stems archive old `.md` under `archive/conversion-backup/`, then overwrite.

## Commands

```powershell
# (assumes Setup env vars above are set)

# Full orchestration (skips Graphify — prints the OpenCode steps to run)
python tools\rulebook_run.py --mode first
python tools\rulebook_run.py --mode monthly

# Or step-by-step
python tools\rulebook_scanner.py
python tools\rulebook_acquire.py
python tools\rulebook_compare.py
python tools\preprocess_pdfs.py --from-plan reports\rulebook\comparison.json
python tools\assess_conversion.py

# After successful preprocess, lock baseline
python tools\rulebook_compare.py --update-baseline
```

### Graphify + enrichment (manual in OpenCode)

Requires `graphify` on PATH and `ANTHROPIC_API_KEY` set. See `reports/runs/<stamp>/GRAPHIFY.txt` after a run, or:

```powershell
# 1) Build the graph  (extract writes under the scanned path; then move it to repo root)
graphify extract corpus --force --mode deep --backend claude --model claude-opus-4-8
Move-Item corpus\graphify-out graphify-out          # only after a fresh extract
graphify cluster-only . --backend claude --model claude-opus-4-8
graphify label . --backend claude --model claude-opus-4-8

# 2) Export the Obsidian vault
graphify export obsidian --dir SAMA_Knowledge_Base_Obsidian

# 3) Fix wikilinks + legal/compliance enrichment (respects GRAPHIFY_VAULT_DIR / _ENRICH_MODEL)
python tools\fix_wikilinks.py
python tools\enrich_graph_notes.py --force          # add --no-apply for a cache-only smoke test
python tools\audit_graph_quality.py                 # optional QA
```

## Enrichment notes

- **Persona:** SAMA compliance/legal analyst. Each edge gets a *"What this link tells you"* narrative (decision-framing → regulatory basis → practical consequence) plus verbatim **Grounding** quotes. Tone is confidence-matched (directive for `EXTRACTED`, tentative for `INFERRED`). No RegTech/system-design advice.
- **Arabic OCR guard:** garbled presentation-form Arabic is never written to a note — the model paraphrases in English + caveats, and a post-process/render guard strips stray glyphs and cleans locators.
- **Config:** `GRAPHIFY_VAULT_DIR` (default `SAMA_Knowledge_Base_Obsidian`), `GRAPHIFY_ENRICH_MODEL` (default `claude-opus-4-8`). Flags: `--force`, `--no-apply`, `--limit-edges N`, `--skip-communities`, `--apply-only`.

## Known limitations

- **Duplicate-label nodes:** the same instrument extracted from multiple source PDFs yields duplicate notes suffixed `_1`, `_2`, … (e.g. `Banking Control Law_10.md`). These resolve correctly (0 broken links) but are noisy; a graph-level dedup + re-export/enrich is the proper fix.
- **Grade-C Arabic sources:** a few PDFs have poor OCR; excerpts from them are paraphrased/caveated rather than quoted.
- **Audit Layer-1** per-document grading is currently non-functional against the graph schema (page counts read empty); Layer-2 grounding + integrity checks are the reliable signals.
