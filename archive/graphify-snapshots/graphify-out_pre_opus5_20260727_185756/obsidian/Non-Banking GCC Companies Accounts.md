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

# Non-Banking GCC Companies Accounts

## Connections

### [[KYC Principle]] — `references` [EXTRACTED]
- **Why:** The GCC companies account-opening rules operationalise the KYC principle by mandating specific ownership verification (≥50% GCC citizenship), beneficial control identification, board member ID verification, and correspondent bank interview procedures, directly implementing the broader KYC obligation in a cross-border corporate context.
- **This node (Page 92 / Rule 300.2.1):** "The above documents shall be completed by the bank's employees directly by interviewing the clients personally (authorized persons) or by a national GCC correspondent bank residing in the country of the company. The correspondent bank shall verify that copies provided for all th…"
- **Related node (Page 21 / Chapter II):** "Banks shall ascertain the nature of the relationship for natural curators, legal agents, custodians and authorized persons when opening accounts and check the validity of the documents submitted."
- **Implication:** For non-resident GCC company onboarding, the bank must document the correspondent bank's identity verification step as a KYC reliance record, clearly evidencing that document authenticity was confirmed at source, which is the auditor-expected substitute for in-person branch verification.

### [[Non-Resident Juristic Persons Accounts]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Non-banking GCC companies (Rule 300.2.1) constitute a defined sub-category within the Non-Resident Juristic Persons chapter (Rule 300.2), receiving preferential treatment (correspondent bank verification, GCC citizen ownership threshold) relative to non-GCC non-resident entities, making the GCC company rules a specific regime nested within the broader non-resident juristic person framework.
- **This node (Page 92 / Rule 300.2.1):** "The memorandum of association and its annexes which clearly indicate the composition of both the capital and the establishment's management and that the ownership of GCC citizens (natural or juristic) exceeds 50% of the company's capital."
- **Related node (Page 4 / Table of Contents):** "300.2 Non-resident juristic persons 66 / 300.2.1 GCC commercial non-banking companies residing in Saudi Arabia 66 / 300.2.2 Non-resident, non-banking (non-GCC) companies and businesses with no contracts or projects in Saudi Arabia 68"
- **Implication:** The bank's KYB workflow must implement a residency and nationality classification gate at onboarding: entities claiming GCC preferential treatment must have their ≥50% GCC ownership confirmed via memorandum of association before being routed to the GCC-specific document checklist rather than the more restrictive non-GCC non-resident track.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
