---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# Risk Rating & Stress Testing

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Credit risk rating governance and its use in capital-adequacy stress testing under SAMA's prudential/risk regime. Covers how internal rating systems must be operated, maintained, and fed into stress-test capital assessments.

## How members connect

- Risk Rating System Operations references Data Maintenance: the integrity and upkeep of underlying data is a precondition for valid rating outputs.
- Risk Rating System Operations references Stress Tests for Capital Adequacy: rating outputs are an obligatory input to capital stress-testing, linking day-to-day rating governance to prudential capital sufficiency.
- Hierarchy is functional, not legal — operational rating obligations feed capital-adequacy assessment obligations.

## Members
- [[Data Maintenance]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Risk Rating System Operations]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Stress Tests for Capital Adequacy]] - concept - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Risk_Rating__Stress_Testing
SORT file.name ASC
```
