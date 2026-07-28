---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Retail Exposure Risk Parameters"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Retail_Exposure_Risk_Parameters
  - graphify/enriched
---

# LGD Floor Calculation for Partially Secured Exposures

## Connections

### [[LGD Parameter Floors for Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When setting LGD inputs for the risk-weight formula, treat the partial-security weighting method and the applicable asset-class LGD floor as one mechanism: the partial-secured calculation blends the unsecured and secured floor values, so you must first identify the correct floors for the exposure class before averaging. The provided text sets out corporate LGD floors and the weighted-average method for partially secured exposures; the linked node covers the retail asset-class definitions and treatment where the corresponding retail floors apply. Conclude that you should verify which asset-class floor table applies to the exposure (corporate vs retail) before computing a partial-secured floor, since using the wrong table understates or overstates the LGD floor.
- **Grounding — this node (Page 121 / 12.17):** "The LGD floor for a partially secured exposure is calculated as a weighted average of the unsecured LGD floor ... and the secured LGD floor"
- **Grounding — related node (Page 32-33 / 7.55-7.60):** "the retail exposure class consists of the follow three sets of exposures ... Regulatory retail ... transactors ... Other retail"
- **Caveat:** The excerpt at 12.17 cross-refers to 'the table in paragraph 12.10'; the retail-specific LGD floor table is not fully reproduced in the provided context, so verify the exact retail floor values in the primary text before relying on the blended calculation.

#graphify/concept #graphify/EXTRACTED #community/Retail_Exposure_Risk_Parameters #graphify/enriched
