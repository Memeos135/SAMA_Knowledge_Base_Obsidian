---
type: community
cohesion: 0.25
members: 9
enriched: true
---

# Operational Risk Standardized Approach

**Cohesion:** 0.25 - loosely connected
**Members:** 9 nodes

## Why this community

Basel-aligned operational risk capital regime under SAMA: the Standardized Approach for calculating minimum operational-risk capital, including the loss-data inputs that drive the multiplier.

## How members connect

- Minimum Capital Requirements for Operational Risk mandates use of the Standardized Approach, which produces Operational Risk Capital (ORC) as the binding output.
- ORC is computed from the Business Indicator Component (BIC), itself derived from the Business Indicator (BI), scaled by the Internal Loss Multiplier (ILM) — a defined calculation chain.
- ILM depends on the Loss Component (LC), linking capital to historical loss experience.
- LC is fed by Loss Data Identification, Collection and Treatment rules and the Detailed Loss Event Type Classification, which set the mandatory data-quality and taxonomy conditions.

## Members
- [[Business Indicator (BI)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Business Indicator Component (BIC)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Detailed Loss Event Type Classification]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Internal Loss Multiplier (ILM)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Loss Component (LC)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Loss Data Identification, Collection and Treatment]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Minimum Capital Requirements for Operational Risk]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Operational Risk Capital (ORC)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Standardized Approach (Operational Risk)]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Operational_Risk_Standardized_Approach
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]

## Top bridge nodes
- [[Business Indicator (BI)]] - degree 2, connects to 1 community
- [[Minimum Capital Requirements for Operational Risk]] - degree 2, connects to 1 community