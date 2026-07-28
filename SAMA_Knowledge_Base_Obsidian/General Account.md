---
source_file: "markdown/SAMA_EN_11081_VER1.md"
type: "concept"
community: "Deposit Account Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Deposit_Account_Rules
  - graphify/enriched
---

# General Account

## Connections

### [[Accounts Operating Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a DTFC may lawfully do with funds in a General Account, read the Accounts Operating Rules together with the General Account definition, because the operating rules set the closed list of permitted credits, withdrawals, transfers and blocking actions applicable to that specific account type. The General Account may only be funded from the accountholder's own bank account or its linked Term Deposit Account, funds must be remitted back only to the source account, and transfers are limited to same-name General Accounts within the same DTFC. A compliance reader should conclude that any credit or withdrawal outside these enumerated channels is non-compliant, and that SAMA-ordered disclosure/blocking overrides ordinary operating permissions.
- **Grounding — this node (Page 55 / Art 195):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts."
- **Grounding — related node (Page 55-56 / Arts 196, 206):** "General Account can ONLY be funded i.e. credited through the following operations... Finance must remit the funds back to the same Bank account... from which General Account was initially funded"

### [[Deposit Account]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When mapping the two account types a Deposit-Taking Finance Company (DTFC) may operate, treat the General Account and the deposit-account/Term-Deposit structure as one integrated regime rather than independent products, because the rules state the General Account's 'sole purpose' is to facilitate operations of Term Deposit Accounts and that it can only be credited from the accountholder's own bank account or from their Term Deposit Account. For a compliance decision this means source-of-funds and name-matching controls (para 197: return funds if remitter name differs) attach at the General Account gateway and govern the whole deposit chain. Conclude that you cannot analyze deposit-account obligations in isolation from the General Account funding/withdrawal constraints.
- **Grounding — this node (Page 55 / para 196):** "General Account can ONLY be funded i.e. credited through the following operations"
- **Grounding — related node (Page 55 / para 195-196):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts"
- **Caveat:** Relation is 'conceptually_related_to' and both nodes cite the same passage; verify whether a distinct 'Deposit Account' definition exists elsewhere in the regulation before relying on a separate meaning.

### [[Freezing and Updating of Accounts]] — `references` [EXTRACTED]
- **What this link tells you:** When determining when a DTFC must freeze balances, note that Chapter 11's freezing triggers operate on the General Account: DTFCs must freeze all General Accounts of juristic entities 90 days after expiry of their license/CR, and must freeze where opening documents contain no validity date. This links the ID-validity and KYC-currency regime directly to the General Account rather than to Term Deposit Accounts. Conclude that freezing consequences of expired identification/authorization crystallize at the General Account, and check the interaction with Term Deposit rules (which allow opening a new Term Deposit even where the related account is frozen if automatic rollover was pre-agreed).
- **Grounding — this node (Page 55 / para 195):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts"
- **Grounding — related node (Page 47 / para 127-128):** "All DTFCs must freeze all General Accounts of juristic entities after 90 days from the expiration date of the respective authorization"

### [[Inactive and Dormant Accounts]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing dormancy obligations, apply Chapter 12's inactivity/dormancy triggers specifically to the General Account, because the chapter counts movement 'by the account holder' on the General Account and expressly provides that a General Account linked to a live Term Account is not treated as having no movement (para 144). This matters because the one-year 'Inactive' and two-year 'Dormant' classifications, and the escalating dual-control activation requirements, are keyed to the General Account rather than the Term Deposit Account. Conclude that the linked live Term Deposit suspends the dormancy clock, and that dormancy controls (isolation, higher-authority activation, annual internal audit) must be scoped to the General Account level.
- **Grounding — this node (Page 55 / para 195):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts"
- **Grounding — related node (Page 49 / para 143-144):** "If a General Account completes an one year period with no movement... must consider such General Account as “Inactive”... If a General Account is linked with a live Term Account then such period will not be counted"

### [[Opening General Accounts for Juristic Persons]] — `references` [EXTRACTED]
- **What this link tells you:** When advising on onboarding a juristic customer, treat the General Account definition as the object that the account-opening rules govern: the juristic-person documentation requirements (Chapters 8-9) determine when and for whom a General Account may lawfully be opened. The General Account is defined narrowly as an internal-books account whose sole purpose is to facilitate Term Deposit operations, and the account-opening chapter expressly prohibits opening it for natural persons and permits it only for juristic persons meeting the KYB documentation. A compliance reader should conclude that eligibility and documentation for a General Account are controlled entirely by these account-opening rules, and that funding/withdrawal mechanics come from the separate operating rules.
- **Grounding — this node (Page 55 / Art 195):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts."
- **Grounding — related node (Page 36 / Chapter 8 / Arts 82-83):** "DTFCs must NOT open General Accounts and Term Deposit Accounts in the name of Natural Persons... DTFCs can only open General Accounts... for juristic Persons"

### [[Term Deposit Account]] — `references` [EXTRACTED]
- **What this link tells you:** When structuring or reviewing a DTFC's deposit products, treat the General Account and Term Deposit Account as a mandatory linked pair, because a Term Deposit Account can only be opened where a General Account of the same customer is already open and active, must be linked to that General Account at initiation, and can only receive credits from and repay principal/profit back to that same General Account. The linkage is one-directional in cardinality (one General Account may link to multiple Term Deposits, but each Term Deposit links to only one General Account) and cannot be de-linked and re-linked. Conclude that funding flow, name/title consistency, and maturity crediting all trace through the General Account, so obligations on one account cannot be assessed without the linkage rules.
- **Grounding — this node (Page 55 / para 200):** "Upon maturity of Term Deposit Account, DTFC must credit the principle and profit amount separately to the General Account from which Term Deposit Account was funded"
- **Grounding — related node (Page 46 / para 120-125):** "A General Deposit Account of the same customer is already open and active... DTFC must linked Term Deposit Account to a General Account upon its initiation"

#graphify/concept #graphify/EXTRACTED #community/Deposit_Account_Rules #graphify/enriched
