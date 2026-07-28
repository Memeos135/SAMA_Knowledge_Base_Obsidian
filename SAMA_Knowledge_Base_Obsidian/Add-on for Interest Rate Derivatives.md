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

# Add-on for Interest Rate Derivatives

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the interest-rate derivative add-on under SA-CCR, recognise that the maturity-bucket offsetting logic operates on the effective notional of each trade, not on raw notionals. The IR add-on (6.59) allocates trades to maturity buckets and permits limited offsetting, but the worked example (12.66) shows each trade's effective notional (Ai = di × MFi × δi) must first be computed and, for margined sets, recalculated with the margined maturity factor before bucket-level aggregation. The practical consequence: for the IR charge you must confirm the effective-notional term (including sign via supervisory delta and the correct maturity factor) is calculated per trade first, because the offsetting benefit within a currency hedging set depends entirely on those signed effective notionals.
- **Grounding — this node (Page 37 / Art 6.59):** "allocating trades to maturity buckets, in which full offsetting of long and short positions is permitted"
- **Grounding — related node (Page 139 / Art 12.66):** "the effective notional for each trade (Ai = di * MFi * δi)... must be recalculated using the maturity factor for the margined netting set"

### [[Hedging Set]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the SA-CCR PFE add-on for interest rate derivatives under this SAMA capital standard, you cannot apply the interest-rate add-on formula without first applying the hedging-set definitions: paragraph 6.48 fixes that IR derivatives form a separate hedging set per currency, which controls where offsetting is (and is not) permitted. The IR add-on section (6.59) then operates inside those hedging sets, using maturity buckets to allow full offset within a bucket and only limited offset across buckets. Conclude that any IR add-on calculation you review must be checked against the correct per-currency hedging-set allocation before its offsetting treatment can be relied upon.
- **Grounding — this node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated."
- **Grounding — related node (Page 34 / 6.48):** "Interest rate derivatives consist of a separate hedging set for each currency."

### [[SA-CCR Sample Portfolio Examples]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the interest-rate derivative add-on rules for SA-CCR capital purposes, treat the worked sample portfolios as the authoritative illustration of how the add-on section (6.59 onward) actually feeds into the EAD calculation. The link holds because Chapter 12's Example 1 is expressly an interest-rate-derivatives netting set that operationalises the add-on methodology set out for that asset class within the same framework document. Use the sample portfolio to confirm your reading of the maturity-bucket allocation and effective-notional steps, but rely on the substantive requirement text in 6.59+ as binding — the examples are 'Application Guidance/Illustrative examples,' not the rule itself.
- **Grounding — this node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated."
- **Grounding — related node (Page 123 / 12.1, 12.3):** "Application Guidance/ Illustrative examples... Example 1: Interest rate derivatives (unmargined netting set)"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing potential future exposure under SA-CCR, the interest rate derivative add-on is a component within that method, not a standalone regime — so its maturity-bucket allocation and aggregation rules only bite once you are inside SA-CCR (i.e. no IMM approval for the relevant trades). The add-on for interest rate derivatives (6.59) feeds the netting-set aggregate add-on described in SA-CCR's PFE section, and note that supervisory correlation parameters do not apply to interest rate derivatives — a scope carve-out you must respect. Practical consequence: apply the IR add-on only within the SA-CCR EAD calculation and confirm you are using the correct maturity-bucket offsetting rather than importing the equity/credit/commodity correlation treatment.
- **Grounding — this node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated."
- **Grounding — related node (Page 18 / 6.1):** "Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions must use SA-CCR, as set out in this chapter."

### [[Supervisory Factor]] — `references` [EXTRACTED]
- **What this link tells you:** When validating the interest-rate add-on within SA-CCR, note that the add-on cannot be computed without the prescribed supervisory factor: 6.47 states supervisory factors convert effective notional amounts into the add-on for each hedging set, and the interest-rate add-on (6.59) relies on these calibrated values. This link tells you the interest-rate charge is driven by a fixed regulatory parameter, not a bank estimate, so the correct value must be drawn from Table 2 (6.75). When checking an IR add-on figure, confirm the supervisory factor used matches the prescribed interest-rate value rather than any internally modelled volatility.
- **Grounding — this node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated"
- **Grounding — related node (Page 34 / 6.47):** "Supervisory factors (SF) are used, together with aggregation formulas, to convert effective notional amounts into the add-on for each hedging set"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
