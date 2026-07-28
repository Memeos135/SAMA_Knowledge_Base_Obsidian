---
type: community
cohesion: 0.33
members: 7
enriched: true
---

# Payment Services Law

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Why this community

Statutory foundation for payment systems oversight — the primary laws and institutional powers under which SAMA regulates and designates payment systems in KSA.

## How members connect

- The Saudi Central Bank Law establishes SAMA and its Board of Directors as the source of authority; the Law of Payments and Payment Services confers the specific mandate over payment systems.
- SIPS is a designation implementing the payment-systems regime — designation triggers heightened oversight obligations for systemically important systems.
- Settlement Finality references SIPS: legal finality of settlement is a protected feature attaching to designated systems, insulating completed transfers from unwind.
- Hierarchy runs law (SAMA Law / Law of Payments) -> regulator powers (SAMA, Board) -> designated systems (SIPS) and their legal effects (settlement finality).

## Members
- [[Board of Directors]] - concept - markdown/SAMA_EN_1293_VER1.md
- [[Law of Payments and Payment Services]] - document - markdown/SAMA_EN_1195_VER1.md
- [[Payment Systems]] - concept - markdown/SAMA_EN_1195_VER1.md
- [[Saudi Central Bank]] - concept - markdown/SAMA_EN_1293_VER1.md
- [[Saudi Central Bank Law]] - document - markdown/SAMA_EN_1293_VER1.md
- [[Settlement Finality]] - concept - markdown/SAMA_EN_1195_VER1.md
- [[Systemically Important Payment System (SIPS)]] - concept - markdown/SAMA_EN_1195_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Payment_Services_Law
SORT file.name ASC
```
