---
type: community
cohesion: 0.24
members: 11
enriched: true
---

# IRB Retail & Corporate Exposures

**Cohesion:** 0.24 - loosely connected
**Members:** 11 nodes

## Why this community

Internal Ratings-Based (IRB) capital treatment for credit risk under the SAMA Basel-aligned framework, covering how banks classify and risk-weight corporate, specialized-lending, and retail exposures. Relevant to capital-adequacy compliance decisions on which IRB approach a bank is permitted to use per exposure class.

## How members connect

- 'IRB Approach Overview' is the parent node scoping the Foundation vs. Advanced IRB choice and pointing to each exposure class and calculation input.
- Exposure-class definitions (Corporates, Retail, QRRE, MSME, Specialized Lending) determine which risk-weight function and parameters apply.
- Risk Components (PD, LGD, EAD, M) feed the Risk Weight Functions; the Supervisory Slotting approach is the fallback for Specialized Lending where own estimates are not available.
- MSME is cross-referenced from both Corporate and Retail classes, marking the boundary where SME treatment shifts between the two.

## Members
- [[Advanced IRB Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Exposures to Corporates]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Foundation IRB Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[IRB Approach Overview]] - document - markdown/SAMA_EN_3502_VER1.md
- [[IRB Risk Components (PD, LGD, EAD, M)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[IRB Risk Weight Functions]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Micro Small and Medium-Sized Entities (MSME)]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Qualifying Revolving Retail Exposures]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Retail Exposure Class]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Specialized Lending]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Supervisory Slotting Criteria Approach]] - concept - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IRB_Retail__Corporate_Exposures
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_IRB Default & Provisions]]
- 1 edge to [[_COMMUNITY_Real Estate Credit Mitigation]]
- 1 edge to [[_COMMUNITY_CCR Collateral & Mitigation]]
- 1 edge to [[_COMMUNITY_IRB CRM & Receivables]]

## Top bridge nodes
- [[IRB Risk Components (PD, LGD, EAD, M)_1]] - degree 4, connects to 2 communities
- [[IRB Approach Overview]] - degree 8, connects to 1 community
- [[Specialized Lending]] - degree 3, connects to 1 community