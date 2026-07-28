---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Liquidity Coverage & Funding Ratios

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

Prudential liquidity regime: the two Basel-derived liquidity metrics SAMA imposes on banks — short-term Liquidity Coverage Ratio (LCR) and structural Net Stable Funding Ratio (NSFR) — with their disclosure templates.

## How members connect

- Hierarchy: the SLCR and SNSF standards set the binding calculation and minimum-ratio obligations; Templates LIQ1/LIQ2 are the mandated disclosure vehicles that operationalize them.
- LIQ1 references the SLCR standard (LCR reporting); LIQ2 references the SNSF standard (NSFR reporting).
- LIQ2's cross-reference to the SLCR standard reflects shared HQLA/inflow-outflow definitions used across both ratios, so defined terms must be read consistently.

## Members
- [[SLCR Liquidity Coverage Ratio Standard]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[SNSF Net Stable Funding Standard]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template LIQ1 Liquidity Coverage Ratio]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template LIQ2 Net Stable Funding Ratio]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Liquidity_Coverage__Funding_Ratios
SORT file.name ASC
```
