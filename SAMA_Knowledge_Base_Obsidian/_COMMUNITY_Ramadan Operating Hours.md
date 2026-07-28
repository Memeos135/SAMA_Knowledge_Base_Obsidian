---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Ramadan Operating Hours

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Operational-hours adjustments for payment and cash-handling infrastructure during Ramadan and Eid. Governs continuity-of-service timing rather than substantive conduct obligations.

## How members connect

- Both are SAMA scheduling notices coordinating the same seasonal period across different rails: SARIE interbank settlement hours and ATM cash-replenishment/transport hours.
- Legal linkage is operational alignment, not obligation hierarchy: settlement windows and cash logistics must be synchronized to preserve payment availability.
- Decision use: confirms which SAMA-mandated timing applies to each service during the holiday period.

## Members
- [[ATM Feeding and Cash Transport Hours During Ramadan]] - document - markdown/SAMA_EN_10399_VER1.md
- [[SARIE Operating Hours During Ramadan and Eid]] - document - markdown/SAMA_EN_10398_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ramadan_Operating_Hours
SORT file.name ASC
```
