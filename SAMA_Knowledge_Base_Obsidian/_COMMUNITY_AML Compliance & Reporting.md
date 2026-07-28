---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# AML Compliance & Reporting

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

The AML/CTF detection-and-reporting obligation chain and its governance: ongoing transaction monitoring feeding suspicious transaction reporting to the national FIU, backed by a dedicated compliance function and senior-management accountability.

## How members connect

- Monitoring and STR reporting are sequential obligations — monitoring is the means by which suspicion is identified, triggering the reporting duty.
- STRs must be filed to SAFIU, the designated recipient; the reporting link fixes the mandatory destination and channel of disclosure.
- The AML/CTF Compliance Function owns the reporting obligation (references STR); it is the accountable unit for filing.
- Senior Management references the Compliance Function — establishing management responsibility for resourcing and overseeing the AML program, i.e. the accountability hierarchy.

## Members
- [[AMLCTF Compliance Function]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Monitoring of Transactions and Activities]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Reporting of Suspicious Transactions]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Saudi Arabia Financial Intelligence Unit (SAFIU)]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Senior Management Responsibilities]] - concept - markdown/SAMA_EN_1704_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AML_Compliance__Reporting
SORT file.name ASC
```
