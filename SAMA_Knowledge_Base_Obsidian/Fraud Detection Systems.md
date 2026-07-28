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

# Fraud Detection Systems

## Connections

### [[Case Management System]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing the response (Detect/Respond) obligations, understand that fraud detection outputs feed directly into the Case Management System: detection generates suspicious-activity alerts, and the Case Management System is mandated to 'record and monitor suspected fraud alerts' and act as the database tracking each case from initial alert to resolution. The two are sequential links in the same obligation chain — detection identifies, case management manages the response. Conclude that gaps in one undermine the other, and that a Member Organisation must show alerts raised by detection systems are captured, allocated and tracked within the Case Management System rather than handled ad hoc.
- **Grounding — this node (Page 46 / 5.1 g):** "Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."
- **Grounding — related node (Page 53 / 6.2 Alert and Case Management):** "The Case Management System should be used to record and monitor suspected fraud alerts, internal and external reports, and case investigations from initial assessment to resolution."

### [[Detect Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing detection obligations, read Fraud Detection Systems as the technology/control specifics mandated within the Detect domain (Section 5), not a discretionary add-on. The Detect domain requires defined, approved and maintained fraud detection standards, and control requirement (g) states those standards 'should include at a minimum' the data sources, controls, and systems/technology used to detect fraud. The consequence: a reviewer should confirm detection systems are documented within the detection standards and justified against the Fraud Risk Assessment, and should not accept detection tooling that lacks the stated rationale and minimum content.
- **Grounding — this node (Page 46 / 5.1(g)):** "Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."
- **Grounding — related node (Page 45 / Section 5.1):** "Member Organisations should have defined, approved, implemented and maintained fraud detection standards which should be aligned to the fraud risks impacting the organisation and its customers."

### [[IT Governance Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating changes to fraud detection systems, note that the Counter-Fraud Framework subordinates configuration changes to SAMA's IT Governance Framework: system configuration changes 'should follow the System Change Management Principles and Control Requirements in SAMA's Information Technology Governance Framework.' The detection-systems obligation therefore cannot be satisfied by the fraud text alone — the governing change-control regime sits in a separate SAMA instrument. Conclude that any assessment of detection-system controls must cross-reference the IT Governance Framework's change-management requirements, and adjustments to detection thresholds or rules inherit those governance obligations.
- **Grounding — this node (Page 24):** "Configuration changes should follow the System Change Management Principles and Control Requirements in SAMA's Information Technology Governance Framework."
- **Grounding — related node (Page 7 / 1.3 Scope):** "The Framework should be implemented in conjunction with other SAMA frameworks ... which should be referred to for specific ... related requirements."

### [[Intelligence Monitoring]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When evaluating a firm's Detect and Prevent domains, treat fraud detection systems and Intelligence Monitoring as feeding each other rather than as siloed functions: newly emerging typologies identified by detection systems are an explicit input into Intelligence Monitoring, and Intelligence Monitoring insights are in turn used to periodically review detection scenarios and parameters. The standard textually links these (4.1.1(e)(2) names detection systems as a threat source; page 49 requires scenario review in view of Intelligence Monitoring insights). Conclude that a firm should be able to demonstrate this two-way flow; static detection rules untouched by intelligence, or intelligence that ignores detection output, indicate a control weakness.
- **Grounding — this node (Page 46 / 5.1(g)(1)):** "Data sources used to inform detection of suspicious activity and fraud ... external databases"
- **Grounding — related node (Page 27 / 4.1.1(e)(2)):** "New and emerging fraud typologies identified by fraud detection systems, fraud investigators or the Co[unter-Fraud Department]"

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
