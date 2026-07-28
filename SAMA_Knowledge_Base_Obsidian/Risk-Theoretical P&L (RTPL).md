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

# Risk-Theoretical P&L (RTPL)

## Connections

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping what data a desk must produce to pass the PLA test, understand that RTPL is one of the two P&L series the test compares — the PLA test has no meaning without it. Para 12.34–12.35 require the test metrics to be computed from the most recent 250 trading days of RTPL and HPL observations, and paras 12.30–12.33 constrain how RTPL input data may or may not be adjusted. A reviewer confirming PLA compliance should therefore check both the integrity of the RTPL series and that any RTPL input-data alignment was documented and notified to SAMA, since improper RTPL adjustments directly distort the test result.
- **Grounding — this node (Page 116 / 12.35):** "the bank must use the time series of the most recent 250 trading days of observations of RTPL and HPL"
- **Grounding — related node (Page 116 / 12.34):** "The PLA requirements are based on two test metrics... to assess the correlation between RTPL and HPL"

### [[Spearman Correlation Metric]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying how the Spearman metric is computed, note that RTPL supplies one of the two rank-ordered P&L series it operates on, so RTPL data quality directly drives the correlation result. Para 12.37 requires banks to rank the RTPL time series by size, and para 12.38 computes the Spearman coefficient of the RTPL and HPL rank series; para 12.33 further bars aligning RTPL and HPL inputs to reduce operational noise. A reviewer should therefore confirm the RTPL series is properly constructed and unadjusted before relying on the resulting Spearman metric for PLA zone allocation.
- **Grounding — this node (Page 116 / 12.37):** "for a time series of RTPL, banks must produce a corresponding time series of ranks based on size"
- **Grounding — related node (Page 116 / 12.38):** "Banks must calculate the Spearman correlation coefficient of the two time series of rank values of RTPL and HPL"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
