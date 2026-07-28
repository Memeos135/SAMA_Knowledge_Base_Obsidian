---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Retail Exposure Risk Parameters

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

IRB credit-risk parameter regime for retail exposures: how banks estimate PD/LGD and apply mandatory regulatory floors when modelling retail credit risk.

## How members connect

- 'Risk Components for Retail Exposures' and 'PD and LGD for Retail Exposures' establish the parameter-estimation requirements; the two LGD-floor provisions constrain those estimates.
- 'LGD Parameter Floors' scopes/limits the PD-LGD estimates by imposing minimum LGD values that override lower modelled outputs.
- The partially-secured LGD floor calculation is a specific application of the general floor rule — an exception/detail branch handling collateral-mismatched exposures.

## Members
- [[LGD Floor Calculation for Partially Secured Exposures]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[LGD Parameter Floors for Retail Exposures]] - document - markdown/SAMA_EN_3502_VER1.md
- [[PD and LGD for Retail Exposures]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Risk Components for Retail Exposures]] - concept - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Retail_Exposure_Risk_Parameters
SORT file.name ASC
```
