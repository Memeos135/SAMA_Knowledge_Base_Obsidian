---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "concept"
community: "Payment Provider Licensing & Accounts"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/Payment_Provider_Licensing__Accounts
  - graphify/enriched
---

# Regulatory Rules for Prepaid Payment Services

## Connections

### [[Inoperative Accounts]] — `references` [EXTRACTED]
- **Why:** The inoperative-accounts rule explicitly lists the asset types in scope (Section 5.1), which encompasses all banking relationships including payment-company client collection accounts; the prepaid/payment-company collection account rules (Section 300.1.3.7) must therefore be read subject to the inoperative-accounts regime regarding dormancy classification and balance handling.
- **This node (Page 51 / Section 300.1.3.7):** "The collection accounts for depositing and retaining the funds of payment companies' clients shall be opened and managed in accordance with the following requirements."
- **Related node (Page 15 / Section 5.1):** "This Rule applies to all assets (accounts, banking relationships, transactions, etc.) in cash and in-kind for natural and juristic persons which are deposited in banks operating in Saudi Arabia."
- **Implication:** Banks hosting payment-company client collection accounts must apply the inoperative-accounts dormancy and abandonment framework to those accounts, requiring system logic to monitor inactivity periods and initiate the prescribed classification and notification steps even for these specialised account types.
- **Caveat:** The source context for node_b (prepaid_services) does not contain an explicit cross-reference back to the inoperative-accounts rule; the linkage is inferred from the broad scope statement in Section 5.1 covering all banking relationships.

### [[Payment Service Provider Licensing Requirements]] — `conceptually_related_to` [INFERRED]
- **Why:** PSP licensing under SAMA_EN_1430 establishes the authorisation gateway for any entity that holds or processes client funds; SAMA_EN_1644 specifies the operational requirements for collection accounts used to deposit and retain payment-company clients' funds, meaning an entity's PSP licence category directly determines what account-opening and fund-retention controls the bank must apply.
- **This node (Page 51 / section 300.1.3.7):** "The collection accounts for depositing and retaining the funds of payment companies' clients shall be opened and managed in accordance with the following requirements: A letter from the Chairperson of the Board of Directors of the company or their authorized representative to th…"
- **Related node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات"
- **Implication:** Banks onboarding a payment company must verify SAMA PSP licence category before opening a collection/safeguarding account, and the account-opening letter must reference the licensed entity name as it appears on the SAMA licence to satisfy both instruments.
- **Caveat:** Node B context is drawn from SAMA_EN_1644 which covers bank account rules broadly; the prepaid-services label applied to node B is an inference — the section quoted addresses payment-company collection accounts, not prepaid card issuance specifically.

#graphify/concept #graphify/INFERRED #community/Payment_Provider_Licensing__Accounts #graphify/enriched
