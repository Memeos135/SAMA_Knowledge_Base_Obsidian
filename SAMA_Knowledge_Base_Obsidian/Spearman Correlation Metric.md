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

# Spearman Correlation Metric

## Connections

### [[Hypothetical P&L (HPL)]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying the Spearman metric, recognise that HPL is the second P&L series it ranks and correlates against RTPL, so HPL construction rules (paras 12.25–12.28: exclude intraday trades, fees, certain valuation adjustments) feed directly into the metric's validity. Para 12.36 requires ranking the HPL time series, and para 12.38 computes the correlation of the RTPL and HPL rank series; para 12.33 prohibits aligning HPL inputs with RTPL to mask noise. A reviewer confirming PLA compliance should check that HPL was compiled per the defined exclusions before treating the Spearman result as reliable for zone allocation.
- **Grounding — this node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL"
- **Grounding — related node (Page 116 / 12.36):** "For a time series of HPL, banks must produce a corresponding time series of ranks based on the size of the P&L"

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating PLA test eligibility, treat the Spearman correlation metric as the second mandatory gating input alongside the KS metric — a desk cannot reach the green zone without meeting the correlation threshold. Para 12.34 establishes the Spearman metric as one of the two PLA requirements (assessing correlation between RTPL and HPL), and para 12.42 makes correlation above 0.80 a green-zone condition and below 0.7 a red-zone trigger. A compliance reviewer confirming IMA eligibility must verify the Spearman result against these bounds, because a weak correlation alone can push a desk to the standardised approach.
- **Grounding — this node (Page 116 / 12.36-12.38):** "Banks must calculate the Spearman correlation coefficient of the two time series of rank values"
- **Grounding — related node (Page 116 / 12.34):** "the Spearman correlation metric to assess the correlation between RTPL and HPL"

### [[Risk-Theoretical P&L (RTPL)]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying how the Spearman metric is computed, note that RTPL supplies one of the two rank-ordered P&L series it operates on, so RTPL data quality directly drives the correlation result. Para 12.37 requires banks to rank the RTPL time series by size, and para 12.38 computes the Spearman coefficient of the RTPL and HPL rank series; para 12.33 further bars aligning RTPL and HPL inputs to reduce operational noise. A reviewer should therefore confirm the RTPL series is properly constructed and unadjusted before relying on the resulting Spearman metric for PLA zone allocation.
- **Grounding — this node (Page 116 / 12.38):** "Banks must calculate the Spearman correlation coefficient of the two time series of rank values of RTPL and HPL"
- **Grounding — related node (Page 116 / 12.37):** "for a time series of RTPL, banks must produce a corresponding time series of ranks based on size"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
