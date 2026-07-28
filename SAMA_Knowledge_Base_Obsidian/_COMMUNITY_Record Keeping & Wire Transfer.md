---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Record Keeping & Wire Transfer

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

AML/CTF operational obligations tying transaction record retention to funds-transfer traceability requirements. Covers the recordkeeping and originator/beneficiary information duties central to the wire-transfer ('travel rule') regime.

## How members connect

- Wire Transfer references Record Keeping because transfer messages and their originator/beneficiary data must be retained for the mandated period to satisfy AML/CTF audit and law-enforcement access.
- The linkage makes recordkeeping the evidentiary backbone of wire-transfer compliance: failure to retain transfer data breaches both obligations.
- Read together as enforceable duties on ordering, intermediary, and beneficiary institutions handling cross-border and domestic transfers.

## Members
- [[Record Keeping_1]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Wire Transfer]] - concept - markdown/SAMA_EN_1704_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Record_Keeping__Wire_Transfer
SORT file.name ASC
```
