---
source_file: "markdown/SAMA_EN_4303_VER1.md"
type: "concept"
community: "Leverage & SA-CCR Requirements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Leverage__SA-CCR_Requirements
  - graphify/enriched
---

# Derivative Exposures Treatment

## Connections

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **What this link tells you:** When building the leverage ratio denominator, derivative exposures are one of the four mandatory components of the exposure measure, so you must add RC plus PFE for derivatives to on-balance-sheet, SFT and OBS items. The exposure-measure rules (no netting, no collateral reduction) constrain how the derivative treatment in section 7.2 is applied — collateral received cannot reduce derivative exposure and the multiplier is fixed at one. Conclude that derivative treatment is a sub-component governed by the overarching exposure-measure prohibitions, not an independently optimizable figure.
- **Grounding — this node (Page 10 / 7.2.1):** "Exposures to derivatives includes the following components under the Leverage ratio exposure measure: (i) Replacement cost (RC) (ii) Potential future exposure (PFE)"
- **Grounding — related node (Page 5 / 5.4):** "Exposure measure should include the following exposures... (ii) Derivative exposures"

### [[PFE Add-on Calculation]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining a bank's derivative exposure for the leverage ratio, you cannot compute the PFE component in isolation from the SA-CCR add-on methodology — the leverage framework's derivative treatment relies on the same PFE add-on construction (aggregate add-on plus multiplier, supervisory factors and correlations) set out in the capital/CCR document. Note the critical scope difference: 4303 fixes the multiplier at one for leverage purposes and prohibits reducing exposure by collateral received, whereas the 4283 PFE mechanics permit collateral/negative MTM recognition. Conclude that you apply the PFE add-on machinery from 4283 but override the collateral and multiplier relief when calculating the leverage ratio exposure measure.
- **Grounding — this node (Page 14 / 7.2.2):** "replacement cost cannot be reduced by collateral received and the multiplier referenced in paragraph 7.2.2 is fixed at one"
- **Grounding — related node (Page 24 / 6.22):** "The PFE add-on consists of: (i) an aggregate add-on component; and (ii) a multiplier that allows for the recognition of excess collateral or negative mark-to-market value"

### [[SA-CCR Standardised Approach]] — `cites` [EXTRACTED]
- **What this link tells you:** When measuring derivative exposures, be aware that the SA-CCR components (replacement cost and PFE) are re-used in the leverage-ratio exposure measure in SAMA_EN_4303, but under modified rules: the leverage framework applies RC and PFE yet forbids netting of collateral received and fixes the PFE multiplier at one. This means the same SA-CCR building blocks yield a different (more conservative) figure for leverage purposes than for risk-based CCR capital. For a compliance decision, do not assume the SA-CCR EAD computed for risk-based capital can be carried over directly to the leverage ratio — apply the 4303 collateral and multiplier restrictions separately.
- **Grounding — this node (SAMA_EN_4303 Page 14 / 7.2):** "banks must not reduce the Leverage ratio exposure measure amount by any collateral received ... the multiplier referenced in paragraph 7.2.2 is fixed at one"
- **Grounding — related node (SAMA_EN_4283 Page 15 / 5.6):** "banks must calculate their counterparty credit risk exposure, or exposure at default (EAD) ... using one of the methods set out"

### [[Written Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how much a bank may reduce its Leverage ratio exposure measure for sold credit protection, treat the written-credit-derivative definition as the gating condition on the derivative-exposure offset rules, not as a separate topic. Paragraph 7.2.2(iii) subjects written credit derivatives to the additional treatment in 7.2.8–7.2.15, and the offset mechanics in the derivative-exposures section (para 7.2.9/7.2.10 with its same-or-more-conservative material-terms test) can only be applied once an instrument is characterized as a 'written credit derivative' under 7.2.11 — which is defined broadly to include any option obliging the bank to provide credit protection. Conclude that you cannot recognize netting of a purchased protection against a sold position unless the sold position first meets the 7.2.11 definition and the purchased leg satisfies the reference-name, seniority, maturity and strike-price conditions cross-referenced here.
- **Grounding — this node (Page 20 / Para 7.2.9 (offset conditions)):** "The resulting amount may be further reduced by the effective notional amount of a purchased credit derivative on the same reference name, provided that... same or more conservative material terms as those in the corresponding written credit derivative."
- **Grounding — related node (Page 22 / Para 7.2.11):** "Written credit derivative refers to a broad range of credit derivatives through which a bank effectively provides credit protection and is not limited solely to credit default swaps and total return swaps."

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
