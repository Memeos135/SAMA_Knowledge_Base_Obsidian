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

# OTC Derivative Life Cycle Events

## Connections

### [[Life Cycle Event Reporting Scenarios]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a bank must report over the life of a trade, read the Appendix B action-type catalogue (New, Modify, Error, Early Termination, Correction, Valuation, Compression) together with the worked reporting scenarios, because the scenarios show which action type applies to each real event. The two are one obligation chain: the life-cycle-event list defines the permitted values, and the scenarios operationalize when each must be used (e.g. novation = termination 'C' plus a new report). A reviewer should not classify a business event by action type without checking both the definition and its matching scenario to confirm the correct report is filed on T+1.
- **Grounding — this node (Page 53 / Appendix B):** "List of reportable life cycle events for OTC derivative transactions: New (N)... Modify (M)... Error (E)... Early Termination (C)... Correction (R)... Valuation update (V)... Compression (Z)"
- **Grounding — related node (Page 54):** "List of life cycle events reporting scenarios for OTC derivative transactions: 1. Submission of a new trade... 2. Modifications to the terms of a contract"

#graphify/document #graphify/EXTRACTED #community/OTC_Derivative_Trade_Reporting #graphify/enriched
