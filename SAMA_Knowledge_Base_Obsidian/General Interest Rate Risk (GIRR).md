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

# General Interest Rate Risk (GIRR)

## Connections

### [[PV01 Sensitivity]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating market-risk capital under SAMA's standardised sensitivities-based method, treat PV01 as the mechanical measure through which GIRR sensitivities are captured: a bank must express each interest-rate delta sensitivity as the value change from a one-basis-point shift, then net and risk-weight those PV01 sensitivities within the GIRR risk class. The link tells you GIRR is not a free-standing charge but is quantified through the PV01/delta sensitivity mechanics of [7.4] and [7.17]. In practice you would check that a bank's GIRR delta figures derive from the independent risk-control unit's pricing models and reconcile PV01 netting (e.g. offsetting opposite-direction swaps to zero) before accepting the reported GIRR capital number.
- **Grounding — this node (Page 387 / [7.4]):** "if a bank's portfolio is made of two interest rate swaps... but of opposite direction, the GIRR on that portfolio would be zero"
- **Grounding — related node (Page 402 / [7.20]):** "the bank can proxy PV01 to CS01"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising interest-rate positions in the trading book, treat GIRR as a defined risk class processed through the sensitivities-based method, so its delta, vega and curvature sensitivities are risk-weighted and aggregated with the other risk classes under the prescribed correlation scenarios. GIRR is expressly listed among the risk classes and interacts with SbM's three-scenario correlation calculation. Conclude that GIRR capital is not stand-alone but part of the SbM aggregation; confirm the applicable GIRR buckets and vertex/tenor rules before computing the charge.
- **Grounding — this node (Page 361):** "Risk class: ... general interest rate risk, credit spread risk ... FX risk, equity risk and commodity risk."
- **Grounding — related node (Page 383):** "the risk-weighted sensitivities are aggregated using specified correlation parameters ... a bank must calculate three sensitivities-based method capital requirement values."

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
