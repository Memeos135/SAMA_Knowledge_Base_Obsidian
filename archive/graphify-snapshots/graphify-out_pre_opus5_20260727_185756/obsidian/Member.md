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

# Member

## Connections

### [[Membership Agreement]] — `references` [EXTRACTED]
- **Why:** The membership agreement is the legal instrument that creates the 'Member' status and simultaneously binds the resulting member to defined data-supply schedules and obligations; a party cannot be a Member—and therefore cannot access or supply credit information—absent a signed, SAMA-approved agreement.
- **This node (Page 14 / Article (42)):** "Members who are committed by membership agreements with companies may not deny or delay the provision of the credit information required by them according to the defined schedules and agreed frequency stipulated in the membership agreements."
- **Related node (Page 8 / Article (21)):** "Each party after signing the agreement will be regarded as a 'member'."
- **Implication:** Member management systems must track agreement execution date, agreed submission frequency, and schedule compliance; failure to supply on schedule is a direct breach of the membership agreement and a regulatory violation, creating an auditable SLA-monitoring requirement.

### [[Negative Decision]] — `references` [EXTRACTED]
- **Why:** A Member is the entity that takes a Negative Decision against a consumer based on credit record data and bears the mandatory obligation to notify the consumer of that decision within a prescribed timeframe, linking Member conduct directly to consumer-rights triggers.
- **This node (Page 14 / Article (45)):** "In case the member has taken a negative decision against the consumer for a cause that is partially or entirely due to any information included in his/her credit record, they shall notify the consumer within 7 working days from the date of taking such decision."
- **Related node (Page 2 / Definitions):** "Negative Decision: Any decision made by a member against a consumer based on his/her credit record."
- **Implication:** Members must implement a decision-notification workflow that automatically triggers a written consumer notice (including the source company name, address, phone, and a copy of the credit record) within 7 working days of any adverse credit decision, with a timestamped evidence trail for SAMA examination.

#graphify/concept #graphify/EXTRACTED #community/Credit_Information_Regulation #graphify/enriched
