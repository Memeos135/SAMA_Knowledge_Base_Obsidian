---
type: community
cohesion: 0.60
members: 6
enriched: true
---

# Targeted Financial Sanctions

**Cohesion:** 0.60 - moderately connected
**Members:** 6 nodes

## Why this community

This community covers the Targeted Financial Sanctions (TFS) compliance regime in KSA, comprising two parallel TFS rule instruments, the primary AML and CTF laws, and the AML/CTF operational and risk assessment guides. It represents the sanctions screening and freeze-without-delay obligation cluster, where regulatory controls must address both UN-listed and domestically designated persons across all regulated entity types.

## How members connect

- TFS Rules 10667 and 10668 are semantically parallel instruments, each referencing the Anti-Money Laundering Law and Counter-Terrorism Crimes and Financing Law as their dual legal bases, establishing that TFS obligations derive from both regimes simultaneously.
- Both TFS rule instruments reference the AML/CTF Guide, positioning the Guide as the operational implementation reference for screening procedures, freeze obligations, and reporting requirements mandated by the TFS Rules.
- The AML/CTF/CPF Business Risk Assessment Guide references the AML Law, CTF Law, and the AML/CTF Guide, anchoring TFS risk as a component of enterprise-level AML/CTF/PF risk assessment rather than a standalone process.
- The Anti-Money Laundering Law and Counter-Terrorism Crimes and Financing Law function as the shared primary law layer, with TFS rules and guides acting as subordinate instruments that must be read consistently with both statutes.
- The cluster implies a screening and monitoring control family: real-time or pre-transaction name screening against consolidated sanctions lists, freeze execution workflows, reporting to competent authorities, and documented risk assessment of TFS exposure by business line.
## Members
- [[AMLCTF Guide]] - concept - markdown/SAMA_EN_10667_VER1.md
- [[AMLCTFCPF Business Risk Assessment Guide]] - document - markdown/SAMA_EN_10911_VER1.md
- [[Anti-Money Laundering Law]] - concept - markdown/SAMA_EN_10667_VER1.md
- [[Counter-Terrorism Crimes and Financing Law]] - concept - markdown/SAMA_EN_10667_VER1.md
- [[Targeted Financial Sanctions Rules (10667)]] - document - markdown/SAMA_EN_10667_VER1.md
- [[Targeted Financial Sanctions Rules (10668)]] - document - markdown/SAMA_EN_10668_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Targeted_Financial_Sanctions
SORT file.name ASC
```
