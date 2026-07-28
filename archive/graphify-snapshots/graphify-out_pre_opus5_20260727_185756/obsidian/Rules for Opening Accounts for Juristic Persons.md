---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Payment Company Accounts & Capital"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Payment_Company_Accounts__Capital
  - graphify/enriched
---

# Rules for Opening Accounts for Juristic Persons

## Connections

### [[Collection Accounts for Debt-Based Crowdfunding]] — `references` [EXTRACTED]
- **Why:** Debt-based crowdfunding collection accounts (Rule 300.1.3.8) are a specialised sub-category of juristic-person accounts under Rule 300, inheriting the general entity-CDD requirements while adding ring-fencing, naming conventions, and SAMA prior-approval controls specific to the crowdfunding account structure.
- **This node (Page 2 / Table of Contents / Rule 300):** "Rules for Opening Bank Accounts for Juristic Persons … 300.1.3 Resident companies"
- **Related node (Page 52 / Rule 300.1.3.8):** "The collection accounts for collecting funds from participants in order to extend credit to beneficiaries shall be opened and managed in accordance with the following requirements: 1. A letter from the Chairperson of the Board of Directors … stating the purpose of opening the ac…"
- **Implication:** Banks must configure a dedicated account-type classification for crowdfunding collection accounts, enforce the prescribed naming convention in core banking, block cash transactions, and gate any inter-account transfers on documented SAMA non-objection before execution.

### [[Collection Accounts for Payment Companies' Clients]] — `references` [EXTRACTED]
- **Why:** Payment-company client-fund collection accounts (Rule 300.1.3.7) are a named sub-type within the juristic-persons chapter (Rule 300), inheriting general entity-CDD requirements while imposing additional ring-fencing obligations that reflect the licensed-payment-company status of the account holder.
- **This node (Page 2 / Table of Contents / Rule 300.1.3):** "300.1.3 Resident companies … 300.1.3.7 [Collection accounts for depositing and retaining the funds of payment companies' clients — as listed in Table of Contents]"
- **Related node (Page 51 / Rule 300.1.3.7):** "The collection accounts for depositing and retaining the funds of payment companies' clients shall be opened and managed in accordance with the following requirements: 1. A letter from the Chairperson of the Board of Directors … stating the purpose of opening the account under t…"
- **Implication:** Banks onboarding payment companies must open a separately classified collection account with a prescribed name, verify the company's payment licence as part of KYB, and enforce ring-fencing controls (no commingling with the company's own operating accounts) as a licensing-condition evidence requirement.
- **Caveat:** The Table of Contents excerpt for node A does not enumerate Rule 300.1.3.7 by name in the provided context pages; locator is inferred from the sequential structure of Rule 300.1.3 sub-sections visible across pages 2 and 51.

### [[Escrow Account for Real Estate Development]] — `references` [EXTRACTED]
- **Why:** The escrow account for real estate development (Rule 300.1.3.6) is a juristic-person account sub-type under Rule 300, requiring the full entity-CDD of the real estate developer plus additional project-level controls (Ministry of Housing licence, disbursement agreements), making it explicitly nested within the juristic-persons framework.
- **This node (Page 2 / Table of Contents / Rule 300):** "Rules for Opening Bank Accounts for Juristic Persons … 300.1.3 Resident companies"
- **Related node (Page 50 / Rule 300.1.3.6 (controls related to opening each individual account, item 1)):** "The bank shall not activate the escrow account for the project unless the license of the project issued by the Off-Plan Sales or Rent Committee in the Ministry of Housing is received."
- **Implication:** The bank's account-opening workflow for real estate escrow accounts must include a mandatory licence-verification checkpoint (Ministry of Housing Off-Plan licence) as a hard activation gate, separate from the standard entity-CDD steps required for all resident companies.

### [[General Instructions for Opening Bank Accounts]] — `references` [EXTRACTED]
- **Why:** The General Instructions (Rule 100) establish cross-cutting obligations—identity verification, disclosure, enforcement, and account-opening timelines—that apply to all customer categories including juristic persons governed under Rule 300. The juristic-persons chapter operationalises those general obligations with entity-specific document and ownership-verification requirements.
- **This node (Page 2 / Table of Contents / Rule 300):** "Rules for Opening Bank Accounts for Juristic Persons … 300.1 Resident juristic persons (including embassies and multilateral organizations)"
- **Related node (Page 32 / Rule 100 (section 15)):** "Banks shall open bank accounts for natural and juristic persons, for whom no approvals from bank's concerned departments are required, within one business day if they meet all bank requirements and within two business days for those who need approvals."
- **Implication:** Banks' onboarding workflows must enforce the one/two-business-day SLA for juristic-person accounts, with audit-trail evidence that entity-specific document checks (memorandum of association, ownership percentages, board formation) were completed within that window.

#graphify/document #graphify/EXTRACTED #community/Payment_Company_Accounts__Capital #graphify/enriched
