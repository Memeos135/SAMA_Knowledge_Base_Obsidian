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

# Margin Period of Risk (MPOR)

## Connections

### [[Maturity Factor]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the maturity factor for margined netting sets, the margin period of risk (MPOR) is the driving input and is subject to floors that can be raised in defined circumstances. Under 6.53 banks must estimate MPOR per netting set and use the higher of that estimate and the relevant floor; 6.54 then imposes a 20-business-day floor for netting sets over 5,000 trades or containing illiquid collateral/hard-to-replace OTC derivatives, and requires doubling the floor after repeated lengthy margin-call disputes. The consequence: before relying on a margined maturity factor, check whether any of the 6.54 exceptions apply, because a triggered higher MPOR floor raises the maturity factor and thus the effective notional and capital charge — this is an enforceable adjustment, not optional.
- **Grounding — this node (Page 36 / Art 6.54):** "the following are exceptions to the floors on the minimum margin period of risk... the floor on the margin period of risk is 20 business days"
- **Grounding — related node (Page 35 / Art 6.53):** "For margined transactions, the maturity factor is calculated using the margin period of risk (MPOR), subject to specified floors"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
