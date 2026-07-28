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

# Hypothetical P&L (HPL)

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing backtesting inputs, treat Hypothetical P&L (HPL) as the second defined comparator (with APL) fed into the backtesting and PLA processes. HPL measures the change in end-of-day portfolio value with positions held constant — excluding intraday trading and new/modified deals — and is subject to distinct valuation-adjustment inclusion rules under [12.26]-[12.28] and strict limits on aligning HPL input data. For a compliance decision you would verify HPL is constructed on this hold-constant basis and that no impermissible input alignment or smoothing has occurred, since HPL feeds both the exception count and the PLA correlation/KS tests that govern desk eligibility.
- **Grounding — this node (Page 114 / [12.25]):** "HPL measures changes in portfolio value that would occur when end-of-day positions remain unchanged, it must not take into account intraday trading nor new or modified deals"
- **Grounding — related node (Page 109-110 / [12.7]):** "The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests"

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing PLA test compliance, understand that HPL is one of the two inputs the test compares — the PLA test assesses correlation and distributional similarity between the risk-theoretical P&L (RTPL) and the HPL. This drives concrete constraints: banks must not align HPL input data with RTPL input data, adjustments for 'residual operational noise' are prohibited, and any permitted RTPL input alignments must be documented and justified to SAMA. Conclude that the integrity of HPL construction (excluding intraday trades, fees, and non-daily valuation adjustments as specified) directly determines whether PLA results are valid, so a reviewer must scrutinise HPL scope before relying on the test outcome.
- **Grounding — this node (Page 116 / 12.33):** "Banks are not permitted to align HPL input data for risk factors with input data used in RTPL."
- **Grounding — related node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL; and the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL"

### [[Spearman Correlation Metric]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying the Spearman metric, recognise that HPL is the second P&L series it ranks and correlates against RTPL, so HPL construction rules (paras 12.25–12.28: exclude intraday trades, fees, certain valuation adjustments) feed directly into the metric's validity. Para 12.36 requires ranking the HPL time series, and para 12.38 computes the correlation of the RTPL and HPL rank series; para 12.33 prohibits aligning HPL inputs with RTPL to mask noise. A reviewer confirming PLA compliance should check that HPL was compiled per the defined exclusions before treating the Spearman result as reliable for zone allocation.
- **Grounding — this node (Page 116 / 12.36):** "For a time series of HPL, banks must produce a corresponding time series of ranks based on the size of the P&L"
- **Grounding — related node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
