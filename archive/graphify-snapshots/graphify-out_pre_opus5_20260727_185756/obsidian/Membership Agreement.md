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

# Membership Agreement

## Connections

### [[Credit Information Company]] — `references` [EXTRACTED]
- **Why:** A Credit Information Company is legally prohibited from collecting credit information from any party until a SAMA-approved membership agreement is executed; the agreement is therefore a mandatory pre-condition and governance instrument that defines the company's data-collection perimeter and member obligations.
- **This node (Page 8 / Article (21)):** "Companies shall sign membership agreements approved by SAMA with any party that wishes to obtain credit information about consumer credit records. Such agreements shall indicate rights and obligations of the parties."
- **Related node (Page 9 / Article (25)):** "not collect credit information from any party prior to signing a membership agreement with that party"
- **Implication:** The company's onboarding workflow must include a hard gate: no data ingestion pipeline or API feed from a prospective member may be activated until a SAMA-approved membership agreement is fully executed and recorded in the company's member registry (Art. 24).

### [[Member]] — `references` [EXTRACTED]
- **Why:** The membership agreement is the legal instrument that creates the 'Member' status and simultaneously binds the resulting member to defined data-supply schedules and obligations; a party cannot be a Member—and therefore cannot access or supply credit information—absent a signed, SAMA-approved agreement.
- **This node (Page 8 / Article (21)):** "Each party after signing the agreement will be regarded as a 'member'."
- **Related node (Page 14 / Article (42)):** "Members who are committed by membership agreements with companies may not deny or delay the provision of the credit information required by them according to the defined schedules and agreed frequency stipulated in the membership agreements."
- **Implication:** Member management systems must track agreement execution date, agreed submission frequency, and schedule compliance; failure to supply on schedule is a direct breach of the membership agreement and a regulatory violation, creating an auditable SLA-monitoring requirement.

#graphify/concept #graphify/EXTRACTED #community/Credit_Information_Regulation #graphify/enriched
