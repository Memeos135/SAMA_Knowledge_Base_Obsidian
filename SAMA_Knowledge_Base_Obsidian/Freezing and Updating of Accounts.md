---
source_file: "markdown/SAMA_EN_11081_VER1.md"
type: "document"
community: "Deposit Account Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Deposit_Account_Rules
  - graphify/enriched
---

# Freezing and Updating of Accounts

## Connections

### [[General Account]] — `references` [EXTRACTED]
- **What this link tells you:** When determining when a DTFC must freeze balances, note that Chapter 11's freezing triggers operate on the General Account: DTFCs must freeze all General Accounts of juristic entities 90 days after expiry of their license/CR, and must freeze where opening documents contain no validity date. This links the ID-validity and KYC-currency regime directly to the General Account rather than to Term Deposit Accounts. Conclude that freezing consequences of expired identification/authorization crystallize at the General Account, and check the interaction with Term Deposit rules (which allow opening a new Term Deposit even where the related account is frozen if automatic rollover was pre-agreed).
- **Grounding — this node (Page 47 / para 127-128):** "All DTFCs must freeze all General Accounts of juristic entities after 90 days from the expiration date of the respective authorization"
- **Grounding — related node (Page 55 / para 195):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts"

### [[Term Deposit Account]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a DTFC may freeze or restrict a customer's accounts, do not treat the General Account in isolation, because the Term Deposit Account is structurally dependent on it: the General Account exists solely to facilitate Term Deposit operations, funds Term Deposits, and receives back principal and profit at maturity. The freezing rules apply to the General Account, and Chapter 12 confirms an inactivity period is suspended while a General Account is linked to a live Term Deposit. You would conclude that freezing/dormancy analysis must trace the linked Term Deposit lifecycle, and note that a new Term Deposit can still be opened where the related account is frozen or dormant only where automatic rollover was pre-agreed.
- **Grounding — this node (Page 47 / para 127):** "All DTFCs must freeze all General Accounts of juristic entities after 90 days from the expiration date of the respective authorization"
- **Grounding — related node (Page 55 / para 195; Page 46 / para 123):** "the sole purpose of the General Account is to facilitate operations of Term Deposit Accounts ... DTFC can open a new Term Deposit Account where related account is frozen or is dormant provided ... automatic rollover"

#graphify/document #graphify/EXTRACTED #community/Deposit_Account_Rules #graphify/enriched
