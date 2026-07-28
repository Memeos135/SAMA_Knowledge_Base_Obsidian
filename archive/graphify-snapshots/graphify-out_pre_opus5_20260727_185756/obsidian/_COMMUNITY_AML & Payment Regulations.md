---
type: community
cohesion: 0.31
members: 9
enriched: true
---

# AML & Payment Regulations

**Cohesion:** 0.31 - loosely connected
**Members:** 9 nodes

## Why this community

This community covers the AML/CFT/PF risk assessment and beneficial ownership identification regime as it applies across banks and payment service providers in KSA, spanning primary law, implementing regulations, and SAMA circulars targeting specific high-risk customer categories. The cluster is defined by the obligation to identify, verify, and document beneficial owners using prescribed methods including the Waatheq platform, with payment regulation layered as a parallel licensing regime sharing implementation rule cross-references.

## How members connect

- The Implementing Regulation to the AML Law and the Implementing Regulations of the Law on Combating Terrorist Crimes and its Financing jointly define the CDD and beneficial ownership standards that the Waatheq, NPO, and Awqaf circulars operationalise for specific entity types.
- The three beneficial owner circulars (Waatheq, NPOs, Awqaf) each reference the AML Implementing Regulation directly, creating a tiered obligation structure: primary law → implementing regulation → sector/entity-specific circular.
- The Business Risk Assessment Guide (AML/CFT/PF) references both AML and CTF implementing regulations, positioning enterprise-level risk assessment as the upstream control that must account for the entity-specific beneficial ownership obligations below it.
- The Implementing Regulation to the Law of Payments and Payment Services references the Implementation Rules for Banking Control Law, establishing that payment service providers inherit AML-aligned implementation expectations in addition to their payment-specific licensing conditions.
- The Law of Payments and Payment Services sits as the primary authority for the payments regime, with its implementing regulation creating a parallel but cross-referenced track to banking AML rules, relevant when assessing PSP customer due diligence obligations.
## Members
- [[Business Risk Assessment Guide (AMLCFTPF)]] - document - markdown/SAMA_EN_10912_VER1.md
- [[Circular Awqaf Beneficial Owner Verification]] - document - markdown/SAMA_EN_11104_VER1.md
- [[Circular Beneficial Owner Query for NPOs]] - document - markdown/SAMA_EN_11005_VER1.md
- [[Circular Waatheq Beneficial Owner Verification]] - document - markdown/SAMA_EN_10959_VER1.md
- [[Implementation Rules for Banking Control Law]] - document - markdown/SAMA_EN_1429_VER1.md
- [[Implementing Regulation to the AML Law]] - document - markdown/SAMA_EN_1428_VER1.md
- [[Implementing Regulation to the Law of Payments and Payment Services]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Implementing Regulations of the Law of Combating Terrorist Crimes and its Financing]] - document - markdown/SAMA_EN_132_VER1_0.md
- [[Law of Payments and Payment Services]] - document - markdown/SAMA_EN_1195_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AML__Payment_Regulations
SORT file.name ASC
```
