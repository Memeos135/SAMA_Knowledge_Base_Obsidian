---
type: community
cohesion: 0.29
members: 8
enriched: true
---

# Real Estate Credit Mitigation

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Why this community

Real estate credit exposures and the credit risk mitigation (CRM) rules applied to them — how LTV, loan splitting, and eligible collateral/guarantees affect risk weighting under the SCRE credit risk framework.

## How members connect

- Classification core: the Real Estate Exposure Class scopes LADC exposures and references the Loan Splitting Approach and LTV Ratio as the mechanics that determine risk weight.
- LTV drives splitting: Loan Splitting Approach and LTV are linked because the split allocation depends on the LTV threshold.
- CRM framework: the Credit Risk Mitigation Framework governs recognized techniques — On-Balance Sheet Netting and Guarantees/Credit Derivatives — and interacts with treatment of Defaulted Exposures.
- Decision use: shows which mitigation is admissible and how real-estate classification plus LTV determine the applicable capital treatment.

## Members
- [[Credit Risk Mitigation Framework]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Defaulted Exposures]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Guarantees and Credit Derivatives (CRM)]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Land Acquisition Development and Construction Exposures]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Loan Splitting Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Loan-to-Value Ratio (LTV)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[On-Balance Sheet Netting_1]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Real Estate Exposure Class_1]] - document - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Real_Estate_Credit_Mitigation
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_CCR Collateral & Mitigation]]
- 1 edge to [[_COMMUNITY_IRB Retail & Corporate Exposures]]

## Top bridge nodes
- [[Credit Risk Mitigation Framework]] - degree 6, connects to 2 communities