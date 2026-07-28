---
type: community
cohesion: 0.20
members: 12
enriched: true
---

# Credit Risk & CCP Capital

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Why this community

Basel-based minimum capital requirements for credit and counterparty credit risk (CCR), including central counterparty (CCP) exposures, as adopted in KSA through the SAMA Basel Framework.

## How members connect

- Hierarchy: SAMA (issuer) and the SAMA Basel Framework sit above the substantive rule 'Minimum Capital Requirements for Credit Risk'; the Guidance Note on Scope of Application and legacy Basel II Circular BCS 290 fix which entities and consolidation basis the framework binds.
- 'Minimum Capital Requirements for Credit Risk' is the hub that the CCR components elaborate — Effective EPE internal model, Cross-Product Netting, CCR in the Trading Book, and SFT haircut floors all reference it as their capital-calculation base.
- CCP capital forms a nested obligation chain: Capital Requirements for CCP Exposures draws on Default Fund Exposure requirements, which in turn depend on the Hypothetical Capital Requirement (KCCP) computation.
- Decision-relevance: these define how a bank must size regulatory capital against counterparty exposures; netting-recognition and haircut-floor conditions are limits/preconditions, not options.

## Members
- [[Basel II Circular BCS 290 (June 2006)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[CCR in the Trading Book]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Capital Requirements for CCP Exposures]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Cross-Product Netting Rules]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Default Fund Exposure Capital Requirement]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Effective EPE Internal Model]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Guidance Note on Scope of Application]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Hypothetical Capital Requirement of CCP (KCCP)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Minimum Capital Requirements for Credit Risk]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Minimum Haircut Floors for SFTs]] - document - markdown/SAMA_EN_3487_VER1.md
- [[SAMA Basel Framework]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Saudi Central Bank (SAMA)_1]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Risk__CCP_Capital
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_SA-CCR & CVA Framework]]
- 3 edges to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 2 edges to [[_COMMUNITY_Leverage Ratio Exposures]]
- 1 edge to [[_COMMUNITY_Standardized Credit Risk Approach]]
- 1 edge to [[_COMMUNITY_Operational Risk Standardized Approach]]
- 1 edge to [[_COMMUNITY_Default Risk Capital]]
- 1 edge to [[_COMMUNITY_Market Risk Backtesting]]
- 1 edge to [[_COMMUNITY_Market Risk Sensitivities]]
- 1 edge to [[_COMMUNITY_SA-CCR Derivative Add-ons]]

## Top bridge nodes
- [[Minimum Capital Requirements for Credit Risk]] - degree 14, connects to 7 communities
- [[Saudi Central Bank (SAMA)_1]] - degree 7, connects to 4 communities
- [[Capital Requirements for CCP Exposures]] - degree 3, connects to 1 community
- [[Cross-Product Netting Rules]] - degree 3, connects to 1 community
- [[Default Fund Exposure Capital Requirement]] - degree 3, connects to 1 community