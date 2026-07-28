---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# Credit Risk RWA Templates

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Basel/SAMA Pillar 3 disclosure templates for credit risk RWA under internal-model approaches (IRB and IMM), covering CRM effects and period-over-period RWA movements.

## How members connect

- All three are prescribed disclosure formats sharing common RWA-flow methodology (opening/closing RWA reconciliation) under internal models.
- CR7 (CRM via credit derivatives), CR8 (IRB credit-risk RWA flows), and CCR7 (counterparty-credit-risk RWA flows under IMM) cross-reference as a linked disclosure set.
- Compliance meaning: banks using IRB/IMM must complete these as an integrated package; figures must be internally consistent across templates.

## Members
- [[Template CCR7 RWA flow statements of CCR exposures under IMM]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR7 IRB effect on RWA of credit derivatives used as CRM]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR8 RWA flow statements of credit risk exposures under IRB]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Risk_RWA_Templates
SORT file.name ASC
```
