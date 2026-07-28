---
type: community
cohesion: 0.29
members: 8
enriched: true
---

# Bank & ECAI Exposures

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Why this community

Risk-weighting of bank and covered-bond exposures using external and standardized credit assessment approaches, and the eligibility/mapping rules for external ratings under the SAMA credit risk standard.

## How members connect

- Approach split: Exposures to Banks and Exposures to Covered Bonds are risk-weighted under either the External (ECRA) or Standardized (SCRA) assessment approach.
- Due diligence condition: Exposures to Banks references Due Diligence Requirements as a precondition to relying on the assigned risk weight.
- Rating eligibility chain: ECRA relies on Use of External Ratings, which in turn depends on ratings from an Eligible Credit Assessment Institution (ECAI) and the prescribed ECAI Rating Mapping.
- Decision use: determines whether an external rating may be used and, if not, which SCRA fallback and due-diligence obligation applies.

## Members
- [[Due Diligence Requirements]] - document - markdown/SAMA_EN_3502_VER1.md
- [[ECAI Rating Mapping]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Eligible Credit Assessment Institution (ECAI)]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Exposures to Banks]] - document - markdown/SAMA_EN_3502_VER1.md
- [[Exposures to Covered Bonds]] - document - markdown/SAMA_EN_3502_VER1.md
- [[External Credit Risk Assessment Approach (ECRA)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Standardized Credit Risk Assessment Approach (SCRA)_1]] - concept - markdown/SAMA_EN_3502_VER1.md
- [[Use of External Ratings]] - document - markdown/SAMA_EN_3502_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bank__ECAI_Exposures
SORT file.name ASC
```
