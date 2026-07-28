---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Unified Number Instructions

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Identity-reference framework: the Unified Number as a customer/entity identifier and the instructions governing its replacement — relevant to identification and KYC data fields.

## How members connect

- 'Unified Number Replacement Instructions' references the defined term 'Unified Number', establishing what identifier the replacement procedure applies to.
- Definitional-plus-procedural link: the term supplies scope, the instructions impose the operational obligation for when/how the identifier changes.
- Decision relevance: affects identity records used across onboarding/CDD; confirm which regime's records must be updated on replacement.

## Members
- [[Unified Number]] - concept - markdown/SAMA_EN_4843_VER1.md
- [[Unified Number Replacement Instructions]] - document - markdown/SAMA_EN_4843_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Unified_Number_Instructions
SORT file.name ASC
```
