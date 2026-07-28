---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# Risk-Weighted Assets Overview

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

Top-level architecture of minimum capital requirements: how total Risk-Weighted Assets decompose into risk-type components and their detailed calculation frameworks. Frames the aggregate capital-adequacy obligation.

## How members connect

- Risk-Weighted Assets is the parent aggregate; it references RWA for Credit Risk and RWA for Operational Risk as constituent components (market risk implied by the wider framework).
- RWA for Credit Risk references SCCR (counterparty credit risk and CVA capital) as its detailed sub-regime.
- RWA for Operational Risk references SOPE as the specific minimum-capital methodology for operational risk — a hierarchy from overview to computational detail.

## Members
- [[RWA for Credit Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[RWA for Operational Risk]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Risk-Weighted Assets]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[SCCR - Minimum Capital Requirements for CCR and CVA]] - document - markdown/SAMA_EN_3487_VER1.md
- [[SOPE - Minimum Capital Requirements for Operational Risk]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Risk-Weighted_Assets_Overview
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_Default Risk Capital]]
- 1 edge to [[_COMMUNITY_Credit Conversion & EAD]]

## Top bridge nodes
- [[Risk-Weighted Assets]] - degree 4, connects to 2 communities
- [[RWA for Credit Risk]] - degree 3, connects to 1 community