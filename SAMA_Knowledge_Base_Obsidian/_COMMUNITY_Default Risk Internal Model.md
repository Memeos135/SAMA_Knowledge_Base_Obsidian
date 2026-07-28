---
type: community
cohesion: 0.22
members: 9
enriched: true
---

# Default Risk Internal Model

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Why this community

Market-risk capital regime for default risk under the Internal Models Approach (IMA), covering the Default Risk Charge (DRC) computed from firm-approved internal models rather than the standardised approach. Relevant to a bank's capital-adequacy compliance for trading-book positions.

## How members connect

- IMA is the umbrella methodology that references the DRC Requirement Internal Model, the Stress Testing Programme, and SAMA supervisory approval — establishing the hierarchy that use of internal models is conditional on supervisory sign-off.
- JTD Risk is quantified through defined building blocks: Gross JTD derives from LGD, and Net JTD is calculated by offsetting Gross JTD positions — these are sequential defined inputs, not free-standing concepts.
- The DRC internal model draws on LGD and VaR as measurement inputs, tying the default-risk charge to the same quantitative apparatus governed by SAMA.

## Members
- [[DRC Requirement Internal Model]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Gross JTD Risk Position]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Internal Models Approach (IMA)_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Jump-to-Default (JTD) Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Loss Given Default (LGD)_2]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Net JTD Risk Position]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[SAMA (Supervisory Authority)]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Stress Testing Programme]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Value-at-Risk (VaR)]] - concept - markdown/SAMA_EN_3553_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Default_Risk_Internal_Model
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_P&L Attribution Testing]]
- 1 edge to [[_COMMUNITY_Standardized Credit Risk Approach]]
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_Default Risk Capital]]
- 1 edge to [[_COMMUNITY_Trading Book Boundary]]
- 1 edge to [[_COMMUNITY_Expected Shortfall Modelling]]

## Top bridge nodes
- [[Internal Models Approach (IMA)_1]] - degree 8, connects to 4 communities
- [[DRC Requirement Internal Model]] - degree 4, connects to 1 community
- [[Jump-to-Default (JTD) Risk_1]] - degree 2, connects to 1 community
- [[Value-at-Risk (VaR)]] - degree 2, connects to 1 community