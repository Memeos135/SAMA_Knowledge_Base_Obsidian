---
source_file: "markdown/SAMA_EN_3467_VER1.md"
type: "concept"
community: "LCR & NSFR Metrics"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/LCR__NSFR_Metrics
  - graphify/enriched
---

# NSFR Derivative Assets

## Connections

### [[Circular 351000133367 (Leverage Ratio)]] — `cites` [EXTRACTED]
- **What this link tells you:** When calculating NSFR derivative assets, the replacement-cost, netting and collateral-offset rules are governed by the Leverage Ratio circular rather than invented in the NSFR guidance. The NSFR text ties eligible bilateral netting to paragraph 20 and the cash variation margin offset to paragraph 24 of Circular No. 351000133367, and otherwise bars collateral from offsetting positive replacement cost. Conclude that whether a derivative asset may be shown net, and whether margin may reduce it, must be validated against that circular's paragraph 20/24 conditions before the derivative-asset amount is entered into the RSF calculation.
- **Grounding — this node (Page 10):** "In calculating NSFR derivative assets, collateral received in connection with derivative contracts may not offset the positive replacement cost amount ... unless it is received in the form of cash variation margin"
- **Grounding — related node (Page 10):** "unless it is received in the form of cash variation margin and meets the conditions as specified in paragraph 24 of the Circular No. 351000133367"

### [[NSFR Derivative Liabilities]] — `shares_data_with` [INFERRED]
- **What this link tells you:** These two items appear operationally linked because each is defined by reference to the other: NSFR derivative assets are measured net of NSFR derivative liabilities where assets exceed liabilities, and derivative liabilities are measured net of derivative assets in the opposite case. This mutual netting means the same replacement-cost inputs and margin treatment feed both figures, so they should be computed together, not independently. Because this 'shares data with' link is inferred, verify against Item #5 Sections A and B that the netting direction and the exclusion of collateral/variation margin have been applied consistently before relying on either figure.
- **Grounding — this node (Page 15 / item (b)):** "Net of NSFR derivative liabilities ... if NSFR derivative assets are greater than NSFR derivative liabilities"
- **Grounding — related node (Page 12 / item (c)):** "Net of NSFR derivative assets ... if NSFR derivative liabilities are greater than NSFR derivative assets"
- **Caveat:** Relationship is INFERRED from the reciprocal netting language; the source frames these as calculation inputs rather than a shared data store — confirm the netting mechanics in Item #5 before relying on the characterisation.

### [[Required Stable Funding (RSF)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's total RSF for NSFR compliance, treat NSFR derivative assets as one input line within the RSF calculation rather than a standalone metric. The RSF total is built by assigning carrying value to asset categories and applying RSF factors, and the derivative-asset amount (net of NSFR derivative liabilities where assets exceed liabilities, plus a 20% add-on on derivative liabilities) feeds directly into that sum. Conclude that any error in computing the netted derivative-asset figure propagates into the RSF denominator of the NSFR, so verify the net derivative treatment against Item #5 Section B before relying on a reported ratio.
- **Grounding — this node (Page 15 / item (b)):** "NSFR derivative assets as calculated according item# 5 ... Net of NSFR derivative liabilities ... if NSFR derivative assets are greater than NSFR derivative liabilities"
- **Grounding — related node (Page 8 / Section B):** "The amount assigned to each category is then multiplied by its associated required stable funding (RSF) factor, and the total RSF is the sum of the weighted amounts"

#graphify/concept #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
