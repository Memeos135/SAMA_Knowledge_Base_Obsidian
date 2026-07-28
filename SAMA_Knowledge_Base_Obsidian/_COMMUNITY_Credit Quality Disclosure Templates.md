---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# Credit Quality Disclosure Templates

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

Pillar 3 credit-risk disclosure regime: standardized templates and tables banks must complete to disclose credit quality of assets, defaulted exposures, prudential treatment of problem assets, and credit risk mitigation.

## How members connect

- CR1 (credit quality of assets) is the anchor and cross-references CR2 (movement in defaulted stock), CR3 (CRM techniques) and the qualitative CRB tables — quantitative disclosures tie back to narrative context.
- CRB and CRB-A are paired qualitative disclosures: CRB gives general credit-quality narrative, CRB-A the prudential treatment of problem/restructured assets, so the two must be read together to interpret the numeric templates.
- Compliance consequence: these are mandatory disclosure obligations that must reconcile with one another; inconsistency between defaulted-loan figures (CR2) and asset-quality figures (CR1/CRB) signals a reporting defect.

## Members
- [[Table CR2 Changes in Stock of Defaulted Loans and Debt Securities]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Table CRB-A Additional Disclosure Related to Prudential Treatment of Problem Assets]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Table CRB Additional Disclosure Related to Credit Quality of Assets]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR1 Credit Quality of Assets]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Template CR3 Credit Risk Mitigation Techniques]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Quality_Disclosure_Templates
SORT file.name ASC
```
