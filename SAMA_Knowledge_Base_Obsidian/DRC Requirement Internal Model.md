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

# DRC Requirement Internal Model

## Connections

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** This cross-reference between the IRB credit-risk regime (capital adequacy document) and the DRC internal model (market-risk document) appears to reflect the conceptual overlap in modelling default risk across the banking and trading books rather than a direct textual obligation link. The provided excerpts for the DRC node concern independent model validation and backtesting generally, not an explicit IRB citation, so the connection reads as thematic. Treat this as a lead only and verify the primary DRC text (SMAR default-risk-charge provisions) for any actual IRB parameter cross-reference before relying on it.
- **Grounding — this node (Page 92 / Art 10.8):** "must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements"
- **Grounding — related node (Page 755):** "subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB)"
- **Caveat:** Relation inferred from thematic model-risk overlap; provided DRC excerpts do not textually cite the IRB approach. Verify the primary DRC provisions before relying on a direct link.

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping what a bank must build and validate to run the IMA, do not treat the default risk charge (DRC) internal model as a standalone product — it is one of the internal models that must be independently validated at least annually under the IMA qualitative criteria before SAMA will permit its use for capital purposes. The framework requires that all internal models used to determine market risk capital, including the DRC model, satisfy the [10.5]–[10.16] qualitative evaluation and obtain SAMA model approval. Conclude that DRC-model outputs cannot be relied upon for regulatory capital unless the DRC model itself has passed the IMA validation and approval gates that govern the broader internal-models regime.
- **Grounding — this node (Page 92 / 10.8):** "The model validation unit must validate all internal models used for purposes of the IMA on at least an annual basis."
- **Grounding — related node (Page 11 / 3.9):** "internal models approach (IMA) for market risk as described in [10] to [13]. SAMA approval is required before using the IMA approach."

### [[Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses an internal model (IMA) for default risk capital, LGD is not a free parameter — [13.38] requires use of the bank's SAMA-approved IRB LGD estimates where they exist. This links the DRC internal model to the LGD input via the same default-risk modelling regime ([13.18]–[13.20]), which itself is contingent on desk-level SAMA approval for credit spread and default risk. A reviewer should confirm the model draws on approved IRB LGD estimates (and IRB-consistent PDs), since desks without SAMA approval fall out of the IMA and revert to the standardised DRC framework where LGD is fixed by rule (e.g. 100% / 75%).
- **Grounding — this node (Page 131 / 13.38; Page 127 / 13.18):** "Banks must have a separate internal model to measure the default risk of trading book positions... Where a bank has approved loss-given-default (LGD) estimates as part of th[e IRB approach]"
- **Grounding — related node (Page 75 / 8.12):** "For calculating the gross JTD, LGD is set as follows: Equity instruments and non-senior debt instruments are assigned an LGD of 100%... Senior debt instruments are assigned an LGD of 75%."
- **Caveat:** Node B's LGD context is the standardised (fixed-percentage) treatment, while the DRC internal-model LGD linkage sits at [13.38] where the IRB LGD sentence is truncated in the provided text; verify the full IMA LGD conditions in the primary source.

### [[Value-at-Risk (VaR)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's internal models approach (IMA) for market risk capital under this SAMA framework, treat Default Risk Charge (DRC) modelling and Value-at-Risk as distinct but co-resident components of the same IMA capital calculation, not interchangeable measures. VaR is defined in the glossary as a measure of worst expected loss over a horizon at a confidence level, whereas the DRC internal model captures jump-to-default losses not reflected in ordinary price-movement measures; both feed the IMA capital requirement subject to the validation, backtesting and independent risk-control obligations in [10]. Consequently, verify that a bank approved for IMA runs and validates each measure on its own terms — you cannot infer DRC adequacy from VaR/backtesting results, and each must independently satisfy SAMA's model-validation and governance requirements.
- **Grounding — this node (Page 92 / 10.8):** "A distinct unit of the bank... must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements."
- **Grounding — related node (Page 6 (glossary)):** "Value at risk (VaR): A measure of the worst expected loss on a portfolio of instruments resulting from market movements over a given time horizon and a pre-defined confidence level."

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Internal_Model #graphify/enriched
