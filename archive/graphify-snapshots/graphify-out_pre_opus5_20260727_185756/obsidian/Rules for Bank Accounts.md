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

# Rules for Bank Accounts

## Connections

### [[Definitions]] — `references` [EXTRACTED]
- **Why:** The Rules for Bank Accounts document is governed by the defined terms in Chapter I; every operative rule (dormant-account classification, freezing, verification, abandonment) derives its legal meaning from the definitions chapter, making that chapter the interpretive foundation for all procedural obligations.
- **This node (Page 16 / Rule 5.2.2):** "Accounts shall be considered dormant after (24) calendar months from the date of the last recorded debit transaction carried out by a customer or his/her authorized agent or the last reliable and documented correspondence."
- **Related node (Page 6 / Chapter I – Definitions):** "Bank Account: An accounting record maintained by a bank licensed to operate in Saudi Arabia… generated under a contract called 'Account Opening Agreement' between the bank and the account holder (the Customer) or its representative."
- **Implication:** Core banking and CDD systems must operationalise the Chapter I definitions (e.g., 'Bank Account', 'Freezing of Account', 'Bank Verification') as system-level data fields so that dormancy and abandonment rules trigger correctly against defined customer-interaction events, enabling auditable rule-execution trails.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** SAMA is the competent authority that issues, updates, and enforces the Rules for Bank Accounts; the Rules explicitly designate SAMA as the sole recipient of disclosure and enforcement requests, the body specifying required forms and timelines, and the source of further instructions that supplement the Rules.
- **This node (Page 22 / Rule 10.1):** "Such requests shall be received only by SAMA except for cases stated in SAMA's instructions. Banks shall carry out requests for disclosure and enforcement according to the form, manner and period specified by SAMA."
- **Related node (Page 1):** "Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** Banks must maintain a dedicated SAMA-interface process for disclosure and enforcement requests (including a secure channel for receiving requests and a documented response workflow with timestamped outputs), and must monitor SAMA's website for rule amendments that immediately alter operative obligations.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
