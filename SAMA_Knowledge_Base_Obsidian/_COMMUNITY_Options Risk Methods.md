---
type: community
cohesion: 0.25
members: 8
enriched: true
---

# Options Risk Methods

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Why this community

Methodologies for computing market-risk capital on options and non-linear positions — which calculation approach a bank may or must use depending on portfolio complexity.

## How members connect

- The Sensitivities-Based Method is the anchor, decomposing risk into Delta, Vega and Curvature components that each carry a capital charge.
- The Delta-plus Method references Vega and the Gamma Risk Capital Requirement, providing an intermediate treatment for non-linear (gamma) exposures.
- The Simplified Approach for Options and the Scenario Approach sit as alternative/fallback methods, conceptually related to the Delta-plus Method — eligibility limits (portfolio size/complexity) govern which a firm may elect.
- Decision point: method selection is not free — the framework scopes which approach applies, affecting the resulting capital charge.

## Members
- [[Curvature Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Delta Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Delta-plus Method_1]] - document - markdown/SAMA_EN_3553_VER1.md
- [[Gamma Risk Capital Requirement_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Scenario Approach_1]] - document - markdown/SAMA_EN_3553_VER1.md
- [[Sensitivities-Based Method_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Simplified Approach for Options_1]] - document - markdown/SAMA_EN_3553_VER1.md
- [[Vega Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Options_Risk_Methods
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Default Risk Capital]]
- 1 edge to [[_COMMUNITY_Standardized Credit Risk Approach]]

## Top bridge nodes
- [[Sensitivities-Based Method_1]] - degree 6, connects to 2 communities