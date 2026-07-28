---
type: community
cohesion: 0.18
members: 11
enriched: true
---

# Credit Classification IFRS 9

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Why this community

Credit risk classification and expected-credit-loss (ECL) provisioning for finance companies, aligning SAMA prudential classification with IFRS 9 staging and impairment.

## How members connect

- Legal anchor: Credit Risk Classification references the Finance Companies Control Law (the enabling statute) and IFRS 9 (the accounting standard whose ECL methodology it operationalises).
- Concept chain: Stage 1/2/3 classification is driven by definitions of Default, Forbearance and Restructuring; Write-off relates to Default, and Restructuring is treated as a form of Forbearance affecting staging.
- Governance and Credit Risk Management provisions impose oversight duties over ECL Provisioning — i.e., the board/management accountability layer sits on top of the IFRS 9 measurement obligation.
- Decision-relevance: staging outcomes determine provisioning levels; misclassification of forborne/restructured exposures directly affects regulatory-provision adequacy.

## Members
- [[Credit Risk Classification]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Credit Risk Management]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Default]] - concept - markdown/SAMA_EN_11055_VER1.md
- [[Expected Credit Loss Provisioning]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Finance Companies Control Law_1]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Forbearance]] - concept - markdown/SAMA_EN_11055_VER1.md
- [[Governance]] - document - markdown/SAMA_EN_11055_VER1.md
- [[IFRS 9]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Restructuring]] - document - markdown/SAMA_EN_11055_VER1.md
- [[Stage 123 Exposure Classification]] - concept - markdown/SAMA_EN_11055_VER1.md
- [[Write-off]] - document - markdown/SAMA_EN_11055_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Classification_IFRS_9
SORT file.name ASC
```
