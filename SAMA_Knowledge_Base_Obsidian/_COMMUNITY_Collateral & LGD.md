---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Collateral & LGD

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Credit-risk capital/provisioning inputs, linking eligible collateral recognition to Loss Given Default estimation under the risk framework.

## How members connect

- Eligible Collateral and Valuation references LGD: recognized, properly valued collateral reduces the LGD applied to an exposure.
- Defined eligibility and valuation criteria act as a scope limit — only collateral meeting those standards may lower LGD.
- Consequence for compliance: mis-valued or ineligible collateral cannot be used to reduce provisioning/capital, affecting credit-risk calculations.

## Members
- [[Eligible Collateral and Valuation]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Loss Given Default (LGD)]] - concept - markdown/SAMA_EN_11055_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Collateral__LGD
SORT file.name ASC
```
