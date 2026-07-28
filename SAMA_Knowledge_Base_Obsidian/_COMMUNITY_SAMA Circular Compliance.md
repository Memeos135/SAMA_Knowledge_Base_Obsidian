---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# SAMA Circular Compliance

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

General duty of supervised financial institutions to comply with SAMA circulars, which sit below primary law and implementing regulations in the instrument hierarchy but are directly enforceable supervisory instructions.

## How members connect

- Single-member node capturing the compliance obligation itself: circulars bind licensed/supervised entities as issued under SAMA's supervisory authority.
- Positions circulars in the hierarchy (law -> regulation -> circular -> guide) as operative instructions elaborating higher instruments.
- Decision point: treat circular requirements as mandatory unless expressly scoped or superseded.

## Members
- [[Financial Institutions Compliance with SAMA Circulars]] - document - markdown/SAMA_EN_2875_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SAMA_Circular_Compliance
SORT file.name ASC
```
