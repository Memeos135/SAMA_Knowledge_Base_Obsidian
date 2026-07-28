---
source_file: "markdown/SAMA_EN_3837_VER1.md"
type: "document"
community: "Aggregation Business Continuity"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Cyber Security Framework (CSF)

## Connections

### [[Cyber Security Framework (referenced by CRFR)]] — `references` [INFERRED]
- **What this link tells you:** The CRFR appears to point back to SAMA's fuller Cyber Security Framework via a 'Ref. to other SAMA Framework' note, suggesting the CRFR is a lighter baseline that expects entities to look to the CSF for the more developed control set. This is inferred: the CRFR page shows the cross-reference marker but the provided text does not explicitly name the CSF document as the referent. A reader should treat the CSF as the likely companion/senior instrument for entities graduating beyond the sandbox, but should confirm the exact reference in the CRFR primary text before assuming CSF controls are incorporated by reference.
- **Grounding — this node (Page 10 / section 2.4):** "The cyber security maturity model distinguishes 6 maturity levels ... a Member Organization must first meet all criteria of the preceding maturity levels."
- **Grounding — related node (Page 7 / section 3.1):** "Ref. to other SAMA Framework"
- **Caveat:** INFERRED: the CRFR excerpt shows only a generic 'Ref. to other SAMA Framework' marker and does not verbatim name the CSF. Confirm the specific referenced framework in the CRFR source before relying on incorporation.

### [[Cyber Security Leadership and Governance Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping who is accountable for cyber security within a Member Organization, start from the Leadership and Governance domain, because the CSF places ultimate responsibility on the Board and assigns defined roles to senior management and the CISO. The policy must include 'a statement of the board's intent' and 'a definition of general and specific responsibilities for cyber security.' For a compliance decision, conclude that governance gaps (unassigned roles, no board endorsement) are direct CSF non-compliance, not merely best-practice shortfalls.
- **Grounding — this node (Page 15 / 3.1.4):** "The Board of Directors has the ultimate responsibility for cyber security"
- **Grounding — related node (Page 15 / 3.1.4 Roles and Responsibilities):** "Responsibilities to implement, maintain, support and promote cyber security should be defined throughout the Member Organization"

### [[Cyber Security Maturity Model]] — `references` [EXTRACTED]
- **What this link tells you:** When judging whether a firm meets the CSF, do not treat control existence as pass/fail; measure against the CSF's six-level maturity model, because SAMA assesses compliance by maturity level and requires all preceding levels be met before claiming a higher one. Controls that are 'not fully defined' or applied inconsistently sit at levels 0-2 and fall short of the level 3 'defined, approved and implemented' expectation. For a compliance decision, conclude that informal or undocumented controls will not satisfy SAMA's maturity assessment even if the control technically operates.
- **Grounding — this node (Page 10 / 2.4):** "In order to achieve levels 3, 4 or 5, a Member Organization must first meet all criteria of the preceding maturity levels"
- **Grounding — related node (Page 10 / 2.4):** "The cyber security maturity model distinguishes 6 maturity levels (0, 1, 2, 3, 4 and 5)"

### [[Cyber Security Operations and Technology Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping technical safeguards for information assets, look to the Operations and Technology domain, which the CSF invokes as the layer where policy translates into implemented controls. The CSF requires senior management to ensure 'standards, processes and procedures reflect security requirements' and the CISO to develop the 'cyber security architecture.' For a compliance decision, conclude that operational and technical controls must trace back to approved policy and architecture, and gaps here are assessed within the same maturity framework rather than exempted.
- **Grounding — this node (Page 16 / 3.1.4):** "ensuring that standards, processes and procedures reflect security requirements"
- **Grounding — related node (Page 15 / 3.1 cyber security policy):** "information is protected in terms of cyber security requirements, in line with the risk appetite"

### [[Cyber Security Risk Management and Compliance Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding how cyber risks may be treated or accepted, apply the Risk Management and Compliance domain, because the CSF mandates a defined risk management process aligned with enterprise risk management and subject to periodic review and audit. Critically, any accepted risk must be within risk appetite, reported to the cyber security committee, and 'does not contradict SAMA regulations' — so risk acceptance cannot be used to waive a SAMA requirement. For a compliance decision, conclude that risk-acceptance sign-offs are bounded: they cannot override mandatory regulatory controls.
- **Grounding — this node (Page 21 / 3.2 control considerations):** "the accepted cyber security risk does not contradict SAMA regulations"
- **Grounding — related node (Page 19 / 3.2):** "A cyber security risk management process should be defined, approved and implemented, and should be aligned with the Member Organization's enterprise risk management process"

### [[Member Organization]] — `implements` [EXTRACTED]
- **What this link tells you:** When identifying who bears the CSF's obligations, the Member Organization is the duty-holder: SAMA owns and mandates the Framework, but the Framework text places adoption, implementation and continued compliance squarely on the Member Organization. Every 'should' in the CSF — strategy, policy, board responsibility, budget allocation — resolves to an enforceable expectation on that entity. For compliance decisions, conclude that responsibility cannot be delegated away (including to cloud providers) and that the entity remains liable for compliance even while an update request is pending.
- **Grounding — this node (Page 7 / 1.5):** "The framework is mandated by SAMA ... The Member Organizations are responsible for adopting and implementing the Framework."
- **Grounding — related node (Page 14):** "The board of the Member Organization should allocate sufficient budget to execute the required cyber security activities."

