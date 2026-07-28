---
type: community
cohesion: 0.12
members: 18
enriched: true
---

# LCR & NSFR Metrics

**Cohesion:** 0.12 - loosely connected
**Members:** 18 nodes

## Why this community

Basel-derived LCR and NSFR calculation mechanics and monitoring tools as adopted by SAMA, covering the numerator/denominator components and supplementary funding-concentration and currency-mismatch metrics.

## How members connect

- Authority chain: components cite the source BCBS LCR (Jan 2013) and NSFR (Oct 2014) documents plus SAMA circulars (BCS 771, Leverage Ratio 351000133367) as the standards SAMA transposes.
- LCR side references the Stock of HQLA formula, Level 2 asset cap, and monitoring tools (funding concentration, significant counterparty, LCR by currency); NSFR side references ASF/RSF, interdependent assets/liabilities and off-balance-sheet exposures.
- Derivative treatment links across the ratio: NSFR Derivative Assets/Liabilities share data and both cite the Leverage Ratio circular for their measurement basis.
- Relationships are largely definitional/calculational cross-references — these are the technical building blocks that operationalize the prudential ratios in communities 20-21.

## Members
- [[Available Stable Funding (ASF)]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[BCBS LCR Document Jan 2013]] - document - markdown/SAMA_EN_3417_VER1.md
- [[BCBS NSFR Document Oct 2014]] - document - markdown/SAMA_EN_3467_VER1.md
- [[Cap on Level 2 Assets Calculation]] - concept - markdown/SAMA_EN_3417_VER1.md
- [[Circular 351000133367 (Leverage Ratio)]] - document - markdown/SAMA_EN_3467_VER1.md
- [[Circular BCS 771 (Dec 2008)]] - document - markdown/SAMA_EN_3467_VER1.md
- [[Concentration of Funding Metric]] - document - markdown/SAMA_EN_3417_VER1.md
- [[Interdependent Assets and Liabilities]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[LCR by Significant Currency]] - document - markdown/SAMA_EN_3417_VER1.md
- [[Liquidity Coverage Ratio (LCR)_1]] - document - markdown/SAMA_EN_3467_VER1.md
- [[Market-related Monitoring Tools]] - document - markdown/SAMA_EN_3417_VER1.md
- [[NSFR Derivative Assets]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[NSFR Derivative Liabilities]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[Net Stable Funding Ratio (NSFR)_1]] - document - markdown/SAMA_EN_3467_VER1.md
- [[Off-Balance Sheet Exposures]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[Required Stable Funding (RSF)]] - concept - markdown/SAMA_EN_3467_VER1.md
- [[Significant Counterparty]] - concept - markdown/SAMA_EN_3417_VER1.md
- [[Stock of HQLA Formula]] - concept - markdown/SAMA_EN_3417_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LCR__NSFR_Metrics
SORT file.name ASC
```
