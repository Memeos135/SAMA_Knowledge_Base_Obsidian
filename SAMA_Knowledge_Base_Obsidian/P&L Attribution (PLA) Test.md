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

# P&L Attribution (PLA) Test

## Connections

### [[Hypothetical P&L (HPL)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing PLA test compliance, understand that HPL is one of the two inputs the test compares — the PLA test assesses correlation and distributional similarity between the risk-theoretical P&L (RTPL) and the HPL. This drives concrete constraints: banks must not align HPL input data with RTPL input data, adjustments for 'residual operational noise' are prohibited, and any permitted RTPL input alignments must be documented and justified to SAMA. Conclude that the integrity of HPL construction (excluding intraday trades, fees, and non-daily valuation adjustments as specified) directly determines whether PLA results are valid, so a reviewer must scrutinise HPL scope before relying on the test outcome.
- **Grounding — this node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL; and the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL"
- **Grounding — related node (Page 116 / 12.33):** "Banks are not permitted to align HPL input data for risk factors with input data used in RTPL."

### [[Internal Models Approach]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When scoping the ongoing conditions for a bank to retain IMA capital treatment, treat the PLA test as an embedded IMA requirement rather than an independent measure: the IMA mandates that the independent risk control unit conduct regular PLA assessments at the trading desk level, and the standard requires the PLA test programme to begin when the internal models capital requirement becomes effective and to be reported for SAMA model approval. PLA results, alongside backtesting and the RFET, feed quarterly into which desks remain eligible for the IMA. Conclude that a compliance reviewer evaluating continued IMA approval should confirm PLA testing is running per the standard, since desk-level PLA failure affects whether that desk stays within the internal-models regime.
- **Grounding — this node (Page 109 / 12.3):** "The implementation of the backtesting programme and the PLA test must begin on the date that the internal models capital requirement becomes effective."
- **Grounding — related node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level."

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating whether a given trading desk may remain in-scope for the IMA, treat the P&L Attribution (PLA) test as a gating requirement operating alongside backtesting, because a desk in the PLA amber zone is subject to a capital surcharge and can only return to green after producing green-zone outcomes and satisfying its backtesting exceptions requirements. The framework requires PLA assessments at desk level and a one-year PLA report for SAMA model approval, and updates the backtesting portfolio scope quarterly based on PLA results. Conclude that IMA desk eligibility must be checked against both PLA and backtesting status — a passing backtest alone does not keep a desk in-scope if it fails PLA.
- **Grounding — this node (Page 118 / 12.44):** "If a trading desk is in the PLA test amber zone, it is not considered an out-of-scope trading desk for use of the IMA."
- **Grounding — related node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level."

### [[Kolmogorov-Smirnov Test Metric]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a trading desk retains eligibility for the Internal Models Approach (IMA), treat the KS test metric as one of the two hard thresholds that determine the PLA test outcome, not as a standalone concept. Under this SAMA market-risk framework, the PLA test allocates a desk to green, amber or red zones, and para 12.42 makes the KS distributional metric a gating input (green requires KS below 0.09; red if KS above 0.12). Consequently, a compliance reviewer confirming IMA eligibility must verify the KS metric against these numeric bounds because a red-zone KS result forces the desk onto the standardised approach until it re-qualifies.
- **Grounding — this node (Page 117 / 12.42):** "a trading desk is allocated to a PLA test red zone, an amber zone or a green zone... the KS distributional test metric is below 0.09"
- **Grounding — related node (Page 117 / 12.41):** "The KS test metric is the largest absolute difference observed between these two empirical cumulative distribution functions at any P&L value."

### [[Risk Factor Eligibility Test (RFET)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When determining which portfolio remains in scope for IMA capital, note that the PLA test and RFET results are consumed together in the same quarterly scope-update exercise. Art 12.7 requires the bank-wide backtesting scope to be updated quarterly based on the latest desk-level backtesting, RFET and PLA test results — so a desk's IMA eligibility depends jointly on these tests, not any one in isolation. A reviewer should therefore check that RFET and PLA outcomes are reconciled to the same quarterly cycle before concluding a desk is validly modelled.
- **Grounding — this node (Page 110 / Art 12.7):** "The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests."
- **Grounding — related node (Page 101 / Art 11.13):** "To pass the RFET, a risk factor ... must meet either of the following criteria on a quarterly basis."
- **Caveat:** Both tests feed the same quarterly scope determination; the label 'shares_data_with' overstates a direct data dependency — the link is that both results are jointly assessed under Art 12.7, not that one supplies inputs to the other.

### [[Risk-Theoretical P&L (RTPL)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping what data a desk must produce to pass the PLA test, understand that RTPL is one of the two P&L series the test compares — the PLA test has no meaning without it. Para 12.34–12.35 require the test metrics to be computed from the most recent 250 trading days of RTPL and HPL observations, and paras 12.30–12.33 constrain how RTPL input data may or may not be adjusted. A reviewer confirming PLA compliance should therefore check both the integrity of the RTPL series and that any RTPL input-data alignment was documented and notified to SAMA, since improper RTPL adjustments directly distort the test result.
- **Grounding — this node (Page 116 / 12.34):** "The PLA requirements are based on two test metrics... to assess the correlation between RTPL and HPL"
- **Grounding — related node (Page 116 / 12.35):** "the bank must use the time series of the most recent 250 trading days of observations of RTPL and HPL"

### [[Spearman Correlation Metric]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating PLA test eligibility, treat the Spearman correlation metric as the second mandatory gating input alongside the KS metric — a desk cannot reach the green zone without meeting the correlation threshold. Para 12.34 establishes the Spearman metric as one of the two PLA requirements (assessing correlation between RTPL and HPL), and para 12.42 makes correlation above 0.80 a green-zone condition and below 0.7 a red-zone trigger. A compliance reviewer confirming IMA eligibility must verify the Spearman result against these bounds, because a weak correlation alone can push a desk to the standardised approach.
- **Grounding — this node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL"
- **Grounding — related node (Page 116 / 12.36-12.38):** "Banks must calculate the Spearman correlation coefficient of the two time series of rank values"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
