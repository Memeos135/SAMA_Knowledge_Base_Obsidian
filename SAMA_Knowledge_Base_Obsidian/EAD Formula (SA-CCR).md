---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# EAD Formula (SA-CCR)

## Connections

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the SA-CCR EAD formula, treat replacement cost as a formula term with a specific prescribed calculation, including the margined-trade formulation RC = max{V − C; TH + MTA − NICA; 0}. The formula EAD = 1.4 × (RC + PFE) pulls RC directly from 6.5–6.21, and the worked examples in section 13 show how collateral, thresholds, MTA and NICA drive whether RC is positive or floored at zero. You would conclude that any EAD calculation must reproduce this exact three-term RC treatment for margined netting sets rather than a simple current-exposure figure.
- **Grounding — this node (Page 568 / 6.2):** "RC = the replacement cost calculated according to 6.5 to 6.21 ... EAD = alpha * (RC + PFE)"
- **Grounding — related node (Page 691 / 13.1):** "the formulation of replacement cost for margined trades, as set out in 6.20: RC = max{V − C; TH + MTA − NICA; 0}"

### [[SA-CCR Sample Portfolio Examples]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating exposure at default under SA-CCR, use the worked sample portfolios as the authoritative illustration of how the EAD formula is applied, not just the abstract definition. The illustrative-examples section explicitly restates the EAD formula (alpha = 1.4 × (RC + multiplier × AddOn)) and then applies it to five sample netting sets. Conclude that the examples ground the mechanics of the formula for CCR exposure measurement; note this SA-CCR EAD differs from the own-EAD estimates under the IRB advanced approach in 16.88, which excludes counterparty-credit-risk transactions governed by the CCR framework.
- **Grounding — this node (Page 672 / 12.2):** "The EAD for all netting sets in SA-CCR is given by the following formula, where alpha is assigned a value of 1.4."
- **Grounding — related node (Page 672 / 12.1):** "This section sets out the calculation of exposure at default (EAD) for five sample portfolios using SA-CCR."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
