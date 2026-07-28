---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# ICAAP Reporting Requirements

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Prudential governance/risk regime: the Internal Capital Adequacy Assessment Process (ICAAP) reporting duty imposed on banks to demonstrate capital adequacy against their risk profile to SAMA.

## How members connect

- Single-member node capturing a recurring supervisory reporting obligation (who reports, to SAMA, on what cadence).
- Subordinate to SAMA's capital-adequacy/risk-governance framework; ICAAP is the institution-side assessment feeding supervisory review.
- No internal edges; standalone prudential obligation with no linked definitions in this cluster.

## Members
- [[ICAAP Reporting Requirements]] - document - markdown/SAMA_EN_8679_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ICAAP_Reporting_Requirements
SORT file.name ASC
```
