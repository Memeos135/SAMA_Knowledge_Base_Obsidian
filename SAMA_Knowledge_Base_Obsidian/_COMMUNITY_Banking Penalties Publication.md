---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Banking Penalties Publication

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

SAMA's regime for publicly disclosing enforcement actions against banks, linking the disclosure mechanism to a standardized taxonomy of violation types.

## How members connect

- The publication Instructions govern when and how SAMA discloses banking penalties, and reference the Classification Guide to categorize each published violation.
- Hierarchy: the Guide functions as a subordinate classification aid to the operative disclosure Instructions.
- Decision-usefulness: a bank assessing reputational/enforcement exposure reads the Instructions for disclosure triggers and the Guide to understand how a given breach will be labelled publicly.

## Members
- [[Instructions for Publishing Banking Penalties]] - document - markdown/SAMA_EN_5544_VER1.md
- [[Violation Topic Classification Guide]] - concept - markdown/SAMA_EN_5544_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Banking_Penalties_Publication
SORT file.name ASC
```
