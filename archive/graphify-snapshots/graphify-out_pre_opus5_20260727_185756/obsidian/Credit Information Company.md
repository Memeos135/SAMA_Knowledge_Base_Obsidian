---
source_file: "markdown/SAMA_EN_961_VER1.md"
type: "concept"
community: "Personal Data Protection"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Personal_Data_Protection
  - graphify/enriched
---

# Credit Information Company

## Connections

### [[Credit Information License]] — `references` [EXTRACTED]
- **Why:** The license is the precondition for a company's legal existence as a Credit Information Company; Article 2 prohibits provision of credit information services without a SAMA-issued license, and Article 3 enumerates the structural, capital, and governance conditions that define the licensed entity's ongoing obligations.
- **This node (Page 1 / Art 1 / document2.md):** "Companies: credit information companies licensed to collect and maintain credit information on consumers, as well as provide members with such information upon their request."
- **Related node (Page 1 / Art 2 / document2.md):** "A natural or juridical person shall not provide credit information services before obtaining a license from SAMA pursuant to the provisions of Law and its Implementing Regulations."
- **Implication:** Any onboarding or KYB workflow that interacts with a credit information company must verify active SAMA licensure as a gate condition, and compliance monitoring must track licence status changes (suspension, revocation) given the prohibition on unlicensed operation.

### [[Credit Record]] — `references` [EXTRACTED]
- **Why:** The Credit Information Company is the sole entity legally empowered to issue Credit Records; the Implementing Regulations impose on companies both the obligation to produce accurate records and the duty to manage disputes, amendments, and retention of information within those records.
- **This node (Page 9 / Art 25 / document2.md):** "Companies shall take all measures and precautions necessary to ensure soundness, accuracy, integrity and completeness of information obtained according to the Law and its Implementing Regulations."
- **Related node (Page 1 / Art 1 / document2.md):** "Credit Record: A report issued by companies containing credit information on a consumer."
- **Implication:** Compliance systems for credit information companies must implement data-quality controls (validation, reconciliation, completeness checks) at the point of record generation, and maintain an auditable log of amendments and dispute annotations per Articles 49–50.

### [[Membership Agreement]] — `references` [EXTRACTED]
- **Why:** A Credit Information Company is legally prohibited from collecting credit information from any party until a SAMA-approved membership agreement is executed; the agreement is therefore a mandatory pre-condition and governance instrument that defines the company's data-collection perimeter and member obligations.
- **This node (Page 9 / Article (25)):** "not collect credit information from any party prior to signing a membership agreement with that party"
- **Related node (Page 8 / Article (21)):** "Companies shall sign membership agreements approved by SAMA with any party that wishes to obtain credit information about consumer credit records. Such agreements shall indicate rights and obligations of the parties."
- **Implication:** The company's onboarding workflow must include a hard gate: no data ingestion pipeline or API feed from a prospective member may be activated until a SAMA-approved membership agreement is fully executed and recorded in the company's member registry (Art. 24).

#graphify/concept #graphify/EXTRACTED #community/Personal_Data_Protection #graphify/enriched
