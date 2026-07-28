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

# Risk Factor Eligibility Test (RFET)

## Connections

### [[Expected Shortfall (ES)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When deciding whether a given risk factor may enter the ES model at all, treat the RFET as the gatekeeper to ES eligibility. Under Art 11.23, a risk factor that fails the RFET (or whose data SAMA deems unsuitable) must be excluded from the ES model and instead capitalised as an NMRF; passing the RFET is a precondition, not a guarantee, since [11.25]-[11.26] impose further modellability principles. A reviewer should therefore check RFET results before accepting that any risk factor is legitimately captured within ES, rather than assuming ES coverage is complete.
- **Grounding — this node (Page 105 / Art 11.23, 11.26):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 118 / Art 13.1):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Caveat:** Relation is 'conceptually_related_to'; the ES/RFET dependency is well supported textually but confirm the precise eligibility articles ([11.13], [11.23]) in the primary text before relying on scope boundaries.

### [[Non-Modellable Risk Factor (NMRF)]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a risk factor for capital purposes, treat NMRF status as the direct consequence of failing the RFET — the two are the two sides of a single eligibility decision. Art 11.13 sets the quantitative RFET thresholds (e.g. at least 24 real price observations per year with no 90-day gap below four, or 100 over 12 months); a factor that fails these, or is deemed to have unsuitable data, must be excluded from the ES model and capitalised as an NMRF under Art 11.23. A reviewer should therefore verify the RFET observation counts before accepting any factor as ES-eligible, and confirm that all failing factors carry the heavier NMRF (SES) capital treatment.
- **Grounding — this node (Page 101 / Art 11.13):** "To pass the RFET ... at least 24 real price observations per year ... or ... at least 100 'real' price observations over the previous 12 months"
- **Grounding — related node (Page 105 / Art 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"

### [[P&L Attribution (PLA) Test]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When determining which portfolio remains in scope for IMA capital, note that the PLA test and RFET results are consumed together in the same quarterly scope-update exercise. Art 12.7 requires the bank-wide backtesting scope to be updated quarterly based on the latest desk-level backtesting, RFET and PLA test results — so a desk's IMA eligibility depends jointly on these tests, not any one in isolation. A reviewer should therefore check that RFET and PLA outcomes are reconciled to the same quarterly cycle before concluding a desk is validly modelled.
- **Grounding — this node (Page 101 / Art 11.13):** "To pass the RFET, a risk factor ... must meet either of the following criteria on a quarterly basis."
- **Grounding — related node (Page 110 / Art 12.7):** "The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests."
- **Caveat:** Both tests feed the same quarterly scope determination; the label 'shares_data_with' overstates a direct data dependency — the link is that both results are jointly assessed under Art 12.7, not that one supplies inputs to the other.

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
