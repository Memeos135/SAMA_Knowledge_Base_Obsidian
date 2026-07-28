---
type: community
cohesion: 0.29
members: 7
enriched: true
---

# Regulatory Data Returns

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Why this community

Prudential and statistical reporting obligations — the periodic returns firms must submit to SAMA and the manual that governs their preparation.

## How members connect

- The Guidance Manual for the Returns Management System is the procedural hub; the quarterly, annual and monthly forms all feed data into / are governed by it.
- The LCR circulars (Revised Amended LCR Regulations and Amended LCR Prudential Returns) sit in a hierarchy: the revised regulation drives the amended prudential returns, which the returns system must reflect.
- Linkage is data-flow and procedural rather than substantive obligation-creating: the forms are the vehicle by which underlying prudential requirements (e.g. LCR) are evidenced to the regulator.
- Compliance relevance: the applicable version of the LCR returns is fixed by the later circular, so filing must track the amended template.

## Members
- [[Annual Regulatory Data Form]] - document - markdown/النموذج السنوي للبيانات التنظيمية.md
- [[Guidance Manual for the Returns Management System]] - document - markdown/الدليل الإرشادي لاستخدام نظام البيانات الإشرافية_0.md
- [[Monthly Sales and Purchases Data Form]] - document - markdown/نموذج البيانات الشهرية للمبيعات والمشتريات.md
- [[Quarterly Currency and Top Clients Form]] - document - markdown/النموذج الربعي للعملات وبيانات أكبر العملاء والعملات المزورة وبيانات الموظفين.md
- [[Quarterly and Annual Financial Statements Comparison Form]] - document - markdown/نموذج المقارنة للقوائم المالية الربعية و السنوية.md
- [[SAMA Circular on Amended LCR Prudential Returns]] - document - markdown/sama circular no (gdbc-341000107020-1434h)en.md
- [[SAMA Circular on Revised Amended LCR Regulations]] - document - markdown/sama circular no (gdbc-361000009335-1436h).md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Regulatory_Data_Returns
SORT file.name ASC
```
