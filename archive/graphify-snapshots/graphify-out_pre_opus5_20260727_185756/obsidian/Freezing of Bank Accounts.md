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

# Freezing of Bank Accounts

## Connections

### [[Electronic Record Requirements]] — `references` [EXTRACTED]
- **Why:** The electronic record system mandated in Chapter II is the foundational data store that must capture and retain customer identity, asset details, and account status fields required to execute freezing, dormancy classification, and abandonment procedures; without a complete electronic record, the time-based triggers and audit trails for freezing cannot be operationalised.
- **This node (Page 18 / Section 5.3):** "Personal and financial data shall be kept by the bank in electronic records according to the technical specifications set by SAMA for easy future reference. A copy of such data shall be submitted to SAMA."
- **Related node (Page 9 / Chapter II / Section 1):** "all banks shall establish an electronic registration system … This system serves as an electronic record, and should include the requirements provided in the paragraphs below … as a basis for opening, operating, and following up bank accounts."
- **Implication:** Banks must configure their core-banking/CRM system to persist the inoperative-account data fields (full name, ID, asset nature, national address, account number) in SAMA-specified technical format so that freezing-stage workflows can be triggered automatically and evidence is available for SAMA submission.

### [[Inoperative Accounts]] — `references` [EXTRACTED]
- **Why:** The freezing-of-accounts regime directly references and builds upon the inoperative-accounts classification framework: an account progresses through defined inactivity periods (dormant → unclaimed → abandoned) before freezing obligations and balance-transfer procedures apply, making the two nodes part of a single sequential lifecycle.
- **This node (Page 22 / Section 10.1):** "banks shall search for all relationships between the bank and the customer, including all active; closed and suspended accounts, inoperative accounts, deposits … and any other relationships or products offered by the bank."
- **Related node (Page 15 / Section 5.1):** "This Rule applies to all assets (accounts, banking relationships, transactions, etc.) in cash and in-kind for natural and juristic persons which are deposited in banks operating in Saudi Arabia."
- **Implication:** Banks must implement an automated account-lifecycle state machine that tracks inactivity periods, triggers classification changes (dormant/unclaimed/abandoned), and links each state transition to the corresponding freezing or enforcement action — all searchable by customer name or ID for SAMA disclosure requests.

#graphify/document #graphify/EXTRACTED #community/Payment_Provider_Licensing__Accounts #graphify/enriched
