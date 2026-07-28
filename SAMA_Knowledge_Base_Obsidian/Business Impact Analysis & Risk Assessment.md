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

# Business Impact Analysis & Risk Assessment

## Connections

### [[Business Continuity Management Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's continuity program is defensible, check that the BIA and Risk Assessment were performed first, because the framework makes them the foundational inputs that drive RTOs, RPOs, MAO and the prioritized list of critical activities feeding the BCP and DRP. Section 2.4 mandates BIA/RA for all relevant activities and requires the BCM committee to endorse the prioritized list and defined recovery objectives. A reviewer should conclude that a BCP or DRP built without documented, committee-endorsed BIA/RA results is unsupported under the framework and its recovery targets cannot be relied upon.
- **Grounding — this node (Page 9):** "The BCM committee should endorse the prioritized list, BIA results, RA and the defined RTOs, RPOs and MAOs."
- **Grounding — related node (Page 8 / 2.4):** "The Member Organization should perform a business impact analysis and risk assessment for all relevant activities to determine the business continuity"

### [[Business Continuity Plan (BCP)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's BCP meets SAMA's BCM Framework, do not evaluate the plan in isolation from the BIA/RA — the two are directly dependent, because the BIA/RA fixes the prioritized activities and the RTOs, RPOs and MAO that the BCP must be built to meet. Section 2.4 requires the BIA to determine recovery objectives, and section 2.5 requires the BCP to continue critical activities 'within predetermined recovery objectives (RTO, RPO and MAO).' A compliance conclusion should therefore check that the BCP's recovery targets trace back to the endorsed BIA/RA results; a BCP with objectives inconsistent with the BIA is non-conforming.
- **Grounding — this node (Page 9 / section 2.4):** "The recovery time objectives (RTOs), recovery point objectives (RPOs) and maximum Acceptable Outage (MAO)"
- **Grounding — related node (Page 10 / section 2.5):** "A process to continue the critical activities within predetermined recovery objectives (RTO, RPO and MAO)"

### [[IT Disaster Recovery Plan (DRP)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When reviewing an IT Disaster Recovery Plan, check that it is explicitly derived from the BIA/RA rather than developed independently — section 2.6 requires the IT DRP to be defined and maintained 'in alignment with business impact analysis,' and even requires third-party continuity contracts to align with BIA and RA outcomes. The BIA/RA supplies the recovery objectives and prioritized critical systems that the DRP must restore. A reader should therefore conclude that a DRP whose recovery scope or timelines do not trace to the endorsed BIA/RA (including RTO/RPO/MAO) is non-conforming, and that outsourcing arrangements must reflect those same BIA-derived requirements.
- **Grounding — this node (Page 9 / section 2.4):** "The recovery time objectives (RTOs), recovery point objectives (RPOs) and maximum Acceptable Outage (MAO)"
- **Grounding — related node (Page 11 / section 2.6):** "An IT DRP to recover and restore technology services and infrastructure components ... should be defined, approved, implemented and maintained in alignment with business impact analysis."

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
