---
type: community
cohesion: 0.40
members: 6
enriched: true
---

# Finance Companies Control Law

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Why this community

This community covers the licensing, prudential, and product-specific regulatory framework for finance companies and BNPL operators in KSA, anchored by the Finance Companies Control Law and its implementing regulations, with the Companies Law and Capital Market Law providing foundational corporate and securities law references. The BNPL-specific instruments (cap circular and regulation rules) represent the product-level overlay that compliance and RegTech controls must map against the parent licensing regime.

## How members connect

- The Implementing Regulations of Finance Companies Control Law operationalise the primary Law, referencing both the Capital Market Law and Companies Law as the corporate governance and securities framework within which licensed finance companies must operate.
- The Finance Companies Control Law (English Translation) similarly cross-references Capital Market Law and Companies Law, confirming that finance company licensing conditions are calibrated against broader KSA corporate and capital markets requirements.
- The BNPL Companies Regulation Rules establish the dedicated product regime for BNPL operators, sitting as a subordinate instrument beneath the Finance Companies Control Law framework.
- The BNPL Financing Cap Increase Circular amends or elaborates the financing exposure limits within the BNPL Rules, referencing the Implementing Regulations directly — creating a three-tier obligation chain (Law → Implementing Regulations → Circular) for cap compliance monitoring.
- The cluster defines the scope boundary for 'Consumer' under the BNPL regime, distinct from AML 'Customer' definitions, which is a critical cross-regime distinction for CDD workflow design in BNPL platforms.
## Members
- [[BNPL Companies Regulation Rules]] - concept - markdown/SAMA_EN_10888_VER1.md
- [[BNPL Financing Cap Increase Circular]] - document - markdown/SAMA_EN_10888_VER1.md
- [[Capital Market Law]] - concept - markdown/SAMA_EN_1023_VER1.md
- [[Companies Law]] - concept - markdown/SAMA_EN_1023_VER1.md
- [[Finance Companies Control Law (English Translation)]] - document - markdown/SAMA_EN_1023_VER1.md
- [[Implementing Regulations of Finance Companies Control Law (Arabic)]] - document - markdown/SAMA_AR_10698_VER1_0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Finance_Companies_Control_Law
SORT file.name ASC
```
