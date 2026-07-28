---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# IRRBB Risk Management

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Interest Rate Risk in the Banking Book (IRRBB) disclosure under SAMA's Pillar 3 regime — the obligation to describe governance/measurement of IRRBB and to report quantitative sensitivity figures.

## How members connect

- Table IRRBBA sets qualitative disclosure of IRRBB management (governance, assumptions, hedging); Template IRRBB1 reports the quantitative outcomes.
- The 'references' link means the numbers in IRRBB1 are only interpretable against the modelling assumptions and controls disclosed in IRRBBA — read as one disclosure package.
- Both implement SAMA's adoption of the Basel IRRBB standard; qualitative context is a precondition for meaningful quantitative reporting.

## Members
- [[Table IRRBBA IRRBB Risk Management]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template IRRBB1 Quantitative IRRBB Info]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IRRBB_Risk_Management
SORT file.name ASC
```
