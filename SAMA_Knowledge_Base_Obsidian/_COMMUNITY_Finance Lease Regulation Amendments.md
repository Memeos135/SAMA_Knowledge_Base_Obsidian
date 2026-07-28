---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Finance Lease Regulation Amendments

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Amendments to the executive (implementing) regulations governing finance lease activity — a change instrument modifying the finance-lease regime for licensed finance companies.

## How members connect

- Single-member cluster acting as an amending instrument: it revises prior Finance Lease Executive Regulations rather than creating a standalone regime.
- Hierarchy: Finance Lease Law -> Finance Lease Executive Regulations -> this amending circular; the circular's provisions must be read as superseding/altering the earlier regulation text.
- No internal edges; consequence for users is versioning — confirm which provisions of the executive regulations are in force post-amendment.

## Members
- [[Amendments to Finance Lease Executive Regulations Circular]] - document - markdown/SAMA_EN_3243_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Finance_Lease_Regulation_Amendments
SORT file.name ASC
```
