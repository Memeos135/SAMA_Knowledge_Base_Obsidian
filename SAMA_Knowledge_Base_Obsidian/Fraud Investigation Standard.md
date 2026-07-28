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

# Fraud Investigation Standard

## Connections

### [[Case Management System]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When mapping investigation obligations, treat the fraud investigation standard and the Case Management System as interdependent: the investigation standard directs a consistent approach (case allocation, materiality assessment, gathering transaction data, IP addresses, recordings), while the Case Management System is required to be the repository recording 'investigative steps followed' and all information needed 'to investigate and resolve the fraud case.' The link appears to reflect that investigation findings are captured within, and drawn from, the case record. Verify against the primary Sections 6.2 and 6.3 before relying on this as a hard data-flow requirement, since the connection is inferred from adjacent controls rather than an explicit cross-reference; conclude that investigation quality and case-record completeness should be assessed together.
- **Grounding — this node (Page 54 / 6.3 Fraud Investigation):** "The fraud investigation standard should direct a consistent approach ... Gathering and analysing information to review the suspicion of fraud."
- **Grounding — related node (Page 53 / 6.2 c):** "Record investigative steps followed ... Act as a repository for all information required to investigate and resolve the fraud case."
- **Caveat:** Relationship is inferred from adjacent controls; the two sections do not contain an explicit cross-reference, so confirm the intended data flow in the primary text.

### [[Intelligence Monitoring]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing investigation and intelligence obligations, recognise that fraud investigation output is a mandated input to Intelligence Monitoring: control 4.1.1(e)(1) requires Intelligence Monitoring to draw on fraud investigation output and scenario analysis to identify trending TTPs. The investigation standard captures data (fraud typology, methods, fraudster IP/Device ID, origin) that directly feeds this monitoring. Conclude that investigation records must be structured to surface typology and TTP information for the monitoring process; investigations that close without feeding intelligence leave a compliance gap across both provisions.
- **Grounding — this node (Page 54 / 6.3, 6.2 fields):** "The methods used to conduct the fraud/fraud typology (e.g., how the fraud was committed, where the funds were transferred if lost)"
- **Grounding — related node (Page 27 / 4.1.1(e)(1)):** "fraud investigation output and Fraud Scenario Analysis covering attempted and actual fraud to identify trending fraud tactics, techniques, and procedures"

### [[Respond Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing investigation obligations, read the Fraud Investigation Standard (6.3) as a mandated sub-domain within the Respond domain that gives effect to the Fraud Response Plan. Section 6 requires prompt investigation and resolution of all suspected or identified fraud, and 6.3 requires a standard directing a consistent approach including case allocation, time-sensitivity and materiality assessment, and evidence gathering. Note the cross-regime link within investigation: external notifications may require reporting to the FIU where suspicion reaches the level in article 15 of the AML Law and article 17 of the CTF Law. The consequence: a reviewer should confirm the investigation standard both meets the consistency requirements and triggers AML/CTF reporting where thresholds are met, so fraud investigation is not siloed from AML obligations.
- **Grounding — this node (Page 54 / Section 6.3):** "Member Organisations should define, approve, implement and maintain a fraud investigation standard to direct a consistent approach to fraud investigation."
- **Grounding — related node (Page 51 / Section 6.1(d)):** "The Fraud Response Plan should require prompt and competent assessment, investigation, and resolution of all suspected or identified fraud."

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
