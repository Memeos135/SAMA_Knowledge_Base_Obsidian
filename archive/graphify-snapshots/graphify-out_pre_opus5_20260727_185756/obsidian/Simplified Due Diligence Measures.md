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

# Simplified Due Diligence Measures

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **Why:** Article 5/5 of the AML Law Implementing Regulations is expressly cited as the legal authority permitting financial institutions to apply simplified CDD measures when ML/TF risks are assessed as low, subject to defined conditions, linking the Law to the simplified-measures operational concept.
- **This node (Page 43 / Section 5):** "Article (5/5) of the Implementing Regulations of the Anti-Money Laundering Law…state that the financial institution may apply simplified measures when the ML/TF risks are low subject to the necessary conditions."
- **Related node (Page 4 / Chapter II Purpose):** "The purpose of this Guide is to help financial institutions…to meet the requirements of the Anti-Money Laundering Law, issued by Royal Decree No. (M/20) dated 05/02/1439H, and its Implementing Regulations, issued under the Decision of the Presidency of State Security No. (14525)…"
- **Implication:** Risk-based CDD workflows must document the low-risk determination before applying simplified measures, retaining evidence that core identity verification and beneficial-owner identification were still performed, and that no ML/TF suspicion existed at the time—auditable at customer and portfolio level.

### [[Due Diligence Measures]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Simplified Due Diligence is an explicitly permitted, risk-proportionate variant of the standard CDD obligation, applicable only when ML/TF risk is assessed as low and no suspicion exists; the regulation makes clear it does not exempt the institution from the core CDD requirements of para 3.7.
- **This node (Page 43 / para 5.3):** "Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owner."
- **Related node (Page 35 / para 3.22(c)):** "The financial institution shall immediately obtain all information related to due diligence, including simplified and enhanced due diligence measures, from the third party."
- **Implication:** The compliance system must enforce that even customers assigned a low-risk/SDD profile still complete mandatory identity verification and beneficial-owner identification steps, with the risk-tier rationale documented and reviewable for any SDD election.

### [[Monitoring of Transactions and Activities]] — `references` [EXTRACTED]
- **Why:** The transaction monitoring section explicitly calibrates monitoring intensity to the customer risk tier, mandating that low-risk customers receiving simplified CDD are subject to a reduced but non-zero monitoring regime, creating a direct operational link between the SDD classification and the monitoring rule applied.
- **This node (Page 43 / Para 5.3):** "Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owner."
- **Related node (Page 49 / Para 7.2(b) and 7.3):** "Implement simplified measures for low-risk customers and businesses, including reducing the rate and frequency of monitoring in the case of low ML/TF risk… it allows the financial institution to implement control procedures in a streamlined and simplified manner."
- **Implication:** The transaction monitoring system must link each customer's risk classification to a specific rule-set tier so that low-risk/SDD customers receive reduced frequency monitoring rules rather than no monitoring, and the configuration of those tiers must be documented and approved at senior management level.

### [[Wire Transfer]] — `references` [EXTRACTED]
- **Why:** The wire transfer section establishes mandatory originator and beneficiary information requirements for all wire transfers regardless of risk level, meaning SDD cannot reduce or waive these data-collection obligations; the carve-outs in Para 14.8 are product-type exclusions, not risk-tier exemptions, reinforcing that SDD's scope reduction does not extend to wire transfer data fields.
- **This node (Page 43 / Para 5.3):** "Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owner."
- **Related node (Page 65 / Para 14.1):** "Before processing a wire transfer, the financial institution should obtain information about the wire transfer originator and beneficiary, keep that information with each wire transfer, and verify that information."
- **Implication:** Wire transfer processing workflows must enforce mandatory originator/beneficiary data fields as a hard pre-execution control that is independent of the customer's SDD risk classification; SDD does not create a permissible exemption from wire transfer information requirements.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
