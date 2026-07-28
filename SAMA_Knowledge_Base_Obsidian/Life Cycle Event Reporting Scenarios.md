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

# Life Cycle Event Reporting Scenarios

## Connections

### [[Action Type Field (Item 53)]] — `references` [EXTRACTED]
- **What this link tells you:** When checking whether a life-cycle report was filed correctly, verify the Action Type (item 53) value against the specific scenario it belongs to, because each scenario prescribes a mandatory action-type code (M for modification/notional change, E for erroneous report, C for novation-termination and early termination). The scenarios are the enforceable mapping between a real event and the code that must populate item 53. A compliance reviewer should conclude that using the wrong action-type value is itself a reporting defect, and that certain codes carry additional field constraints (e.g. item 14 Internal unique trade ID must coincide with a previously reported ID and cannot be modified).
- **Grounding — this node (Page 54):** "List of life cycle events reporting scenarios for OTC derivative transactions"
- **Grounding — related node (Page 54-55 / Item 53):** "a Modification report (table 2 item 53 “Action type” populated with “M”)... submit an error report (table 2 item 53 “Action type” populated with the value “E”)"

### [[Internal Unique Trade ID (Item 14)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing any subsequent life-cycle report (modification, error, early termination, notional change), confirm that item 14 Internal Unique Trade ID exactly matches the originally reported code, because every scenario requires this field to be 'fully coincident' with a previously reported ID and prohibits modifying or correcting it. The Internal Unique Trade ID is the key that links each business event back to the original trade record. A reviewer should conclude that a life-cycle report with a mismatched or altered item 14 will not correctly attach to its trade and is a reporting defect, regardless of whether the substantive event was otherwise valid.
- **Grounding — this node (Page 54):** "2. Modifications to the terms of a contract... 5. Submission of an early termination report... 6. Notional increase or decrease"
- **Grounding — related node (Page 54-55 / Item 14):** "“Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”. The “Internal unique trade ID” cannot be subject to correction."

### [[OTC Derivative Life Cycle Events]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a bank must report over the life of a trade, read the Appendix B action-type catalogue (New, Modify, Error, Early Termination, Correction, Valuation, Compression) together with the worked reporting scenarios, because the scenarios show which action type applies to each real event. The two are one obligation chain: the life-cycle-event list defines the permitted values, and the scenarios operationalize when each must be used (e.g. novation = termination 'C' plus a new report). A reviewer should not classify a business event by action type without checking both the definition and its matching scenario to confirm the correct report is filed on T+1.
- **Grounding — this node (Page 54):** "List of life cycle events reporting scenarios for OTC derivative transactions: 1. Submission of a new trade... 2. Modifications to the terms of a contract"
- **Grounding — related node (Page 53 / Appendix B):** "List of reportable life cycle events for OTC derivative transactions: New (N)... Modify (M)... Error (E)... Early Termination (C)... Correction (R)... Valuation update (V)... Compression (Z)"

#graphify/document #graphify/EXTRACTED #community/OTC_Derivative_Trade_Reporting #graphify/enriched
