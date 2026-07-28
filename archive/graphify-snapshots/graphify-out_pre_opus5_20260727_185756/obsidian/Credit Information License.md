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

# Credit Information License

## Connections

### [[Credit Information Company]] — `references` [EXTRACTED]
- **Why:** The license is the precondition for a company's legal existence as a Credit Information Company; Article 2 prohibits provision of credit information services without a SAMA-issued license, and Article 3 enumerates the structural, capital, and governance conditions that define the licensed entity's ongoing obligations.
- **This node (Page 1 / Art 2 / document2.md):** "A natural or juridical person shall not provide credit information services before obtaining a license from SAMA pursuant to the provisions of Law and its Implementing Regulations."
- **Related node (Page 1 / Art 1 / document2.md):** "Companies: credit information companies licensed to collect and maintain credit information on consumers, as well as provide members with such information upon their request."
- **Implication:** Any onboarding or KYB workflow that interacts with a credit information company must verify active SAMA licensure as a gate condition, and compliance monitoring must track licence status changes (suspension, revocation) given the prohibition on unlicensed operation.

### [[Saudi Central Bank (SAMA)]] — `references` [EXTRACTED]
- **Why:** The Credit Information License concept is definitionally and operationally anchored to SAMA: no entity may provide credit information services without a SAMA-issued licence, and ongoing licence conditions require continuous SAMA approval of systems, governance documents, and instructions.
- **This node (Page 2 / Article 2):** "A natural or juridical person shall not provide credit information services before obtaining a license from SAMA pursuant to the provisions of Law and its Implementing Regulations."
- **Related node (Page 2 / Article 3):** "obtain SAMA approval on the computer system used in provision of the credit information services … comply with the instructions and business rules issued by SAMA."
- **Implication:** A credit information company's licence management workflow must include tracked SAMA approvals for its Articles of Association, IT systems, and any material changes thereto; absence of documented SAMA sign-off on the core platform is a direct licensing breach, not merely a procedural gap.

#graphify/concept #graphify/EXTRACTED #community/Credit_Information_Regulation #graphify/enriched
