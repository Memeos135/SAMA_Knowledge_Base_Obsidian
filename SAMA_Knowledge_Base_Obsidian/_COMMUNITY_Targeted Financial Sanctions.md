---
type: community
cohesion: 0.28
members: 9
enriched: true
---

# Targeted Financial Sanctions

**Cohesion:** 0.28 - loosely connected
**Members:** 9 nodes

## Why this community

KSA targeted financial sanctions (TFS) regime: obligations on financial institutions to screen against, freeze, and report on UN/domestic sanctions lists, grounded in the AML statutory framework. Covers the sanctions/TFS compliance problem-space end to end.

## How members connect

- The Targeted Financial Sanctions Rules are the anchor instrument, referencing the AML Law as its statutory basis (law -> implementing rules).
- The Rules impose and cross-reference the operational duties: list management, screening, alert handling/escalation, freezing/unfreezing, record keeping, and training — each a mandatory control component.
- Screening and Sanctions List Management are conceptually paired (screening depends on current list data); alert handling feeds freezing/unfreezing as the enforcement action.
- The '(Copy)' node is a semantic duplicate of the Rules — treat as the same authority, not a separate obligation.

## Members
- [[Alert Handling and Escalation]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Anti-Money Laundering Law]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Freezing and Unfreezing Procedures]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Record Keeping]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Sanctions List Management]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Screening Procedures and Controls]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Targeted Financial Sanctions Rules]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Targeted Financial Sanctions Rules (Copy)]] - document - markdown/SAMA_EN_10668_VER1.md
- [[Training and Awareness]] - document - markdown/SAMA_EN_10667_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Targeted_Financial_Sanctions
SORT file.name ASC
```
