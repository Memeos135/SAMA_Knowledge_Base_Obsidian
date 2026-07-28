---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# G-SIB Indicators Template

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Identification of Global Systemically Important Banks through mandated indicator reporting (size, interconnectedness, complexity, cross-jurisdictional activity). Feeds systemic-risk classification and any resulting capital surcharge obligations.

## How members connect

- Single-member community: the GSIB1 template captures the indicator set used for G-SIB assessment.
- No internal edges; obligation is submission of the specified systemic indicators.

## Members
- [[Template GSIB1 G-SIB Indicators]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/G-SIB_Indicators_Template
SORT file.name ASC
```