### [[SAMA (CSF Owner)]] — `references` [EXTRACTED]
- **What this link tells you:** When resolving ambiguity in the CSF's principles or control considerations, note that SAMA is the sole authority for interpretation, ownership and updates — a Member Organization cannot self-interpret away an obligation. This matters because risk-acceptance decisions under the CSF must not contradict SAMA regulations, and update requests must be formally submitted to and approved by SAMA before the Framework changes. For compliance decisions, conclude that interpretive disputes and requested deviations should be escalated to SAMA, and that pending requests do not suspend the existing obligation.
- **Grounding — this node (Page 21):** "the accepted cyber security risk does not contradict SAMA regulations"
- **Grounding — related node (Page 7 / 1.6):** "SAMA, as the owner of the Framework, is solely responsible for providing interpretations of the principles, objectives and control considerations"

### [[SAMA Business Continuity Minimum Requirements (referenced)]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's cyber security obligations extend to resilience and continuity, treat business continuity as an in-scope requirement rather than a separate discipline, because the CSF expressly requires that 'cyber security is reflected in business continuity management.' The CSF also defines 'business continuity' in its glossary (per ISO 22301) and applies its controls to all information assets. For a compliance decision, conclude that a firm cannot demonstrate CSF compliance while excluding continuity considerations from its cyber security program.
- **Grounding — this node (Page 15 / 3.1 cyber security policy):** "cyber security is reflected in business continuity management"
- **Grounding — related node (Page 46 (glossary)):** "Business continuity — the capability of an organization to continue delivery of IT and business services at acceptable predefined levels following a disruptive incident"

### [[SAMA Cyber Security Framework (referenced)]] — `references` [INFERRED]
- **What this link tells you:** If you are scoping an aggregation entity's cybersecurity obligations, the CSF referenced at clause 2.4.3 of the Aggregation Instructions appears to be the same SAMA Cyber Security Framework document (SAMA_EN_3837), meaning the entity's platform-security and breach-notification duties should be read against that framework's control set and maturity model rather than as free-standing requirements. The Instructions state they 'shall not prejudice' the CSF and separately require the entity to strengthen platform cybersecurity, so the two operate cumulatively. Because this link is inferred from a name match rather than an explicit citation, verify in the primary CSF text that its stated scope ('Member Organizations') captures aggregation-activity licensees before relying on it as the governing standard.
- **Grounding — this node (Page 15):** "The cyber security policy should include... a definition of general and specific responsibilities for cyber security."
- **Grounding — related node (Page 3 / clause 2.4.3; Page 6 / clause 8.1):** "These Instructions shall not prejudice the provisions contained in relevant laws and instructions... The Cyber Security Framework issued by SAMA."
- **Caveat:** Link inferred from title match; the CSF's 'Member Organization' scope may not expressly enumerate aggregation-activity licensees — confirm applicability in the primary CSF text.

### [[SAMA Cyber Security Framework (referenced)]] — `references` [INFERRED]
- **What this link tells you:** This link appears to connect the BCM Framework's reference to 'the SAMA Cyber Security Framework' with the actual CSF document (SAMA_EN_3837). If confirmed, the CSF is the concrete instrument the BCM Framework points to for cyber controls, meaning its maturity model and control considerations (e.g. that cyber security be reflected in business continuity management) are the operative source. Before relying on this, verify that 3837 is the same version/framework the BCM note intends, since the BCM text names the framework only generically.
- **Grounding — this node (SAMA_EN_3837 Page 15 / 3.1.3):** "cyber security requirements that ensure: ... 8. cyber security is reflected in business continuity management."
- **Grounding — related node (Page 12 / section 2.7 note):** "please refer to the SAMA - Cyber Security Framework."
- **Caveat:** Relation is INFERRED — the BCM note cites the CSF generically; confirm document identity and version before treating 3837 as the referenced framework.

### [[Third Party Cyber Security Domain]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping a Member Organization's cyber security obligations, do not treat outsourcing and cloud arrangements as outside the CSF's reach — the Framework expressly extends its control considerations into third-party relationships, requiring SAMA approval before using cloud services and mandating contractual cyber security requirements, data-location, segregation and audit rights. This makes the Third Party Cyber Security domain a substantive component of the CSF, not an optional annex. For compliance decisions, conclude that vendor and cloud contracts must carry the CSF controls through to the provider, and verify prior SAMA approval where data leaves the Kingdom.
- **Grounding — this node (Page 15):** "cyber security requirements that ensure ... compliance with regulatory and contractual obligations are being met"
- **Grounding — related node (Page 38):** "the Member Organization should obtain SAMA approval prior to using cloud services or signing the contract with the cloud provider"

#graphify/document #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
