---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Systemically Important Banks

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

Prudential regime for identifying and capitalising systemically important banks in KSA. Covers how SAMA designates domestic systemically important banks (D-SIBs) and imposes additional capital burdens on them, aligned to the Basel/BCBS global framework.

## How members connect

- The D-SIBs Framework is the governing instrument; it references the D-SIB Assessment Methodology (how a bank is identified) and Higher Loss Absorbency (the resulting capital surcharge obligation).
- Assessment Methodology operationalises designation through Scoring and Bucketing, which in turn determines the HLA bucket — a chain from measurement to the capital consequence.
- Methodology references the BCBS G-SIBs Framework as the international benchmark SAMA adapts for the domestic context; treat G-SIB text as source/analogue, not directly binding on D-SIB designation.

## Members
- [[D-SIB Assessment Methodology]] - concept - markdown/SAMA_EN_3468_VER1.md
- [[D-SIBs Framework]] - document - markdown/SAMA_EN_3468_VER1.md
- [[G-SIBs Framework (BCBS)]] - document - markdown/SAMA_EN_3468_VER1.md
- [[Higher Loss Absorbency (HLA)]] - concept - markdown/SAMA_EN_3468_VER1.md
- [[Scoring and Bucketing]] - concept - markdown/SAMA_EN_3468_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Systemically_Important_Banks
SORT file.name ASC
```
