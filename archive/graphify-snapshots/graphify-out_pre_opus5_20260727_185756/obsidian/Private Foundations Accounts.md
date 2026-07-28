---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Bank Account Operation Rules"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# Private Foundations Accounts

## Connections

### [[Ministry of Human Resources and Social Development]] — `references` [EXTRACTED]
- **Why:** MHRSD approval is explicitly required for private foundations when the trustee board wishes to authorise signatories beyond the board chairman/vice-chairman and financial officer, making MHRSD a mandatory third-party approval authority in the account signatory control framework for foundations.
- **This node (Page 65):** "Should the trustee board wish to authorize person(s) other than those mentioned above, the approval of the MHRSD shall be obtained."
- **Related node (Page 46):** "A copy of the license issued by the Ministry of Human Resources and Social Development… and the approval for the account's authorized signatories (for private societies/foundations or cooperative associations)."
- **Implication:** Banks must implement a signatory-change workflow for private foundation accounts that routes non-standard authorisation requests to an MHRSD approval checkpoint before updating account operating mandates in the core banking system, with the MHRSD approval letter retained as evidence.

### [[Private Associations Accounts]] — `semantically_similar_to` [INFERRED]
- **Why:** Both private associations and private foundations are non-profit legal entities licensed by MHRSD, subject to analogous SAMA bank-account controls including dual-control withdrawals, SAR-only accounts, compliance-department approval, prohibition on cash dealings, and joint-signature requirements, indicating parallel regulatory treatment within the same rulebook section.
- **This node (Page 65):** "Private foundations are not allowed to carry out any cash dealings. Withdrawal from the foundation's main account shall be made under dual control."
- **Related node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities… Bank accounts for these associations and offices shall be opened in Saudi riyal only."
- **Implication:** A single KYB customer-type framework can cover both private associations and private foundations under a shared NPO/charity risk tier, but the system must still distinguish entity sub-type to enforce the foundation-specific prohibition on cash dealings and the requirement for MHRSD approval of non-standard signatories.
- **Caveat:** The node_b context provided (pages 16, 17, 22) does not contain private-foundation-specific text; the private foundations excerpt is sourced from page 65 visible in node_a's broader document context, so the semantic similarity is confirmed by the source document but the node_b context field is not the direct evidence source.

#graphify/document #graphify/INFERRED #community/Bank_Account_Operation_Rules #graphify/enriched
