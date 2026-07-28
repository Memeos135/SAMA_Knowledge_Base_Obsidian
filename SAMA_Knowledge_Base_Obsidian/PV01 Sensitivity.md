---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Sensitivities"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# PV01 Sensitivity

## Connections

### [[Delta Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring delta sensitivities for interest-rate (GIRR) instruments, treat PV01 as the sensitivity input to the delta-risk calculation, and note the explicit fallback permission linking it to CS01. Under the same SAMA Market Risk standard, delta risk requires prescribed sensitivities (7.15–7.38); PV01 is defined there and 7.20 states that where a bank lacks counterparty-specific money market curves it 'can proxy PV01 to CS01.' You should conclude that PV01 is a mandatory delta input and that the PV01-to-CS01 proxy is a conditional allowance, not a free substitution — check whether the money-market-curve condition is met before relying on it.
- **Grounding — this node (SAMA_EN_3487_VER1.md / Page 402 (7.20)):** "In cases where the bank does not have counterparty-specific money market curves, the bank can proxy PV01 to CS01"
- **Grounding — related node (SAMA_EN_3487_VER1.md / Page 387 (7.4)):** "For each risk factor ... a sensitivity is determined as set out in [7.15] to [7.38]."

### [[General Interest Rate Risk (GIRR)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating market-risk capital under SAMA's standardised sensitivities-based method, treat PV01 as the mechanical measure through which GIRR sensitivities are captured: a bank must express each interest-rate delta sensitivity as the value change from a one-basis-point shift, then net and risk-weight those PV01 sensitivities within the GIRR risk class. The link tells you GIRR is not a free-standing charge but is quantified through the PV01/delta sensitivity mechanics of [7.4] and [7.17]. In practice you would check that a bank's GIRR delta figures derive from the independent risk-control unit's pricing models and reconcile PV01 netting (e.g. offsetting opposite-direction swaps to zero) before accepting the reported GIRR capital number.
- **Grounding — this node (Page 402 / [7.20]):** "the bank can proxy PV01 to CS01"
- **Grounding — related node (Page 387 / [7.4]):** "if a bank's portfolio is made of two interest rate swaps... but of opposite direction, the GIRR on that portfolio would be zero"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
