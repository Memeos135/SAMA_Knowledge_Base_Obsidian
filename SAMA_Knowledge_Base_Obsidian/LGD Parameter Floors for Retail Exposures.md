---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "Retail Exposure Risk Parameters"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Retail_Exposure_Risk_Parameters
  - graphify/enriched
---

# LGD Parameter Floors for Retail Exposures

## Connections

### [[LGD Floor Calculation for Partially Secured Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When setting LGD inputs for the risk-weight formula, treat the partial-security weighting method and the applicable asset-class LGD floor as one mechanism: the partial-secured calculation blends the unsecured and secured floor values, so you must first identify the correct floors for the exposure class before averaging. The provided text sets out corporate LGD floors and the weighted-average method for partially secured exposures; the linked node covers the retail asset-class definitions and treatment where the corresponding retail floors apply. Conclude that you should verify which asset-class floor table applies to the exposure (corporate vs retail) before computing a partial-secured floor, since using the wrong table understates or overstates the LGD floor.
- **Grounding — this node (Page 32-33 / 7.55-7.60):** "the retail exposure class consists of the follow three sets of exposures ... Regulatory retail ... transactors ... Other retail"
- **Grounding — related node (Page 121 / 12.17):** "The LGD floor for a partially secured exposure is calculated as a weighted average of the unsecured LGD floor ... and the secured LGD floor"
- **Caveat:** The excerpt at 12.17 cross-refers to 'the table in paragraph 12.10'; the retail-specific LGD floor table is not fully reproduced in the provided context, so verify the exact retail floor values in the primary text before relying on the blended calculation.

### [[PD and LGD for Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** If you are estimating LGD for retail exposures under the advanced IRB approach, read the LGD parameter floors as a binding constraint layered on top of the retail PD/LGD estimation rules — floors set a regulatory minimum below which own-estimated LGD cannot fall. Both provisions operate within the same retail asset-class regime defined by paragraphs 7.55–7.60 and the sub-class segmentation, so the floor applies according to the same retail classification used for the parameter estimate. Check that any own-estimated retail LGD is compared against the applicable floor for its sub-class before it feeds into RWA, rather than treating the estimation and the floor as independent steps.
- **Grounding — this node (Page 33 / Para 7.57):** "“Regulatory retail” exposures are defined as retail exposures that meet all of the criteria listed below"
- **Grounding — related node (Page 98 / Para 10.21):** "Within the retail asset class category, banks are required to identify separately three sub-classes of exposures"
- **Caveat:** Both nodes share nearly identical retail-class context; the specific LGD-floor values are not shown in the provided excerpts, so verify the floor figures in the primary text.

#graphify/document #graphify/EXTRACTED #community/Retail_Exposure_Risk_Parameters #graphify/enriched
