---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "concept"
community: "Bank Account Operation Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# Ministry of Hajj and Umrah

## Connections

### [[Hajj Organizer Bank Account Rules]] — `references` [EXTRACTED]
- **Why:** The Ministry of Hajj and Umrah is the mandatory licensing and approving authority throughout the Hajj organizer account lifecycle: account opening approval, authorised signatory attestation, permitted payee lists, fund-transfer portal access, and account reactivation each require a formal Ministry letter or attestation.
- **This node (Page 58):** "The Hajj organizer shall present to the bank a letter from the Ministry of Hajj and Umrah approving opening a bank account for the pilgrim affairs office and including the office's information."
- **Related node (Page 59):** "The bank shall provide the organizer and the Ministry of Hajj and Umrah with the IBAN number of the organizer's account on a form designed for this purpose."
- **Implication:** The KYB/account-opening workflow for Hajj organizers must include a document-intake checkpoint that validates the Ministry of Hajj and Umrah approval letter before any account is activated, with the original letter retained in the customer file as primary evidence.

### [[Pilgrim Affairs Office Bank Account Rules]] — `references` [EXTRACTED]
- **Why:** The Ministry of Hajj and Umrah functions as a mandatory intermediary in the pilgrim affairs office account regime: its approval letter is a condition precedent to account opening, it attests contracted-party lists that control permissible deposits and withdrawals, and it must receive the IBAN upon account establishment, making it a co-regulator of account operations alongside SAMA.
- **This node (Page 58 / Reactivation rules):** "the bank shall obtain a letter from the Ministry of Hajj and Umrah, including the same information specified in the form filled out by the ministry when it first approved the account opening … the list shall be attested by the Ministry of Hajj and Umrah."
- **Related node (Page 56 / Pilgrim affairs office rules):** "The bank shall conclude an account opening agreement with the authorized signatories specified in the letter of the Ministry of Hajj and Umrah, addressed to the bank … The bank shall provide the pilgrim affairs office and the Ministry of Hajj and Umrah with the IBAN number."
- **Implication:** The onboarding workflow for pilgrim affairs offices must include document-collection checkpoints for the Ministry of Hajj and Umrah approval letter and attested contracted-party list before account activation, with annual reactivation re-verification of both documents and IBAN re-notification to the Ministry.

#graphify/concept #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
