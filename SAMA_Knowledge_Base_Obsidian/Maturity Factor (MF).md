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

# Maturity Factor (MF)

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing an SA-CCR calculation, do not treat the maturity factor as a separate adjustment applied later — it is a direct multiplicative component of effective notional. The prescribed formula A_i = c_i * MF_i * delta_i means the maturity factor scales the adjusted notional to reflect the time horizon over which potential future exposure is measured, and its value differs for margined versus unmargined netting sets. You should conclude that whether a netting set is margined materially changes effective notional (and therefore the capital charge), so confirm the correct MF variant has been used before relying on the result.
- **Grounding — this node (Page 576):** "The maturity factor (MF)... takes account of the time period over which the potential future exposure is calculated... varies depending on whether the netting set is margined or unmargined"
- **Grounding — related node (Page 688 / 12.66):** "For the interest rate add-on, the effective notional for each trade (𝐴𝑖 = 𝑐𝑖 ∗ 𝑀𝐴𝑖 ∗ 𝛼𝑖) ... must be recalculated using the maturity factor for the margined netting set"

### [[Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital for margined netting sets, treat the margin period of risk (MPOR) as a driver of the maturity factor, not a standalone metric. The MF for margined trades is calculated from the applicable MPOR, and SAMA imposes higher supervisory floors — 20 business days for netting sets over 5000 transactions or containing illiquid collateral, and a doubled floor after repeated margin-call disputes — which feed directly into MF and thus the exposure. You should conclude that these MPOR floors raise the maturity factor and the resulting capital charge, so confirm which floor applies to a given netting set before validating the MF used.
- **Grounding — this node (Page 586):** "1 year can be converted into 250 business days in the denominator of the MF formula if MPOR is expressed in business days"
- **Grounding — related node (Page 585 / 6.54):** "For netting sets consisting of more than 5000 transactions... the floor on the margin period of risk is 20 business days... For netting sets containing... illiquid collateral... 20 business days"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
