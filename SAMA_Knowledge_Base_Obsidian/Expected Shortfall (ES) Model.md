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

# Expected Shortfall (ES) Model

## Connections

### [[IMCC Aggregate Capital Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When aggregating IMA market-risk capital, understand that the ES model output feeds into the IMCC aggregate capital requirement rather than standing alone. The SMAR disclosure regime treats ES as one of the regulatory models whose coverage of the total capital requirement must be reported, and the IMCC is the internally-modelled aggregate charge into which the constrained/unconstrained ES results are combined. You would conclude that an ES result is an ingredient of the IMCC total and should be reconciled against the aggregate charge, not read as the final capital number.
- **Grounding — this node (Page 475 / Art 13.2):** "ES must be computed on a daily basis for the bank-wide internal models to determine market risk capital requirements."
- **Grounding — related node (Page 751 / Minimum capital requirement):** "Pillar 1 capital requirements at the reporting date. This will normally be RWA * 8% but may differ if a floor is applicable"
- **Caveat:** The IMCC node's provided context is disclosure/reporting text; the ES-to-IMCC aggregation mechanics are not directly quoted here, so confirm the IMA aggregation formula in the primary SMAR text before relying on it.

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a bank must model to use the IMA, the ES model is the core measure — it, together with DRC and SES, comprises the IMA capital computation. A risk factor that fails SAMA's data/modellability standards must be excluded from the ES model and instead capitalised as a non-modellable risk factor (NMRF/SES), which affects both the capital number and disclosure. Conclude that IMA reliance depends on risk factors qualifying for ES modelling; check risk-factor eligibility (RFET) and SAMA's modellability principles before assuming a factor sits inside the ES model rather than attracting an NMRF charge.
- **Grounding — this node (Page 461):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 843):** "For ES models, banks must provide the following information: (a) A description of trading desks covered by the ES models"

### [[Liquidity Horizon]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the ES capital measure, treat liquidity horizons as a mandatory scaling input rather than an optional refinement. Para 13.4 requires the liquidity horizons in [13.12]/Table 2 to be reflected by scaling an ES computed at a 10-day base horizon, with different horizons (10 to 120 days) assigned per risk-factor category. You would conclude that an ES figure cannot be validated without confirming the correct liquidity-horizon assignment for each risk factor, since the horizon directly changes the capital output.
- **Grounding — this node (Page 475 / Art 13.4):** "the liquidity horizons described in [13.12] must be reflected by scaling an ES calculated on a base horizon... base liquidity horizon of 10 days"
- **Grounding — related node (Page 479 / Table 2):** "Liquidity horizon n by risk factor... Interest rate: specified currencies ... 10 ... Credit spread: volatility 120"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
