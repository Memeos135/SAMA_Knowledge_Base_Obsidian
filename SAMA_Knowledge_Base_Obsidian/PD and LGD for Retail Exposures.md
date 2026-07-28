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

# PD and LGD for Retail Exposures

## Connections

### [[LGD Parameter Floors for Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** If you are estimating LGD for retail exposures under the advanced IRB approach, read the LGD parameter floors as a binding constraint layered on top of the retail PD/LGD estimation rules — floors set a regulatory minimum below which own-estimated LGD cannot fall. Both provisions operate within the same retail asset-class regime defined by paragraphs 7.55–7.60 and the sub-class segmentation, so the floor applies according to the same retail classification used for the parameter estimate. Check that any own-estimated retail LGD is compared against the applicable floor for its sub-class before it feeds into RWA, rather than treating the estimation and the floor as independent steps.
- **Grounding — this node (Page 98 / Para 10.21):** "Within the retail asset class category, banks are required to identify separately three sub-classes of exposures"
- **Grounding — related node (Page 33 / Para 7.57):** "“Regulatory retail” exposures are defined as retail exposures that meet all of the criteria listed below"
- **Caveat:** Both nodes share nearly identical retail-class context; the specific LGD-floor values are not shown in the provided excerpts, so verify the floor figures in the primary text.

### [[Risk Components for Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When determining IRB risk components for retail exposures, treat these two provisions as parts of one integrated retail regime: the retail exposure class definition (regulatory retail, transactors, other retail, and the QRRE sub-class) sets the segmentation that the PD/LGD estimation applies to. The link matters because retail PD and LGD must be estimated at the pool/sub-portfolio level consistent with the three retail sub-classes (residential mortgage, QRRE, other retail), so a misclassification at the definitional stage flows directly into the risk parameters and RWA. Confirm which sub-class an exposure falls into under paragraphs 7.55–7.59 and 10.21–10.22 before assigning risk components.
- **Grounding — this node (Page 33 / Para 7.60):** "The risk weights that apply to exposures in the retail asset class are as follows... risk weighted at 75%... 45%... 100%."
- **Grounding — related node (Page 98 / Para 10.21):** "Within the retail asset class category, banks are required to identify separately three sub-classes of exposures"

#graphify/concept #graphify/EXTRACTED #community/Retail_Exposure_Risk_Parameters #graphify/enriched
