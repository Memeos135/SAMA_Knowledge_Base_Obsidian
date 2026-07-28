---
source_file: "markdown/SAMA_EN_5419_VER1.md"
type: "concept"
community: "APR Calculation Rules"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/APR_Calculation_Rules
  - graphify/enriched
---

# APR Calculation Method (Net Present Value)

## Connections

### [[Annex 1 APR Calculation|Annex 1: APR Calculation]] — `semantically_similar_to` [INFERRED]
- **What this link tells you:** The APR Rules' NPV method and the Consumer Financing Regulations' Annex 1 appear to state substantially the same APR calculation, including the shared discount-rate definition and the same assumptions (contract validity for the agreed term, exclusion of non-compliance charges, treatment of unquantifiable variable charges, two-basis-point precision). One apparent divergence to verify: the APR Rules compute periods on a 365-day-year basis (Art 9), whereas Annex 1 states periods 'shall be based on a year of 12 equal months.' Before relying on a single method, confirm which day-count convention applies to your product, as the two instruments phrase this differently.
- **Grounding — this node (Page 16 / Art 9(1)):** "the date of each payment received or payable by the borrower shall be calculated on the basis of 365 days a year."
- **Grounding — related node (Page 35 / Annex 1):** "For the purpose of calculating APR, periods between dates shall be based on a year of 12 equal months."
- **Caveat:** INFERRED semantic similarity; the methods largely align but the day-count basis differs textually — verify the governing convention for the specific regime before treating them as identical.

### [[Rules Governing Calculation of APR]] — `references` [EXTRACTED]
- **What this link tells you:** When checking whether an APR computation is defensible, read this method as the prescribed calculation basis defined by the Rules, not an optional approach. Article 6 mandates the net present value method with the stated formula, and Article 1's definition of APR as the discount rate equating present value of borrower payments to present value of finance advanced fixes what the method must produce; Articles 9-10 then constrain inputs (365-day basis, fixed-rate assumption for floating cost, credit-card assumptions). You should conclude that the acceptable APR is uniquely determined by this NPV method plus the defined 'Total Cost of Finance' inputs, so deviations in methodology or excluded/included costs are compliance failures regardless of the headline rate quoted.
- **Grounding — this node (Page 12 / Art 1):** "APR: The discount rate at which the present value of payments ... equals the present value of all payments of the amount of financing available to the borrower"
- **Grounding — related node (Page 14 / Art 6):** "The APR should be calculated based on the net present value method using the following formula"

### [[SAMA APR Calculator (Excel)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Treat the SAMA Excel calculator and the net-present-value method as a single compliance obligation rather than alternatives: Article 4 mandates use of the SAMA-issued Excel calculator, and Article 6 specifies that APR be computed by the NPV method embodied in that tool. The calculator is the prescribed means of applying the method, and Article 5(2) requires providers using any automated tool to reconcile results against the SAMA Excel calculator. You would conclude that a firm's own APR figure is defensible only if the underlying method matches Article 6 and reconciles to the SAMA calculator output.
- **Grounding — this node (Page 14 / Art 6):** "The APR should be calculated based on the net present value method using the following formula."
- **Grounding — related node (Page 14 / Art 4):** "Finance providers shall utilize the Excel based calculator issued by SAMA for the purpose of implementing the Rules."
- **Caveat:** Link is INFERRED (both concepts drawn from same document); the operational tie is textually strong but the 'conceptually_related_to' label is analytic — confirm against Articles 4–6.

#graphify/concept #graphify/INFERRED #community/APR_Calculation_Rules #graphify/enriched
