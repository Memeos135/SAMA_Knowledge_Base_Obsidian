---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Foreign Investors Accounts (Rule 400)

## Connections

### [[Anti-Money Laundering Law]] — `references` [EXTRACTED]
- **Why:** Rule 400 of the Bank Accounts Rules explicitly conditions account opening for foreign investors on compliance with AML obligations, including UBO identification at the 25% threshold and rejection of applicants from jurisdictions non-compliant with FATF Recommendations, directly operationalising the Anti-Money Laundering Law's CDD requirements in the account-opening context.
- **This node (Page 100 / Rule 400.4):** "Real beneficiaries holding ultimate control shall be identified and verified (as a minimum, a natural owner holding 25% as specified in the memorandum of association and its annexes or according to the available data)."
- **Related node (Page 12 / Chapter V):** "Anyone who commits any of the following acts shall be considered to have committed a money laundering offence: 1. Transfer, transportation, or performing of any transaction with funds while knowing that they are proceeds of crime in order to conceal or disguise the illegitimate…"
- **Implication:** Banks' KYB/CDD onboarding workflows for foreign investors must enforce a hard UBO identification gate at 25% ownership and must include a country-of-origin FATF-compliance check before account activation, with evidence retained for examiner review.

### [[FATF]] — `references` [EXTRACTED]
- **Why:** Rule 400 of the Bank Accounts Rules explicitly bars account opening for foreign investors whose countries do not adequately apply FATF Recommendations or are subject to UN Security Council decisions, embedding FATF membership/compliance status as a mandatory eligibility screen in the account-opening regime.
- **This node (Page 101 / Rule 400 (concluding paragraph)):** "Applications submitted by foreign investors whose countries never (or insufficiently) apply the FATF Recommendations, or some decisions have been issued against them by the Security Council, shall not be accepted."
- **Related node (Page 6 / Chapter IV Definitions):** "Financial Action Task Force (FATF): An inter-government organization … whose tasks include setting standards and promoting effective implementation of legal, regulatory and operational measures to combat money laundering, terrorist financing, and proliferation financing."
- **Implication:** The onboarding system for foreign investor accounts must incorporate an automated or manually enforced FATF jurisdiction-status check (referencing current FATF black/grey lists and UN SC resolutions) as a blocking control prior to account approval.

### [[KYC Principle]] — `references` [EXTRACTED]
- **Why:** Rule 400 for foreign investors not covered by the Foreign Investment Law expressly requires ultimate beneficial ownership identification (25% threshold), ownership structure mapping, and licence verification from the country of origin, directly operationalising the KYC/CDD principle for a high-risk, cross-border investor category.
- **This node (Page 100 / Rule 400.4):** "Real beneficiaries holding ultimate control shall be identified and verified (as a minimum, a natural owner holding 25% as specified in the memorandum of association and its annexes or according to the available data)."
- **Related node (Page 21 / Chapter II):** "The Compliance Department shall have the authority and right to timely access the customer identification data, due diligence information, transaction records and other relevant data."
- **Implication:** The onboarding system for foreign investor accounts must capture and store a verified UBO record at the 25% threshold, linked to the foreign licence/registration document, with the compliance department granted system-level read access to this data as an auditable control requirement.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
