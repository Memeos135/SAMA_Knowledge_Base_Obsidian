---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Finance Statement Publication

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Financial disclosure/transparency obligations for finance companies, governing how and when licensed finance companies must publish their financial statements under SAMA supervision.

## How members connect

- Single-member cluster: the circular imposes a publication obligation on finance companies (who must disclose, in what form, within what timing).
- Sits subordinate to the Finance Companies Control Law and its implementing regulations as a supervisory instruction operationalizing disclosure duties.
- No internal edges present; treat as a standalone reporting/transparency requirement rather than part of an obligation chain in this graph.

## Members
- [[Publication of Finance Company Financial Statements Circular]] - document - markdown/SAMA_EN_3223_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Finance_Statement_Publication
SORT file.name ASC
```
