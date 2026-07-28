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

# Account Closure Rules

## Connections

### [[General Rules for Operation of Bank Accounts]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Account closure rules and general account operation rules form a single regulatory lifecycle framework within Chapter IV of the Bank Accounts Rules: the dormancy thresholds, double-supervision requirements, and balance-transfer procedures in the operation rules directly determine when and how closure or transfer to suspense/abandoned status is triggered.
- **This node (Page 17 / Rule 5.2.4 (abandoned accounts)):** "The bank may close customer accounts whose balances are equal to (1,000) riyals and less, provided that the customer is notified a month prior to the date of closing, and notifies him when closing, document the notices and save them in his file."
- **Related node (Page 16 / Rule 5.2.2):** "Accounts shall be considered dormant after (24) calendar months from the date of the last recorded debit transaction carried out by a customer or his/her authorized agent or the last reliable and documented correspondence."
- **Implication:** Banks must implement an automated account-lifecycle monitoring rule that triggers at 24 months of inactivity, escalates through double-supervision workflows, generates customer notification at the 30-day pre-closure point, and retains documentary evidence of all notices and balance-transfer actions for examiner inspection.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
