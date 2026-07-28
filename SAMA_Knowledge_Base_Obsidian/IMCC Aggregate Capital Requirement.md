---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Backtesting"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Backtesting
  - graphify/enriched
---

# IMCC Aggregate Capital Requirement

## Connections

### [[Expected Shortfall (ES) Model]] — `references` [EXTRACTED]
- **What this link tells you:** When aggregating IMA market-risk capital, understand that the ES model output feeds into the IMCC aggregate capital requirement rather than standing alone. The SMAR disclosure regime treats ES as one of the regulatory models whose coverage of the total capital requirement must be reported, and the IMCC is the internally-modelled aggregate charge into which the constrained/unconstrained ES results are combined. You would conclude that an ES result is an ingredient of the IMCC total and should be reconciled against the aggregate charge, not read as the final capital number.
- **Grounding — this node (Page 751 / Minimum capital requirement):** "Pillar 1 capital requirements at the reporting date. This will normally be RWA * 8% but may differ if a floor is applicable"
- **Grounding — related node (Page 475 / Art 13.2):** "ES must be computed on a daily basis for the bank-wide internal models to determine market risk capital requirements."
- **Caveat:** The IMCC node's provided context is disclosure/reporting text; the ES-to-IMCC aggregation mechanics are not directly quoted here, so confirm the IMA aggregation formula in the primary SMAR text before relying on it.

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
