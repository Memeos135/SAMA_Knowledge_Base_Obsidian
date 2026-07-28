---
type: community
cohesion: 0.14
members: 14
enriched: true
---

# Payment Company Accounts & Capital

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Why this community

This community addresses the prudential and operational account-opening framework applicable to licensed payment companies in KSA, sitting at the intersection of the Payment Services Provider regime (capital adequacy, e-money classification, fund safeguarding) and SAMA's general bank account rules (KYC/AML, natural/juristic person onboarding, remote account opening). The cluster is the control surface for both licensing conditions and client-money protection obligations.

## How members connect

- Classification-driven capital obligations: Small Payment Company and E-Money Company classifications determine applicable Initial and Ongoing Capital Requirements, making classification the first compliance trigger in the capital adequacy chain.
- Safeguarding as a ring-fencing obligation: Protection and Safeguarding of Protected Funds is conceptually tied to E-Money classification and operationalized through Collection Accounts for Payment Companies' Clients — the account structure is the mechanism for client-money isolation.
- KYC/AML as a cross-cutting precondition: General Instructions for Opening Bank Accounts and the Updating Account Data obligation both reference KYC Principle and AML/CFT Requirements, embedding CDD as a prerequisite for account opening and maintenance regardless of account type.
- Account-opening rules as a tiered framework: Rules for Natural Persons, Juristic Persons, and Remote Opening each reference the General Instructions as the baseline, with Juristic Person rules additionally specifying purpose-specific accounts (crowdfunding collection, real estate escrow, payment company client accounts).
- Purpose-specific collection accounts: Collection Accounts for Debt-Based Crowdfunding and Escrow Accounts for Real Estate Development appear under the Juristic Person rules, indicating that sector-specific licensing conditions (crowdfunding, real estate development) feed account-type obligations back into the payment account framework.
- Ongoing capital as a dynamic prudential control: Ongoing Capital Requirements reference both classification tiers, requiring continuous monitoring rather than a one-time threshold check — implying a recurring capital adequacy reporting and breach-notification obligation.
## Members
- [[Collection Accounts for Debt-Based Crowdfunding]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Collection Accounts for Payment Companies' Clients]] - document - markdown/SAMA_EN_1644_VER1.md
- [[E-Money Company Classification]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Escrow Account for Real Estate Development]] - document - markdown/SAMA_EN_1644_VER1.md
- [[General Instructions for Opening Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Initial Capital Requirements]] - document - markdown/SAMA_EN_1430_VER1.md
- [[KYC Principle and AMLCFT Requirements]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Ongoing Capital Requirements]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Protection and Safeguarding of Protected Funds]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Rules for Opening Accounts for Juristic Persons]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Rules for Opening Accounts for Natural Persons]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Rules for Remote Opening of Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Small Payment Company Classification]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Updating Account Data]] - document - markdown/SAMA_EN_1644_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Payment_Company_Accounts__Capital
SORT file.name ASC
```
