---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Asset Encumbrance Template

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Prudential disclosure of asset encumbrance, covering the extent to which a bank's assets are pledged or otherwise unavailable to unsecured creditors. Relevant to liquidity risk and resolution planning under SAMA's Pillar 3 / disclosure regime.

## How members connect

- Single-member community: the ENC template is a standalone reporting instrument requiring structured disclosure of encumbered vs. unencumbered assets.
- No internal linkages present; compliance obligation is to complete and submit the template as prescribed.

## Members
- [[Template ENC - Asset Encumbrance]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Asset_Encumbrance_Template
SORT file.name ASC
```
