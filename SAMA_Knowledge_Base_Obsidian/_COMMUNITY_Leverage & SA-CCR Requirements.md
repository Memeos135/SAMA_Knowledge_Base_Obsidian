---
type: community
cohesion: 0.14
members: 16
enriched: true
---

# Leverage & SA-CCR Requirements

**Cohesion:** 0.14 - loosely connected
**Members:** 16 nodes

## Why this community

Leverage ratio and SA-CCR exposure measurement plus the output floor: the non-risk-based backstop and standardised counterparty exposure rules that constrain and aggregate a bank's RWA under SAMA's framework.

## How members connect

- SA-CCR (with PFE Add-on, Maturity Factor and Margin Period of Risk) is the mandated standardised method for derivative counterparty exposure, cited by both Derivative Exposures Treatment and the CCR/CVA minimum-capital rules.
- The Leverage Ratio Exposure Measure aggregates derivative, SFT, off-balance-sheet (CCF) and written-credit-derivative exposures into the non-risk-based denominator.
- The Output Floor (72.5% RWA) binds together RWA for credit, market, and CCR/CVA risk — capping the benefit of internal models by flooring total RWA against standardised outputs.
- RWA for CCR and CVA cites the SAMA CCR and CVA minimum-capital provision, linking the exposure calculation back to the capital requirement it feeds.

## Members
- [[Derivative Exposures Treatment]] - concept - markdown/SAMA_EN_4303_VER1.md
- [[Leverage Ratio Exposure Measure_1]] - concept - markdown/SAMA_EN_4303_VER1.md
- [[Margin Period of Risk (MPOR)_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Maturity Factor]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Off-Balance Sheet Items  CCFs]] - concept - markdown/SAMA_EN_4303_VER1.md
- [[Output Floor (72.5% RWA)]] - concept - markdown/SAMA_EN_4376_VER1.md
- [[PFE Add-on Calculation]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[RWA for CCR and CVA]] - concept - markdown/SAMA_EN_4376_VER1.md
- [[RWA for Credit Risk_1]] - concept - markdown/SAMA_EN_4376_VER1.md
- [[RWA for Market Risk_1]] - concept - markdown/SAMA_EN_4376_VER1.md
- [[SA-CCR Standardised Approach]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[SAMA CCR and CVA Minimum Capital Requirements]] - document - markdown/SAMA_EN_4283_VER1.md
- [[SAMA Leverage Ratio Framework]] - document - markdown/SAMA_EN_4303_VER1.md
- [[SAMA Output Floor Requirements]] - document - markdown/SAMA_EN_4376_VER1.md
- [[Securities Financing Transaction Exposures]] - concept - markdown/SAMA_EN_4303_VER1.md
- [[Written Credit Derivatives]] - concept - markdown/SAMA_EN_4303_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Leverage__SA-CCR_Requirements
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_CCP Exposure Calculation]]
- 1 edge to [[_COMMUNITY_SA-CCR Supervisory Parameters]]

## Top bridge nodes
- [[PFE Add-on Calculation]] - degree 4, connects to 1 community
- [[Maturity Factor]] - degree 3, connects to 1 community