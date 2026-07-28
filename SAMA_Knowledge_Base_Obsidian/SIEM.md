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

# SIEM

## Connections

### [[Cyber Security Operations and Technology Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating the Operations and Technology domain, note that SIEM is the tooling underpinning the mandated Cyber Security Event Management process (3.3.14) and the threat intelligence process, both of which require a defined, approved, implemented and effectiveness-reviewed process supporting a SOC. SIEM itself is a glossary-defined capability; the enforceable obligation is the event-management/monitoring process it supports, not the acquisition of a named product. Conclude that the compliance test is whether a monitoring process and SOC arrangement exist and are effectiveness-reviewed, with SIEM as one supporting source rather than a standalone requirement.
- **Grounding — this node (Page 55 (glossary)):** "A security information and event management (SIEM) tool is a system that provides the ability to gather security data from information system components"
- **Grounding — related node (Page 33 / 3.3.14):** "The Member Organization should define, approve and implement a security event management process to analyze operational and security loggings and respond to security events."
- **Caveat:** SIEM appears only as a glossary/definition term and as a listed internal source for threat intelligence; the binding obligation is the event-management process, so treat the SIEM link as supporting context rather than an independent requirement.

### [[Security Operations Center (SOC)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating whether a Member Organization's monitoring capability meets the event-management control, read SIEM as the tooling that feeds the SOC function rather than a separate requirement. The framework's glossary defines SIEM as a system that gathers security data 'and presents that data as actionable information,' and lists SIEM among the internal sources supporting threat intelligence and SOC monitoring. For assessment purposes, conclude that a SOC without SIEM-type aggregation is unlikely to satisfy the 24x7 continuous monitoring expectation, but confirm the specific SIEM obligation against the operative control text (glossary definitions are descriptive, not stand-alone mandates).
- **Grounding — this node (Page 55 / Glossary (SIEM)):** "a system that provides the ability to gather security data from information system components and presents that data as actionable information via a single interface"
- **Grounding — related node (Page 35 / 3.3 Control considerations):** "the use of internal sources, such as ... security tooling, Security Information and Event Monitoring (SIEM)"
- **Caveat:** SIEM appears only in glossary/threat-intelligence lists; confirm any direct SIEM obligation against the operative SOC control text.

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
