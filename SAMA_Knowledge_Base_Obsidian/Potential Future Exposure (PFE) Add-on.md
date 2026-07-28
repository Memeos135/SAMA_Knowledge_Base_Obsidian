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

# Potential Future Exposure (PFE) Add-on

## Connections

### [[Add-on for Commodity Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When building the PFE add-on for a portfolio containing commodity derivatives, the commodity asset-class add-on is one of the asset-class components summed into total PFE, computed by prescribed hedging sets (energy, metals, agriculture, other) and fixed supervisory factors. The framework bars any modelling discretion — 'Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons' — so only the specified supervisory factors and correlations may be used. Conclude that commodity add-ons must be derived mechanically from the mandated factors and folded into the aggregate PFE; internally estimated volatilities or betas cannot be substituted.
- **Grounding — this node (Page 592 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons"
- **Grounding — related node (Page 593 / 6.72 step 4):** "multiplying the combined effective notional for that commodity ... by the supervisory factor that is specified for that commodity type"

### [[Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating counterparty credit risk capital under SA-CCR for a bank's credit derivative book, treat the credit-derivative add-on not as a standalone figure but as one of the five asset-class components that feed the overall PFE add-on. The credit-derivative add-on rules (offsetting of written vs purchased protection, identical reference names, pool coverage) are the asset-class-specific formula that produces the credit component of the netting-set PFE, which is then reported with the 1.4 alpha factor. Conclude that the offsetting conditions in the credit-derivative provisions directly limit the PFE add-on you may recognise, so mis-scoping identical reference names or 'more conservative material terms' overstates permitted offsets and understates required capital.
- **Grounding — this node (Page 874 / row 9):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures calculated in accordance with SLEV7.2.2 (ii) and (v)."
- **Grounding — related node (Page 714 / 7.2.x):** "The resulting amount may be further reduced by the effective notional amount of a purchased credit derivative on the same reference name, provided that..."

### [[Add-on for Equity Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the PFE add-on for equity derivatives, apply the equity-specific supervisory factors as the only permitted volatility inputs — banks are explicitly barred from modelling their own individual volatilities or beta estimates. The equity add-on is one asset-class formula within the aggregate netting-set PFE add-on, using two prescribed supervisory factors (single entities vs indices). Conclude that any internal-model or externally-sourced beta assumption in the equity component is non-compliant, and that the equity add-on you recognise must derive solely from SAMA's prescribed factors before feeding the aggregate PFE.
- **Grounding — this node (Page 874 / row 9):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures calculated in accordance with SLEV7.2.2 (ii) and (v)."
- **Grounding — related node (Page 592 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons, including estimating individual volatilities or taking publicly available estimates of beta."

### [[Add-on for Foreign Exchange Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the PFE add-on for FX derivatives, use the FX asset-class steps (effective notional, currency-pair hedging sets, and the fixed 4% supervisory factor) to produce the FX component that is summed into the aggregate netting-set PFE add-on. The provision confirms FX is one of the five asset classes whose asset-class add-ons are aggregated, and that supervisory correlation parameters do not apply to FX. Conclude that you must scope FX offsetting only within same-currency-pair hedging sets and apply the prescribed 4% factor — no correlation-based partial offset across pairs — before the result enters the reported PFE.
- **Grounding — this node (Page 874 / row 9):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures calculated in accordance with SLEV7.2.2 (ii) and (v)."
- **Grounding — related node (Page 588 / 6.62):** "The prescribed supervisory factor in the HS foreign exchange derivative asset class is set at 4%, which means that AddOn_HS = |A_HS| * 0.04."

### [[Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the PFE add-on for interest rate derivatives, apply the IR-specific maturity-bucket approach — full offsetting within a bucket, only limited offsetting between buckets — to produce the IR component of the aggregate netting-set PFE add-on. Note that supervisory correlation parameters do not apply to interest rate derivatives, so the IR add-on's offsetting is governed by maturity-bucket aggregation rather than by the single-factor correlation used for equity/credit/commodity. Conclude that the IR add-on must be built from the maturity-bucket formula, and that carrying over correlation-parameter offsets from other asset classes into the IR component would be non-compliant.
- **Grounding — this node (Page 874 / row 9):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures calculated in accordance with SLEV7.2.2 (ii) and (v)."
- **Grounding — related node (Page 586 / 6.59):** "It does this by allocating trades to maturity buckets, in which full offsetting of long and short positions is permitted, and by using an aggregation formula that only permits limited offsetting between maturity buckets."

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When deriving EAD for derivatives, the PFE add-on is a mandatory additive component, not a substitute for RC: EAD = 1.4 × (RC + PFE), so both must be computed and the 1.4 alpha factor applied. The leverage-ratio disclosure confirms the same treatment, requiring the PFE add-on 'reported with the 1.4 alpha factor applied' alongside RC. Conclude that any EAD or leverage-exposure figure omitting the PFE add-on, or failing to apply alpha, is understated and non-compliant with the SA-CCR/leverage requirements.
- **Grounding — this node (Page 874 / row 9):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures ... reported with the 1.4 alpha factor applied"
- **Grounding — related node (Page 568 / 6.2):** "RC = the replacement cost calculated according to 6.5 to 6.21 ... PFE = the amount for potential future exposure ... EAD = alpha * (RC + PFE)"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring counterparty exposure under SA-CCR, treat the PFE add-on as a mandatory component of the exposure calculation rather than a standalone item. The framework defines EAD as alpha (1.4) times the sum of replacement cost and PFE, with PFE computed per 6.22–6.79, and the leverage-ratio disclosure separately requires the PFE add-on with the 1.4 alpha factor applied. You would conclude that any SA-CCR exposure figure is incomplete without the PFE add-on, and that the same add-on feeds both the CCR capital charge and the leverage exposure measure.
- **Grounding — this node (Page 874):** "Add-on amount for the potential future exposure (PFE) of all derivative exposures... reported with the 1.4 alpha factor applied as specified in SLEV7.2.2"
- **Grounding — related node (Page 568 / 6.2):** "PFE = the amount for potential future exposure calculated according to 6.22 to 6.79"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
