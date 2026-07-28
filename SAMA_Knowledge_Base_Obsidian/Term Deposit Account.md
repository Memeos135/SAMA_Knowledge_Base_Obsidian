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

# Term Deposit Account

## Connections

### [[Accounts Operating Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping disclosure and blocking obligations, note that the account-operating rules (Ch. 8/14) expressly extend to Term Deposit Accounts: a DTFC's search response to SAMA for disclosing or blocking must cover 'all active, closed, suspense, inactive, dormant General Accounts and Term Deposit accounts,' and Chapter 8 confirms Term Deposit Accounts may only be opened for juristic persons (not natural persons). This means Term Deposit Accounts are not carved out of the general account-administration, disclosure, and blocking regime. Conclude that any completeness check on disclosure/blocking to SAMA must include Term Deposit Accounts and their transaction records, and that eligibility rules (juristic-only) apply equally to them.
- **Grounding — this node (Page 46 / para 119):** "DTFCs can open a Term Deposit Account for its customer provided following requirements are met"
- **Grounding — related node (Page 53 / para 179):** "disclosing of all relations... including... all active, closed, suspense, inactive, dormant General Accounts and Term Deposit accounts etc."

### [[Freezing and Updating of Accounts]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a DTFC may freeze or restrict a customer's accounts, do not treat the General Account in isolation, because the Term Deposit Account is structurally dependent on it: the General Account exists solely to facilitate Term Deposit operations, funds Term Deposits, and receives back principal and profit at maturity. The freezing rules apply to the General Account, and Chapter 12 confirms an inactivity period is suspended while a General Account is linked to a live Term Deposit. You would conclude that freezing/dormancy analysis must trace the linked Term Deposit lifecycle, and note that a new Term Deposit can still be opened where the related account is frozen or dormant only where automatic rollover was pre-agreed.
- **Grounding — this node (Page 55 / para 195; Page 46 / para 123):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts ... DTFC can open a new Term Deposit Account where related account is frozen or is dormant provided ... automatic rollover"
- **Grounding — related node (Page 47 / para 127):** "All DTFCs must freeze all General Accounts of juristic entities after 90 days from the expiration date of the respective authorization"

### [[General Account]] — `references` [EXTRACTED]
- **What this link tells you:** When structuring or reviewing a DTFC's deposit products, treat the General Account and Term Deposit Account as a mandatory linked pair, because a Term Deposit Account can only be opened where a General Account of the same customer is already open and active, must be linked to that General Account at initiation, and can only receive credits from and repay principal/profit back to that same General Account. The linkage is one-directional in cardinality (one General Account may link to multiple Term Deposits, but each Term Deposit links to only one General Account) and cannot be de-linked and re-linked. Conclude that funding flow, name/title consistency, and maturity crediting all trace through the General Account, so obligations on one account cannot be assessed without the linkage rules.
- **Grounding — this node (Page 46 / para 120-125):** "A General Deposit Account of the same customer is already open and active... DTFC must linked Term Deposit Account to a General Account upon its initiation"
- **Grounding — related node (Page 55 / para 200):** "Upon maturity of Term Deposit Account, DTFC must credit the principle and profit amount separately to the General Account from which Term Deposit Account was funded"

#graphify/concept #graphify/EXTRACTED #community/Deposit_Account_Rules #graphify/enriched
