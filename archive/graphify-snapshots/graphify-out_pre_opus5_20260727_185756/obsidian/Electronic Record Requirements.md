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

# Electronic Record Requirements

## Connections

### [[Freezing of Bank Accounts]] — `references` [EXTRACTED]
- **Why:** The electronic record system mandated in Chapter II is the foundational data store that must capture and retain customer identity, asset details, and account status fields required to execute freezing, dormancy classification, and abandonment procedures; without a complete electronic record, the time-based triggers and audit trails for freezing cannot be operationalised.
- **This node (Page 9 / Chapter II / Section 1):** "all banks shall establish an electronic registration system … This system serves as an electronic record, and should include the requirements provided in the paragraphs below … as a basis for opening, operating, and following up bank accounts."
- **Related node (Page 18 / Section 5.3):** "Personal and financial data shall be kept by the bank in electronic records according to the technical specifications set by SAMA for easy future reference. A copy of such data shall be submitted to SAMA."
- **Implication:** Banks must configure their core-banking/CRM system to persist the inoperative-account data fields (full name, ID, asset nature, national address, account number) in SAMA-specified technical format so that freezing-stage workflows can be triggered automatically and evidence is available for SAMA submission.

#graphify/document #graphify/EXTRACTED #community/Payment_Provider_Licensing__Accounts #graphify/enriched
