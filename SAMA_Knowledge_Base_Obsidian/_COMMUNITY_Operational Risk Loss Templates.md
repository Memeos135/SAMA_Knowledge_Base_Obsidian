---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# Operational Risk Loss Templates

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Operational risk capital calculation under the Basel-aligned standardised approach, expressed through SAMA's prescribed reporting templates. Defines the mandatory data components that determine minimum operational risk capital.

## How members connect

- Templates OR1 (Historical Losses) and OR2 (Business Indicator and Subcomponents) both reference OR3 (Minimum Required Operational Risk Capital): OR1 and OR2 are input components whose values drive the OR3 capital result.
- The linkage is a calculation chain — loss history and business indicator feed the minimum capital figure; misreporting in OR1/OR2 directly affects the enforceable OR3 requirement.
- Clustering reflects a single obligation: correct completion of all three is required for compliant operational risk capital reporting.

## Members
- [[Template OR1 Historical Losses_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template OR2 Business Indicator and Subcomponents_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template OR3 Minimum Required Operational Risk Capital_1]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Operational_Risk_Loss_Templates
SORT file.name ASC
```
