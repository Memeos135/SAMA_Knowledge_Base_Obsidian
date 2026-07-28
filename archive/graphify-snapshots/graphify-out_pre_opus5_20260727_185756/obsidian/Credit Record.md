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

# Credit Record

## Connections

### [[Consumer]] — `references` [EXTRACTED]
- **Why:** The Consumer's rights, obligations of members toward the consumer, and consumer protections are all expressed directly in relation to the credit record as the legal object—Arts 16, 40–45 treat the credit record as the primary instrument through which the consumer's creditworthiness is assessed, disclosed, and corrected.
- **This node (Page 7 / Art 17):** "Companies have the right to maintain the negative information in the consumer credit record for no more than five years from the debt or dispute settlement date. An exception is the cases of bankruptcy, insolvency and delayed Zakat or tax obligations which shall be maintained in…"
- **Related node (Page 14 / Art 43):** "The consumer shall have the right to know all information contained in his/her credit record. The consumer may request his/her record from any credit information company free of charge, if: 1. the record is requested for the first time..."
- **Implication:** Credit information company platforms must implement retention lifecycle controls that automatically enforce the 5-year / 10-year / until-settlement tiering per Art 17, and expose consumer-facing inquiry interfaces that satisfy the Art 43 free-access entitlements under defined conditions, with logs demonstrating eligibility checks.

### [[Consumer Consent]] — `references` [EXTRACTED]
- **Why:** Written consumer consent is the legal prerequisite that gates a member's authority to submit a consumer's credit information to a licensed company for inclusion in the credit record; without it, Art 40 prohibits the data flow that populates the record, making consent the access-control condition for record creation and updating.
- **This node (Page 7 / Art 18):** "At the request of the member, the company may include in the credit record of a partner in a partnership credit information relating to the other partners after obtaining their written consent."
- **Related node (Page 13 / Art 40):** "obtain the written consent of the consumer upon inquiry, and his/her approval to provide licensed companies with his/her credit information."
- **Implication:** Member onboarding and credit-inquiry workflows must capture, timestamp, and retain written consent records as a mandatory pre-condition before any data submission to the credit bureau, with the consent artefact linkable to the specific credit record entry for SAMA examination purposes.

### [[Credit Information Company]] — `references` [EXTRACTED]
- **Why:** The Credit Information Company is the sole entity legally empowered to issue Credit Records; the Implementing Regulations impose on companies both the obligation to produce accurate records and the duty to manage disputes, amendments, and retention of information within those records.
- **This node (Page 1 / Art 1 / document2.md):** "Credit Record: A report issued by companies containing credit information on a consumer."
- **Related node (Page 9 / Art 25 / document2.md):** "Companies shall take all measures and precautions necessary to ensure soundness, accuracy, integrity and completeness of information obtained according to the Law and its Implementing Regulations."
- **Implication:** Compliance systems for credit information companies must implement data-quality controls (validation, reconciliation, completeness checks) at the point of record generation, and maintain an auditable log of amendments and dispute annotations per Articles 49–50.

### [[Negative Decision]] — `references` [EXTRACTED]
- **Why:** A Negative Decision is defined as any decision made by a member against a consumer based on his/her Credit Record; Article (45) then mandates that when such a decision is taken the member must notify the consumer of the Negative Information in that Credit Record within 7 working days, directly linking the record's content to the member's disclosure obligation.
- **This node (Page 7 / Article (17)):** "Companies have the right to maintain the negative information in the consumer credit record for no more than five years from the debt or dispute settlement date."
- **Related node (Page 14-15 / Article (45)):** "In case the member has taken a negative decision against the consumer for a cause that is partially or entirely due to any information included in his/her credit record, they shall notify the consumer within 7 working days from the date of taking such decision with the negative…"
- **Implication:** Member systems must generate a timestamped adverse-action notice within 7 working days of any credit denial or restriction that was informed by Credit Record content, including the specific Negative Information relied upon and the sourcing company's details, creating an auditable evidence trail per Article (45).

### [[Negative Information]] — `references` [EXTRACTED]
- **Why:** The Credit Record is the repository in which Negative Information is maintained, retained, flagged during disputes, and ultimately deleted or modified; Article (17) sets explicit retention limits on Negative Information within the Credit Record, and Articles (49)-(51) govern how disputed Negative Information must be annotated or removed from that record.
- **This node (Page 7 / Article (17)):** "Companies have the right to maintain the negative information in the consumer credit record for no more than five years from the debt or dispute settlement date. An exception is the cases of bankruptcy, insolvency and delayed Zakat or tax obligations which shall be maintained in…"
- **Related node (Page 13 / Article (41)):** "The member shall inform the consumer about any negative information that will be sent to companies within 30 working days as of registering such information in the consumer's record."
- **Implication:** Credit information systems must enforce tiered retention rules per category of Negative Information (5 years standard, 10 years for bankruptcy/insolvency/Zakat-tax, indefinite for outstanding judicial cases) and trigger automated expiry or suppression flags on the Credit Record at the applicable threshold.

#graphify/concept #graphify/EXTRACTED #community/Personal_Data_Protection #graphify/enriched
