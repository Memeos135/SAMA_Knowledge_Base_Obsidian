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

# Cyber Security Operations and Technology Domain

## Connections

### [[Cyber Security Framework (CSF)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping technical safeguards for information assets, look to the Operations and Technology domain, which the CSF invokes as the layer where policy translates into implemented controls. The CSF requires senior management to ensure 'standards, processes and procedures reflect security requirements' and the CISO to develop the 'cyber security architecture.' For a compliance decision, conclude that operational and technical controls must trace back to approved policy and architecture, and gaps here are assessed within the same maturity framework rather than exempted.
- **Grounding — this node (Page 15 / 3.1 cyber security policy):** "information is protected in terms of cyber security requirements, in line with the risk appetite"
- **Grounding — related node (Page 16 / 3.1.4):** "ensuring that standards, processes and procedures reflect security requirements"

### [[Cyber Security Operations and Technology]] — `semantically_similar_to` [INFERRED]
- **What this link tells you:** For an entity determining its operations/technology control obligations, the CRFR and the CSF each carry an Operations and Technology domain covering similar subject matter, but they appear to be separate standards scaled to different regulated populations — the CRFR a mandatory baseline for early-stage sandbox entities and the CSF a maturity-assessed regime for Member Organizations. This connection is inferred from topical similarity rather than any citation between the two texts. A reader should not assume CSF-level operational controls or maturity expectations automatically bind a sandbox entity; confirm which document is the applicable instrument for the entity's status.
- **Grounding — this node (Page 10 / section 2.4):** "The cyber security maturity level will be measured with the help of a predefined cyber security maturity model ... 6 maturity levels."
- **Grounding — related node (Page 8 / section 3.2):** "Entities should conduct penetration testing (PT) twice a year as a minimum or after major/critical change to comprehensively evaluate its cyber security defense capability."
- **Caveat:** Relation is INFERRED from shared domain topic; no cross-reference is present and the instruments apply to different entity populations. Verify the governing standard for the entity in question.

### [[SIEM]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating the Operations and Technology domain, note that SIEM is the tooling underpinning the mandated Cyber Security Event Management process (3.3.14) and the threat intelligence process, both of which require a defined, approved, implemented and effectiveness-reviewed process supporting a SOC. SIEM itself is a glossary-defined capability; the enforceable obligation is the event-management/monitoring process it supports, not the acquisition of a named product. Conclude that the compliance test is whether a monitoring process and SOC arrangement exist and are effectiveness-reviewed, with SIEM as one supporting source rather than a standalone requirement.
- **Grounding — this node (Page 33 / 3.3.14):** "The Member Organization should define, approve and implement a security event management process to analyze operational and security loggings and respond to security events."
- **Grounding — related node (Page 55 (glossary)):** "A security information and event management (SIEM) tool is a system that provides the ability to gather security data from information system components"
- **Caveat:** SIEM appears only as a glossary/definition term and as a listed internal source for threat intelligence; the binding obligation is the event-management process, so treat the SIEM link as supporting context rather than an independent requirement.

### [[Secure SDLC]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the Operations and Technology domain's obligations, understand that Secure SDLC / application security controls (section 3.3.6) sit within it as a required, monitored control area rather than a design preference. The domain requires that application cyber security standards be defined, approved, implemented, monitored, and periodically evaluated for effectiveness. Conclude that secure development is a compliance requirement whose evidence of monitoring and effectiveness review is examinable, not an internal engineering choice.
- **Grounding — this node (Page 10 / 2.4):** "Cyber security controls are defined, approved and implemented in a structured and formalized way."
- **Grounding — related node (Page 27 / 3.3.6):** "The Member Organization should define, approve and implement cyber security standards for application systems. The compliance with these standards should be monitored"
- **Caveat:** Node B's context principally shows Application Security (3.3.6) and glossary items; the specific 'Secure SDLC' provision is inferred from the application-security control area rather than a distinct quoted SDLC clause. Verify the precise SDLC control text before relying on it.

### [[Security Operations Center (SOC)]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping who must run continuous security monitoring under the SAMA Cyber Security Framework, treat the SOC as a required component of the Operations and Technology domain's event-management obligations, not an optional add-on. The framework's event-management principle requires a Member Organization to establish 'a designated team responsible for security monitoring (i.e., Security Operations Center (SOC))' with 24x7 resourcing, so SOC capability is how the domain's monitoring/response requirement is discharged. For a compliance assessment, conclude that absence of a functioning SOC (or equivalent) is a gap against the operations/technology control set, and check maturity-level evidence against the framework's maturity model.
- **Grounding — this node (Page 33 / 3.3.14):** "The Member Organization should define, approve and implement a security event management process to analyze operational and security loggings and respond to security events."
- **Grounding — related node (Page 33 / 3.3.14(4)(a)):** "the establishment of a designated team responsible for security monitoring (i.e., Security Operations Center (SOC))"

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
