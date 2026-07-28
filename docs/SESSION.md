# SAMA Knowledge Base — Session Memory

> IDE/agent runbook for this workspace.  
> Generated: 2026-07-22 · Updated: 2026-07-28  
> **Not** a second source of truth for layout — see `README.md` for folders; this file tracks *how we work* and *what’s open*.

Cursor loads continuity via `.cursor/rules/sama-session-memory.mdc` (alwaysApply), which **points here** rather than duplicating paths.

---

## 1. Project Overview

| Field | Value |
|---|---|
| Root | `C:\Users\memeo\Downloads\CursorProjects\SAMAKnowledgeBase` |
| Objective | SAMA regulatory PDFs → corpus MD → Graphify/Obsidian → enrichment → Orchestrator (Legal Map→Dig → Reviewer → Formatter) |
| Graphify CLI | `graphify` on PATH (uv tool; e.g. `~/.local/bin/graphify`) |
| LLM backend | Claude Opus 4.8 (`claude-opus-4-8`) via `ANTHROPIC_API_KEY` (env only). NOTE: 5.x models (opus-5 etc.) emit thinking blocks that break graphify 0.9.23 — use 4.8. |
| Enrichment env | `GRAPHIFY_VAULT_DIR=SAMA_Knowledge_Base_Obsidian`, `GRAPHIFY_ENRICH_MODEL=claude-opus-4-8` |
| PDF source | `C:\Users\memeo\Downloads\SAMA_DOCS\` |
| PDF backup | `C:\Users\memeo\Downloads\SAMA_DOCS_bak\` |
| Ingest root | `corpus\` (markdown under `corpus\markdown\`) |
| Session (this file) | `docs\SESSION.md` |
| IDE rule | `.cursor\rules\sama-session-memory.mdc` |
| Agent personas | `docs\agents\` |

Live counts: check disk / `graphify-out\graph.json` — do not treat remembered numbers as authoritative.

---

## 2. Knowledge Graph (operational notes)

| Path | Role |
|---|---|
| `graphify-out\graph.json` | Live graph (1816 nodes / 1848 edges / 336 communities) |
| `graphify-out\GRAPH_REPORT.md` | Community report |
| `SAMA_Knowledge_Base_Obsidian\` | Obsidian vault (open THIS in Obsidian) |
| `graphify-out\enrichment_cache.json` | Enrichment cache (legal/compliance persona in `tools\enrich_graph_notes.py`) |

### Wikilinks
- After `graphify export obsidian`, run `python tools\fix_wikilinks.py` if slash/colon labels break links.
- Enrichment uses a safe `wikilink()` helper (alias form for forbidden chars) so broken links are not reintroduced. Current vault: 5796 links, 0 broken.

### Enrichment behaviour (legal/compliance persona)
- Each edge → **"What this link tells you"** (decision framing → regulatory basis → practical consequence) + verbatim **Grounding** quotes; confidence-matched tone; no RegTech/system advice.
- **Arabic OCR guard:** garbled presentation-form Arabic is never written — paraphrased in English + caveat; render/store guards strip stray glyphs and clean locators.
- Flags: `--force`, `--no-apply` (cache-only smoke test), `--limit-edges N`, `--skip-communities`, `--apply-only`.

### Known limitation — duplicate-label nodes
- Same instrument extracted from multiple PDFs → duplicate notes suffixed `_1`, `_2`, … (e.g. `Banking Control Law_10.md`). They resolve (0 broken links) but are noisy; proper fix = graph-level dedup + re-export/enrich.

### Sources
- Regulatory text: `corpus\markdown\`
- Page images (200 DPI): `assets\page-images\` — **not** for Graphify if MD exists
- Conversion QA: `reports\conversion\`
- Graph QA: `reports\graph\`

---

## 3. Key artifacts

| Path | Role |
|---|---|
| `deliverables\` | KYB / analysis Word docs |
| `docs\agents\00_orchestrator.md` | Orchestrator (routes Tasks) |
| `docs\agents\01_legal_compliance.md` | Legal/Compliance (Map→Dig owner) |
| `docs\agents\01a_corpus_mapper.md` | Corpus Mapper (Coverage Map) |
| `docs\agents\01b_corpus_extractor.md` | Corpus Extractor (Evidence Packs) |
| `docs\agents\02_completeness_reviewer.md` | Completeness Reviewer |
| `docs\agents\03_output_formatter.md` | Output Formatter |
| `docs\agents\query_config.md` | Query modes + hard rules |
| `docs\agents\README.md` | Map→Dig workflow |
| `.opencode\agents\*.md` | OpenCode primary/subagents |
| `reports\conversion\CONVERSION_QUALITY_REPORT.md` | PDF→MD quality |
| `reports\graph\GRAPH_QUALITY_AUDIT.md` | Graph/enrichment audit |

---

## 4. Analysis notes (Merchant / KYB — durable holdings)

- Merchant **is** a customer under AML/CTF (business relationship + settlement), not under BNPL “Consumer”.
- “Third party” ≠ merchant (CDD-reliance meaning).
- Minimum KYB → AML/CTF Guide §3.3; UBO ≥25% where applicable.
- PSP/payment-gateway merchants that receive settlement → KYB required under AML framing.

### Cross-regime sketch (verify against corpus before asserting)

| Regime | Notes | Instruments (examples) |
|---|---|---|
| Banking | Strong entity-type doc rules | `SAMA_EN_1644` |
| AML/CTF | CDD/EDD/SDD + BO | `SAMA_EN_1704`, `SAMA_EN_1428` |
| PSP / POS | Weaker explicit merchant KYC in payments instruments | e.g. `SAMA_EN_8725` |
| BNPL | Consumer CDD + store contract; store KYB may be gap | `SAMA_EN_6523` |
| Finance companies | Often defers to AML | `SAMA_EN_1023` |

BO tooling circulars (examples): Waatheq `10959`, NCNP `11005`, Awqaf `11104`.

---

## 5. Agent workflow (regulatory questions)

Do **not** merge voices. Order:

0. **Orchestrator** — Tab `orchestrator`; routes Legal → Reviewer → Formatter
1. **Legal/Compliance** — facets; Tasks **Mapper** then **Extractor**
2. **Corpus Mapper** — grep/graph → Coverage Map
3. **Corpus Extractor** — dig P1 stems → Evidence Packs
4. **Completeness Reviewer** — map dig hygiene; pushback to Legal
5. **Output Formatter** — Final answer / Coverage / Gaps / Sources

See `docs/agents/query_config.md` / `docs/agents/README.md`.  
**Corpus text wins** over the graph.

---

## 6. Commands (cheat sheet)

Prefer `README.md` if this section drifts.

```powershell
# graphify must be on PATH (verify: graphify --version)
$env:ANTHROPIC_API_KEY     = "<env only>"
$env:GRAPHIFY_VAULT_DIR    = "SAMA_Knowledge_Base_Obsidian"
$env:GRAPHIFY_ENRICH_MODEL = "claude-opus-4-8"
$env:TESSDATA_PREFIX       = "$PWD\tools\tessdata"

