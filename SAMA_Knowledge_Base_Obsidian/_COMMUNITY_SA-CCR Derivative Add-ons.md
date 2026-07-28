---
type: community
cohesion: 0.15
members: 13
enriched: true
---

# SA-CCR Derivative Add-ons

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Why this community

Basel SA-CCR counterparty credit-risk capital methodology as adopted by SAMA — the PFE add-on calculation for derivative exposures and the alternative Internal Models Method.

## How members connect

- The PFE Add-on is the aggregating provision that references the five asset-class add-ons (interest rate, FX, credit, equity, commodity).
- Each add-on is built from shared computational inputs — Hedging Set, Effective Notional, Supervisory Factor and Maturity Factor — establishing a definitional dependency chain.
- Maturity Factor is defined by reference to the Margin Period of Risk (MPOR), linking add-on calculation to margining assumptions.
- IMM is the alternative approach, referencing Effective EPE and MPOR — flagging that a firm's method choice determines which parameters govern its capital calculation.

## Members
- [[Add-on for Commodity Derivatives]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Add-on for Credit Derivatives]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Add-on for Equity Derivatives]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Add-on for Foreign Exchange Derivatives]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Add-on for Interest Rate Derivatives]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Effective Expected Positive Exposure (Effective EPE)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Effective Notional]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Hedging Set]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Internal Models Method (IMM)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Margin Period of Risk (MPOR)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Maturity Factor (MF)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Potential Future Exposure (PFE) Add-on]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Supervisory Factor (SF)]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SA-CCR_Derivative_Add-ons
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SA-CCR & CVA Framework]]
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_Market Risk Backtesting]]
- 1 edge to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 1 edge to [[_COMMUNITY_Leverage Ratio Exposures]]
- 1 edge to [[_COMMUNITY_Market Risk Sensitivities]]
- 1 edge to [[_COMMUNITY_CCP Exposure Calculation]]
- 1 edge to [[_COMMUNITY_CCR & CVA Capital Requirements]]

## Top bridge nodes
- [[Internal Models Method (IMM)]] - degree 7, connects to 5 communities
- [[Effective Expected Positive Exposure (Effective EPE)]] - degree 3, connects to 2 communities
- [[Potential Future Exposure (PFE) Add-on]] - degree 7, connects to 1 community
- [[Effective Notional]] - degree 3, connects to 1 community