---
type: community
cohesion: 0.08
members: 31
enriched: true
---

# Regulatory Capital Disclosure Templates

**Cohesion:** 0.08 - loosely connected
**Members:** 31 nodes

## Why this community

Basel III / SAMA Pillar 3 public disclosure templates for regulatory capital, RWA, leverage, liquidity, market/counterparty/credit and securitisation risk. Compliance relevance: these define the mandatory content and format of prudential disclosures banks must publish to SAMA and the market.

## How members connect

- KM1 (Key Metrics) is the hub: it aggregates and cross-references the composition (CC1), liquidity (LIQ1/LIQ2), leverage (LR2) and RWA overview (OV1) figures, so consistency across templates is a compliance obligation.
- OV1 (Overview of RWA) is the second hub, reconciling each risk-type template (CR, CCR, SEC, MR, CVA, CMS) into the total RWA that drives capital ratios.
- Reconciliation chain (LIA -> LI1 -> LI2 -> PV1) links accounting statements to regulatory exposures, evidencing why disclosed regulatory values differ from carrying values.
- TLAC-specific templates (KM2, TLAC1) apply only to G-SIB scope, a limiting condition distinct from the general capital templates.

## Members
- [[Table LIA Explanations of Differences Between Accounting and Regulatory Exposure]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CC1 Composition of Regulatory Capital]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CC2 Reconciliation of Regulatory Capital to Balance Sheet]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CCR1 Analysis of CCR Exposures by Approach_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CCR8 Exposures to Central Counterparties_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CCyB1 Countercyclical Capital Buffer]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CDC Capital Distribution Constraints]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CMS1 Modelled vs Standardised RWA]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CMS2 Comparison of Modelled and Standardised RWA for Credit Risk]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR4 Standardised Approach Credit Risk Exposure and CRM Effects_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR5 Standardised Approach Exposures by Asset Classes and Risk Weights_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR6 IRB Credit Risk Exposures by Portfolio and PD Range_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR9 IRB Backtesting of PD Per Portfolio_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CVA2 Full Basic Approach BA-CVA]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CVA4 RWA Flow Statements SA-CVA]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template KM1 Key Metrics_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template KM2 Key Metrics TLAC]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LI1 Financial Statements vs Regulatory Exposures]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LI2 Main Sources of Differences Between Regulatory and Carrying Values]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LIQ1 Liquidity Coverage Ratio_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LIQ2 Net Stable Funding Ratio_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LR1 Accounting Assets vs Leverage Exposure]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template LR2 Leverage Ratio Common Disclosure]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template MR1 Market Risk Standardised Approach]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template MR2 Market Risk IMA]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template OV1 Overview of RWA_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template PV1 Prudent Valuation Adjustments]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template SEC1 Securitisation Exposures in Banking Book]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template SEC3 Securitisation Exposures - OriginatorSponsor]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template SEC4 Securitisation Exposures - Investor]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template TLAC1 TLAC Composition for G-SIBs]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Regulatory_Capital_Disclosure_Templates
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Basic Approach CVA]]
- 1 edge to [[_COMMUNITY_CCR & CVA Capital Requirements]]

## Top bridge nodes
- [[Template OV1 Overview of RWA_1]] - degree 14, connects to 2 communities