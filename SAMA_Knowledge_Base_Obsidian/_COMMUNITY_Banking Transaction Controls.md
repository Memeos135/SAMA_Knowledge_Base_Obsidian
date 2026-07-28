---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# Banking Transaction Controls

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Controls governing execution of banking-procedure transactions through SAMA's interbank system. Governance/operational-risk regime for how supervised banks process transactions.

## How members connect

- The circular imposes SAMA-set controls on banking procedure transactions and references the SAMA Net System as the channel/infrastructure to which those controls attach.
- Legal consequence: banks must observe the prescribed controls when transacting via SAMA Net; the system reference scopes where the obligation applies.

## Members
- [[Circular on Controls for Banking Procedure Transactions]] - document - markdown/SAMA_EN_5480_VER1.md
- [[SAMA Net System]] - concept - markdown/SAMA_EN_5480_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Banking_Transaction_Controls
SORT file.name ASC
```
