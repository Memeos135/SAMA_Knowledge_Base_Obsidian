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

# Pilgrim Affairs Office Bank Account Rules

## Connections

### [[Dual Control  Joint Signature|Dual Control / Joint Signature]] — `references` [EXTRACTED]
- **Why:** The Pilgrim Affairs Office Bank Account Rules expressly mandate dual control as an operational condition of the account, linking the general dual-control principle—applied across multiple high-risk or sensitive account types in the Rules—to this specific non-resident, seasonal-use account category.
- **This node (Page 56 / Pilgrim affairs office rules):** "The bank shall ensure that such accounts are subject to dual control."
- **Related node (Page 76 / Rule 300.1.5.14 (dual control general principle)):** "Withdrawal from these accounts shall be as per dual control, and in case of withdrawal by checks, check shall be payable to the first beneficiary."
- **Implication:** Banks must configure system-level dual-authorisation controls on pilgrim affairs office accounts so that no single user can approve withdrawals or transfers; this must be evidenced in access-rights audit logs reviewable by SAMA examiners.

### [[Hajj Organizer Bank Account Rules]] — `semantically_similar_to` [INFERRED]
- **Why:** Both rule sets govern foreign Hajj-related entities (pilgrim affairs offices and Hajj organizers/tourism companies) opening SAR-only accounts in Saudi banks, share near-identical structural requirements—Ministry of Hajj and Umrah approval letter, SAMA pre-approval, dual control, single-bank restriction, contracted-party payment lists—and operate under the same Rule 300.1.5.1 chapter, making them functionally parallel sub-regimes.
- **This node (Page 56 / Pilgrim affairs office rules):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account. The bank shall ensure that such accounts are subject to dual control."
- **Related node (Page 59 / Hajj organizer rules):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account. The bank shall ensure that such accounts are subject to dual control."
- **Implication:** A single KYB/account-opening workflow template can serve both Hajj organizer and pilgrim affairs office onboarding, but must branch on entity-type classification and maintain separate contracted-party lists attested by the Ministry of Hajj and Umrah as distinct evidence files.

### [[Ministry of Hajj and Umrah]] — `references` [EXTRACTED]
- **Why:** The Ministry of Hajj and Umrah functions as a mandatory intermediary in the pilgrim affairs office account regime: its approval letter is a condition precedent to account opening, it attests contracted-party lists that control permissible deposits and withdrawals, and it must receive the IBAN upon account establishment, making it a co-regulator of account operations alongside SAMA.
- **This node (Page 56 / Pilgrim affairs office rules):** "The bank shall conclude an account opening agreement with the authorized signatories specified in the letter of the Ministry of Hajj and Umrah, addressed to the bank … The bank shall provide the pilgrim affairs office and the Ministry of Hajj and Umrah with the IBAN number."
- **Related node (Page 58 / Reactivation rules):** "the bank shall obtain a letter from the Ministry of Hajj and Umrah, including the same information specified in the form filled out by the ministry when it first approved the account opening … the list shall be attested by the Ministry of Hajj and Umrah."
- **Implication:** The onboarding workflow for pilgrim affairs offices must include document-collection checkpoints for the Ministry of Hajj and Umrah approval letter and attested contracted-party list before account activation, with annual reactivation re-verification of both documents and IBAN re-notification to the Ministry.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** The Pilgrim Affairs Office Bank Account Rules impose a mandatory pre-opening approval process in which the bank's compliance department must submit an application to SAMA with all documents, and SAMA's approval is a condition precedent to account opening, establishing SAMA as a direct regulatory actor within the rule.
- **This node (Page 56 / Rule 300.1.5.1 (pilgrim affairs)):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Related node (Page 1):** "Rules for Bank Accounts Updated March 2022 … Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** The bank's compliance system must include a tracked SAMA-approval workflow for pilgrim affairs office accounts, with same-day or next-business-day submission SLAs and documented evidence of SAMA's affirmative response before account activation.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
