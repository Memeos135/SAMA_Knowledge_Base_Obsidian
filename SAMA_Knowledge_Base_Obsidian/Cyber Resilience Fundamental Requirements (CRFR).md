---
source_file: "markdown/SAMA_EN_3726_VER1.md"
type: "document"
community: "Aggregation Business Continuity"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Cyber Resilience Fundamental Requirements (CRFR)

## Connections

### [[Business Continuity Management Framework (referenced by CRFR)]] — `cites` [EXTRACTED]
- **What this link tells you:** When applying the CRFR to a sandbox entity, note that its Resilience domain (BCP/DRP and backup/restoration controls) draws its business-continuity concepts from the BCM/ISO 22301 lineage cited in the CRFR glossary rather than being self-defined. The CRFR glossary sources 'Business Continuity' and 'BCM' to ISO 22301, and its section 3.3 imposes BCP and DRP obligations expressly. You should conclude that CRFR resilience controls are the binding requirements for in-scope sandbox entities, with the BCM definitions supplying the meaning of the continuity terms they use.
- **Grounding — this node (SAMA_EN_3726 Page 9 / 3.3 Resilience):** "The Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP) should be defined, approved, communicated, implemented and periodically reviewed"
- **Grounding — related node (SAMA_EN_3726 Page 10 / Appendix A Glossary):** "Business Continuity Management (BCM) ... Source: ISO 22301:2012 - Business continuity management systems — Requirements"

### [[Cyber Security Framework (referenced by CRFR)]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing a sandbox entity's cyber obligations, treat the CRFR as a scaled-down onramp that points back to SAMA's fuller Cyber Security Framework rather than as a self-contained regime. The control sections carry explicit 'Ref. to other SAMA Framework(s)' pointers (e.g. Event Management, Identity and Access Management, Application Security), signalling that graduating entities are expected to migrate toward the CSF's more detailed controls. For a compliance decision, conclude that meeting CRFR controls is a minimum baseline for sandbox stages and check the corresponding CSF control domains before treating an entity as fully compliant for licensing.
- **Grounding — this node (Page 3 / Section 1 Introduction):** "SAMA developed the Cyber Resilience Fundamental Requirements ... specifically intended for entities that are recently established and are in the early stages"
- **Grounding — related node (Page 7 / Page 9 (Control Requirements)):** "Ref. to other SAMA Framework(s) ... Cyber Security Framework - 3.3.14 Cyber Security Event Management - 3.3.5 Identity and Access Management"

### [[Cyber Security Leadership and Governance]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which cyber obligations bind a sandbox entity's board and senior management, note that 'Cyber Security Leadership and Governance' is one of the CRFR's three structural domains and carries enforceable control requirements (e.g. establishing a governance structure, approving policies, running risk assessments). The document names this domain in its structure (Section 2.1) and then populates it with numbered controls at 3.1.x, so the governance obligations flow directly from the framework's own architecture. For a compliance decision, conclude that governance and board-level accountability are in-scope CRFR requirements, not optional guidance, and that failure here can support SAMA prohibiting sandbox graduation/licensing.
- **Grounding — this node (Page 5 / Section 2.1 Structure):** "The Fundamental Requirements is structured around four domains, including: Cyber Security Leadership and Governance"
- **Grounding — related node (Page 7 / Control 3.1.1):** "Entities should develop a robust Cyber Security Governance structure that is supported with appropriate resources to oversee and control overall approach to cyber security."

### [[Cyber Security Operations and Technology]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the technical controls a sandbox entity must meet, note that 'Cyber Security Operations and Technology' is a named CRFR domain populated with concrete, testable obligations — encryption, periodic vulnerability assessments, and penetration testing at least twice yearly. These flow from the framework's own structure (Section 2.1) into the numbered 3.2.x controls, making them mandatory baseline requirements, not aspirational statements. For a compliance decision, conclude that operational/technical shortfalls (e.g. failing to run PT after a critical change) are demonstrable non-compliance that can block sandbox graduation or licensing.
- **Grounding — this node (Page 5 / Section 2.1 Structure):** "The Fundamental Requirements is structured around four domains, including: ... Cyber Security Operations and Technology"
- **Grounding — related node (Page 8 / Control 3.2.6):** "Entities should conduct penetration testing (PT) twice a year as a minimum or after major/critical change to comprehensively evaluate its cyber security defense capability."

