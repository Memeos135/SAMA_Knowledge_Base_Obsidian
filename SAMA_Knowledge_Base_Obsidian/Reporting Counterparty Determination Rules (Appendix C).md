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

# Reporting Counterparty Determination Rules (Appendix C)

## Connections

### [[Internal Unique Trade ID (Item 14)]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding which party bears the KSA reporting obligation and therefore who assigns the trade identifier, read Appendix C's counterparty-determination rules together with the Internal Unique Trade ID field. Appendix C fixes who is the 'reporting counterparty' (e.g. the financial counterparty against a non-financial one; the local financial counterparty against an international counterparty or CCP), and that reporting counterparty is the entity that generates and populates item 14. A reviewer should conclude that identifier responsibility follows the reporting obligation: the party identified under Appendix C must ensure the Internal Unique Trade ID is generated and stays consistent across all life-cycle reports, since it cannot be modified or corrected.
- **Grounding — this node (Page 57 / Appendix C):** "the financial counterparty of the transaction shall be responsible of submitting the transaction report... the local financial counterparty shall be subject to the local reporting obligation"
- **Grounding — related node (Page 54 / Item 14):** "table 2 item 14 “Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”. The “Internal unique trade ID” cannot be subject to modification."

#graphify/document #graphify/EXTRACTED #community/OTC_Derivative_Trade_Reporting #graphify/enriched
