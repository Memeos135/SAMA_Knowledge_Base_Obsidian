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

# IT Disaster Recovery Plan (DRP)

## Connections

### [[BCP and DRP Testing]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's IT DRP obligation is actually discharged, don't treat the plan's existence and its testing as one requirement — the BCM Framework imposes them as distinct, cumulative duties. Section 2.6/2.7 requires the IT DRP to be defined, approved, implemented and maintained, while section 2.9 separately mandates executing a DR test 'combined with BCP' at least once a year and evaluating IT DR infrastructure readiness. You should conclude that a documented DRP alone is non-compliant absent the periodic, evidenced testing cycle described in 2.9.2.
- **Grounding — this node (Page 11 / section 2.6):** "An IT DRP to recover and restore technology services and infrastructure components ... should be defined, approved, implemented and maintained"
- **Grounding — related node (Page 13 / section 2.9.2):** "The Member Organization should periodically execute a DR test combined with BCP ("at least once a year")"

### [[Business Continuity Management Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing recovery capability, treat the IT Disaster Recovery Plan (DRP) as a mandatory framework component (section 2.6) that must be built in alignment with the BIA and integrated into the overall BCM program, not as a standalone IT deliverable. The framework requires an approved DRP, an alternative data center (whose location needs SAMA approval), equivalent cyber/physical controls, third-party contracts aligned to BIA/RA outcomes, and annual DR testing combined with the BCP. A reviewer should verify the DRP's recovery scope traces to the BIA, that SAMA approval for the alternative site exists, and that accountability for BCM integration sits with the BCM Manager.
- **Grounding — this node (Page 11 / 2.6):** "An IT DRP ... should be defined, approved, implemented and maintained in alignment with business impact analysis."
- **Grounding — related node (Page 5):** "IT Disaster recovery (IT DR) is part of BCM which includes policies, standards, procedures and processes pertaining to resilience, recovery or continuation of technology infrastructure"

### [[Business Impact Analysis & Risk Assessment]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When reviewing an IT Disaster Recovery Plan, check that it is explicitly derived from the BIA/RA rather than developed independently — section 2.6 requires the IT DRP to be defined and maintained 'in alignment with business impact analysis,' and even requires third-party continuity contracts to align with BIA and RA outcomes. The BIA/RA supplies the recovery objectives and prioritized critical systems that the DRP must restore. A reader should therefore conclude that a DRP whose recovery scope or timelines do not trace to the endorsed BIA/RA (including RTO/RPO/MAO) is non-conforming, and that outsourcing arrangements must reflect those same BIA-derived requirements.
- **Grounding — this node (Page 11 / section 2.6):** "An IT DRP to recover and restore technology services and infrastructure components ... should be defined, approved, implemented and maintained in alignment with business impact analysis."
- **Grounding — related node (Page 9 / section 2.4):** "The recovery time objectives (RTOs), recovery point objectives (RPOs) and maximum Acceptable Outage (MAO)"

### [[Resilience (CRFR)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are scoping continuity/recovery obligations across two SAMA instruments, note that the BCM Framework's IT DRP requirement and the CRFR Resilience domain address the same subject matter but bind different populations and carry different consequences. The BCM Framework applies to established Member Organizations (banks and subsidiaries), whereas the CRFR is aimed at newly established sandbox entities, where failure to demonstrate compliance can block sandbox graduation/licensing. You should map an entity to the correct instrument by its status: do not assume BCM Framework controls satisfy CRFR resilience requirements, or vice versa, without checking applicability.
- **Grounding — this node (Page 11 / section 2.6):** "An IT DRP to recover and restore technology services and infrastructure components ... should be defined, approved, implemented and maintained"
- **Grounding — related node (SAMA_EN_3726 Page 5 / section 2.1):** "The Fundamental Requirements is structured around four domains, including: ... and Resilience."
- **Caveat:** Link is a topical correspondence between two separate frameworks with different scopes; verify applicability of each to the entity before relying on either to satisfy the other.

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
