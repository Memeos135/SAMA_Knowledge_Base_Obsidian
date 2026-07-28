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

# General Instructions for Opening Bank Accounts

## Connections

### [[KYC Principle and AMLCFT Requirements|KYC Principle and AML/CFT Requirements]] — `references` [EXTRACTED]
- **Why:** The general account-opening instructions prescribe identity verification, risk management, and compliance-department sign-off requirements that are the procedural implementation of the overarching KYC/AML principle; the two nodes are linked because account-opening controls are the primary point at which KYC/AML obligations are initially discharged.
- **This node (Page 29 / Section 5 (Remote Opening — Corporations)):** "The bank is responsible for verifying the identity of the corporation by using documents, data or information acquired from a reliable and independent source … the corporation's capital, its owners and the ownership percentage of each owner … the persons authorized to open and o…"
- **Related node (Page 59):** "the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account … the bank shall ensure that such accounts are subject to dual control."
- **Implication:** Banks must configure onboarding workflows to enforce compliance-department review and, for designated account types, SAMA pre-approval as a hard gate before account activation, with a documented audit trail of identity verification sources satisfying both the general opening instructions and KYC/AML obligations.

### [[Rules for Opening Accounts for Juristic Persons]] — `references` [EXTRACTED]
- **Why:** The General Instructions (Rule 100) establish cross-cutting obligations—identity verification, disclosure, enforcement, and account-opening timelines—that apply to all customer categories including juristic persons governed under Rule 300. The juristic-persons chapter operationalises those general obligations with entity-specific document and ownership-verification requirements.
- **This node (Page 32 / Rule 100 (section 15)):** "Banks shall open bank accounts for natural and juristic persons, for whom no approvals from bank's concerned departments are required, within one business day if they meet all bank requirements and within two business days for those who need approvals."
- **Related node (Page 2 / Table of Contents / Rule 300):** "Rules for Opening Bank Accounts for Juristic Persons … 300.1 Resident juristic persons (including embassies and multilateral organizations)"
- **Implication:** Banks' onboarding workflows must enforce the one/two-business-day SLA for juristic-person accounts, with audit-trail evidence that entity-specific document checks (memorandum of association, ownership percentages, board formation) were completed within that window.

### [[Rules for Opening Accounts for Natural Persons]] — `references` [EXTRACTED]
- **Why:** Rule 100 sets the general procedural framework—including account-opening timelines, disclosure obligations, and enforcement procedures—that directly governs natural-person accounts opened under Rule 200, making Rule 100 a mandatory prerequisite layer for all Rule 200 operations.
- **This node (Page 32 / Rule 100 (section 15)):** "Banks shall open bank accounts for natural and juristic persons … within one business day if they meet all bank requirements and within two business days for those who need approvals. The applicant must be informed in writing of any missing or additional requirements upon applic…"
- **Related node (Page 2 / Table of Contents / Rule 200):** "Rules for Opening Accounts for Natural Persons … 200.1 Natural persons residing in Saudi Arabia … 200.1.1 Saudi natural persons"
- **Implication:** The onboarding system for natural persons must enforce the one/two-business-day clock from application submission, log written notification of deficiencies, and link this to the identity-verification controls in Rule 200 sub-sections to produce a complete audit trail.

### [[Rules for Remote Opening of Bank Accounts]] — `references` [EXTRACTED]
- **Why:** The General Instructions establish baseline identity-verification and risk-management obligations that apply to all account openings; the Remote Opening rules are a specialised extension of those obligations, imposing additional controls (independent-source verification, secure ATM activation) precisely because the in-person verification safeguard is absent.
- **This node (Page 29 / Rule 100 (remote opening sub-section)):** "Appropriate standards must be set to manage risks associated with these accounts before approving the opening of such accounts in order to avoid opening an account for a company or a person with whom dealing is prohibited, for an incompetent person or the like."
- **Related node (Page 29 / Rules for Remote Opening (section 5, item 1)):** "The bank is responsible for verifying the identity of the corporation by using documents, data or information acquired from a reliable and independent source. The following at least shall be checked: The name and legal form of the corporation, the powers that regulate and govern…"
- **Implication:** Digital onboarding workflows for remote account opening must include an automated risk-screening gate (prohibited-persons/entities check) and an independent-source document-verification step before account activation, with the ATM card activation mechanism logged as a separate control event.

#graphify/document #graphify/EXTRACTED #community/Payment_Company_Accounts__Capital #graphify/enriched
