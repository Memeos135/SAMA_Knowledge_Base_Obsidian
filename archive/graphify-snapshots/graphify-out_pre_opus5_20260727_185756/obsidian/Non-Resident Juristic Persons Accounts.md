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

# Non-Resident Juristic Persons Accounts

## Connections

### [[Liquidation and Financial Restructuring Accounts]] — `conceptually_related_to` [INFERRED]
- **Why:** Both liquidation accounts and non-resident juristic person accounts appear sequentially in the same procedural chapter (Rules 300.1.7 and 300.2 respectively) and share the structural challenge of verifying legal authority and beneficial control for entities whose principal establishment or registration is outside normal domestic parameters, requiring elevated document verification and court-order or embassy-certified evidence.
- **This node (Page 4 / Table of Contents):** "300.2 Non-resident juristic persons 66 / 300.2.1 GCC commercial non-banking companies residing in Saudi Arabia 66"
- **Related node (Page 89 / Rule 300.1.7):** "The bank shall receive the court order that includes: Commencing any liquidation or administrative liquidation procedures against a natural or juristic person. Appointing one or more bankruptcy officeholder and specifying their names and powers."
- **Implication:** A bank's KYB system should apply a parallel elevated-authority-verification control to both liquidation accounts (court order as authority document) and non-resident juristic person accounts (embassy certification/correspondent bank verification), ensuring that the authorised operator field is always linked to a verified legal instrument rather than a self-declared mandate.
- **Caveat:** The conceptual linkage is structural/positional within the rulebook rather than an explicit cross-reference between the two rules; confidence is inferred from shared document-verification logic.

### [[Non-Banking GCC Companies Accounts]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Non-banking GCC companies (Rule 300.2.1) constitute a defined sub-category within the Non-Resident Juristic Persons chapter (Rule 300.2), receiving preferential treatment (correspondent bank verification, GCC citizen ownership threshold) relative to non-GCC non-resident entities, making the GCC company rules a specific regime nested within the broader non-resident juristic person framework.
- **This node (Page 4 / Table of Contents):** "300.2 Non-resident juristic persons 66 / 300.2.1 GCC commercial non-banking companies residing in Saudi Arabia 66 / 300.2.2 Non-resident, non-banking (non-GCC) companies and businesses with no contracts or projects in Saudi Arabia 68"
- **Related node (Page 92 / Rule 300.2.1):** "The memorandum of association and its annexes which clearly indicate the composition of both the capital and the establishment's management and that the ownership of GCC citizens (natural or juristic) exceeds 50% of the company's capital."
- **Implication:** The bank's KYB workflow must implement a residency and nationality classification gate at onboarding: entities claiming GCC preferential treatment must have their ≥50% GCC ownership confirmed via memorandum of association before being routed to the GCC-specific document checklist rather than the more restrictive non-GCC non-resident track.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** The Non-Resident Juristic Persons Accounts section (Rule 300.2) is issued under SAMA's supervisory authority; specific sub-rules (e.g., Rule 300.2.8) impose an obligation to inform SAMA when opening accounts for non-GCC payment card companies, making SAMA both the issuing authority and a mandatory notification recipient.
- **This node (Page 98 / Rule 300.2.8):** "after obtaining approval of the CEO/general director and the manager of compliance department to open a bank account and informing SAMA when opening such account, the bank may hold intermediary accounts in Saudi riyals for these companies"
- **Related node (Page 1):** "Rules for Bank Accounts Updated March 2022 … Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** Banks must log and evidence same-day notification to SAMA when opening intermediary SAR accounts for non-resident, non-GCC payment card companies; the compliance workflow must include a SAMA-notification step with a documented audit trail.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
