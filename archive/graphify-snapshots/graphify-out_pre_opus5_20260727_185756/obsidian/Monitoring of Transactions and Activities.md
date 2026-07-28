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

# Monitoring of Transactions and Activities

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **Why:** Article 13 of the Anti-Money Laundering Law is directly cited as the statutory basis requiring financial institutions to continuously monitor transactions, documents, and data against customer profiles; the Guide's Monitoring section operationalises this legal obligation through risk-based procedural requirements.
- **This node (Page 48 / Section 7):** "Article (13) of the Anti-Money Laundering Law and Article (69) of the Law on Combating Terrorism Crimes and Financing state the financial institution's responsibilities to continuously monitor transactions, documents and data to ensure that they are consistent with the informati…"
- **Related node (Page 4 / Chapter II Purpose):** "The purpose of this Guide is to help financial institutions... to meet the requirements of the Anti-Money Laundering Law, issued by Royal Decree No. (M/20) dated 05/02/1439H, and its Implementing Regulations."
- **Implication:** Transaction monitoring systems must be calibrated to risk-tier classifications, tested at least annually, and integrated with customer profile data—with documented test results and tuning records available to demonstrate Article 13 compliance to SAMA examiners.

### [[Correspondence Relationship]] — `references` [EXTRACTED]
- **Why:** Section 13 of the Correspondence Relationship regime explicitly cross-references the Monitoring of Transactions and Activities Section, requiring financial institutions to apply continuous control measures from that section specifically to detect unusual activity in correspondent accounts, making transaction monitoring an embedded obligation within correspondent banking due diligence.
- **This node (Page 48 / Section 7, Para 7.1):** "The financial institution shall put in place measures and procedures based on the risk assessment results to monitor transactions and identify unusual transactions and activities. The measures and procedures shall be effectively implemented and documented by the financial instit…"
- **Related node (Page 64 / Section 13, Para 13.3):** "The financial institution should apply appropriate control measures as indicated under the Monitoring of Transactions and Activities Section, including continuous control measures for correspondence accounts to detect any unusual activity or behavior in the correspondence relati…"
- **Implication:** Correspondent account monitoring must be configured as a distinct, continuously active rule set within the transaction monitoring system, with documented senior-management approval, evidencing that general monitoring obligations under Section 7 are applied at the correspondent-relationship level.

### [[FATF]] — `references` [EXTRACTED]
- **Why:** The SAMA AML/CTF Guide's risk-based monitoring framework is explicitly positioned as an implementation of FATF standards; FATF's standard-setting role is the normative source from which the risk-based approach to transaction monitoring — including enhanced/simplified tiering and mandatory electronic systems — derives its authority in the KSA context.
- **This node (Page 48 / Section 7 / Art 7.2):** "The financial institution shall apply a risk-based monitoring approach according to the degree and levels of risk derived from the ML/TF risk assessment results."
- **Related node (Page 3 / Introduction):** "Saudi Arabia joined the Financial Action Task Force (FATF) in June 2019 … SAMA has adopted various initiatives that include measures and other criteria in response to international developments in this field."
- **Implication:** SAMA examiners will benchmark the financial institution's transaction monitoring framework against FATF Recommendation 10 (ongoing due diligence) and related guidance; audit evidence should demonstrate that risk-tiered monitoring rules, technology system adequacy, and annual testing are documented and calibrated to FATF-aligned risk categories.

### [[Reporting of Suspicious Transactions]] — `references` [EXTRACTED]
- **Why:** Section 7 explicitly identifies detection and referral of suspicious transactions to the SAFIU as the primary output of transaction monitoring, establishing a direct procedural dependency: the monitoring function triggers the reporting obligation defined in Section 8, creating an end-to-end detect-to-report workflow.
- **This node (Page 48 / Section 7, opening paragraph):** "The monitoring of transactions and activities, including those unusual and suspicious, is an important element for applying the risk-based approach as it enables the financial institution to identify and report any suspicious transactions or activities to the SAFIU."
- **Related node (Page 52 / Section 8, Para 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behavior is related to ML/TF acts."
- **Implication:** The transaction monitoring system must have a documented escalation path that converts flagged unusual activity into a timed STR workflow, with evidence of investigation, approval levels, and SAFIU submission timestamps auditable end-to-end.

### [[SAFIU]] — `references` [EXTRACTED]
- **Why:** The Monitoring of Transactions and Activities section explicitly names SAFIU as the mandatory recipient of suspicious transaction or activity reports detected through the monitoring process, establishing a direct operational output relationship between the transaction monitoring function and the SAFIU reporting obligation.
- **This node (Page 48 / Section 7 / intro):** "it enables the financial institution to identify and report any suspicious transactions or activities to the SAFIU"
- **Related node (Page 6 / Definitions):** "Saudi Arabia Financial Intelligence Unit (SAFIU): A national center that receives information and reports related to crimes of money laundering, terrorist financing, predicate offenses, or proceeds of crime"
- **Implication:** The transaction monitoring system must produce a documented alert-to-STR pipeline, with evidence that unusual activity escalations are triaged and, where warranted, transmitted to SAFIU — auditors will expect to see the linkage between system alerts and filed reports.

### [[Simplified Due Diligence Measures]] — `references` [EXTRACTED]
- **Why:** The transaction monitoring section explicitly calibrates monitoring intensity to the customer risk tier, mandating that low-risk customers receiving simplified CDD are subject to a reduced but non-zero monitoring regime, creating a direct operational link between the SDD classification and the monitoring rule applied.
- **This node (Page 49 / Para 7.2(b) and 7.3):** "Implement simplified measures for low-risk customers and businesses, including reducing the rate and frequency of monitoring in the case of low ML/TF risk… it allows the financial institution to implement control procedures in a streamlined and simplified manner."
- **Related node (Page 43 / Para 5.3):** "Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owner."
- **Implication:** The transaction monitoring system must link each customer's risk classification to a specific rule-set tier so that low-risk/SDD customers receive reduced frequency monitoring rules rather than no monitoring, and the configuration of those tiers must be documented and approved at senior management level.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
