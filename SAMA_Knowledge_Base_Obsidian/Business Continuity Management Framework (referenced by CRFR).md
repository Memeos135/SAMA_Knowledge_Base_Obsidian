---
source_file: "markdown/SAMA_EN_3726_VER1.md"
type: "concept"
community: "Aggregation Business Continuity"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Business Continuity Management Framework (referenced by CRFR)

## Connections

### [[Business Continuity Management Framework]] — `references` [INFERRED]
- **What this link tells you:** This link appears to connect the full BCM Framework (SAMA 3709) with the business-continuity concept as it surfaces in the separate Cyber Resilience Fundamental Requirements (SAMA 3726), which both draw on ISO 22301's BCM definition. The CRFR is a lighter regime 'specifically intended for entities that are recently established and are in the early stages,' so its BCP/DRP requirement is a compressed reference rather than the full framework. Before relying on this, verify which regime applies to your entity: a sandbox/early-stage FinTech under CRFR faces the abbreviated resilience control, whereas banks and Member Organizations remain bound by the full 3709 framework.
- **Grounding — this node (3726 Page 9 / 3.3):** "The Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP) should be defined, approved, communicated, implemented and periodically reviewed"
- **Grounding — related node (Page 5 / 1.1):** "SAMA has developed a Business Continuity Management (BCM) framework for member organizations"
- **Caveat:** Relationship is INFERRED: the two documents share the ISO 22301-based BCM concept but are distinct instruments applying to different populations; confirm applicable regime in the primary texts before treating them as equivalent.

### [[Cyber Resilience Fundamental Requirements (CRFR)]] — `cites` [EXTRACTED]
- **What this link tells you:** When applying the CRFR to a sandbox entity, note that its Resilience domain (BCP/DRP and backup/restoration controls) draws its business-continuity concepts from the BCM/ISO 22301 lineage cited in the CRFR glossary rather than being self-defined. The CRFR glossary sources 'Business Continuity' and 'BCM' to ISO 22301, and its section 3.3 imposes BCP and DRP obligations expressly. You should conclude that CRFR resilience controls are the binding requirements for in-scope sandbox entities, with the BCM definitions supplying the meaning of the continuity terms they use.
- **Grounding — this node (SAMA_EN_3726 Page 10 / Appendix A Glossary):** "Business Continuity Management (BCM) ... Source: ISO 22301:2012 - Business continuity management systems — Requirements"
- **Grounding — related node (SAMA_EN_3726 Page 9 / 3.3 Resilience):** "The Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP) should be defined, approved, communicated, implemented and periodically reviewed"

#graphify/concept #graphify/INFERRED #community/Aggregation_Business_Continuity #graphify/enriched
