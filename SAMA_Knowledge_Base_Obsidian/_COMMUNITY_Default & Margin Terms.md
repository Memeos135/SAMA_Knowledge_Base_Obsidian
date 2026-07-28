---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Default & Margin Terms

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

Contractual close-out/collateral terminology, defined terms governing default and margining in secured/derivative-style financial agreements — the mechanics triggered when a counterparty fails.

## How members connect

- Event of Default is the trigger term; on its occurrence, Default Market Value governs how exposures are valued for close-out, hence the reference link.
- Exercise Notice is the procedural act conceptually tied to enforcing rights following an Event of Default.
- Margin Maintenance references Default Market Value because maintenance calls and shortfalls are measured against that valuation basis.

## Members
- [[Default Market Value]] - concept - markdown/SAMA_EN_6073_VER1.md
- [[Event of Default]] - concept - markdown/SAMA_EN_6073_VER1.md
- [[Exercise Notice]] - concept - markdown/SAMA_EN_6073_VER1.md
- [[Margin Maintenance]] - concept - markdown/SAMA_EN_6073_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Default__Margin_Terms
SORT file.name ASC
```
