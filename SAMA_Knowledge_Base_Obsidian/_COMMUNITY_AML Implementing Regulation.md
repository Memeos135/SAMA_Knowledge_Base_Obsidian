---
type: community
cohesion: 0.20
members: 10
enriched: true
---

# AML Implementing Regulation

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Why this community

The core AML/CTF obligation set under the SAMA AML Implementing Regulation (1428): CDD, PEP handling, correspondent/reliance rules, wire transfers, and suspicious-activity reporting to the FIU. Defines the enforceable duties of financial institutions in the AML regime.

## How members connect

- The AML Implementing Regulation (SAMA 1428) is the parent instrument that references and gives legal force to CDD, STR filing, MLA, and the Directorate of Financial Intelligence; the AML/CTF Compliance Obligation ties back to it as the source authority.
- Customer Due Diligence is the anchor obligation: PEP screening and Reliance on Another Institution are conceptually subordinate refinements (enhanced measures for PEPs; conditional outsourcing of CDD steps that does not transfer ultimate liability).
- Suspicious Transaction Reports and Cross-Border Declarations feed the Directorate of Financial Intelligence, establishing the reporting channel; Wire Transfer Requirements can trigger STR obligations where transfers lack required originator/beneficiary data.

## Members
- [[AML Implementing Regulation (SAMA 1428)]] - document - markdown/SAMA_EN_1428_VER1.md
- [[AMLCTF Compliance Obligation]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Cross-Border Declaration]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Customer Due Diligence]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Directorate of Financial Intelligence]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Mutual Legal Assistance]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Politically Exposed Persons]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Reliance on Another Institution]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Suspicious Transaction Report]] - concept - markdown/SAMA_EN_1428_VER1.md
- [[Wire Transfer Requirements]] - concept - markdown/SAMA_EN_1428_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AML_Implementing_Regulation
SORT file.name ASC
```
