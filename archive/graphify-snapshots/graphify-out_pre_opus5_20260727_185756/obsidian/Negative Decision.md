---
source_file: "markdown/document2.md"
type: "concept"
community: "Credit Information Regulation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Credit_Information_Regulation
  - graphify/enriched
---

# Negative Decision

## Connections

### [[Credit Record]] — `references` [EXTRACTED]
- **Why:** A Negative Decision is defined as any decision made by a member against a consumer based on his/her Credit Record; Article (45) then mandates that when such a decision is taken the member must notify the consumer of the Negative Information in that Credit Record within 7 working days, directly linking the record's content to the member's disclosure obligation.
- **This node (Page 14-15 / Article (45)):** "In case the member has taken a negative decision against the consumer for a cause that is partially or entirely due to any information included in his/her credit record, they shall notify the consumer within 7 working days from the date of taking such decision with the negative…"
- **Related node (Page 7 / Article (17)):** "Companies have the right to maintain the negative information in the consumer credit record for no more than five years from the debt or dispute settlement date."
- **Implication:** Member systems must generate a timestamped adverse-action notice within 7 working days of any credit denial or restriction that was informed by Credit Record content, including the specific Negative Information relied upon and the sourcing company's details, creating an auditable evidence trail per Article (45).

### [[Member]] — `references` [EXTRACTED]
- **Why:** A Member is the entity that takes a Negative Decision against a consumer based on credit record data and bears the mandatory obligation to notify the consumer of that decision within a prescribed timeframe, linking Member conduct directly to consumer-rights triggers.
- **This node (Page 2 / Definitions):** "Negative Decision: Any decision made by a member against a consumer based on his/her credit record."
- **Related node (Page 14 / Article (45)):** "In case the member has taken a negative decision against the consumer for a cause that is partially or entirely due to any information included in his/her credit record, they shall notify the consumer within 7 working days from the date of taking such decision."
- **Implication:** Members must implement a decision-notification workflow that automatically triggers a written consumer notice (including the source company name, address, phone, and a copy of the credit record) within 7 working days of any adverse credit decision, with a timestamped evidence trail for SAMA examination.

#graphify/concept #graphify/EXTRACTED #community/Credit_Information_Regulation #graphify/enriched
