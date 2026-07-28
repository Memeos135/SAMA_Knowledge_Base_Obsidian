---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Trading Book Securitisation Exposures

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Trading-book securitisation exposure disclosure under the capital/market-risk regime. Covers how banks must report securitisation positions held in the trading book for Pillar 3 transparency.

## How members connect

- Single-member cluster (Template SEC2) with no internal edges; sits within the broader securitisation disclosure framework and is the quantitative counterpart to qualitative SECA (community 293).
- Decision consequence: banks must populate this template to evidence trading-book securitisation capital treatment; it scopes reporting to trading-book (not banking-book) positions.

## Members
- [[Template SEC2 Securitisation exposures in the trading book]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Trading_Book_Securitisation_Exposures
SORT file.name ASC
```
