---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Bank Account Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Account_Rules
  - graphify/enriched
---

# Rules for Bank Accounts

## Connections

### [[Bank Accounts for Liquidation and Financial Restructuring]] — `references` [EXTRACTED]
- **What this link tells you:** When a customer enters bankruptcy or company liquidation, consult Rule 300.1.7 (Bank Accounts for Liquidation and Financial Restructuring) as the specific procedure that governs who may open and operate the account and what court/appointment documents are required. This link matters because control shifts from the account holder to a liquidation officeholder or bankruptcy committee under court order pursuant to the Bankruptcy Law or Companies Law, and the account must be specifically named as a 'Liquidation Account'. Conclude that ordinary authorised-signatory and operation rules are displaced during liquidation, and verify the court order, officeholder identity and mandated account naming before permitting transactions.
- **Grounding — this node (Page 4 / Table of Contents):** "300.1.7 Bank accounts for liquidation and financial restructuring 64"
- **Grounding — related node (Page 89 / 300.1.7):** "The bank may open bank accounts for liquidation, for depositing the proceeds of the sale of the bankruptcy assets covering the debtor's debt."

### [[Chapter I Definitions|Chapter I: Definitions]] — `references` [EXTRACTED]
- **What this link tells you:** When applying any operative rule in the Rules for Bank Accounts — such as dormant-account handling or freezing — read the defined terms in Chapter I as controlling, because the same document states those meanings apply 'wherever mentioned herein.' For example, 'Freezing of Account' and 'Bank Account' have specific defined scopes that constrain when suspension or account measures are legitimate. You should conclude that the operative obligations (dormancy, disclosure, enforcement) cannot be interpreted independently of Chapter I definitions, and should cross-check each term's defined meaning before relying on an operative provision.
- **Grounding — this node (Page 16-22):** "Accounts shall be considered dormant after (24) calendar months from the date of the last recorded debit transaction"
- **Grounding — related node (Page 6 / Chapter I):** "The following terms and phrases, wherever mentioned herein, shall have the meanings assigned thereto unless the context otherwise requires"

### [[Chapter II Supervisory Rules and Controls|Chapter II: Supervisory Rules and Controls]] — `references` [EXTRACTED]
- **What this link tells you:** When you are mapping obligations under the Rules for Bank Accounts, treat Chapter II (Supervisory Rules and Controls) as the governing prudential/supervisory layer that sits above the specific account-type procedures. The parent document's table of contents lists Chapter II as a distinct block (pages 9–22) covering dormancy classification, disclosure and enforcement — so requirements like double supervision over dormant files or SAMA-only disclosure requests derive from this chapter, not from the procedural rules in Chapter III. Conclude that any account-opening or operation obligation must be read together with these overarching supervisory controls, and check Chapter II before assuming a procedural rule is complete.
- **Grounding — this node (Page 16-17 / 5.2.2):** "Banks shall establish policies and procedures to ensure double supervision over the files of such accounts, with a supervision level higher than that applied to the other files."
- **Grounding — related node (Page 2 / Table of Contents):** "Chapter II Supervisory Rules and Controls 9"

### [[Chapter III Procedural Rules|Chapter III: Procedural Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping account-opening obligations, read Chapter III as the operative procedural detail sitting under the umbrella Rules for Bank Accounts, keyed to customer type. Chapter III (rules 100–600) prescribes the specific documentation and eligibility conditions for natural persons, juristic persons (including KYB-relevant categories like licensed businesses, e-commerce with no premises, money changers), and government entities, and Chapter II expressly directs that these detailed requirements form the basis for opening accounts. Conclude that for any given account, you must locate the applicable Chapter III sub-rule for that customer category rather than relying on the general chapters alone, since the granular identification and eligibility conditions live there.
- **Grounding — this node (Page 9 / Ch II):** "detailed requirements provided in Chapters III and IV herein, as a basis for opening, operating, and following up bank accounts"
- **Grounding — related node (Page 2 / Ch III ToC):** "Chapter III Procedural Rules... 100 General Instructions for Opening Bank Accounts... 200 Rules for Opening Accounts for Natural Persons"

