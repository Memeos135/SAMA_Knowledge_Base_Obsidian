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

# Effective Notional

## Connections

### [[Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the SA-CCR add-on for the credit derivative asset class, Step 1 is to compute each trade's effective notional (adjusted notional × supervisory delta × maturity factor) exactly as defined in 6.35–6.56, then aggregate per referenced entity/index before applying the supervisory factor. So the credit add-on cannot be built without first producing the effective notional per trade. For a calculation-review decision, confirm the effective-notional step is completed and correctly signed before entity-level aggregation and correlation weighting are applied; errors upstream in effective notional propagate directly into the credit derivatives add-on and hence PFE.
- **Grounding — this node (Page 130 / 12.31):** "The effective notional for each trade in the netting set (𝐴�𝑖) is calculated using the formula 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖"
- **Grounding — related node (Page 40 / 6.63 Step 1):** "Calculate the effective notional for each trade in the netting set that is in the credit derivative asset class... 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖, where each term is as defined in 6.35 to 6.56."

### [[Add-on for Foreign Exchange Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the SA-CCR PFE add-on for FX derivatives for capital purposes, do not treat the FX add-on formula as self-contained: it is built directly on the effective notional defined earlier in the framework. Under 6.62 Step 1, the FX asset-class add-on begins by calculating each trade's effective notional as the product of adjusted notional, supervisory delta and maturity factor (Ai = di × MFi × δi), then aggregates these by currency-pair hedging set before applying the 4% supervisory factor. Conclude that any error or definitional choice in the effective-notional inputs (6.35–6.56) propagates into the FX add-on, so validation of the FX capital charge must trace back to those upstream terms rather than stopping at the 4% factor.
- **Grounding — this node (Page 130 / Art 12.31):** "The effective notional for each trade in the netting set (Ai) is calculated using the formula Ai = di * MFi * δi"
- **Grounding — related node (Page 39 / Art 6.62):** "Calculate the effective notional for each trade in the netting set that is in the foreign exchange derivative asset class... the product of the following three terms"

### [[Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the interest-rate derivative add-on under SA-CCR, recognise that the maturity-bucket offsetting logic operates on the effective notional of each trade, not on raw notionals. The IR add-on (6.59) allocates trades to maturity buckets and permits limited offsetting, but the worked example (12.66) shows each trade's effective notional (Ai = di × MFi × δi) must first be computed and, for margined sets, recalculated with the margined maturity factor before bucket-level aggregation. The practical consequence: for the IR charge you must confirm the effective-notional term (including sign via supervisory delta and the correct maturity factor) is calculated per trade first, because the offsetting benefit within a currency hedging set depends entirely on those signed effective notionals.
- **Grounding — this node (Page 139 / Art 12.66):** "the effective notional for each trade (Ai = di * MFi * δi)... must be recalculated using the maturity factor for the margined netting set"
- **Grounding — related node (Page 37 / Art 6.59):** "allocating trades to maturity buckets, in which full offsetting of long and short positions is permitted"

### [[Adjusted Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying any SA-CCR add-on figure, treat adjusted notional as a required input to effective notional, not an interchangeable concept. The framework defines effective notional as Ai = di × MFi × δi, where di is the adjusted notional — and adjusted notional itself is asset-class-specific (e.g. for FX the foreign-currency leg converted to SAR; for interest rate/credit the notional multiplied by supervisory duration). The consequence: if the adjusted notional is mis-specified (wrong currency leg, missing duration adjustment, or wrong treatment of variable/leveraged notionals under 6.39), every downstream effective notional and add-on is wrong, so a capital-charge review must first confirm the correct adjusted-notional definition was applied per asset class.
- **Grounding — this node (Page 130 / Art 12.31):** "the effective notional for each trade... is calculated using the formula Ai = di * MFi * δi"
- **Grounding — related node (Page 30 / Art 6.37-6.38):** "For foreign exchange derivatives, the adjusted notional is defined as the notional of the foreign currency leg... converted to the Saudi Riyal (SAR)"

### [[Maturity Factor]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating effective notional, note the maturity factor (MF) is one of its three mandatory multiplicative terms and its formula differs by whether the netting set is margined or unmargined. Per 6.51 the unmargined MF uses the lesser of one year and remaining maturity floored at ten business days, while 6.53 requires margined trades to use the margin period of risk subject to specified floors — so the same trade produces a different effective notional depending on collateral arrangements. The consequence: when reviewing a capital charge you must confirm the correct MF branch (margined vs unmargined) and the applicable floor were used, because choosing the wrong maturity-factor rule directly distorts effective notional and therefore the add-on.
- **Grounding — this node (Page 130 / Art 12.31):** "The effective notional for each trade in the netting set (Ai) is calculated using the formula Ai = di * MFi * δi"
- **Grounding — related node (Page 35 / Art 6.51):** "the calculation of the effective notional for an unmargined transaction includes the following maturity factor"

### [[Supervisory Delta Adjustment]] — `references` [EXTRACTED]
- **What this link tells you:** When computing SA-CCR add-ons, the supervisory delta is a direct input into the effective notional: each trade's effective notional (𝐴�ᵢ) equals adjusted notional × maturity factor × supervisory delta (𝛼�ᵢ). The delta carries the sign (+1 long / -1 short for non-options) and the non-linearity of options, so it is what lets long and short positions offset within a hedging set. For a calculation-review decision, confirm that the delta is assigned per trade under 6.40–6.43 before the effective notional is derived; a wrong delta sign directly mis-states the effective notional and the resulting add-on.
- **Grounding — this node (Page 130 / 12.31):** "The effective notional for each trade in the netting set (𝐴�𝑖) is calculated using the formula 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖"
- **Grounding — related node (Page 31 / 6.40):** "The supervisory delta adjustment (𝛼�𝑖) parameters are also defined at the trade i level and are applied to the adjusted notional amounts to reflect the direction of the transaction and its non-linearity."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
