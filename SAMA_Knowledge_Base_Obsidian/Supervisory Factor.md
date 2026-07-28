---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "SA-CCR Supervisory Parameters"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR_Supervisory_Parameters
  - graphify/enriched
---

# Supervisory Factor

## Connections

### [[Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When validating the interest-rate add-on within SA-CCR, note that the add-on cannot be computed without the prescribed supervisory factor: 6.47 states supervisory factors convert effective notional amounts into the add-on for each hedging set, and the interest-rate add-on (6.59) relies on these calibrated values. This link tells you the interest-rate charge is driven by a fixed regulatory parameter, not a bank estimate, so the correct value must be drawn from Table 2 (6.75). When checking an IR add-on figure, confirm the supervisory factor used matches the prescribed interest-rate value rather than any internally modelled volatility.
- **Grounding — this node (Page 34 / 6.47):** "Supervisory factors (SF) are used, together with aggregation formulas, to convert effective notional amounts into the add-on for each hedging set"
- **Grounding — related node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated"

### [[Table 2 Summary of Supervisory Parameters|Table 2: Summary of Supervisory Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When applying any asset-class add-on formula, the supervisory factor is not a free choice — its authoritative numeric values are fixed in Table 2 under 6.75 (e.g. 0.50% for interest rate, 4.0% for FX, and graded credit factors by rating). This link tells you the defined term 'supervisory factor' resolves to specific prescribed figures, and banks are barred from substituting their own estimates. When reviewing a capital calculation, cross-check the supervisory factor applied against the Table 2 value for the relevant asset class and subclass before relying on the result.
- **Grounding — this node (Page 27 / (7)):** "The supervisory factor is the supervisory specified change in value of the underlying risk factor on which the potential future exposure calculation is based"
- **Grounding — related node (Page 45 / 6.75, Table 2):** "Table 2 includes the supervisory factors, correlations and supervisory option volatility add-ons for each asset class and subclass"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Supervisory_Parameters #graphify/enriched
