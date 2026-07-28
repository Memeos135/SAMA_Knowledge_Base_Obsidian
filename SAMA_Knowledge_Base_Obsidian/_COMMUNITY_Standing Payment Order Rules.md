---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Standing Payment Order Rules

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Payments/finance-company operational rules governing standing payment orders (recurring/automatic payment instructions) used by financing entities.

## How members connect

- Single-member cluster defining the rules for establishing, executing, and amending standing payment orders by financing entities.
- Cross-regime relevance: sits at the intersection of payments/PSP mechanics and finance-company obligations, with consumer-authorization and disclosure implications.

## Members
- [[Standing Payment Order for Financing Entity Rules]] - document - markdown/SAMA_EN_11027_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Standing_Payment_Order_Rules
SORT file.name ASC
```
