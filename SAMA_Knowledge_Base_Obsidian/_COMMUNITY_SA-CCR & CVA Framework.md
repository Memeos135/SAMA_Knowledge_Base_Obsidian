---
type: community
cohesion: 0.16
members: 18
enriched: true
---

# SA-CCR & CVA Framework

**Cohesion:** 0.16 - loosely connected
**Members:** 18 nodes

## Why this community

Counterparty credit risk (SA-CCR) and credit valuation adjustment (CVA) capital framework, defining how banks compute derivative and SFT exposures and the associated CVA capital charge.

## How members connect

- SA-CCR is the anchor: it references the CCR Framework it implements and the components (EAD, Replacement Cost, Netting Set, NICA) that build the exposure calculation, with worked examples (SA-CCR Sample Portfolio) and the EAD Formula as illustrative detail.
- Replacement Cost is elaborated by Netting Set, NICA and Standard Margin Agreements effects — collateral and netting arrangements directly reduce measured exposure.
- The CVA Framework cross-references SA-CCR (exposure feeds CVA) and branches into BA-CVA (reduced and full versions) and SA-CVA delta/vega risk classes, with Eligible CVA Hedges recognized as offsets.
- Master Netting Agreements for SFTs and the Market Risk Framework are referenced as adjacent regimes governing exposure aggregation and risk-class treatment.

## Members
- [[Basic Approach for CVA (BA-CVA)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Counterparty Credit Risk (CCR) Framework]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Credit Valuation Adjustment (CVA) Framework]] - document - markdown/SAMA_EN_3487_VER1.md
- [[EAD Formula (SA-CCR)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Eligible CVA Hedges]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Exposure at Default (EAD)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Full Version of BA-CVA]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Market Risk Framework]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Master Netting Agreements for SFTs]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Net Independent Collateral Amount (NICA)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Netting Set]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Reduced Version of BA-CVA]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Regulatory CVA Calculation]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Replacement Cost (RC)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[SA-CCR Sample Portfolio Examples]] - document - markdown/SAMA_EN_3487_VER1.md
- [[SA-CVA Delta and Vega Risk Classes]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Standard Margin Agreements Effect on RC]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Standardized Approach for CCR (SA-CCR)]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SA-CCR__CVA_Framework
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 3 edges to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 3 edges to [[_COMMUNITY_SA-CCR Derivative Add-ons]]
- 2 edges to [[_COMMUNITY_IRB Credit Risk Approach]]
- 2 edges to [[_COMMUNITY_Leverage Ratio Exposures]]

## Top bridge nodes
- [[Standardized Approach for CCR (SA-CCR)]] - degree 17, connects to 4 communities
- [[Exposure at Default (EAD)]] - degree 9, connects to 3 communities
- [[Replacement Cost (RC)]] - degree 7, connects to 1 community
- [[Master Netting Agreements for SFTs]] - degree 3, connects to 1 community