---
type: community
cohesion: 0.22
members: 9
enriched: true
---

# OTC Derivatives Reporting

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Why this community

OTC derivatives trade-reporting and risk-mitigation regime, requiring reporting to a SAMA-authorised Trade Repository and prescribing bilateral risk-mitigation duties.

## How members connect

- The parent requirement splits into Section A (trade reporting obligations) and Section B (risk mitigation obligations) as its two operative limbs.
- Section A references the reporting mechanics: submission to the SAMA Authorised TR, use of UPI and UTI identifiers, and coverage of Reportable Life Cycle Events.
- The instrument supersedes SAMA Circular 42056371, marking the prior circular as replaced for hierarchy/version purposes.
- The v1.0 node is a semantically identical version of the current requirement, indicating the same instrument under versioning.

## Members
- [[OTC Derivatives TR Reporting & Risk Mitigation Requirements]] - document - markdown/SAMA_EN_10592_VER1.md
- [[OTC Derivatives TR Reporting & Risk Mitigation Requirements (v1.0)]] - document - markdown/SAMA_EN_10593_VER1_0.md
- [[Reportable Life Cycle Events]] - concept - markdown/SAMA_EN_10592_VER1.md
- [[SAMA Authorised Trade Repository (TR)]] - concept - markdown/SAMA_EN_10592_VER1.md
- [[Section A Trade Reporting Requirements]] - concept - markdown/SAMA_EN_10592_VER1.md
- [[Section B Risk Mitigation Requirements]] - concept - markdown/SAMA_EN_10592_VER1.md
- [[Superseded SAMA Circular 42056371]] - document - markdown/SAMA_EN_10592_VER1.md
- [[Unique Product Identifier (UPI)]] - concept - markdown/SAMA_EN_10592_VER1.md
- [[Unique Trade Identifier (UTI)]] - concept - markdown/SAMA_EN_10592_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OTC_Derivatives_Reporting
SORT file.name ASC
```
