---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "concept"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# KYC Principle

## Connections

### [[Due Diligence Measures]] — `conceptually_related_to` [INFERRED]
- **Why:** The KYC principle embedded in SAMA_EN_1644 (bank account rules) establishes the foundational customer-identification obligation and mandates ongoing electronic transaction monitoring; SAMA_EN_1704 operationalises those obligations into a structured CDD/EDD framework with risk-tiered measures, third-party reliance conditions, and periodic reverification—making the two nodes functionally interdependent across AML and account-operation regimes.
- **This node (Page 21 / Section 8):** "Banks should have appropriate systems in place to monitor the customer's transactions and activities … Manual transaction monitoring is not sufficient and banks shall invest in developing electronic systems … to continuously monitor customers' transactions."
- **Related node (Page 36 / Para 3.24):** "The financial institution shall periodically verify (at least annually) that the third party has the sufficient capabilities and powers required to fulfill the due diligence requirements in a professional manner."
- **Implication:** A bank's CDD/KYC technology stack must satisfy both the account-operation rules' demand for integrated electronic monitoring and the AML Guide's annual third-party CDD capability verification, meaning vendor or outsourced CDD solutions require documented annual assessments evidenced in the compliance file.
- **Caveat:** INFERRED: the 1644 KYC principle node's source context focuses on dormant/abandoned accounts and authorized-person checks rather than providing a single KYC definition article; the link to 1704 due diligence is strong conceptually but the verbatim anchor from 1644 is drawn from the monitoring section rather than a dedicated KYC definitional clause.

### [[Foreign Investors Accounts (Rule 400)]] — `references` [EXTRACTED]
- **Why:** Rule 400 for foreign investors not covered by the Foreign Investment Law expressly requires ultimate beneficial ownership identification (25% threshold), ownership structure mapping, and licence verification from the country of origin, directly operationalising the KYC/CDD principle for a high-risk, cross-border investor category.
- **This node (Page 21 / Chapter II):** "The Compliance Department shall have the authority and right to timely access the customer identification data, due diligence information, transaction records and other relevant data."
- **Related node (Page 100 / Rule 400.4):** "Real beneficiaries holding ultimate control shall be identified and verified (as a minimum, a natural owner holding 25% as specified in the memorandum of association and its annexes or according to the available data)."
- **Implication:** The onboarding system for foreign investor accounts must capture and store a verified UBO record at the 25% threshold, linked to the foreign licence/registration document, with the compliance department granted system-level read access to this data as an auditable control requirement.

### [[Non-Banking GCC Companies Accounts]] — `references` [EXTRACTED]
- **Why:** The GCC companies account-opening rules operationalise the KYC principle by mandating specific ownership verification (≥50% GCC citizenship), beneficial control identification, board member ID verification, and correspondent bank interview procedures, directly implementing the broader KYC obligation in a cross-border corporate context.
- **This node (Page 21 / Chapter II):** "Banks shall ascertain the nature of the relationship for natural curators, legal agents, custodians and authorized persons when opening accounts and check the validity of the documents submitted."
- **Related node (Page 92 / Rule 300.2.1):** "The above documents shall be completed by the bank's employees directly by interviewing the clients personally (authorized persons) or by a national GCC correspondent bank residing in the country of the company. The correspondent bank shall verify that copies provided for all th…"
- **Implication:** For non-resident GCC company onboarding, the bank must document the correspondent bank's identity verification step as a KYC reliance record, clearly evidencing that document authenticity was confirmed at source, which is the auditor-expected substitute for in-person branch verification.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
