---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "concept"
community: "Default Risk Internal Model"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default_Risk_Internal_Model
  - graphify/enriched
---

# Value-at-Risk (VaR)

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying whether a bank's backtesting is being performed correctly for capital purposes, note that VaR is the benchmark against which the test operates: an 'exception' is defined as a day where actual or hypothetical loss exceeds the model's daily VaR. The standard fixes the VaR calibration used — a one-day holding period at the 99th percentile confidence level — so a reviewer checking exception counts must confirm the VaR measure is calibrated on that basis before the green/amber/red zone consequences apply. Conclude that any backtesting result is only meaningful, and any add-on or model disallowance defensible, when tied to a properly calibrated VaR measure as defined in the standard.
- **Grounding — this node (Page 6 (glossary)):** "Value at risk (VaR): A measure of the worst expected loss on a portfolio of instruments resulting from market movements over a given time horizon and a pre-defined confidence level."
- **Grounding — related node (Page 109 / 12.4–12.5):** "Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL)"

### [[DRC Requirement Internal Model]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's internal models approach (IMA) for market risk capital under this SAMA framework, treat Default Risk Charge (DRC) modelling and Value-at-Risk as distinct but co-resident components of the same IMA capital calculation, not interchangeable measures. VaR is defined in the glossary as a measure of worst expected loss over a horizon at a confidence level, whereas the DRC internal model captures jump-to-default losses not reflected in ordinary price-movement measures; both feed the IMA capital requirement subject to the validation, backtesting and independent risk-control obligations in [10]. Consequently, verify that a bank approved for IMA runs and validates each measure on its own terms — you cannot infer DRC adequacy from VaR/backtesting results, and each must independently satisfy SAMA's model-validation and governance requirements.
- **Grounding — this node (Page 6 (glossary)):** "Value at risk (VaR): A measure of the worst expected loss on a portfolio of instruments resulting from market movements over a given time horizon and a pre-defined confidence level."
- **Grounding — related node (Page 92 / 10.8):** "A distinct unit of the bank... must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements."

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Internal_Model #graphify/enriched
