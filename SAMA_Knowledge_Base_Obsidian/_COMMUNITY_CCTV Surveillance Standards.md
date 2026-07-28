---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# CCTV Surveillance Standards

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Physical security standards for the financial sector, specifying CCTV technical requirements tied to defined surveillance purposes.

## How members connect

- The specifications document references the surveillance objectives, so the technical requirements (camera quality, coverage) are scoped by the intended function.
- Objectives define graded terms — Identification, Recognition, Detection — that set the compliance benchmark each installed system must meet.
- Decision consequence: an entity's CCTV adequacy is assessed against the objective category applicable to a given zone, not a single uniform spec.

## Members
- [[CCTV Specifications for Financial Sector]] - document - markdown/SAMA_EN_11037_VER1.md
- [[CCTV Surveillance Objectives (IdentificationRecognitionDetection)]] - concept - markdown/SAMA_EN_11037_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CCTV_Surveillance_Standards
SORT file.name ASC
```
