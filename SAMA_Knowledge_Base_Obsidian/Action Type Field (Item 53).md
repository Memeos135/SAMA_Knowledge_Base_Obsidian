---
source_file: "markdown/SAMA_EN_10593_VER1_0.md"
type: "document"
community: "OTC Derivative Trade Reporting"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/OTC_Derivative_Trade_Reporting
  - graphify/enriched
---

# Action Type Field (Item 53)

## Connections

### [[Life Cycle Event Reporting Scenarios]] — `references` [EXTRACTED]
- **What this link tells you:** When checking whether a life-cycle report was filed correctly, verify the Action Type (item 53) value against the specific scenario it belongs to, because each scenario prescribes a mandatory action-type code (M for modification/notional change, E for erroneous report, C for novation-termination and early termination). The scenarios are the enforceable mapping between a real event and the code that must populate item 53. A compliance reviewer should conclude that using the wrong action-type value is itself a reporting defect, and that certain codes carry additional field constraints (e.g. item 14 Internal unique trade ID must coincide with a previously reported ID and cannot be modified).
- **Grounding — this node (Page 54-55 / Item 53):** "a Modification report (table 2 item 53 “Action type” populated with “M”)... submit an error report (table 2 item 53 “Action type” populated with the value “E”)"
- **Grounding — related node (Page 54):** "List of life cycle events reporting scenarios for OTC derivative transactions"

#graphify/document #graphify/EXTRACTED #community/OTC_Derivative_Trade_Reporting #graphify/enriched
