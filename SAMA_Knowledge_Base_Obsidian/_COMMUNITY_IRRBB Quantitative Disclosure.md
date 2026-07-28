---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# IRRBB Quantitative Disclosure

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Prudential disclosure regime for Interest Rate Risk in the Banking Book (IRRBB), pairing qualitative governance disclosure with mandated quantitative reporting.

## How members connect

- Template IRRBB1 (quantitative figures) references Table IRRBBA (risk-management objectives/policies) so numbers are read against the bank's stated IRRBB governance.
- Hierarchy of disclosure: the qualitative table frames methodology and assumptions that the quantitative template must reflect.
- Both are Pillar 3-style disclosure obligations; incomplete or inconsistent pairing undermines regulatory transparency requirements.

## Members
- [[Table IRRBBA IRRBB risk management objectives and policies]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template IRRBB1 Quantitative information on IRRBB]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IRRBB_Quantitative_Disclosure
SORT file.name ASC
```
