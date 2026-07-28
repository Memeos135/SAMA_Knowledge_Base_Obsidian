---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "document"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Reporting of Suspicious Transactions

## Connections

### [[AMLCTF Compliance Function|AML/CTF Compliance Function]] — `references` [EXTRACTED]
- **Why:** Section 9 assigns the AML/CTF Compliance Function officer direct operational responsibility for receiving, analysing, and escalating suspicious transaction reports to the SAFIU, expressly cross-referencing the Reporting of Suspicious Transactions Section as the governing procedure, making the compliance function the accountable owner of the STR lifecycle.
- **This node (Page 52 / Section 8, Para 8.1):** "The financial institution shall set up and document procedures for reporting suspicious transactions, implementing them effectively, and ensuring that they are approved at the level of the board of directors."
- **Related node (Page 57 / Section 9, Para 9.3(e)):** "Reporting suspicious transactions to the SAFIU as soon as the suspicion is detected in accordance with the reporting procedures followed in addition to preparing a technical report on the suspicion case as stated in the Reporting of Suspicious Transactions Section."
- **Implication:** The AML/CTF compliance officer must be named in board-approved STR procedures as the accountable decision-maker for SAFIU submissions, and the system must capture a dated audit trail from internal flag through officer review to SAFIU dispatch.

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **Why:** Article 13 of the AML Law mandates continuous transaction monitoring, which is the statutory predicate for the Guide's Reporting of Suspicious Transactions section, creating a direct legal citation chain from the Law to the STR operational framework.
- **This node (Page 48 / Section 7):** "Article (13) of the Anti-Money Laundering Law and Article (69) of the Law on Combating Terrorism Crimes and Financing state the financial institution's responsibilities to continuously monitor transactions, documents and data to ensure that they are consistent with the informati…"
- **Related node (Page 5 / Chapter IV Definitions):** "Anti-Money Laundering Law: The Anti-Money Laundering Law issued by Royal Decree No. (M/20) dated 05/02/1439H."
- **Implication:** Transaction-monitoring systems must be configured to generate alerts that feed a documented internal STR workflow—including immediate SAFIU reporting upon reasonable grounds of suspicion, maintenance of confidentiality, and ten-year retention of investigation records—all evidenceable to SAMA as statutory compliance.

### [[Monitoring of Transactions and Activities]] — `references` [EXTRACTED]
- **Why:** Section 7 explicitly identifies detection and referral of suspicious transactions to the SAFIU as the primary output of transaction monitoring, establishing a direct procedural dependency: the monitoring function triggers the reporting obligation defined in Section 8, creating an end-to-end detect-to-report workflow.
- **This node (Page 52 / Section 8, Para 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behavior is related to ML/TF acts."
- **Related node (Page 48 / Section 7, opening paragraph):** "The monitoring of transactions and activities, including those unusual and suspicious, is an important element for applying the risk-based approach as it enables the financial institution to identify and report any suspicious transactions or activities to the SAFIU."
- **Implication:** The transaction monitoring system must have a documented escalation path that converts flagged unusual activity into a timed STR workflow, with evidence of investigation, approval levels, and SAFIU submission timestamps auditable end-to-end.

### [[SAFIU]] — `references` [EXTRACTED]
- **Why:** The Reporting of Suspicious Transactions section governs the mechanics, conditions, and content of mandatory disclosures to SAFIU, making SAFIU the designated external authority to whom all STRs must be submitted immediately upon detection of reasonable grounds for suspicion.
- **This node (Page 52 / Art 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behaviour is related to ML/TF acts."
- **Related node (Page 6 / Definitions):** "The SAFIU analyzes and investigates such reports and information before submitting related results to the competent authorities, promptly or upon request. The SAFIU reports to the President of State Security and has sufficient operational independence."
- **Implication:** The STR workflow must enforce immediate, direct reporting to SAFIU upon triggering of reasonable grounds, using SAFIU-approved forms and accompanied by a technical report (six-month account statement, CDD documents, and narrative analysis), with board-approved procedures and a named responsible officer evidenced in writing.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** The Reporting of Suspicious Transactions section mandates direct reporting to SAMA (alongside SAFIU) for accounts and transactions linked to UN Security Council designation lists, and requires submission of internal controls surveys and AML/CTF data to SAMA, establishing SAMA as a parallel regulatory recipient distinct from the SAFIU intelligence function.
- **This node (Page 57 / Section 9, Para 9.3(f)):** "Reporting any accounts, business relationships, or financial transactions related to the names included in the lists of the Security Council committees… to SAMA, as mentioned in Paragraph (8.15) under the Reporting of Suspicious Transactions Section."
- **Related node (Page 1 / Cover):** "The Anti-Money Laundering and Counter-Terrorism Financing (AML/CTF) Guide — AML/CTF Department, Saudi Central Bank, RABI' I 1441H (November 2019)."
- **Implication:** Compliance systems must maintain two distinct reporting channels — SAFIU for STRs and SAMA for sanctions-linked account notifications — with separate workflow triggers, submission records, and response tracking for each regulator.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
