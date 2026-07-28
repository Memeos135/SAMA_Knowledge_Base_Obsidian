---
type: community
cohesion: 0.25
members: 8
enriched: true
---

# Credit Conversion & EAD

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Why this community

Credit risk capital measurement — quantifying exposure at default (EAD), including off-balance-sheet conversion, under the SAMA credit risk minimum capital framework, plus the Pillar 3 disclosure templates that report asset quality.

## How members connect

- Definitional chain: EAD Estimation Requirements and EAD under Foundation Approach both apply Credit Conversion Factors to translate Off-Balance Sheet Items into a credit-equivalent exposure amount.
- Hierarchy: Off-Balance Sheet Items and the templates sit under SCRE — Minimum Capital Requirements for Credit Risk as the governing capital regulation.
- Disclosure linkage: Templates CR1, CR2, and CR3 cross-reference one another to report credit quality, defaulted-loan movements, and mitigation coverage consistently.
- Decision use: clarifies which conversion inputs and approach (foundation vs. estimation) drive the reported/regulatory exposure figure.

## Members
- [[Credit Conversion Factors]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[EAD Estimation Requirements]] - document - markdown/SAMA_EN_3487_VER1.md
- [[EAD under Foundation Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Off-Balance Sheet Items]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[SCRE - Minimum Capital Requirements for Credit Risk]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR1 - Credit Quality of Assets]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template CR2 - Changes in Stock of Defaulted Loans]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template CR3 Credit risk mitigation techniques overview]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Conversion__EAD
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Standardized Credit Risk Approach]]
- 1 edge to [[_COMMUNITY_IRB Credit Risk Approach]]
- 1 edge to [[_COMMUNITY_Leverage Ratio Exposures]]
- 1 edge to [[_COMMUNITY_Risk-Weighted Assets Overview]]
- 1 edge to [[_COMMUNITY_Credit & Securitization Templates]]
- 1 edge to [[_COMMUNITY_IRB CRM & Receivables]]

## Top bridge nodes
- [[Credit Conversion Factors]] - degree 4, connects to 1 community
- [[Off-Balance Sheet Items]] - degree 3, connects to 1 community
- [[SCRE - Minimum Capital Requirements for Credit Risk]] - degree 3, connects to 1 community
- [[Template CR3 Credit risk mitigation techniques overview]] - degree 2, connects to 1 community
- [[EAD Estimation Requirements]] - degree 2, connects to 1 community