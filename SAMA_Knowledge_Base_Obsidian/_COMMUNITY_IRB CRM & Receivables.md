---
type: community
cohesion: 0.18
members: 11
enriched: true
---

# IRB CRM & Receivables

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Why this community

Credit risk mitigation (CRM) and exposure-at-default measurement under the IRB approach, with a focus on purchased receivables, guarantees/credit derivatives, and repo-style/SFT exposure treatment. Governs how banks recognize protection and compute EAD for capital purposes.

## How members connect

- 'Treatment of Guarantees and Credit Derivatives (CRM)' is shared by both Foundation and Advanced CRM recognition nodes, differentiating the eligibility and estimation rules per IRB tier.
- EAD and 'EAD under Advanced Approach' link to repo-style/master-netting treatment and the VaR Models approach for SFTs as alternative exposure-measurement routes.
- Purchased Receivables nodes chain: Eligible Purchased Receivables -> RWA for Default Risk -> Top-Down Approach for corporate receivables, defining the specialized capital treatment.
- Effective Maturity (M) connects to repo/netting treatment as a parameter input.

## Members
- [[CRM Recognition under Advanced Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[CRM Recognition under Foundation Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[EAD under Advanced Approach]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Effective Maturity (M)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Eligible Purchased Receivables]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Exposure at Default (EAD)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[RWA for Default Risk (Purchased Receivables)]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Top-Down Approach for Purchased Corporate Receivables]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Treatment of Guarantees and Credit Derivatives (CRM)]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Treatment of Repo-Style Transactions and Master Netting]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[VaR Models Approach for SFTs]] - concept - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IRB_CRM__Receivables
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_IRB Retail & Corporate Exposures]]
- 1 edge to [[_COMMUNITY_Securitization IRB Approach]]
- 1 edge to [[_COMMUNITY_Credit Conversion & EAD]]

## Top bridge nodes
- [[Eligible Purchased Receivables]] - degree 4, connects to 2 communities
- [[Exposure at Default (EAD)_1]] - degree 3, connects to 1 community