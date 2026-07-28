---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Bank Account Operation Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# General Rules for Operation of Bank Accounts

## Connections

### [[Account Closure Rules]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Account closure rules and general account operation rules form a single regulatory lifecycle framework within Chapter IV of the Bank Accounts Rules: the dormancy thresholds, double-supervision requirements, and balance-transfer procedures in the operation rules directly determine when and how closure or transfer to suspense/abandoned status is triggered.
- **This node (Page 16 / Rule 5.2.2):** "Accounts shall be considered dormant after (24) calendar months from the date of the last recorded debit transaction carried out by a customer or his/her authorized agent or the last reliable and documented correspondence."
- **Related node (Page 17 / Rule 5.2.4 (abandoned accounts)):** "The bank may close customer accounts whose balances are equal to (1,000) riyals and less, provided that the customer is notified a month prior to the date of closing, and notifies him when closing, document the notices and save them in his file."
- **Implication:** Banks must implement an automated account-lifecycle monitoring rule that triggers at 24 months of inactivity, escalates through double-supervision workflows, generates customer notification at the 30-day pre-closure point, and retains documentary evidence of all notices and balance-transfer actions for examiner inspection.

### [[Cash and Deposit Controls (ATMCAM)|Cash and Deposit Controls (ATM/CAM)]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Both nodes govern permissible banking operations on accounts, but from complementary angles: the account operation rules define when accounts become dormant/abandoned and who may transact on them, while the cash deposit controls prescribe identity-capture and authorization requirements for the act of depositing funds—including into accounts held by third parties. A cash deposit into a dormant account (which the rules explicitly permit) must simultaneously satisfy the depositor-identification regime, creating a direct operational intersection.
- **This node (Page 107 / Chapter II Rule 3.1.1–3.1.2 cross-reference):** "When a natural person wants to deposit funds … in his/her bank account, another natural person's account or juristic person's account, the bank in this case shall obtain the personal information of the depositor."
- **Related node (Page 16 / Section 5.2.2):** "Dormant accounts shall be allowed to accept all deposits, domestic and international transfers and dividends made by another person other than the account holder. The account status shall not be changed from dormant to active."
- **Implication:** Banks must configure deposit-capture workflows to collect full depositor identification (name, address, ID number, signature, telephone) even when the destination account is flagged dormant, and must ensure the dormant flag is not automatically cleared by such deposit events.

### [[Dual Control  Joint Signature|Dual Control / Joint Signature]] — `references` [EXTRACTED]
- **Why:** The General Rules for Operation of Bank Accounts explicitly mandate double supervision for dormant-account activation and file management, which is the operational expression of the dual-control principle applied across sensitive account categories, establishing dual control as a cross-cutting operational standard rather than a category-specific rule.
- **This node (Page 17 / Rule 5.2 (unclaimed/abandoned accounts)):** "Banks shall establish policies and procedures to ensure double supervision over the files of such accounts, with a supervision level higher than that applied to the other files."
- **Related node (Page 65 / Rule (private foundations)):** "Withdrawal from the foundation's main account shall be made under dual control. If disbursement is made by a check, the check shall be payable to the first beneficiary."
- **Implication:** Banks must configure transaction-authorisation controls so that any debit or activation on a dormant, abandoned, or high-sensitivity account (courts, foundations, Hajj offices) requires two independent authorisations at a seniority level at or above branch/operations manager, with each approval event logged and attributable.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
