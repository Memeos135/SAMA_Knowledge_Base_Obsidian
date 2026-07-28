---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# POS Payment Requirements

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Point-of-sale payment-acceptance obligations for PSPs/merchants — device technical standards, pre-onboarding KYC, and e-payment enablement for associations/non-profits. Bridges payments regulation with customer-verification duties.

## How members connect

- POS Devices 4G Upgrade references the Associations/Non-profits e-payment enablement, linking device modernization to expanded acceptor categories.
- KYC Verification Before POS Sale/Operation is conceptually tied to device deployment, imposing merchant-identification (KYB-type) duties before POS activation.
- Cross-regime note: the KYC-before-sale obligation connects payments/PSP rules to customer-due-diligence expectations, treating the merchant/acceptor as a subject of verification.

## Members
- [[E-Payments for Associations and Non-profits]] - document - markdown/SAMA_EN_8731_VER1.md
- [[KYC Verification Before POS SaleOperation]] - document - markdown/SAMA_EN_8725_VER1.md
- [[POS Devices Upgrade to 4G Technology]] - document - markdown/SAMA_EN_8724_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/POS_Payment_Requirements
SORT file.name ASC
```
