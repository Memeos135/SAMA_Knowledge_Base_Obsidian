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

# Stressed Expected Shortfall (SES)

## Connections

### [[IMCC (Aggregate Capital Requirement for Modellable Risk Factors)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** These two concepts appear to sit on opposite sides of the same internal-models capital calculation: IMCC is the aggregate charge for modellable risk factors captured in the ES model, while SES is the add-on charge for non-modellable factors excluded from it. The provided context does not contain a direct cross-reference between the IMCC and SES nodes, so the link is inferential — the connection is that a factor either flows into the ES/IMCC calculation or, on failing modellability, into SES. Before relying on this as an authoritative cross-reference, check the aggregate market-risk capital formula (referenced around [13.43]) in the primary text to confirm how IMCC and SES are summed.
- **Grounding — this node (Page 107 / Principle six):** "The data used to determine stressed expected shortfall (ESR,S) must be reflective of market prices observed and/or quoted in the period of stress"
- **Grounding — related node (Page 26 / [6.1]-[6.2]):** "the risk-weighted assets for market risk under the standardised approach are determined by multiplying the capital requirements"
- **Caveat:** Relation is 'conceptually_related_to'; the supplied context shows no explicit IMCC-SES cross-reference, so verify the aggregation rule in the primary standard before treating the two as formally linked.

### [[Non-Modellable Risk Factor (NMRF)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital treatment of a bank's internal market-risk model, treat NMRF classification and the SES charge as a single consequence chain: any risk factor that fails the RFET or the modellability principles must be excluded from the ES model and instead attracts a Stressed Expected Shortfall (SES) capital requirement. The text expressly links the two — a non-modellable risk factor 'receives an SES capital requirement,' and Principle six governs the stressed-period data used to derive it. For a compliance review you would conclude that removing a factor from the ES model does not remove its capital burden; you should verify how the SES charge is computed per desk, since SES amounts also drive whether backtesting exceptions may be disregarded.
- **Grounding — this node (Page 110):** "a non-modellable risk factor that receives an SES capital requirement that is in excess of the maximum of the APL loss or HPL loss for that day"
- **Grounding — related node (Page 105 / [11.23]):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
