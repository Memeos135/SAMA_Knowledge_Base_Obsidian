---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Risk-Weighted Assets Overview"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Risk-Weighted_Assets_Overview
  - graphify/enriched
---

# Risk-Weighted Assets

## Connections

### [[Output Floor Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a domestic bank's capital adequacy, treat the output floor not as a standalone rule but as a constraint applied on top of the RWA calculation, because the floor is expressly defined as a limit on RWAs derived from internal models relative to standardised-approach outputs. The Output Floor Requirements reference RWA as the object being floored, and prohibit certain modelled approaches (IRB, SEC-IRBA, IMA, VaR, IMM) from the floor base. You should conclude that any RWA figure reported to SAMA must be reconciled against the floored calculation, and that internal-model RWAs cannot fall below the calibrated percentage of standardised RWAs.
- **Grounding — this node (Page 490 / 14.1):** "The risk-weighted assets for market risk under the simplified standardised approach are determined by multiplying the capital requirements ... by 12.5"
- **Grounding — related node (Page 729 / para 1.1):** "banks using internal models to derive RWAs will be subject to a floor requirement that is applied to RWAs"

### [[RWA for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When decomposing a bank's total RWA, treat RWA for credit risk as a defined subset of the aggregate RWA concept, with strict scope boundaries: it expressly excludes counterparty credit risk, credit valuation adjustments and securitisation exposures in the banking book, each reported elsewhere. This matters because misclassifying an exposure between credit-risk RWA and these excluded categories distorts both the standardised/modelled split and the floor base. You should check that credit-risk RWA is scoped per SCRE (row 1) and that excluded positions are carried into their designated rows/sections rather than double-counted.
- **Grounding — this node (Page 751):** "Credit risk (excluding counterparty credit risk): RWA and capital requirements according to the credit risk standard of the Basel framework (SCRE)"
- **Grounding — related node (Page 755 / row 1):** "Credit risk (excluding counterparty credit risk, credit valuation adjustments and securitisation exposures in the banking book)"

### [[RWA for Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring a bank's market-risk capital, treat RWA for market risk as a component of total RWA computed by converting the capital requirement into RWA via the 12.5 multiplier, under either the IMA or the (simplified) standardised approach. This scoping matters because market-risk RWA is a distinct row from credit-risk RWA and feeds separately into the aggregate and the output floor's modelled-vs-standardised comparison. You should conclude that market-risk RWA must be derived using the prescribed capital-requirement-times-12.5 method for the applicable approach, and reported in its own line rather than blended with credit risk.
- **Grounding — this node (Page 490 / 13.46):** "The risk-weighted assets for market risk under the IMA are determined by multiplying the capital requirements ... by 12.5"
- **Grounding — related node (Page 751):** "Minimum capital requirement T ... This will normally be RWA * 8% but may differ if a floor is applicable"

### [[RWA for Operational Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's total Pillar 1 capital requirement under SAMA's capital framework, treat operational risk RWA as a distinct, additive component of the overall RWA aggregate — not a subset of market or credit risk. The framework computes total RWA by summing separately-calculated credit, market and operational risk charges (each converted to RWA, e.g. capital requirement × 12.5), so a change in the operational risk methodology affects the denominator of the capital ratio independently. For a compliance decision, verify that operational risk RWA is calculated per its own chapter and added, and do not net or offset it against the other risk classes.
- **Grounding — this node (Page 490 / 14.1):** "The risk-weighted assets for market risk under the simplified standardised approach are determined by multiplying the capital requirements... by 12.5."
- **Grounding — related node (Page 751):** "Minimum capital requirement T: Pillar 1 capital requirements at the reporting date. This will normally be RWA * 8%"

#graphify/concept #graphify/EXTRACTED #community/Risk-Weighted_Assets_Overview #graphify/enriched
