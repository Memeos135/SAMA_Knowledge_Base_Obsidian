---
source_file: "markdown/SAMA_EN_2340_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Covered Bonds

## Connections

### [[Large Exposure (LEX) Rules for Banks]] — `references` [EXTRACTED]
- **What this link tells you:** When assigning an exposure value to covered bond holdings for LEX purposes, do not default to the 100% nominal value — Appendix VIII permits a reduced value of no less than 20% only if strict conditions are met. The Rules define covered bonds and set the eligibility tests (qualifying underlying asset pool, at least 10% over-collateralisation, LTV thresholds for RRE/CRE), and identify the issuing bank as the counterparty to which the value is assigned. Conclude that the preferential 20% treatment is conditional and must be justified against every listed criterion; failing any condition, the full 100% nominal value applies against the LEX limit.
- **Grounding — this node (Page 33 / Appendix VIII):** "A covered bond satisfying the conditions set out in the next paragraph may be assigned an exposure value of no less than 20% of the nominal value... Other covered bonds must be assigned an exposure value equal to 100%"
- **Grounding — related node (Page 18 / Section 6):** "the banks shall also meet the following additional requirements... report all exposures net of amounts reduced by eligible CRM techniques."

### [[Level 2 Assets]] — `semantically_similar_to` [INFERRED]
- **What this link tells you:** These two concepts *appear* related only at a surface level — both are prudential asset classifications carrying haircuts and preferential treatment — but they sit in different regimes and serve different purposes. 'Covered bonds' in Appendix VIII of the LEX Rules concern exposure-value assignment for large-exposure (concentration) limits, whereas 'Level 2 assets' in the LCR document concern the composition and 40% cap of a bank's high-quality liquid asset stock for liquidity coverage. Treat this as a thematic lead, not an operative link: do not assume covered-bond eligibility under LEX affects HQLA/Level 2 classification, and verify each regime's own criteria independently before relying on any overlap.
- **Grounding — this node (Page 33 / Appendix VIII):** "A covered bond ... may be assigned an exposure value of no less than 20% of the nominal value of the bank's covered bond holding."
- **Grounding — related node (Page 12):** "'Level 1' assets can be included without limit, while 'Level 2' assets can only comprise up to 40% of the total ... stock."
- **Caveat:** Inferred/semantic link across two different regimes (large-exposure limits vs. LCR liquidity). No cross-reference exists between them in the provided text; do not treat as an operative connection.

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
