---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Trading Book Policy

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

Boundary and governance rules separating the trading book from the banking book for market-risk capital purposes. Determines which positions attract trading-book treatment and how transfers between books are controlled.

## How members connect

- Trading Book and Banking Book are the two defined regulatory buckets; their conceptual pairing sets the classification boundary that drives capital treatment.
- The Trading Book Policy Statement (TPS) is the required governing document evidencing how a bank assigns and manages trading-book positions.
- Trading Desk is the organisational unit for trading-book activity; Internal Risk Transfer governs movements between banking and trading books, referencing both to constrain arbitrage of the boundary.

## Members
- [[Banking Book]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Internal Risk Transfer]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Trading Book]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Trading Book Policy Statement (TPS)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Trading Desk]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Trading_Book_Policy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]

## Top bridge nodes
- [[Internal Risk Transfer]] - degree 3, connects to 1 community