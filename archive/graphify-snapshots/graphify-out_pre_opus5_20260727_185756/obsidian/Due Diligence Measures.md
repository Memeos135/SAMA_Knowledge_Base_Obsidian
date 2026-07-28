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

# Due Diligence Measures

## Connections

### [[Anti-Money Laundering Law]] — `references` [EXTRACTED]
- **Why:** The AML Law directly mandates due diligence as a preventive measure obligation on FIs and DNFBPs, calibrating its intensity to customer risk profile; Articles 7–13 collectively establish due diligence as the primary operational control mechanism through which the Law's risk-based approach is operationalised.
- **This node (Page 4 / Article 7):** "Determine the extent of due diligence measures based on the risks relation to a customer or business relationship. Where a higher risk of money laundering was identified, they shall apply enhanced due diligence measures."
- **Related node (Page 5 / Article 13):** "Monitor and scrutinize transactions, document and data on an ongoing basis to ensure that they are consistent with the reporting entity's knowledge of the customer, the customer's commercial activities and risk profile, and where necessary the customer's source of funds."
- **Implication:** RegTech systems must implement a risk-tiered CDD/EDD workflow that dynamically links customer risk scoring to monitoring rule intensity, with a documented audit trail demonstrating that enhanced scrutiny was triggered and applied when elevated ML/TF risk was identified.

### [[Preventive Measures (CTF)]] — `shares_data_with` [INFERRED]
- **Why:** AML Due Diligence Measures (Art 7–8, SAMA_EN_791) and CTF Preventive Measures (Art 63–66, SAMA_EN_853) impose materially identical CDD/EDD data-collection obligations on FIs and DNFBPs — customer identity, risk profile, source of funds, beneficial ownership — meaning the same customer data set must simultaneously satisfy both regimes' requirements.
- **This node (Page 4 / Art 7):** "Apply due diligence measures to their customers… Determine the extent of due diligence measures based on the risks relation to a customer or business relationship. Where a higher risk of money laundering was identified, they shall apply enhanced due diligence measures."
- **Related node (Page 14 / Art 64):** "FIs and DNFBPs shall apply due diligence measures, and determine the extent of due diligence measures, on the basis of TF risks, to its customers and the business relationship, and shall apply enhanced due diligence measures when the TF risks are high."
- **Implication:** A unified KYC/CDD workflow and customer risk-scoring engine must capture and tag data attributes sufficient to satisfy both ML-risk and TF-risk assessments; separate ML and TF risk scores should be maintained per customer record so that EDD triggers under either regime are independently auditable.
- **Caveat:** The 'shares_data_with' relation is inferred from the structural and substantive overlap of the two regimes' CDD requirements rather than an explicit cross-reference between the two source documents; no article in either law directly cites the other for data-sharing purposes.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
