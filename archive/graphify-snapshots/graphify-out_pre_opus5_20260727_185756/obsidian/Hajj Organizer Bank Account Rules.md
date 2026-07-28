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

# Hajj Organizer Bank Account Rules

## Connections

### [[Dual Control  Joint Signature|Dual Control / Joint Signature]] — `references` [EXTRACTED]
- **Why:** The Hajj organizer bank account rules explicitly mandate dual control as an operational requirement for these accounts, directly instantiating the general dual-control concept within a specific high-risk customer segment subject to SAMA pre-approval.
- **This node (Page 59):** "The bank shall ensure that such accounts are subject to dual control."
- **Related node (Page 76):** "Withdrawal from these accounts shall be as per dual control, and in case of withdrawal by checks, check shall be payable to the first beneficiary."
- **Implication:** Banks onboarding Hajj organizers must configure account operating rules in their core banking system to enforce a two-signatory release for all debits, evidenced by system-level controls and auditable transaction logs reviewable by SAMA examiners.

### [[Ministry of Hajj and Umrah]] — `references` [EXTRACTED]
- **Why:** The Ministry of Hajj and Umrah is the mandatory licensing and approving authority throughout the Hajj organizer account lifecycle: account opening approval, authorised signatory attestation, permitted payee lists, fund-transfer portal access, and account reactivation each require a formal Ministry letter or attestation.
- **This node (Page 59):** "The bank shall provide the organizer and the Ministry of Hajj and Umrah with the IBAN number of the organizer's account on a form designed for this purpose."
- **Related node (Page 58):** "The Hajj organizer shall present to the bank a letter from the Ministry of Hajj and Umrah approving opening a bank account for the pilgrim affairs office and including the office's information."
- **Implication:** The KYB/account-opening workflow for Hajj organizers must include a document-intake checkpoint that validates the Ministry of Hajj and Umrah approval letter before any account is activated, with the original letter retained in the customer file as primary evidence.

### [[Pilgrim Affairs Office Bank Account Rules]] — `semantically_similar_to` [INFERRED]
- **Why:** Both rule sets govern foreign Hajj-related entities (pilgrim affairs offices and Hajj organizers/tourism companies) opening SAR-only accounts in Saudi banks, share near-identical structural requirements—Ministry of Hajj and Umrah approval letter, SAMA pre-approval, dual control, single-bank restriction, contracted-party payment lists—and operate under the same Rule 300.1.5.1 chapter, making them functionally parallel sub-regimes.
- **This node (Page 59 / Hajj organizer rules):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account. The bank shall ensure that such accounts are subject to dual control."
- **Related node (Page 56 / Pilgrim affairs office rules):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account. The bank shall ensure that such accounts are subject to dual control."
- **Implication:** A single KYB/account-opening workflow template can serve both Hajj organizer and pilgrim affairs office onboarding, but must branch on entity-type classification and maintain separate contracted-party lists attested by the Ministry of Hajj and Umrah as distinct evidence files.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** The Hajj organizer account rules impose an explicit pre-opening SAMA approval requirement administered through the bank's compliance department, making SAMA a mandatory licensing gate for this high-risk seasonal account type with cross-border cash flows.
- **This node (Page 59):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account... the compliance department, in turn, shall submit such documents to SAMA on the same day or at the beginning of the foll…"
- **Related node (Page 1):** "Rules for Bank Accounts Updated March 2022... Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** Banks must build a same-day SAMA submission SLA into their Hajj organizer onboarding workflow, with compliance department sign-off as a mandatory upstream control and a two-working-day account opening cap enforced at the system level.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
