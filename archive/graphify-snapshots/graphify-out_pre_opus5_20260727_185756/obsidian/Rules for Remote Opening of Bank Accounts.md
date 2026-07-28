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

# Rules for Remote Opening of Bank Accounts

## Connections

### [[General Instructions for Opening Bank Accounts]] — `references` [EXTRACTED]
- **Why:** The General Instructions establish baseline identity-verification and risk-management obligations that apply to all account openings; the Remote Opening rules are a specialised extension of those obligations, imposing additional controls (independent-source verification, secure ATM activation) precisely because the in-person verification safeguard is absent.
- **This node (Page 29 / Rules for Remote Opening (section 5, item 1)):** "The bank is responsible for verifying the identity of the corporation by using documents, data or information acquired from a reliable and independent source. The following at least shall be checked: The name and legal form of the corporation, the powers that regulate and govern…"
- **Related node (Page 29 / Rule 100 (remote opening sub-section)):** "Appropriate standards must be set to manage risks associated with these accounts before approving the opening of such accounts in order to avoid opening an account for a company or a person with whom dealing is prohibited, for an incompetent person or the like."
- **Implication:** Digital onboarding workflows for remote account opening must include an automated risk-screening gate (prohibited-persons/entities check) and an independent-source document-verification step before account activation, with the ATM card activation mechanism logged as a separate control event.

#graphify/document #graphify/EXTRACTED #community/Payment_Company_Accounts__Capital #graphify/enriched
