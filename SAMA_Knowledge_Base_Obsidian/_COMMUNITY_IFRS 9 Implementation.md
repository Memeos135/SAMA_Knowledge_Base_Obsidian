---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# IFRS 9 Implementation

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

Accounting-standards compliance regime: SAMA's phased mandate for finance companies (and banks) to adopt IFRS 9 / IAS, layered as standard -> implementing regulation -> circulars setting timing and implementation.

## How members connect

- The Implementing Regulation of the Finance Companies Control Law provides the legal basis; the Circular on Timing of Adopting IAS references it to fix when adoption is required.
- The IFRS 9 Implementation Plan circular references the IFRS 9 standard itself, translating the substantive standard into a supervised implementation obligation.
- The two circulars are semantically linked as parallel timing/implementation instruments — read together to determine the applicable compliance deadline and scope.

## Members
- [[Circular on IFRS 9 Financial Instruments Implementation Plan]] - document - markdown/SAMA_EN_5477_VER1.md
- [[Circular on Timing of Adopting IAS]] - document - markdown/SAMA_EN_5455_VER1.md
- [[IFRS 9 - Financial Instruments]] - document - markdown/SAMA_EN_5477_VER1.md
- [[Implementing Regulation of Finance Companies Control Law_2]] - document - markdown/SAMA_EN_5455_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IFRS_9_Implementation
SORT file.name ASC
```
