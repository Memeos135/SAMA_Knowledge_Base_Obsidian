---
type: community
cohesion: 0.15
members: 16
enriched: true
---

# Market Risk Backtesting

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Why this community

Market-risk capital under the Internal Models Approach (IMA): the eligibility, backtesting and P&L-attribution gateway a bank must pass to keep using internal models for trading-book capital under SAMA's Basel-aligned market-risk regime.

## How members connect

- IMA is the parent authorisation; ES Model, RFET, PLA Test and Backtesting are the referenced conditions a firm must satisfy to retain and calibrate model-based capital.
- RFET operationalises the split between modellable and Non-Modellable Risk Factors (NMRF); NMRFs are capitalised separately via Stressed ES (SES), which then feeds the IMCC aggregate requirement alongside ES.
- Backtesting compares Actual vs Hypothetical P&L and assigns Green/Amber/Red zones — an obligation whose outcome (Red) triggers loss of IMA eligibility; PLA compares Risk-Theoretical vs Hypothetical P&L using Spearman and Kolmogorov-Smirnov metrics as the pass/fail tests.
- Liquidity Horizon scales both the ES model and the DRC (default risk) component, linking risk-factor tenor to the capital number.

## Members
- [[Actual P&L (APL)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Backtesting]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Backtesting GreenAmberRed Zones]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[DRC Requirement Model (IMA)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Expected Shortfall (ES) Model]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Hypothetical P&L (HPL)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[IMCC Aggregate Capital Requirement]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Internal Models Approach (IMA)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Kolmogorov-Smirnov Test Metric]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Liquidity Horizon]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Non-Modellable Risk Factor (NMRF)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[P&L Attribution (PLA) Test]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Risk Factor Eligibility Test (RFET)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Risk-Theoretical P&L (RTPL)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Spearman Correlation Metric]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Stressed Expected Shortfall (SES)]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Market_Risk_Backtesting
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 1 edge to [[_COMMUNITY_SA-CCR Derivative Add-ons]]

## Top bridge nodes
- [[Backtesting]] - degree 6, connects to 1 community
- [[Internal Models Approach (IMA)]] - degree 6, connects to 1 community
- [[DRC Requirement Model (IMA)]] - degree 3, connects to 1 community