# Orchestrated pipeline (Graphify is manual — see GRAPHIFY.txt)
python tools\rulebook_run.py --mode first
python tools\rulebook_run.py --mode monthly

python tools\rulebook_scanner.py
python tools\rulebook_acquire.py
python tools\rulebook_compare.py
python tools\preprocess_pdfs.py --from-plan reports\rulebook\comparison.json
python tools\assess_conversion.py
python tools\rulebook_compare.py --update-baseline

# Graphify + enrichment (OpenCode, after preprocess)
graphify extract corpus --force --mode deep --backend claude --model claude-opus-4-8
Move-Item corpus\graphify-out graphify-out          # only after a fresh extract
graphify cluster-only . --backend claude --model claude-opus-4-8
graphify label . --backend claude --model claude-opus-4-8
graphify export obsidian --dir SAMA_Knowledge_Base_Obsidian
python tools\fix_wikilinks.py
python tools\enrich_graph_notes.py --force          # add --no-apply for a cache-only smoke test
python tools\audit_graph_quality.py
```

---

## 7. Layout pointer

Canonical tree: **`README.md`**.  
`scanner-sama-docs/` · `corpus/` · `assets/` · `tools/` · `reports/{rulebook,conversion,graph,runs}/` · `archive/` · `graphify-out/` · `docs/` · `deliverables/`

---

## 8. Open todos

- [ ] (Optional) Graph-level **node dedup** to collapse `_N` duplicate-label notes, then re-export + re-enrich.
- [ ] (Optional) Re-OCR the worst Grade-C Arabic PDFs to lift grounding above 86.7%.
- [ ] Monthly schedule once baseline is locked.

Done recently: full corpus (387 MD) extracted with `claude-opus-4-8` (1816 nodes / 1848 edges / 336 communities, ~$21); legal/compliance enrichment of all edges + communities (~$25-30) with Arabic-OCR guards; vault exported to `SAMA_Knowledge_Base_Obsidian` (2151 notes, 0 broken links); codebase hardened (requirements.txt, portable paths, correct enrich defaults); rulebook scanner+acquire; unified preprocess; compare+orchestrator; replace-on-update policy.

---

## 9. Recovery

1. Read this file + `README.md`.  
2. `graphify query "check graph state"`.  
3. If graph broken: `archive\graphify-snapshots\` or re-extract from `corpus`.

---

*End of session memory.*
