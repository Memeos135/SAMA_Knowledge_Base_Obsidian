---
type: community
cohesion: 0.08
members: 32
enriched: true
---

# Market Risk Sensitivities

**Cohesion:** 0.08 - loosely connected
**Members:** 32 nodes

## Why this community

Market risk capital regime: the standardised measurement of trading-book risk, spanning the Sensitivities-Based Method (SBM), the Simplified Standardised Approach, and legacy maturity/duration and options methods. Defines how banks quantify capital charges for market risk.

## How members connect

- SBM is the organizing parent, decomposing risk into Delta, Vega and Curvature and referencing the risk classes (GIRR, CSR, Equity, Commodity, FX) to which those sensitivities apply.
- Sensitivity definitions chain into risk classes: PV01 measures GIRR delta, CS01 measures CSR delta; CSR further references the Correlation Trading Portfolio special treatment.
- The Simplified Standardised Approach is an alternative regime referencing simplified interest-rate/commodities/equity/FX treatments and the Maturity/Duration methods, splitting Specific vs General Market Risk.
- Options treatment is scoped via the Simplified Approach, Delta-plus Method and Scenario Approach, with Gamma/Vega and Supervisory Delta adjustments defining the capture of non-linear risk.

## Members
- [[CS01 Sensitivity]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Commodities Risk]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Commodities Risk (Simplified SA)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Commodity Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Correlation Trading Portfolio (CTP)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Credit Spread Risk (CSR)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Curvature Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Delta Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Delta-plus Method]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Duration Method]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Duration Method_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Equity Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Equity Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Foreign Exchange (FX) Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Gamma Risk Capital Requirement]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[General Interest Rate Risk (GIRR)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[General Market Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[General Market Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Interest Rate Risk]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Interest Rate Risk (Simplified SA)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Maturity Method]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Maturity Method_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[PV01 Sensitivity]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Scenario Approach]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Sensitivities-Based Method]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Simplified Approach for Options]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Simplified Standardised Approach]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Simplified Standardised Approach_1]] - document - markdown/SAMA_EN_3553_VER1.md
- [[Specific Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Specific Risk_1]] - concept - markdown/SAMA_EN_3553_VER1.md
- [[Supervisory Delta Adjustment]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Vega Risk]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Market_Risk_Sensitivities
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_Default Risk Capital]]
- 1 edge to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 1 edge to [[_COMMUNITY_SA-CCR Derivative Add-ons]]
- 1 edge to [[_COMMUNITY_Trading Book Boundary]]

## Top bridge nodes
- [[Sensitivities-Based Method]] - degree 10, connects to 2 communities
- [[Specific Risk_1]] - degree 4, connects to 2 communities
- [[Interest Rate Risk (Simplified SA)]] - degree 6, connects to 1 community
- [[Simplified Standardised Approach]] - degree 5, connects to 1 community
- [[Supervisory Delta Adjustment]] - degree 2, connects to 1 community