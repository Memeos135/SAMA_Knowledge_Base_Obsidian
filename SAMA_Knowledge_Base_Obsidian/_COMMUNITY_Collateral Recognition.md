---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Collateral Recognition

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

Credit risk mitigation regime: which collateral types SAMA recognises and how they feed loss and exposure estimates. Sets eligibility and haircut/recognition conditions for reducing credit RWA.

## How members connect

- Supervisory LGD and EAD Estimates is the anchor: recognised collateral (financial receivables, real estate, other physical, leasing) feeds into supervisory loss and exposure parameters.
- Each collateral category references the others and is benchmarked against Commercial and Residential Real Estate Collateral as the reference recognition standard.
- Recognition of Leasing is treated by analogy to real-estate collateral, indicating shared eligibility and valuation conditions.

## Members
- [[Commercial and Residential Real Estate Collateral]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Other Physical Collateral]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Recognition of Financial Receivables]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Recognition of Leasing]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Supervisory LGD and EAD Estimates]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Collateral_Recognition
SORT file.name ASC
```
