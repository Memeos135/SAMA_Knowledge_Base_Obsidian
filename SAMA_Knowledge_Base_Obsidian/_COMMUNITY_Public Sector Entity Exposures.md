---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Public Sector Entity Exposures

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Credit risk capital treatment for exposures to Public Sector Entities (PSEs) under SAMA's Basel-aligned capital adequacy framework. Governs risk-weighting of claims on non-central-government public bodies.

## How members connect

- Single-node community: defines the risk-weight classification and treatment for PSE exposures for regulatory capital purposes.
- Sits within the standardised approach to credit risk; distinguishable from and often cross-referenced against sovereign exposure treatment.
- Decision relevance: determines the capital charge a bank must hold, so correct classification of a counterparty as PSE versus corporate/sovereign is the operative compliance question.

## Members
- [[Exposures to Public Sector Entities]] - document - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Public_Sector_Entity_Exposures
SORT file.name ASC
```
