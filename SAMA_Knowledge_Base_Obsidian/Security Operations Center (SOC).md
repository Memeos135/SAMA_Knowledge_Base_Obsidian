---
source_file: "markdown/SAMA_EN_3837_VER1.md"
type: "concept"
community: "Aggregation Business Continuity"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Security Operations Center (SOC)

## Connections

### [[Cyber Security Event Management]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating whether a Member Organization's event-management controls are adequate, understand that the SOC is the operational function through which event detection and monitoring are expected to be discharged — SOC monitoring is expressly assigned as a CISO responsibility. The Framework lists 'monitoring of the cyber security activities (SOC monitoring)' among the CISO's duties, linking the event-management control domain to a defined operational capability. For a compliance decision, conclude that absence or immaturity of a monitoring/SOC capability undermines the event-management control area; the connection here reflects a functional dependency rather than a formal cross-reference between article numbers.
- **Grounding — this node (Page 16 / 3.1.4 control 4(e)):** "monitoring of the cyber security activities (SOC monitoring)"
- **Grounding — related node (Page 15 / 3.1.3(f)):** "cyber security breaches and suspected cyber security weaknesses are reported"
- **Caveat:** The link is functional/inferred from the CISO's monitoring duties; the excerpts do not show an explicit article cross-reference between event management and SOC, so verify the dedicated event-management section in the primary text.

### [[Indicator of Compromise]] — `references` [EXTRACTED]
- **What this link tells you:** When interpreting the SOC's detection role, indicators of compromise are the signals the SOC is expected to detect and act on, so the two concepts should be read as operationally linked within the framework's incident and threat handling controls. The glossary's incident-management entries and the threat intelligence process (which routes follow-up to the SOC) frame IoCs as inputs to SOC monitoring and response. This connection appears supported by the framework's structure rather than by an explicit single clause naming both, so before relying on it verify the specific SOC/incident-detection control text.
- **Grounding — this node (Page 35 / 3.3.16):** "the action-ability for follow-up (for e.g., SOC, Risk Management)"
- **Grounding — related node (Page 51 / Glossary):** "a predetermined set of instructions or procedures to detect, respond to, and limit consequences of a malicious cyber-attack against an organization's information system(s)"
- **Caveat:** The direct IoC-to-SOC link is inferred from the framework's incident/threat handling structure rather than a single explicit clause; confirm the primary SOC control text before relying on it.

### [[Threat Management]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a Member Organization's obligations under the SAMA Cyber Security Framework, treat the SOC and threat intelligence functions as interdependent rather than standalone controls. The framework's threat intelligence management process (3.3.16) expressly lists the SOC as a recipient for 'action-ability for follow-up', so intelligence outputs are meant to feed SOC operations. In an assessment you should confirm both processes exist, are approved, and are linked — an SOC without an intelligence feed, or intelligence with no operational follow-up channel, would not satisfy the control considerations.
- **Grounding — this node (Page 35 / 3.3.16):** "the relevance of the derived intelligence and the action-ability for follow-up (for e.g., SOC, Risk Management)"
- **Grounding — related node (Page 35 / 3.3.16):** "the use of internal sources, such as ... SIEM, support functions (e.g., Legal, Audit, IT Helpdesk, Forensics, Fraud Management, Risk Management, Compliance)"

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
