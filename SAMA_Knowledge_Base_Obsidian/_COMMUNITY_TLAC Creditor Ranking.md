---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# TLAC Creditor Ranking

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Total Loss-Absorbing Capacity (TLAC) creditor-hierarchy disclosures for resolution planning — showing where TLAC-eligible instruments rank in insolvency at the resolution-entity and material-subgroup levels.

## How members connect

- TLAC3 discloses creditor ranking at the resolution entity; TLAC2 does so at material subgroup entities — parallel templates covering different points in the group structure.
- The 'references' link ties subgroup rankings to the resolution-entity ranking so the loss-absorption waterfall can be read across the group.
- Both are subordinate resolution/prudential reporting instruments under SAMA's TLAC framework.

## Members
- [[Template TLAC2 Material Subgroup Entity Creditor Ranking]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template TLAC3 Resolution Entity Creditor Ranking]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TLAC_Creditor_Ranking
SORT file.name ASC
```
