---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Leverage Ratio Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Leverage_Ratio_Exposures
  - graphify/enriched
---

# Leverage Ratio Exposure Measure

## Connections

### [[Derivative Exposures Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When building the leverage ratio denominator, derivative exposures are one of the four mandatory components of the exposure measure, so you must add RC plus PFE for derivatives to on-balance-sheet, SFT and OBS items. The exposure-measure rules (no netting, no collateral reduction) constrain how the derivative treatment in section 7.2 is applied — collateral received cannot reduce derivative exposure and the multiplier is fixed at one. Conclude that derivative treatment is a sub-component governed by the overarching exposure-measure prohibitions, not an independently optimizable figure.
- **Grounding — this node (Page 5 / 5.4):** "Exposure measure should include the following exposures... (ii) Derivative exposures"
- **Grounding — related node (Page 10 / 7.2.1):** "Exposures to derivatives includes the following components under the Leverage ratio exposure measure: (i) Replacement cost (RC) (ii) Potential future exposure (PFE)"

### [[Off-Balance Sheet Items  CCFs|Off-Balance Sheet Items / CCFs]] — `references` [EXTRACTED]
- **What this link tells you:** When compiling the exposure measure, do not omit off-balance-sheet items — they are the fourth mandatory component, covering commitments (even unconditionally cancellable), direct credit substitutes, acceptances and letters of credit, converted via CCFs using the standardized approach for credit risk. Section 7.4 defines the OBS treatment that feeds the exposure-measure total enumerated in 5.4. Conclude that OBS items must be brought on-measure through CCF conversion; the leverage ratio's non-risk-based backstop still captures contingent exposures.
- **Grounding — this node (Page 5 / 5.4):** "Exposure measure should include the following exposures... (iv) Off-balance sheet (OBS) items."
- **Grounding — related node (Page 29 / 7.4.1):** "OBS items include commitments (including liquidity facilities), whether or not unconditionally cancellable, direct credit substitutes, acceptances, standby letters of credit and trade letters of credit."

### [[SAMA Leverage Ratio Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing which entities and items fall within the leverage ratio, treat the exposure measure as the operative denominator defined by this framework document, not as a free-standing concept. The framework document sets scope (all domestic banks, consolidated and standalone, excluding foreign bank branches), the 3% minimum and quarterly Q17 reporting, while the exposure measure concept specifies what must be included or deducted (Tier 1 deductions, PVAs, securitizations, no liability deductions). Conclude that the exposure-measure rules only bite on entities within the document's stated scope and must be read together with its capital-measure and reporting requirements.
- **Grounding — this node (Page 5 / 6.1):** "Banks must not use physical or financial collateral, guarantees or other credit risk mitigation techniques to reduce the Leverage ratio exposure measure"
- **Grounding — related node (Page 4 / 5.1, 5.6):** "The Leverage ratio is defined as the capital measure (the numerator) divided by the exposure measure (the denominator)... Banks' Leverage ratio must be at least 3% at all time."

### [[Securities Financing Transaction Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring SFT exposure for the leverage ratio, apply the dedicated section 7.3 methodology rather than netting freely — SFT exposures are the third mandatory component of the exposure measure and netting is only recognized on a counterparty-by-counterparty basis under a legally enforceable qualifying master netting agreement. Absent a qualifying MNA, each transaction is its own netting set (Ei* = max{0, Ei – Ci}). Conclude that SFT netting relief is conditional on legal enforceability at default/insolvency, so you must verify enforceable MNA coverage before applying any offset in the denominator.
- **Grounding — this node (Page 7 / 5.4):** "Securities financing transaction (SFT) exposures... should be included in the Leverage ratio exposure measure except for the following"
- **Grounding — related node (Page 26 / 7.3.4):** "The effects of bilateral netting agreements for covering SFTs will be recognized on a counterparty-by-counterparty basis if the agreements are legally enforceable in each relevant jurisdiction"

#graphify/concept #graphify/EXTRACTED #community/Leverage_Ratio_Exposures #graphify/enriched
