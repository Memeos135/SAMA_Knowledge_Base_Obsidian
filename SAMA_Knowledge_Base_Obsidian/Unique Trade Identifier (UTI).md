---
source_file: "markdown/SAMA_EN_10592_VER1.md"
type: "concept"
community: "OTC Derivatives Reporting"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/OTC_Derivatives_Reporting
  - graphify/enriched
---

# Unique Trade Identifier (UTI)

## Connections

### [[Section A Trade Reporting Requirements|Section A: Trade Reporting Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's TR reporting obligations, treat the UTI/Internal Unique Trade ID rules as an integral part of Section A's compulsory reporting duty, not a separate technical annex. Section A requires reporting of each reportable transaction and its life-cycle events on the T+1 timeline, and the identifier scheme determines how each contract is uniquely tracked across those events (including 'Linked UTI' referencing on novation for central clearing). A compliance reviewer should conclude that a Section A report is not complete or compliant unless the trade carries a valid unique identifier per the UTI rules, including the provisional-blank/modification workaround where a foreign generating entity has not yet supplied the UTI.
- **Grounding — this node (Page 25-26 / Item 15):** "only one trade identifier should be applicable to every single OTC derivative contract that is reported to SATR and that the same trade identifier is not used for any other derivative contract"
- **Grounding — related node (Page 8 / para 16-17):** "open a new one with the reference to the old trade identifier in the field “Linked UTI”... reports to the SAMA authorised TR reportable transactions... before 23:59:59 of the next business day (T+1)"

#graphify/concept #graphify/EXTRACTED #community/OTC_Derivatives_Reporting #graphify/enriched
