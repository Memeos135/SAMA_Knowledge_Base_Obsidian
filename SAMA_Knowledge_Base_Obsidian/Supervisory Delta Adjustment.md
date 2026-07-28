---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Sensitivities"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# Supervisory Delta Adjustment

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When computing SA-CCR add-ons, the supervisory delta is a direct input into the effective notional: each trade's effective notional (𝐴�ᵢ) equals adjusted notional × maturity factor × supervisory delta (𝛼�ᵢ). The delta carries the sign (+1 long / -1 short for non-options) and the non-linearity of options, so it is what lets long and short positions offset within a hedging set. For a calculation-review decision, confirm that the delta is assigned per trade under 6.40–6.43 before the effective notional is derived; a wrong delta sign directly mis-states the effective notional and the resulting add-on.
- **Grounding — this node (Page 31 / 6.40):** "The supervisory delta adjustment (𝛼�𝑖) parameters are also defined at the trade i level and are applied to the adjusted notional amounts to reflect the direction of the transaction and its non-linearity."
- **Grounding — related node (Page 130 / 12.31):** "The effective notional for each trade in the netting set (𝐴�𝑖) is calculated using the formula 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖"

### [[Table 2 Summary of Supervisory Parameters|Table 2: Summary of Supervisory Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the supervisory delta for options, use the supervisory option volatility (𝜎ᵢ) prescribed in Table 2 rather than a bank-chosen figure—6.42 expressly directs to Table 2 in 6.75 for the volatility input. Table 2 fixes those parameters (e.g. 50% for interest rate, 15% for FX) by asset class and subclass. For a calculation-review decision, cross-check that any option delta uses the Table 2 volatility for the relevant asset class; substituting a market-implied or internal volatility would deviate from the standardized method.
- **Grounding — this node (Page 31 / 6.42(2)):** "The supervisory volatility 𝜎𝑖 an option is specified on the basis of supervisory factor applicable to the trade (see Table 2 in 6.75)."
- **Grounding — related node (Page 45 / 6.75 Table 2):** "Table 2 includes the supervisory factors, correlations and supervisory option volatility add-ons for each asset class and subclass."

#graphify/concept #graphify/INFERRED #community/Market_Risk_Sensitivities #graphify/enriched
