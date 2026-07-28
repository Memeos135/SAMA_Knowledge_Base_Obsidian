---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Interest Rate Shock Scenarios

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

SAMA's standardised interest-rate-risk-in-the-banking-book (IRRBB) shock scenarios; a supervisory measurement framework defining prescribed rate movements banks must apply in stress testing.

## How members connect

- Standardised Interest Rate Shock Scenarios is the parent provision that references each individual scenario (parallel, short-rate, long-rate) as mandated inputs.
- Rotation Shocks (steepener/flattener) are composite scenarios derived from the short- and long-rate shocks, so they depend on those definitions.
- No hierarchy of law/circular here — these are technical sub-components of a single supervisory methodology; compliance means applying all prescribed scenarios, not choosing among them.

## Members
- [[Long Rate Shock Scenario]] - concept - markdown/SAMA_EN_10621_VER1.md
- [[Parallel Shock Scenario]] - concept - markdown/SAMA_EN_10621_VER1.md
- [[Rotation Shocks (SteepenerFlattener)]] - concept - markdown/SAMA_EN_10621_VER1.md
- [[Short Rate Shock Scenario]] - concept - markdown/SAMA_EN_10621_VER1.md
- [[Standardised Interest Rate Shock Scenarios]] - document - markdown/SAMA_EN_10621_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Interest_Rate_Shock_Scenarios
SORT file.name ASC
```
