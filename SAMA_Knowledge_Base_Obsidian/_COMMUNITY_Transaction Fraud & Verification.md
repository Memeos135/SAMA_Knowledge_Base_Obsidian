---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Transaction Fraud & Verification

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Payment-transaction fraud prevention tied to customer authentication — relevant to payments/PSP and card-acquiring risk controls.

## How members connect

- Identity verification via a trusted source functions as the front-end control that mitigates the fraud vectors arising in preauthorization/advice transactions.
- Relationship is conceptual: reliable customer verification reduces exposure to the described fraud, but neither provision defines the other.

## Members
- [[Customer Identity Verification via Trusted Source]] - document - markdown/SAMA_EN_4833_VER1.md
- [[Fraud via Preauthorization and Advice Transactions]] - document - markdown/SAMA_EN_4830_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Transaction_Fraud__Verification
SORT file.name ASC
```
