---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# GCC-NET POS Service

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Payments regime: rules governing the GCC-NET point-of-sale payment service, i.e., cross-GCC card acceptance/interoperability at merchant POS terminals under SAMA's payment-system oversight.

## How members connect

- Single-member node 'GCC-NET POS Payment Service' defining a specific payment scheme/service.
- Sits within the PSP/payments regulatory space, engaging merchant acceptance and settlement obligations.
- No internal edges present; link to broader payment-services and card-scheme rules to establish obligation chains.

## Members
- [[GCC-NET POS Payment Service]] - document - markdown/SAMA_EN_10319_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GCC-NET_POS_Service
SORT file.name ASC
```
