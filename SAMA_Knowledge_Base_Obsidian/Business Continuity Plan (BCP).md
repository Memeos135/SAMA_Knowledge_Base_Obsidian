---
source_file: "markdown/SAMA_EN_3709_VER1.md"
type: "concept"
community: "Aggregation Business Continuity"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Business Continuity Plan (BCP)

## Connections

### [[BCP and DRP Testing]] — `references` [EXTRACTED]
- **What this link tells you:** When judging BCP compliance, note that having a defined BCP is not sufficient — section 2.9 imposes a separate, enforceable obligation to test it, requiring BCP simulation exercises at least once a year to demonstrate the plan actually works and that staff and third parties can execute it. The testing requirement operationalizes and validates the BCP obligation in section 2.5. A reader should conclude that both an approved BCP and documented annual test results are needed to evidence conformity; an untested plan leaves a compliance gap even if fully drafted.
- **Grounding — this node (Page 10 / section 2.5):** "A BCP should be defined, approved, implemented and maintained in readiness for use during disruptive incidents"
- **Grounding — related node (Page 13 / section 2.9.1):** "The Member Organization should periodically conduct BCP simulation test exercises ("at least once a year")"

### [[Business Continuity Management Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping continuity obligations under SAMA circular 3709, treat the Business Continuity Plan (BCP) as a mandatory component the framework requires each Member Organization to define, approve, implement and maintain — not an optional deliverable. The framework's control considerations set the BCP as the operational plan enabling continued delivery of 'important and urgent activities' at a pre-defined level during disruption, and the framework mandates annual BCP simulation testing. A compliance reviewer should confirm the BCP exists, is board/committee-approved, and is exercised at least yearly, because its absence is a direct breach of the mandatory framework, not a best-practice gap.
- **Grounding — this node (Page 10 / 2.6):** "A BCP should be defined, approved, implemented and maintained in readiness for use during disruptive incidents, to enable the Member organization to continue delivering its important and urgent activities"
- **Grounding — related node (Page 5):** "All Member Organizations are required to comply with these requirements and integrate it formally in their BCM program."

### [[Business Impact Analysis & Risk Assessment]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's BCP meets SAMA's BCM Framework, do not evaluate the plan in isolation from the BIA/RA — the two are directly dependent, because the BIA/RA fixes the prioritized activities and the RTOs, RPOs and MAO that the BCP must be built to meet. Section 2.4 requires the BIA to determine recovery objectives, and section 2.5 requires the BCP to continue critical activities 'within predetermined recovery objectives (RTO, RPO and MAO).' A compliance conclusion should therefore check that the BCP's recovery targets trace back to the endorsed BIA/RA results; a BCP with objectives inconsistent with the BIA is non-conforming.
- **Grounding — this node (Page 10 / section 2.5):** "A process to continue the critical activities within predetermined recovery objectives (RTO, RPO and MAO)"
- **Grounding — related node (Page 9 / section 2.4):** "The recovery time objectives (RTOs), recovery point objectives (RPOs) and maximum Acceptable Outage (MAO)"

### [[Resilience (CRFR)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are advising an entity in SAMA's regulatory sandbox / early-stage FinTech population, note that the BCP obligations in the full BCM Framework and the Resilience domain of the Cyber Resilience Fundamental Requirements (CRFR) address the same continuity-of-service concern but apply to different populations and at different levels of rigor. The CRFR is deliberately a lighter, risk-based mandatory baseline for recently established entities, whereas the BCM Framework sets the fuller Member Organization program. Determine which instrument governs your entity by its applicability scope before assuming BCM-level BCP detail applies; sandbox participants are subject to CRFR self-assessment rather than the full BCM control set.
- **Grounding — this node (Page 10 / section 2.5):** "A BCP should be defined, approved, implemented and maintained in readiness for use during disruptive incidents"
- **Grounding — related node (Page 5-6 / section 2):** "the fundamental requirements sets the essential cyber security and resilience mandatory requirements for entities that are within the scope of applicability"
- **Caveat:** The link is a thematic cross-regime overlap (continuity/resilience); confirm each instrument's applicability scope to determine which BCP standard binds a given entity.

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
