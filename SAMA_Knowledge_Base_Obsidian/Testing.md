---
source_file: "markdown/SAMA_EN_11051_VER1.md"
type: "document"
community: "IT & Shariah Governance"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IT__Shariah_Governance
  - graphify/enriched
---

# Testing

## Connections

### [[Quality Assurance]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two sub-domains appear complementary rather than identical, and the distinction matters for who signs off a change: Testing (3.4.5) verifies the change works against approved test cases, while Quality Assurance (3.4.11) requires an independent function to assess quality against business/user requirements before production release. The QA principle expressly demands independent existence and reporting authority, so a reviewer should not treat successful testing as discharging the separate QA obligation. Verify the primary text, as the link is inferred: both are control-requirement sub-domains within System Change Management but no explicit cross-reference between them is quoted.
- **Grounding — this node (Page 30 / 3.4.5):** "All changes should be formally tested and accepted by the concern business users"
- **Grounding — related node (Page 33 / 3.4.11):** "quality assurance process should be defined ... to independently ascertain quality of the changes ... prior moving them to the production environment"
- **Caveat:** Relationship is INFERRED — both are System Change Management sub-domains but the provided text does not explicitly cross-reference QA to Testing; confirm in the primary framework before treating them as a single control.

### [[System Change Management]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing whether a change may lawfully be promoted to production, the testing requirements are not optional add-ons — the framework expressly makes them part of System Change Management (3.4). It mandates minimum testing types (unit, SIT, stress, security, UAT), testing on a separate environment against approved test cases, formal business-user acceptance, and prohibits using production data. Conclude that a change lacking the prescribed testing evidence does not meet the System Change Management control set, so an auditor should verify the test-case documentation and sanitized-data rule are satisfied before deployment.
- **Grounding — this node (Page 30 / 3.4.5):** "All changes to information system should be thoroughly tested on a separate test environment in accordance with the approved test cases"
- **Grounding — related node (Page 30 / 3.4):** "the following types of testing should be considered as part of system change management. unit testing; ... user acceptance testing (UAT)"

#graphify/document #graphify/EXTRACTED #community/IT__Shariah_Governance #graphify/enriched