### [[General Rules for Operation of Bank Accounts]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing obligations that arise after an account is live — deposits, dormant/abandoned status, and closure — treat Chapter IV as the operative operational limb of the Rules for Bank Accounts, distinct from the opening rules. The dormant-account controls (24-month trigger, double supervision, restrictions on withdrawals, balance treatment as liabilities, and closure of low-balance accounts with notice) form part of this operation regime and impose continuing bank duties throughout the account lifecycle. Conclude that compliance testing of ongoing account handling must reference the operation rules, not just onboarding, and that dormancy classification and enforcement/disclosure procedures carry their own confidentiality and process constraints.
- **Grounding — this node (Page 2 ToC (Ch IV) / Page 16):** "Chapter IV General Rules for Operation of Bank Accounts... Account closure"
- **Grounding — related node (Page 16 / 5.2.2):** "Accounts shall be considered dormant after (24) calendar months from the date of the last recorded debit transaction"

### [[Government Entity Account Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When advising on any government-entity account, use the Government Entity Account Rules (Rule 500) as the controlling regime, because they impose entity-specific restrictions that override the general account rules — Ministry of Finance approval for foreign-currency or bank-transfer, Council of Ministers approval for any overdraft/facility, and a Saudis-only signatory rule. This link tells you these accounts are a distinct compliance track with additional government-approval gatekeeping. Conclude that ordinary opening/operation permissions cannot be assumed for government entities, and check Rule 500 for the required MoF/SAMA authorisations before acting.
- **Grounding — this node (Page 5 / Table of Contents):** "500 Rules for Opening Bank Accounts for Government Entities 73"
- **Grounding — related node (Page 102 / 500.1):** "Signatories of the accounts of Saudi government entities and agencies shall be Saudis only. No authorization shall be granted to non-Saudis in this regard."

### [[Non-resident Commercial Bank Correspondent Accounts]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a non-resident bank relationship may be opened, read the parent Rules together with Rule 300.2.5 on correspondent accounts, which is the specific carve-out governing non-resident commercial banks (including GCC banks and central banks). This matters cross-regime: correspondent banking is a recognised higher-risk AML/CTF category, and note that non-resident money changers and non-GCC payment card companies are cross-referenced back to 300.2.5's documentation requirements or subjected to outright prohibition absent senior/compliance approval and SAMA notification. Conclude that eligibility and CDD depth for these entities are set by these specific sub-rules, and verify which sub-rule (300.2.5–300.2.8) applies to the counterparty type before opening.
- **Grounding — this node (Page 22 / 10.1):** "banks shall search for all relationships between the bank and the customer, including all active; closed and suspended accounts."
- **Grounding — related node (Page 98 / 300.2.8):** "Banks are not permitted to open accounts for such companies. However, after obtaining approval of the CEO/general director and the manager of compliance department."

### [[Non-resident Juristic Persons Account Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what documentation and account controls apply to a non-resident juristic person, treat the 300.2 category rules as a specialized sub-set of the general Rules for Bank Accounts rather than a standalone regime. The parent Rules set the baseline controls (dormancy, disclosure/enforcement, freezing, electronic record) applicable to all customers including juristic persons, while the 300.2 section adds category-specific opening conditions for each type of non-resident entity (GCC companies, non-GCC businesses, foreign banks, insurers, payment card companies). You should conclude that opening a non-resident juristic account requires satisfying both the general supervisory requirements and the specific 300.2 sub-category controls, and check which 300.2.x sub-paragraph matches the entity's exact status.
- **Grounding — this node (Page 16 / 5.2.2):** "the person authorized to operate the account if the account is for a juristic person"
- **Grounding — related node (Page 4 / 300.2):** "300.2 Non-resident juristic persons 66 ... 300.2.1 GCC commercial non-banking companies residing in Saudi Arabia"

### [[WAMY Bank Account Rules]] — `references` [EXTRACTED]
- **What this link tells you:** When opening or maintaining an account for a specific named entity like the World Assembly of Muslim Youth, apply the entity-specific WAMY conditions on top of the general account rules rather than treating them as alternatives. The WAMY provisions form part of the same Rules for Bank Accounts and layer additional controls — single main account, joint/main signatures, compliance-department and CEO approval, deposit/withdrawal restrictions, mandatory notification to SAMA — over the baseline requirements applicable to all account holders. You should conclude that the WAMY account is subject to both the general supervisory controls and these heightened entity-specific restrictions, and verify that source-of-funds, real-beneficiary and competent-authority approval conditions are all met.
- **Grounding — this node (Page 22 / 10.1):** "banks shall search for all relationships between the bank and the customer, including all active; closed and suspended accounts"
- **Grounding — related node (Page 84 / WAMY):** "One main account only shall be opened under WAMY's name ... SAMA must be informed when the account is opened"

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Rules #graphify/enriched
