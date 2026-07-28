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

# Kolmogorov-Smirnov Test Metric

## Connections

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a trading desk retains eligibility for the Internal Models Approach (IMA), treat the KS test metric as one of the two hard thresholds that determine the PLA test outcome, not as a standalone concept. Under this SAMA market-risk framework, the PLA test allocates a desk to green, amber or red zones, and para 12.42 makes the KS distributional metric a gating input (green requires KS below 0.09; red if KS above 0.12). Consequently, a compliance reviewer confirming IMA eligibility must verify the KS metric against these numeric bounds because a red-zone KS result forces the desk onto the standardised approach until it re-qualifies.
- **Grounding — this node (Page 117 / 12.41):** "The KS test metric is the largest absolute difference observed between these two empirical cumulative distribution functions at any P&L value."
- **Grounding — related node (Page 117 / 12.42):** "a trading desk is allocated to a PLA test red zone, an amber zone or a green zone... the KS distributional test metric is below 0.09"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
