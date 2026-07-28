---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Struck-off Commercial Registers

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Handling of entities whose commercial registers have been struck off — bearing on ongoing due diligence, account maintenance, and continued dealing with legal persons that have lost legal standing.

## How members connect

- Single-member cluster: the circular transmits lists of struck-off commercial registers for institutions to act upon.
- Feeds ongoing CDD/KYB and relationship-review obligations, since a struck-off registration undermines a customer's legal existence and authority.

## Members
- [[Struck-off Commercial Registers Lists Circular]] - document - markdown/SAMA_EN_9670_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Struck-off_Commercial_Registers
SORT file.name ASC
```
