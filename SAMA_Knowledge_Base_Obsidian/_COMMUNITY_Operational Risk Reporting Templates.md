---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Operational Risk Reporting Templates

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

Operational risk capital regime: the standard defining minimum operational-risk capital and the three disclosure templates capturing loss history, business indicator, and resulting capital charge.

## How members connect

- The SOPE standard is the governing rule; OR1 (historical losses) and OR3 (minimum required capital) reference it directly as their calculation basis.
- OR2 (business indicator and subcomponents) feeds OR3 — the indicator drives the capital figure, so the templates form a sequential input-to-output obligation chain.
- Read together the templates evidence compliance with the single capital requirement set in SOPE; definitions of loss and business-indicator components are anchored in that standard.

## Members
- [[SOPE Operational Risk Standard]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template OR1 Historical losses]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template OR2 Business indicator and subcomponents]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template OR3 Minimum required operational risk capital]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Operational_Risk_Reporting_Templates
SORT file.name ASC
```
