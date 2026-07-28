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

# Private Associations Accounts

## Connections

### [[Bank Compliance Department]] — `references` [EXTRACTED]
- **Why:** The bank's compliance department acts as a mandatory gateway for private association (and Hajj/pilgrim-office) account opening: it must review documents, approve the account, and submit the SAMA application, creating a direct procedural dependency between the compliance function and this customer-type's onboarding rules.
- **This node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities… Bank accounts for these associations and offices shall be opened in Saudi riyal only."
- **Related node (Page 59):** "The bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Implication:** Compliance department workflows must include a formal sign-off step and same-day document escalation trigger for private association account applications, with the compliance manager's approval documented and the SAMA submission timestamped to evidence adherence to the same-day or next-working-day deadline.
- **Caveat:** The node_b context pages (16, 17, 22) relate to dormant/abandoned accounts generally; the direct private-association compliance-department link is drawn from Page 61 (node_a context) and Page 65, not from the dormant-account pages shown in node_b's context field.

### [[Ministry of Human Resources and Social Development]] — `references` [EXTRACTED]
- **Why:** MHRSD is the statutory licensing authority for private associations; the rules condition the bank's ability to open accounts for these entities on production of a valid MHRSD licence, making MHRSD authorisation a prerequisite document in the KYB onboarding chain.
- **This node (Page 46):** "A copy of the license issued by the Ministry of Human Resources and Social Development… and the approval for the account's authorized signatories (for private societies/foundations or cooperative associations)."
- **Related node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities, including their branches, as well as Da'wah offices and the like."
- **Implication:** The bank's KYB document checklist for private association onboarding must include a current MHRSD licence as a mandatory, non-waivable document, with licence validity monitored to trigger account review or suspension upon expiry.

### [[Private Foundations Accounts]] — `semantically_similar_to` [INFERRED]
- **Why:** Both private associations and private foundations are non-profit legal entities licensed by MHRSD, subject to analogous SAMA bank-account controls including dual-control withdrawals, SAR-only accounts, compliance-department approval, prohibition on cash dealings, and joint-signature requirements, indicating parallel regulatory treatment within the same rulebook section.
- **This node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities… Bank accounts for these associations and offices shall be opened in Saudi riyal only."
- **Related node (Page 65):** "Private foundations are not allowed to carry out any cash dealings. Withdrawal from the foundation's main account shall be made under dual control."
- **Implication:** A single KYB customer-type framework can cover both private associations and private foundations under a shared NPO/charity risk tier, but the system must still distinguish entity sub-type to enforce the foundation-specific prohibition on cash dealings and the requirement for MHRSD approval of non-standard signatories.
- **Caveat:** The node_b context provided (pages 16, 17, 22) does not contain private-foundation-specific text; the private foundations excerpt is sourced from page 65 visible in node_a's broader document context, so the semantic similarity is confirmed by the source document but the node_b context field is not the direct evidence source.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
