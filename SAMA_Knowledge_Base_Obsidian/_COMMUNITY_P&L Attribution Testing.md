---
type: community
cohesion: 0.29
members: 10
enriched: true
---

# P&L Attribution Testing

**Cohesion:** 0.29 - loosely connected
**Members:** 10 nodes

## Why this community

Model-validation regime for the Internal Models Approach (IMA) to market risk capital. Governs whether a bank may keep using its own model by testing model output against realized/theoretical P&L.

## How members connect

- Backtesting and the PLA Test are the two mandatory validation gates conditioning continued IMA use; both are subordinate diagnostics of the Internal Models Approach.
- The P&L definitions (RTPL, HPL, APL) are the defined inputs: PLA compares RTPL against HPL; backtesting compares model VaR against APL/HPL.
- Spearman correlation and Kolmogorov-Smirnov are the prescribed PLA pass/fail metrics; Green/Amber/Red zones are the backtesting classification driving capital multiplier consequences.
- Risk Factor Modellability scopes which risk factors may enter the model, feeding back into IMA eligibility.

## Members
- [[Actual P&L (APL)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Backtesting_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Backtesting GreenAmberRed Zones_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Hypothetical P&L (HPL)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Internal Models Approach]] - document - markdown/SAMA_EN_3553_VER1.md
- [[Kolmogorov-Smirnov Test Metric_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[P&L Attribution (PLA) Test_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Risk Factor Modellability_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Risk-Theoretical P&L (RTPL)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Spearman Correlation Metric_1]] - concept - markdown/SAMA_EN_3553_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PL_Attribution_Testing
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Default Risk Internal Model]]
- 1 edge to [[_COMMUNITY_Expected Shortfall Modelling]]

## Top bridge nodes
- [[P&L Attribution (PLA) Test_1]] - degree 7, connects to 2 communities
- [[Backtesting_1]] - degree 7, connects to 1 community