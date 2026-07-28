---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# ATM Transaction Requirements

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Payments operational/consumer-facing requirements for ATM transactions, defining receipt obligations across cash and non-cash transaction types. Relevant to deciding disclosure/receipt duties at the ATM point of service.

## How members connect

- The ATM Receipts Initiative sets the receipt-provision requirement and references the transaction categories it applies to.
- 'Cash Withdrawal Transaction Stream' and 'Non-cash Transactions Stream' function as scoping definitions delimiting which transactions trigger the receipt obligation.
- Links are definitional/scoping — the streams determine the coverage of the receipt requirement rather than impose separate obligations.

## Members
- [[Cash Withdrawal Transaction Stream]] - document - markdown/SAMA_EN_11076_VER1.md
- [[Non-cash Transactions Stream]] - document - markdown/SAMA_EN_11076_VER1.md
- [[Requirements for ATM Receipts Initiative]] - document - markdown/SAMA_EN_11076_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ATM_Transaction_Requirements
SORT file.name ASC
```
