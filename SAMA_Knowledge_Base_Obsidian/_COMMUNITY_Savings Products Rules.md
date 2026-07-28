---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Savings Products Rules

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Consumer-facing disclosure standards for bank savings products, centered on standardized rate presentation.

## How members connect

- The General Rules for Savings Products in Banks are the binding requirement; the Annual Equivalent Rate (AER) is a defined disclosure metric mandated within them.
- The reference edge fixes AER as the required, comparable rate-expression banks must disclose to depositors.
- Decision consequence: savings-product terms must present returns via the defined AER to meet the Rules' transparency obligation.

## Members
- [[Annual Equivalent Rate (AER)]] - concept - markdown/SAMA_EN_9538_VER1.md
- [[General Rules for Savings Products in Banks]] - document - markdown/SAMA_EN_9538_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Savings_Products_Rules
SORT file.name ASC
```