### [[Entities (early-stage)]] — `implements` [EXTRACTED]
- **What this link tells you:** When determining who bears the CRFR obligations, note the framework is expressly addressed to and imposed upon early-stage/sandbox 'Entities', so its control requirements ('Entities should...') are the actor for each obligation. The CRFR sets mandatory requirements for entities within scope and conditions sandbox graduation/licensing on demonstrating compliance, while requiring entities to run their own risk assessments. A reader should conclude that these obligations attach to the sandbox entity as licensee-candidate, and that failure to comply can block graduation or a license request.
- **Grounding — this node (Page 4 / section 1.4):** "In the event that an entity is not able to demonstrate compliance with the Fundamental Requirements, SAMA reserves the right to prohibit the sandboxing graduation/license request of the entity."
- **Grounding — related node (Page 7 / section 3.1):** "Entities should develop a robust Cyber Security Governance structure that is supported with appropriate resources to oversee and control overall approach to cyber security."

### [[NISTIR 7298r3 Glossary]] — `cites` [EXTRACTED]
- **What this link tells you:** When interpreting defined terms in the CRFR (e.g. 'Audit', 'Availability', 'Cyber security incident'), read them against their cited external source rather than assuming a SAMA-specific meaning, because the glossary expressly attributes these definitions to NISTIR 7298r3. This matters where a control's scope turns on a defined term — the enforceable obligation is only as broad as the imported definition. For a compliance decision, use the NIST-sourced definitions to fix the boundaries of each control, but note SAMA remains 'solely responsible' for authoritative interpretation, so the citation informs meaning without displacing SAMA's interpretive authority.
- **Grounding — this node (Page 4 / Section 1.5 Interpretation):** "SAMA, as the owner of the Fundamental Requirements, is solely responsible for providing interpretations of the principles and control requirements"
- **Grounding — related node (Page 10-11 / Appendix A Glossary):** "Availability Ensuring timely and reliable access to and use of information. Source: NISTIR 7298r3 Glossary of Key Information Security Terms"

### [[Resilience (CRFR)]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the mandatory scope of the CRFR for a sandbox entity, treat 'Resilience' as one of the framework's constituent domains rather than an optional add-on. The CRFR document itself defines its structure around four domains including Resilience, and its control requirements are numbered within these domains and stated as mandatory for in-scope entities. A reader should conclude that demonstrating compliance for sandbox graduation/licensing requires satisfying the Resilience domain controls, not only governance and operations controls.
- **Grounding — this node (Page 5 / section 2.1):** "The Fundamental Requirements is structured around four domains, including: Cyber Security Leadership and Governance; Cyber Security Operations and Technology; and Resilience."
- **Grounding — related node (Page 6 / section 2.2):** "the fundamental requirements sets the essential cyber security and resilience mandatory requirements for entities that are within the scope of applicability."

### [[SAMA Regulatory Sandbox Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When advising a firm entering SAMA's Regulatory Sandbox, treat CRFR compliance as a gating condition for graduation/licensing rather than a parallel obligation, because the CRFR was purpose-built for early-stage sandbox entities and expressly ties enforcement to the sandbox pathway. The Introduction links the two — the November 2019 sandbox framework and the CRFR developed for entities in early stages — and Section 1.4 gives SAMA the power to prohibit graduation for non-compliance. For a compliance decision, conclude that inability to demonstrate CRFR compliance is a direct sandbox-exit risk, so cyber readiness must be evidenced before requesting graduation or a license.
- **Grounding — this node (Page 4 / Section 1.4 Compliance):** "In the event that an entity is not able to demonstrate compliance with the Fundamental Requirements, SAMA reserves the right to prohibit the sandboxing graduation/license request of the entity."
- **Grounding — related node (Page 3 / Section 1 Introduction):** "SAMA has designed a Regulatory Sandbox which welcomes local as well as international firms wishing to test new digital solutions in a 'live' environment"

#graphify/document #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
