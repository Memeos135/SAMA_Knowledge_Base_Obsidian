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

# Required Stable Funding (RSF)

## Connections

### [[NSFR Derivative Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's total RSF for NSFR compliance, treat NSFR derivative assets as one input line within the RSF calculation rather than a standalone metric. The RSF total is built by assigning carrying value to asset categories and applying RSF factors, and the derivative-asset amount (net of NSFR derivative liabilities where assets exceed liabilities, plus a 20% add-on on derivative liabilities) feeds directly into that sum. Conclude that any error in computing the netted derivative-asset figure propagates into the RSF denominator of the NSFR, so verify the net derivative treatment against Item #5 Section B before relying on a reported ratio.
- **Grounding — this node (Page 8 / Section B):** "The amount assigned to each category is then multiplied by its associated required stable funding (RSF) factor, and the total RSF is the sum of the weighted amounts"
- **Grounding — related node (Page 15 / item (b)):** "NSFR derivative assets as calculated according item# 5 ... Net of NSFR derivative liabilities ... if NSFR derivative assets are greater than NSFR derivative liabilities"

### [[Net Stable Funding Ratio (NSFR)]] — `references` [EXTRACTED]
- **What this link tells you:** When operationalising the NSFR, understand that RSF is one of the two defined components of the ratio itself: the NSFR is defined as available stable funding relative to required stable funding, so any RSF-factor determination directly drives the compliance numerator/denominator. RSF is measured by assigning asset and off-balance-sheet carrying values to categories and multiplying by category-specific RSF factors. Conclude that changes to how an asset is categorised (or its residual maturity/encumbrance treatment) feed straight into the ≥100% NSFR requirement, so RSF classification decisions are compliance-determinative, not merely descriptive.
- **Grounding — this node (Page 8 / Section B):** "The amount assigned to each category is then multiplied by its associated required stable funding (RSF) factor, and the total RSF is the sum of the weighted amounts"
- **Grounding — related node (Page 5 / Section 4):** "The NSFR is defined as the amount of available stable funding relative to the amount of required stable funding. This ratio should be equal to at least 100%"

### [[Off-Balance Sheet Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping RSF, do not limit the calculation to on-balance-sheet assets: off-balance-sheet (OBS) exposures are explicitly part of the required stable funding measure. Section B measures RSF from the liquidity risk profile of both assets and OBS exposures, adding OBS activity (or potential liquidity exposure) multiplied by its RSF factor to the weighted asset amounts. Conclude that omitting contingent/OBS items understates required stable funding, so confirm that OBS activity has been assigned an RSF factor when checking NSFR compliance.
- **Grounding — this node (Page 8 / Section B):** "the total RSF is the sum of the weighted amounts added to the amount of OBS activity (or potential liquidity exposure) multiplied by its associated RSF factor"
- **Grounding — related node (Page 8 / Section B heading):** "Definition of required stable funding for assets and off-balance sheet exposures"

#graphify/concept #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
