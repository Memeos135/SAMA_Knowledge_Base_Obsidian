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

# Maturity Factor

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating effective notional, note the maturity factor (MF) is one of its three mandatory multiplicative terms and its formula differs by whether the netting set is margined or unmargined. Per 6.51 the unmargined MF uses the lesser of one year and remaining maturity floored at ten business days, while 6.53 requires margined trades to use the margin period of risk subject to specified floors — so the same trade produces a different effective notional depending on collateral arrangements. The consequence: when reviewing a capital charge you must confirm the correct MF branch (margined vs unmargined) and the applicable floor were used, because choosing the wrong maturity-factor rule directly distorts effective notional and therefore the add-on.
- **Grounding — this node (Page 35 / Art 6.51):** "the calculation of the effective notional for an unmargined transaction includes the following maturity factor"
- **Grounding — related node (Page 130 / Art 12.31):** "The effective notional for each trade in the netting set (Ai) is calculated using the formula Ai = di * MFi * δi"

### [[Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the maturity factor for margined netting sets, the margin period of risk (MPOR) is the driving input and is subject to floors that can be raised in defined circumstances. Under 6.53 banks must estimate MPOR per netting set and use the higher of that estimate and the relevant floor; 6.54 then imposes a 20-business-day floor for netting sets over 5,000 trades or containing illiquid collateral/hard-to-replace OTC derivatives, and requires doubling the floor after repeated lengthy margin-call disputes. The consequence: before relying on a margined maturity factor, check whether any of the 6.54 exceptions apply, because a triggered higher MPOR floor raises the maturity factor and thus the effective notional and capital charge — this is an enforceable adjustment, not optional.
- **Grounding — this node (Page 35 / Art 6.53):** "For margined transactions, the maturity factor is calculated using the margin period of risk (MPOR), subject to specified floors"
- **Grounding — related node (Page 36 / Art 6.54):** "the following are exceptions to the floors on the minimum margin period of risk... the floor on the margin period of risk is 20 business days"

### [[PFE Add-on Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's counterparty credit risk capital charge under SAMA's SA-CCR framework, treat the maturity factor as an integral input to the PFE add-on rather than a separate step: the effective notional feeding each asset-class add-on is calculated as adjusted notional × supervisory delta × maturity factor (6.35–6.56), and those add-ons aggregate into the PFE add-on (6.22). The link tells you that time-horizon assumptions (one-year floor for unmargined trades, MPOR floors for margined trades) directly scale the add-on and therefore the exposure at default. When reviewing a capital calculation, verify the maturity factor is applied consistently with the margined/unmargined distinction in 6.51–6.56 before accepting the reported PFE add-on.
- **Grounding — this node (Page 35 / 6.51):** "the calculation of the effective notional for an unmargined transaction includes the following maturity factor, where 𝑀𝑖 is the remaining maturity"
- **Grounding — related node (Page 24 / 6.22):** "The PFE add-on consists of: (i) an aggregate add-on component; and (ii) a multiplier that allows for the recognition of excess collateral"

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
