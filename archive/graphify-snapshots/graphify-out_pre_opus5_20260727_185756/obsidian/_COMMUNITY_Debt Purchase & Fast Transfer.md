---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Debt Purchase & Fast Transfer

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Consumer finance debt portfolio transactions intersecting with domestic payment infrastructure, specifically the SARIE Fast Transfer System. This community covers the regulatory conditions governing the purchase of consumer finance receivables and the settlement or notification mechanics that reference SARIE, linking credit/finance company obligations to payment system operational requirements. The cluster highlights a cross-regime interaction between consumer finance rules and payment infrastructure compliance.

## How members connect

- Consumer Finance Debt Purchase Instructions reference SARIE Fast Transfer System for settlement or disbursement mechanics associated with purchased receivables
- Debt purchase eligibility, pricing, and borrower notification obligations in the Instructions interact with real-time payment capabilities of SARIE
- Borrower rights on debt transfer (notification, continuity of terms) create data and messaging requirements executable via SARIE infrastructure
- Finance company licensing conditions span both instruments: credit origination rules and payment system access/participation rules
- Operational risk and settlement finality considerations under SARIE are relevant to the timing obligations imposed by the Debt Purchase Instructions
## Members
- [[Consumer Finance Debt Purchase Instructions]] - document - markdown/SAMA_EN_2082_VER1.md
- [[SARIE Fast Transfer System]] - concept - markdown/SAMA_EN_2082_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Debt_Purchase__Fast_Transfer
SORT file.name ASC
```
