---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Insurance Types

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

Taxonomy of insurance/risk-transfer arrangements distinguishing genuine risk transfer from retained-risk structures — relevant to characterization of coverage and prudential/accounting treatment.

## How members connect

- The members are contrasted concepts: Regular Insurance (full risk transfer), Finite Risk Insurance (limited/blended transfer), and Self Insurance (risk retention).
- Finite Risk sits conceptually between Regular and Self Insurance, marking the boundary where an arrangement may not qualify as true insurance.
- Deductibles is referenced by Regular Insurance as a retained-risk feature within an otherwise transferring policy — a decision point for how much risk is genuinely ceded.

## Members
- [[Deductibles]] - concept - markdown/SAMA_EN_9492_VER1.md
- [[Finite Risk Insurance]] - concept - markdown/SAMA_EN_9492_VER1.md
- [[Regular Insurance]] - concept - markdown/SAMA_EN_9492_VER1.md
- [[Self Insurance]] - concept - markdown/SAMA_EN_9492_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Insurance_Types
SORT file.name ASC
```
