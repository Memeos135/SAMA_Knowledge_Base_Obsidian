---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Payment Provider Licensing & Accounts"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Payment_Provider_Licensing__Accounts
  - graphify/enriched
---

# Inoperative Accounts

## Connections

### [[Freezing of Bank Accounts]] — `references` [EXTRACTED]
- **Why:** The freezing-of-accounts regime directly references and builds upon the inoperative-accounts classification framework: an account progresses through defined inactivity periods (dormant → unclaimed → abandoned) before freezing obligations and balance-transfer procedures apply, making the two nodes part of a single sequential lifecycle.
- **This node (Page 15 / Section 5.1):** "This Rule applies to all assets (accounts, banking relationships, transactions, etc.) in cash and in-kind for natural and juristic persons which are deposited in banks operating in Saudi Arabia."
- **Related node (Page 22 / Section 10.1):** "banks shall search for all relationships between the bank and the customer, including all active; closed and suspended accounts, inoperative accounts, deposits … and any other relationships or products offered by the bank."
- **Implication:** Banks must implement an automated account-lifecycle state machine that tracks inactivity periods, triggers classification changes (dormant/unclaimed/abandoned), and links each state transition to the corresponding freezing or enforcement action — all searchable by customer name or ID for SAMA disclosure requests.

### [[Regulatory Rules for Prepaid Payment Services]] — `references` [EXTRACTED]
- **Why:** The inoperative-accounts rule explicitly lists the asset types in scope (Section 5.1), which encompasses all banking relationships including payment-company client collection accounts; the prepaid/payment-company collection account rules (Section 300.1.3.7) must therefore be read subject to the inoperative-accounts regime regarding dormancy classification and balance handling.
- **This node (Page 15 / Section 5.1):** "This Rule applies to all assets (accounts, banking relationships, transactions, etc.) in cash and in-kind for natural and juristic persons which are deposited in banks operating in Saudi Arabia."
- **Related node (Page 51 / Section 300.1.3.7):** "The collection accounts for depositing and retaining the funds of payment companies' clients shall be opened and managed in accordance with the following requirements."
- **Implication:** Banks hosting payment-company client collection accounts must apply the inoperative-accounts dormancy and abandonment framework to those accounts, requiring system logic to monitor inactivity periods and initiate the prescribed classification and notification steps even for these specialised account types.
- **Caveat:** The source context for node_b (prepaid_services) does not contain an explicit cross-reference back to the inoperative-accounts rule; the linkage is inferred from the broad scope statement in Section 5.1 covering all banking relationships.

#graphify/document #graphify/EXTRACTED #community/Payment_Provider_Licensing__Accounts #graphify/enriched
