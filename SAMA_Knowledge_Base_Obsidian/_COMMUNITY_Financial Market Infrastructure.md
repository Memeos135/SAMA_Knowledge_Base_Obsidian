---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# Financial Market Infrastructure

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Oversight of systemically important payment and settlement systems under FMI standards, addressing classification, principle-based supervision, and legal certainty of settlement.

## How members connect

- 'Payment Systems Classification' references 'Financial Market Infrastructure Principles' — classification determines which systems are held to the PFMI standards.
- 'Settlement Finality and Insolvency' provides the legal-certainty backbone (finality protection against insolvency clawback), a core FMI principle for classified systems.
- Hierarchy runs from classification (scope) to applicable principles (obligations) to specific legal protections (settlement finality).

## Members
- [[Financial Market Infrastructure Principles]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Payment Systems Classification]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Settlement Finality and Insolvency]] - concept - markdown/SAMA_EN_1430_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Financial_Market_Infrastructure
SORT file.name ASC
```
