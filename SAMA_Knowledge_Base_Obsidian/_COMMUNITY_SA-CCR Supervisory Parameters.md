---
type: community
cohesion: 0.23
members: 13
enriched: true
---

# SA-CCR Supervisory Parameters

**Cohesion:** 0.23 - loosely connected
**Members:** 13 nodes

## Why this community

The supervisory parameter set underpinning SA-CCR add-on calculations under SAMA's counterparty credit-risk rules, including the summary parameter table and worked examples.

## How members connect

- Effective Notional is the central computed input, derived from Adjusted Notional and the Supervisory Delta Adjustment, and feeds every asset-class add-on.
- Supervisory Factor and Supervisory Correlation Parameters are regulator-prescribed values applied within each add-on and consolidated in Table 2: Summary of Supervisory Parameters.
- Hedging Set defines the netting scope within which the parameters operate across the FX, commodity and interest-rate add-ons.
- SA-CCR Sample Portfolio Examples reference the add-ons to illustrate correct application — useful as interpretive/worked guidance rather than a source of obligations.

## Members
- [[Add-on for Commodity Derivatives_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Add-on for Credit Derivatives_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Add-on for Equity Derivatives_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Add-on for Foreign Exchange Derivatives_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Add-on for Interest Rate Derivatives_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Adjusted Notional]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Effective Notional_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Hedging Set_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[SA-CCR Sample Portfolio Examples_1]] - document - markdown/SAMA_EN_4283_VER1.md
- [[Supervisory Correlation Parameters]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Supervisory Delta Adjustment_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Supervisory Factor]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Table 2 Summary of Supervisory Parameters]] - document - markdown/SAMA_EN_4283_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SA-CCR_Supervisory_Parameters
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_CCP Exposure Calculation]]
- 1 edge to [[_COMMUNITY_Leverage & SA-CCR Requirements]]

## Top bridge nodes
- [[Effective Notional_1]] - degree 6, connects to 1 community
- [[Add-on for Interest Rate Derivatives_1]] - degree 5, connects to 1 community
- [[SA-CCR Sample Portfolio Examples_1]] - degree 4, connects to 1 community