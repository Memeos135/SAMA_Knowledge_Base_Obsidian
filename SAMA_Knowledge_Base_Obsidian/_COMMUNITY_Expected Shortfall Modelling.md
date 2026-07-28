---
type: community
cohesion: 0.40
members: 6
enriched: true
---

# Expected Shortfall Modelling

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Why this community

Internal-models market-risk capital regime (FRTB-style) — the Expected Shortfall measurement framework and the tests that determine which risk factors qualify for modelled capital versus add-on treatment.

## How members connect

- Expected Shortfall (ES) is the core measure; Liquidity Horizon scales it, and IMCC aggregates modellable-risk-factor capital from ES.
- RFET is the gating test that classifies risk factors; those failing become Non-Modellable Risk Factors (NMRF).
- NMRF capital is captured via Stressed Expected Shortfall (SES), which feeds alongside IMCC into the total internal-models charge.
- These are definitional/computational dependencies (measure -> test -> classification -> capital add-on), not a legal hierarchy.

## Members
- [[Expected Shortfall (ES)]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[IMCC (Aggregate Capital Requirement for Modellable Risk Factors)]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Liquidity Horizon_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Non-Modellable Risk Factor (NMRF)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Risk Factor Eligibility Test (RFET)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Stressed Expected Shortfall (SES)_1]] - concept - markdown/SAMA_EN_3553_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Expected_Shortfall_Modelling
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Default Risk Internal Model]]
- 1 edge to [[_COMMUNITY_P&L Attribution Testing]]

## Top bridge nodes
- [[Expected Shortfall (ES)]] - degree 4, connects to 1 community
- [[Risk Factor Eligibility Test (RFET)_1]] - degree 3, connects to 1 community