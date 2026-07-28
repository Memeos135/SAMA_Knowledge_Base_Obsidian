---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "concept"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# SAFIU

## Connections

### [[AMLCTF Compliance Function|AML/CTF Compliance Function]] — `references` [EXTRACTED]
- **Why:** The AML/CTF compliance function bears explicit responsibility for determining and executing STR submissions to SAFIU, including designating the responsible officer, maintaining confidentiality, and providing SAFIU with additional information on request; SAFIU therefore represents the primary external regulatory interface for the compliance function's suspicious-activity reporting obligations.
- **This node (Page 52 / Para 8.1(e)):** "Determining the employee or officer responsible for reporting to the SAFIU about suspicious transactions."
- **Related node (Page 56 / Para 9.3):** "The responsibilities shall include all AML/CTF work… Continuously reviewing the business policies and procedures of the financial institution and monitoring their implementation in addition to recommending measures to be taken to meet the AML/CTF requirements."
- **Implication:** The AML/CTF compliance function's job description and governance framework must formally designate a named SAFIU reporting officer, document the internal escalation-to-submission workflow with board-level approval, and maintain an evidence trail of all SAFIU submissions and responses for examiner review.

### [[Anti-Money Laundering Law]] — `references` [EXTRACTED]
- **Why:** The AML Law establishes the legal basis for suspicious transaction reporting obligations, and the SAFIU is the designated national recipient of those reports; the Guide explicitly defines SAFIU and operationalises the Law's reporting duty through detailed STR procedures directed at SAFIU.
- **This node (Page 6 / Chapter IV Definitions):** "Saudi Arabia Financial Intelligence Unit (SAFIU): A national center that receives information and reports related to crimes of money laundering, terrorist financing, predicate offenses, or proceeds of crime according to the Anti-Money Laundering Law... The SAFIU analyzes and inv…"
- **Related node (Page 5 / Chapter IV Definitions):** "Anti-Money Laundering Law: The Anti-Money Laundering Law issued by Royal Decree No. (M/20) dated 05/02/1439H."
- **Implication:** Financial institutions must maintain a documented STR workflow that names SAFIU as the mandatory external recipient and logs every submission, rejection decision, and SAFIU information request response as an auditable record.

### [[Monitoring of Transactions and Activities]] — `references` [EXTRACTED]
- **Why:** The Monitoring of Transactions and Activities section explicitly names SAFIU as the mandatory recipient of suspicious transaction or activity reports detected through the monitoring process, establishing a direct operational output relationship between the transaction monitoring function and the SAFIU reporting obligation.
- **This node (Page 6 / Definitions):** "Saudi Arabia Financial Intelligence Unit (SAFIU): A national center that receives information and reports related to crimes of money laundering, terrorist financing, predicate offenses, or proceeds of crime"
- **Related node (Page 48 / Section 7 / intro):** "it enables the financial institution to identify and report any suspicious transactions or activities to the SAFIU"
- **Implication:** The transaction monitoring system must produce a documented alert-to-STR pipeline, with evidence that unusual activity escalations are triaged and, where warranted, transmitted to SAFIU — auditors will expect to see the linkage between system alerts and filed reports.

### [[Politically Exposed Persons (PEPs)]] — `references` [EXTRACTED]
- **Why:** PEP relationships are high-risk business relationships requiring EDD; where PEP activity raises ML/TF suspicion, the financial institution is obligated to file a suspicious transaction report (STR) with SAFIU, making SAFIU the mandatory reporting destination for PEP-triggered suspicions and creating a direct operational pathway from PEP monitoring to SAFIU notification.
- **This node (Page 52 / Para 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behavior is related to ML/TF acts."
- **Related node (Page 39 / Section 4B):** "The financial institution shall take reasonable measures to identify whether a customer or beneficial owner is a PEP. In cases of high-risk business relationships with PEPs, the financial institution shall apply enhanced due diligence measures."
- **Implication:** The PEP monitoring workflow must include an escalation path that, upon detection of suspicious activity in a PEP relationship, automatically routes the case for STR preparation and direct submission to SAFIU, with the six-month account statement and CDD documents attached per Para 8.9 requirements.

### [[Reporting of Suspicious Transactions]] — `references` [EXTRACTED]
- **Why:** The Reporting of Suspicious Transactions section governs the mechanics, conditions, and content of mandatory disclosures to SAFIU, making SAFIU the designated external authority to whom all STRs must be submitted immediately upon detection of reasonable grounds for suspicion.
- **This node (Page 6 / Definitions):** "The SAFIU analyzes and investigates such reports and information before submitting related results to the competent authorities, promptly or upon request. The SAFIU reports to the President of State Security and has sufficient operational independence."
- **Related node (Page 52 / Art 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behaviour is related to ML/TF acts."
- **Implication:** The STR workflow must enforce immediate, direct reporting to SAFIU upon triggering of reasonable grounds, using SAFIU-approved forms and accompanied by a technical report (six-month account statement, CDD documents, and narrative analysis), with board-approved procedures and a named responsible officer evidenced in writing.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
