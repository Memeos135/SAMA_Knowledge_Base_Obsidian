---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# LEI Agreement & Data Protection

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Intersection of LEI (Legal Entity Identifier) enrollment through financial institutions and Saudi personal data protection obligations. Relevant where LEI registration processes handle personal data of authorized representatives or beneficial owners.

## How members connect

- Link is conceptual, not hierarchical: the LEI agreement is an operational instrument, while PDPL Amendments M/148 sets the enforceable data-protection baseline it must respect.
- Compliance consequence: institutions issuing/renewing LEIs must ensure any personal data processed in that workflow satisfies PDPL consent, lawful-basis, and cross-border transfer requirements.
- Flag cross-regime interaction: entity-identification (KYB-adjacent) data handling triggers data-protection duties distinct from the LEI registration purpose.

## Members
- [[LEI IssuanceUpdateRenewal Agreement via Financial Institution]] - document - markdown/إصدار وتحديث وتجديد معرّف الكيانات القانونية من خلال مؤسسة مالية.md
- [[Personal Data Protection Law Amendments M148]] - document - markdown/تعديل نظام حماية البيانات الشخصية-م148.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LEI_Agreement__Data_Protection
SORT file.name ASC
```
