---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Backtesting"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Backtesting
  - graphify/enriched
---

# Backtesting

## Connections

### [[Actual P&L (APL)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating a bank's backtesting compliance, understand that Actual P&L (APL) is one of the defined inputs the backtesting process compares against model-generated VaR to test model conservatism. The standard defines APL as the daily P&L including intraday trading, time effects and new/modified deals but excluding fees, commissions and specified valuation adjustments — and it is APL loss (alongside HPL) that determines whether a desk-level exception can be disregarded. For a compliance decision you would check that APL is constructed to the [12.26]-[12.28] exclusions, because a mis-specified APL directly distorts exception counts and therefore the backtesting-zone outcome and any add-on.
- **Grounding — this node (Page 110):** "an SES capital requirement that is in excess of the maximum of the APL loss or HPL loss for that day, it is permitted to be disregarded"
- **Grounding — related node (Page 7 (definitions) / [12.25]):** "The actual P&L derived from the daily P&L process. It includes intraday trading as well as time effects and new and modified deals, but excludes fees and commissions"

### [[Backtesting GreenAmberRed Zones|Backtesting Green/Amber/Red Zones]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the supervisory consequence of a bank's backtesting results, read the backtesting process together with the green/amber/red zone classification, because the zones are the mechanism that converts exception counts into SAMA responses. The green zone triggers no add-on, the amber zone (beginning at five exceptions in a 250-observation sample) triggers a higher capital requirement, and the red zone (ten exceptions) triggers an automatic multiplier increase or possible disallowance of the model. For a compliance decision you would map the bank's 12-month exception count onto these thresholds to anticipate whether a capital add-on or model disallowance is presumptive.
- **Grounding — this node (Page 111 / [12.10]-[12.15]):** "If a bank's model falls into the backtesting red zone, SAMA will automatically increase the multiplication factor applicable to the bank's model or may disallow use of the model"
- **Grounding — related node (Page 172 / [16.17]):** "the backtesting amber zone begins at five exceptions... the beginning of the backtesting red zone... occurs with 10 exceptions"

### [[Hypothetical P&L (HPL)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing backtesting inputs, treat Hypothetical P&L (HPL) as the second defined comparator (with APL) fed into the backtesting and PLA processes. HPL measures the change in end-of-day portfolio value with positions held constant — excluding intraday trading and new/modified deals — and is subject to distinct valuation-adjustment inclusion rules under [12.26]-[12.28] and strict limits on aligning HPL input data. For a compliance decision you would verify HPL is constructed on this hold-constant basis and that no impermissible input alignment or smoothing has occurred, since HPL feeds both the exception count and the PLA correlation/KS tests that govern desk eligibility.
- **Grounding — this node (Page 109-110 / [12.7]):** "The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests"
- **Grounding — related node (Page 114 / [12.25]):** "HPL measures changes in portfolio value that would occur when end-of-day positions remain unchanged, it must not take into account intraday trading nor new or modified deals"

### [[Internal Models Approach]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can keep using its internal model for market risk capital, treat backtesting not as a stand-alone diagnostic but as a gating condition on IMA eligibility. Under this SAMA market risk standard the IMA requires an independent risk control unit to conduct regular backtesting of both desk-level and bank-wide models, and backtesting outcomes drive SAMA's response — a higher multiplication factor, a backtesting add-on, or outright disallowance of the model. The practical conclusion: a compliance reviewer evaluating continued IMA approval should read backtesting results as directly determinative of the model's regulatory standing, not as a separate exercise.
- **Grounding — this node (Page 111 / 12.14–12.15):** "SAMA may consider whether to disallow the bank's use of the model for market risk capital requirement purposes altogether... will automatically increase the multiplication factor"
- **Grounding — related node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level... backtesting of its bank-wide internal models"

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may keep using its internal models for market risk capital, treat backtesting not as an optional diagnostic but as a condition of continued IMA eligibility, because the framework mandates ongoing backtesting of both trading-desk and bank-wide internal models and ties SAMA responses (add-ons, multiplier increases, or model disallowance) directly to backtesting outcomes. The 'green/amber/red zone' regime and the one-year backtesting report required for SAMA model approval make backtesting the mechanism by which IMA use is validated and priced. Conclude that a compliance assessment of IMA status must confirm the bank runs, documents, and explains all backtesting exceptions — failure exposes the bank to a backtesting add-on or loss of model approval.
- **Grounding — this node (Page 111 / 12.14-12.15):** "in the case of severe problems with the basic integrity of the model, SAMA may consider whether to disallow the bank's use of the model for market risk capital requirement purposes altogether"
- **Grounding — related node (Page 92 / 10.7):** "The bank must also conduct regular backtesting of its bank-wide internal models used for determining market risk capital requirements."

### [[Risk Factor Modellability]] — `references` [EXTRACTED]
- **What this link tells you:** When adjudicating whether a backtesting exception can be legitimately disregarded, check the modellability status of the risk factor driving it: the standard permits an exception to be set aside only where it is driven by a non-modellable risk factor (NMRF) that receives an SES capital requirement exceeding the day's loss, and only with SAMA notification and supporting documentation. Risk factor modellability (RFET and the [11.25]–[11.26] principles) is what determines whether a factor is an NMRF in the first place, so the two concepts are directly linked in the exception-treatment test. Conclude that a bank cannot claim the disregard relief without first establishing, to SAMA's satisfaction, that the factor is genuinely non-modellable and separately capitalised at the required desk level.
- **Grounding — this node (Page 110 / 12.6):** "If the backtesting exception at a desk-level test is being driven by a non-modellable risk factor that receives an SES capital requirement... it is permitted to be disregarded"
- **Grounding — related node (Page 105 / 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"

### [[Value-at-Risk (VaR)]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying whether a bank's backtesting is being performed correctly for capital purposes, note that VaR is the benchmark against which the test operates: an 'exception' is defined as a day where actual or hypothetical loss exceeds the model's daily VaR. The standard fixes the VaR calibration used — a one-day holding period at the 99th percentile confidence level — so a reviewer checking exception counts must confirm the VaR measure is calibrated on that basis before the green/amber/red zone consequences apply. Conclude that any backtesting result is only meaningful, and any add-on or model disallowance defensible, when tied to a properly calibrated VaR measure as defined in the standard.
- **Grounding — this node (Page 109 / 12.4–12.5):** "Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL)"
- **Grounding — related node (Page 6 (glossary)):** "Value at risk (VaR): A measure of the worst expected loss on a portfolio of instruments resulting from market movements over a given time horizon and a pre-defined confidence level."

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
