---
source_file: "markdown/SAMA_EN_2217_VER1.md"
type: "concept"
community: "Counter-Fraud Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Case Management System

## Connections

### [[Fraud Detection Systems]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing the response (Detect/Respond) obligations, understand that fraud detection outputs feed directly into the Case Management System: detection generates suspicious-activity alerts, and the Case Management System is mandated to 'record and monitor suspected fraud alerts' and act as the database tracking each case from initial alert to resolution. The two are sequential links in the same obligation chain — detection identifies, case management manages the response. Conclude that gaps in one undermine the other, and that a Member Organisation must show alerts raised by detection systems are captured, allocated and tracked within the Case Management System rather than handled ad hoc.
- **Grounding — this node (Page 53 / 6.2 Alert and Case Management):** "The Case Management System should be used to record and monitor suspected fraud alerts, internal and external reports, and case investigations from initial assessment to resolution."
- **Grounding — related node (Page 46 / 5.1 g):** "Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."

### [[Fraud Investigation Standard]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When mapping investigation obligations, treat the fraud investigation standard and the Case Management System as interdependent: the investigation standard directs a consistent approach (case allocation, materiality assessment, gathering transaction data, IP addresses, recordings), while the Case Management System is required to be the repository recording 'investigative steps followed' and all information needed 'to investigate and resolve the fraud case.' The link appears to reflect that investigation findings are captured within, and drawn from, the case record. Verify against the primary Sections 6.2 and 6.3 before relying on this as a hard data-flow requirement, since the connection is inferred from adjacent controls rather than an explicit cross-reference; conclude that investigation quality and case-record completeness should be assessed together.
- **Grounding — this node (Page 53 / 6.2 c):** "Record investigative steps followed ... Act as a repository for all information required to investigate and resolve the fraud case."
- **Grounding — related node (Page 54 / 6.3 Fraud Investigation):** "The fraud investigation standard should direct a consistent approach ... Gathering and analysing information to review the suspicion of fraud."
- **Caveat:** Relationship is inferred from adjacent controls; the two sections do not contain an explicit cross-reference, so confirm the intended data flow in the primary text.

### [[Respond Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping Respond-domain obligations, treat the Case Management System (6.2) as a mandatory component of the fraud response, not optional infrastructure. Section 6 (Respond) requires a Fraud Response Plan governing assessment, investigation and resolution, and sub-domain 6.2 requires implementing and maintaining a Case Management System to record, monitor and store data 'from initial assessment to resolution.' The consequence: a reviewer should confirm the case system operationalises the Response Plan (allocation, tracking, evidence repository, restricted access) and treat absence of such a system as a gap against a mandated control requirement.
- **Grounding — this node (Page 53 / Section 6.2):** "Member Organisations should implement and maintain a Case Management System to manage the response to fraud and act as a database for fraud case data."
- **Grounding — related node (Page 51 / Section 6.1):** "Member Organisations should define, approve, implement and maintain a Fraud Response Plan to outline the organisational response to an actual or suspected fraud incident."

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
