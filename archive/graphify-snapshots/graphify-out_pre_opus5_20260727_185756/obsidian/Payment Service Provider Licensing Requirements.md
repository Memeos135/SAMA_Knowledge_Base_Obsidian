---
source_file: "markdown/SAMA_EN_1430_VER1.md"
type: "document"
community: "Payment Provider Licensing & Accounts"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Payment_Provider_Licensing__Accounts
  - graphify/enriched
---

# Payment Service Provider Licensing Requirements

## Connections

### [[Regulatory Rules for Prepaid Payment Services]] — `conceptually_related_to` [INFERRED]
- **Why:** PSP licensing under SAMA_EN_1430 establishes the authorisation gateway for any entity that holds or processes client funds; SAMA_EN_1644 specifies the operational requirements for collection accounts used to deposit and retain payment-company clients' funds, meaning an entity's PSP licence category directly determines what account-opening and fund-retention controls the bank must apply.
- **This node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات"
- **Related node (Page 51 / section 300.1.3.7):** "The collection accounts for depositing and retaining the funds of payment companies' clients shall be opened and managed in accordance with the following requirements: A letter from the Chairperson of the Board of Directors of the company or their authorized representative to th…"
- **Implication:** Banks onboarding a payment company must verify SAMA PSP licence category before opening a collection/safeguarding account, and the account-opening letter must reference the licensed entity name as it appears on the SAMA licence to satisfy both instruments.
- **Caveat:** Node B context is drawn from SAMA_EN_1644 which covers bank account rules broadly; the prepaid-services label applied to node B is an inference — the section quoted addresses payment-company collection accounts, not prepaid card issuance specifically.

#graphify/document #graphify/INFERRED #community/Payment_Provider_Licensing__Accounts #graphify/enriched
