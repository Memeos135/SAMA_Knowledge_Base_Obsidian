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

# PFE Add-on Calculation

## Connections

### [[Derivative Exposures Treatment]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining a bank's derivative exposure for the leverage ratio, you cannot compute the PFE component in isolation from the SA-CCR add-on methodology — the leverage framework's derivative treatment relies on the same PFE add-on construction (aggregate add-on plus multiplier, supervisory factors and correlations) set out in the capital/CCR document. Note the critical scope difference: 4303 fixes the multiplier at one for leverage purposes and prohibits reducing exposure by collateral received, whereas the 4283 PFE mechanics permit collateral/negative MTM recognition. Conclude that you apply the PFE add-on machinery from 4283 but override the collateral and multiplier relief when calculating the leverage ratio exposure measure.
- **Grounding — this node (Page 24 / 6.22):** "The PFE add-on consists of: (i) an aggregate add-on component; and (ii) a multiplier that allows for the recognition of excess collateral or negative mark-to-market value"
- **Grounding — related node (Page 14 / 7.2.2):** "replacement cost cannot be reduced by collateral received and the multiplier referenced in paragraph 7.2.2 is fixed at one"

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When validating an SA-CCR exposure, the PFE add-on calculation is the engine behind the PFE component that feeds EAD — it is not a stand-alone diagnostic. Paragraph 6.22 defines PFE = multiplier × AddOn(aggregate), and 6.58 builds the aggregate add-on as the sum of asset-class add-ons; this then enters EAD via EAD = alpha × (RC + PFE). Note the prohibition in 6.71 on internal modelling assumptions for add-ons — banks must use the prescribed supervisory factors — so when checking an EAD, confirm the add-on used only supervisory parameters, since deviations understate exposure and capital.
- **Grounding — this node (Page 24 / 6.22):** "The PFE add-on consists of ... an aggregate add-on component; and ... a multiplier ... PFE = multiplier ∗ AddOnaggregate"
- **Grounding — related node (Page 16 / 5.10):** "the exposure amount or EAD for a given counterparty is equal to the sum of the exposure amounts"

### [[Maturity Factor]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's counterparty credit risk capital charge under SAMA's SA-CCR framework, treat the maturity factor as an integral input to the PFE add-on rather than a separate step: the effective notional feeding each asset-class add-on is calculated as adjusted notional × supervisory delta × maturity factor (6.35–6.56), and those add-ons aggregate into the PFE add-on (6.22). The link tells you that time-horizon assumptions (one-year floor for unmargined trades, MPOR floors for margined trades) directly scale the add-on and therefore the exposure at default. When reviewing a capital calculation, verify the maturity factor is applied consistently with the margined/unmargined distinction in 6.51–6.56 before accepting the reported PFE add-on.
- **Grounding — this node (Page 24 / 6.22):** "The PFE add-on consists of: (i) an aggregate add-on component; and (ii) a multiplier that allows for the recognition of excess collateral"
- **Grounding — related node (Page 35 / 6.51):** "the calculation of the effective notional for an unmargined transaction includes the following maturity factor, where 𝑀𝑖 is the remaining maturity"

### [[SA-CCR Standardised Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When validating a SA-CCR EAD figure, treat the PFE add-on as a mandatory component of that standardized approach rather than a discretionary refinement: SA-CCR exposure is built from replacement cost plus the PFE add-on, and the framework fixes the add-on inputs (supervisory factors, correlation parameters, multiplier). Both concepts sit within Chapter 6 of the same framework, with para 6.71 explicitly barring banks from making modelling assumptions in the PFE add-on. For a compliance decision, conclude that the add-on must use only the prescribed supervisory values and that a bank cannot substitute internal volatility estimates.
- **Grounding — this node (Page 43 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons ... bank must only use the ... supervisory factors that are defined"
- **Grounding — related node (Page 15 / 5.7(1)):** "Standardized approach for measuring counterparty credit risk exposures (SACCR), which is set out in Chapter 6 of this framework."

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
