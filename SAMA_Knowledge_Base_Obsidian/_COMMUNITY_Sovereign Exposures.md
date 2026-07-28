---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Sovereign Exposures

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Credit risk capital treatment for sovereign exposures under SAMA's capital adequacy rules. Sets risk weights for claims on central governments and central banks.

## How members connect

- Single-node community: establishes the sovereign risk-weight regime driving minimum capital requirements.
- Foundational reference point; PSE and other exposure classes are calibrated relative to sovereign treatment.
- Decision relevance: correct sovereign classification governs the (often preferential) risk weight applied, directly affecting capital adequacy ratios.

## Members
- [[Exposures to Sovereigns]] - document - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Sovereign_Exposures
SORT file.name ASC
```
