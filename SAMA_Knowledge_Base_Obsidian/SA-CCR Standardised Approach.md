---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "Leverage & SA-CCR Requirements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Leverage__SA-CCR_Requirements
  - graphify/enriched
---

# SA-CCR Standardised Approach

## Connections

### [[Derivative Exposures Treatment]] — `cites` [EXTRACTED]
- **What this link tells you:** When measuring derivative exposures, be aware that the SA-CCR components (replacement cost and PFE) are re-used in the leverage-ratio exposure measure in SAMA_EN_4303, but under modified rules: the leverage framework applies RC and PFE yet forbids netting of collateral received and fixes the PFE multiplier at one. This means the same SA-CCR building blocks yield a different (more conservative) figure for leverage purposes than for risk-based CCR capital. For a compliance decision, do not assume the SA-CCR EAD computed for risk-based capital can be carried over directly to the leverage ratio — apply the 4303 collateral and multiplier restrictions separately.
- **Grounding — this node (SAMA_EN_4283 Page 15 / 5.6):** "banks must calculate their counterparty credit risk exposure, or exposure at default (EAD) ... using one of the methods set out"
- **Grounding — related node (SAMA_EN_4303 Page 14 / 7.2):** "banks must not reduce the Leverage ratio exposure measure amount by any collateral received ... the multiplier referenced in paragraph 7.2.2 is fixed at one"

### [[PFE Add-on Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** When validating a SA-CCR EAD figure, treat the PFE add-on as a mandatory component of that standardized approach rather than a discretionary refinement: SA-CCR exposure is built from replacement cost plus the PFE add-on, and the framework fixes the add-on inputs (supervisory factors, correlation parameters, multiplier). Both concepts sit within Chapter 6 of the same framework, with para 6.71 explicitly barring banks from making modelling assumptions in the PFE add-on. For a compliance decision, conclude that the add-on must use only the prescribed supervisory values and that a bank cannot substitute internal volatility estimates.
- **Grounding — this node (Page 15 / 5.7(1)):** "Standardized approach for measuring counterparty credit risk exposures (SACCR), which is set out in Chapter 6 of this framework."
- **Grounding — related node (Page 43 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons ... bank must only use the ... supervisory factors that are defined"

### [[SAMA CCR and CVA Minimum Capital Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping counterparty-credit-risk capital obligations, read the SA-CCR method as the default exposure-measurement engine mandated by this framework: banks must use SA-CCR (SACCR) for OTC derivatives, exchange-traded derivatives and long settlement transactions unless they hold SAMA approval to use the IMM. The framework document sets out SA-CCR in Chapter 6 and links its EAD output to the risk-weighting step in para 5.12. For a compliance decision, conclude that absent explicit IMM approval, SA-CCR governs, and any deviation requires documented SAMA authorization.
- **Grounding — this node (Page 15 / 5.7(1)):** "Standardized approach for measuring counterparty credit risk exposures (SACCR) ... This method must be used if the bank does not have approval to use the internal models method (IMM)."
- **Grounding — related node (Page 87 / 11.5):** "The capital requirement for CVA risk must be calculated by all banks involved in covered transactions in both banking book and trading book."

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
