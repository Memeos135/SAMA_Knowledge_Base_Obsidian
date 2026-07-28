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

# Non-Modellable Risk Factor (NMRF)

## Connections

### [[Risk Factor Eligibility Test (RFET)]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a risk factor for capital purposes, treat NMRF status as the direct consequence of failing the RFET — the two are the two sides of a single eligibility decision. Art 11.13 sets the quantitative RFET thresholds (e.g. at least 24 real price observations per year with no 90-day gap below four, or 100 over 12 months); a factor that fails these, or is deemed to have unsuitable data, must be excluded from the ES model and capitalised as an NMRF under Art 11.23. A reviewer should therefore verify the RFET observation counts before accepting any factor as ES-eligible, and confirm that all failing factors carry the heavier NMRF (SES) capital treatment.
- **Grounding — this node (Page 105 / Art 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 101 / Art 11.13):** "To pass the RFET ... at least 24 real price observations per year ... or ... at least 100 'real' price observations over the previous 12 months"

### [[Stressed Expected Shortfall (SES)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital treatment of a bank's internal market-risk model, treat NMRF classification and the SES charge as a single consequence chain: any risk factor that fails the RFET or the modellability principles must be excluded from the ES model and instead attracts a Stressed Expected Shortfall (SES) capital requirement. The text expressly links the two — a non-modellable risk factor 'receives an SES capital requirement,' and Principle six governs the stressed-period data used to derive it. For a compliance review you would conclude that removing a factor from the ES model does not remove its capital burden; you should verify how the SES charge is computed per desk, since SES amounts also drive whether backtesting exceptions may be disregarded.
- **Grounding — this node (Page 105 / [11.23]):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 110):** "a non-modellable risk factor that receives an SES capital requirement that is in excess of the maximum of the APL loss or HPL loss for that day"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
