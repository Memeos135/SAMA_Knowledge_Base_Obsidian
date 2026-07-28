---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR Derivative Add-ons"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR_Derivative_Add-ons
  - graphify/enriched
---

# Add-on for Foreign Exchange Derivatives

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the SA-CCR PFE add-on for FX derivatives for capital purposes, do not treat the FX add-on formula as self-contained: it is built directly on the effective notional defined earlier in the framework. Under 6.62 Step 1, the FX asset-class add-on begins by calculating each trade's effective notional as the product of adjusted notional, supervisory delta and maturity factor (Ai = di × MFi × δi), then aggregates these by currency-pair hedging set before applying the 4% supervisory factor. Conclude that any error or definitional choice in the effective-notional inputs (6.35–6.56) propagates into the FX add-on, so validation of the FX capital charge must trace back to those upstream terms rather than stopping at the 4% factor.
- **Grounding — this node (Page 39 / Art 6.62):** "Calculate the effective notional for each trade in the netting set that is in the foreign exchange derivative asset class... the product of the following three terms"
- **Grounding — related node (Page 130 / Art 12.31):** "The effective notional for each trade in the netting set (Ai) is calculated using the formula Ai = di * MFi * δi"

### [[Hedging Set]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the FX add-on, note the hedging-set definition governs the aggregation: 6.48(2) requires a separate hedging set for each currency pair, and 6.62 builds the FX add-on by allocating trades to those per-currency-pair hedging sets, summing effective notionals within each, then applying the 4% supervisory factor. This link tells you offsetting is only permitted within a currency pair, not across pairs. When checking an FX add-on, confirm trades are grouped strictly by currency pair before the 4% factor is applied.
- **Grounding — this node (Page 39 / 6.62(2)):** "In the foreign exchange derivative asset class the hedging sets consist of all the derivatives that reference the same currency pair"
- **Grounding — related node (Page 34 / 6.48(2)):** "FX derivatives consist of a separate hedging set for each currency pair"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
