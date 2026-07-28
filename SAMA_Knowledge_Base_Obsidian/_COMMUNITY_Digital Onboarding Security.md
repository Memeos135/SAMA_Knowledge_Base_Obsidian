---
type: community
cohesion: 0.29
members: 7
enriched: true
---

# Digital Onboarding Security

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Why this community

Security and identity-verification controls for remote/digital onboarding and access to lending apps and e-wallets, anchored in SAMA Cybersecurity Requirements. Governs how a financial institution must authenticate persons at onboarding and in transactions.

## How members connect

- 'Minimum Verification Controls' is the hub obligation: it references OTP, MFA, biometric onboarding, and the sector-specific E-Wallet and Lending Application special controls as the concrete methods that satisfy it.
- The reference to SAMA Cybersecurity Requirements subordinates these controls to SAMA's overarching cyber framework — verification measures must be read as one facet of that regime.
- Biometric, OTP and MFA are alternative/cumulative authentication mechanisms; the E-Wallet and Lending controls scope them to specific product contexts, so obligations vary by product line.
- Note the AML overlap: identity verification here is a security control, distinct from (but supporting) CDD/KYC identification obligations under the AML regime.

## Members
- [[Biometric Authentication for Remote Onboarding]] - document - markdown/SAMA_EN_2883_VER1.md
- [[E-Wallet Security Controls]] - document - markdown/SAMA_EN_2888_VER1.md
- [[Lending Application Special Controls]] - concept - markdown/SAMA_EN_2888_VER1.md
- [[Minimum Verification Controls]] - document - markdown/SAMA_EN_2888_VER1.md
- [[Multi Factor Authentication (MFA)]] - concept - markdown/SAMA_EN_2888_VER1.md
- [[One-Time-Password Mechanism (OTP)]] - concept - markdown/SAMA_EN_2888_VER1.md
- [[SAMA Cybersecurity Requirements]] - concept - markdown/SAMA_EN_2888_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Digital_Onboarding_Security
SORT file.name ASC
```
