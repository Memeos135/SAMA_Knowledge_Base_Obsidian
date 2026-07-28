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

# Internal Unique Trade ID (Item 14)

## Connections

### [[Life Cycle Event Reporting Scenarios]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing any subsequent life-cycle report (modification, error, early termination, notional change), confirm that item 14 Internal Unique Trade ID exactly matches the originally reported code, because every scenario requires this field to be 'fully coincident' with a previously reported ID and prohibits modifying or correcting it. The Internal Unique Trade ID is the key that links each business event back to the original trade record. A reviewer should conclude that a life-cycle report with a mismatched or altered item 14 will not correctly attach to its trade and is a reporting defect, regardless of whether the substantive event was otherwise valid.
- **Grounding — this node (Page 54-55 / Item 14):** "“Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”. The “Internal unique trade ID” cannot be subject to correction."
- **Grounding — related node (Page 54):** "2. Modifications to the terms of a contract... 5. Submission of an early termination report... 6. Notional increase or decrease"

### [[Reporting Counterparty Determination Rules (Appendix C)]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding which party bears the KSA reporting obligation and therefore who assigns the trade identifier, read Appendix C's counterparty-determination rules together with the Internal Unique Trade ID field. Appendix C fixes who is the 'reporting counterparty' (e.g. the financial counterparty against a non-financial one; the local financial counterparty against an international counterparty or CCP), and that reporting counterparty is the entity that generates and populates item 14. A reviewer should conclude that identifier responsibility follows the reporting obligation: the party identified under Appendix C must ensure the Internal Unique Trade ID is generated and stays consistent across all life-cycle reports, since it cannot be modified or corrected.
- **Grounding — this node (Page 54 / Item 14):** "table 2 item 14 “Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”. The “Internal unique trade ID” cannot be subject to modification."
- **Grounding — related node (Page 57 / Appendix C):** "the financial counterparty of the transaction shall be responsible of submitting the transaction report... the local financial counterparty shall be subject to the local reporting obligation"

#graphify/document #graphify/EXTRACTED #community/OTC_Derivative_Trade_Reporting #graphify/enriched
