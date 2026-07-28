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

# Ministry of Human Resources and Social Development

## Connections

### [[Cooperative Associations and Funds]] — `references` [EXTRACTED]
- **Why:** The bank account opening rules for cooperative associations under establishment expressly require a letter from the Ministry of Human Resources and Social Development (MHRSD) authorising account opening, and all subsequent actions (period extension, fund return) are conditioned on MHRSD approval, making MHRSD a mandatory gate-keeping authority in this onboarding workflow.
- **This node (Page 61 / Rule 300.1.5.2):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities, including their branches, as well as Da'wah offices and the like."
- **Related node (Page 70 / Rule 300.1.5.6):** "The bank shall receive a letter from the competent authority at the Ministry of Human Resources and Social Development (MHRSD), stating that the cooperative association is under establishment and that the MHRSD agrees on opening an account for the association to raise its capita…"
- **Implication:** The bank's KYB onboarding workflow for cooperative associations must include a hard gate requiring a valid, current MHRSD authorisation letter before account activation; the trust account must be flagged for automatic closure or extension request at six months, with the MHRSD approval document retained as the audit trigger.

### [[Private Associations Accounts]] — `references` [EXTRACTED]
- **Why:** MHRSD is the statutory licensing authority for private associations; the rules condition the bank's ability to open accounts for these entities on production of a valid MHRSD licence, making MHRSD authorisation a prerequisite document in the KYB onboarding chain.
- **This node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities, including their branches, as well as Da'wah offices and the like."
- **Related node (Page 46):** "A copy of the license issued by the Ministry of Human Resources and Social Development… and the approval for the account's authorized signatories (for private societies/foundations or cooperative associations)."
- **Implication:** The bank's KYB document checklist for private association onboarding must include a current MHRSD licence as a mandatory, non-waivable document, with licence validity monitored to trigger account review or suspension upon expiry.

### [[Private Foundations Accounts]] — `references` [EXTRACTED]
- **Why:** MHRSD approval is explicitly required for private foundations when the trustee board wishes to authorise signatories beyond the board chairman/vice-chairman and financial officer, making MHRSD a mandatory third-party approval authority in the account signatory control framework for foundations.
- **This node (Page 46):** "A copy of the license issued by the Ministry of Human Resources and Social Development… and the approval for the account's authorized signatories (for private societies/foundations or cooperative associations)."
- **Related node (Page 65):** "Should the trustee board wish to authorize person(s) other than those mentioned above, the approval of the MHRSD shall be obtained."
- **Implication:** Banks must implement a signatory-change workflow for private foundation accounts that routes non-standard authorisation requests to an MHRSD approval checkpoint before updating account operating mandates in the core banking system, with the MHRSD approval letter retained as evidence.

#graphify/concept #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
