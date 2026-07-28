---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Unencumbered Assets Metric

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Prudential liquidity metric — the Available Unencumbered Assets measure used in liquidity-risk supervision, identifying assets free of encumbrance that could support funding needs.

## How members connect

- Single-member cluster: defines a supervisory liquidity/risk metric rather than imposing a conduct obligation directly.
- Belongs to the governance/risk (liquidity-risk) regime and is typically referenced by liquidity reporting and risk-management requirements.
- No internal edges present; its decision-usefulness depends on the reporting framework that calls upon this metric.

## Members
- [[Available Unencumbered Assets Metric]] - document - markdown/SAMA_EN_3417_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Unencumbered_Assets_Metric
SORT file.name ASC
```
