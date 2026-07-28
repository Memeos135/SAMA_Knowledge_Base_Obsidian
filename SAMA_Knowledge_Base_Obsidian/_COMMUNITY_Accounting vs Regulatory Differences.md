---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Accounting vs Regulatory Differences

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Pillar 3 disclosure templates reconciling financial-statement (accounting) scope of consolidation with the prudential/regulatory scope used for capital purposes. This covers the bank's obligation to explain why balance-sheet carrying values differ from regulatory exposure amounts.

## How members connect

- LI1 maps accounting vs regulatory consolidation scopes; LI2 explains the drivers of exposure-amount differences that LI1 surfaces.
- The 'references' link is an explanatory chain: LI2 elaborates the sources behind the reconciliation LI1 presents, so both must be read together for a coherent disclosure.
- Both are subordinate reporting instruments implementing SAMA's adoption of the Basel Pillar 3 framework.

## Members
- [[Template LI1 - Differences Between Accounting and Regulatory Scopes]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template LI2 - Main Sources of Differences in Exposure Amounts]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Accounting_vs_Regulatory_Differences
SORT file.name ASC
```
