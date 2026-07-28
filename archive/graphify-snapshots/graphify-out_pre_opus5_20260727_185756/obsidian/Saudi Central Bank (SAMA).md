---
source_file: "markdown/SAMA_EN_1430_VER1.md"
type: "concept"
community: "SAMA Supervision & Enforcement"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SAMA_Supervision__Enforcement
  - graphify/enriched
---

# Saudi Central Bank (SAMA)

## Connections

### [[Credit Information License]] — `references` [EXTRACTED]
- **Why:** The Credit Information License concept is definitionally and operationally anchored to SAMA: no entity may provide credit information services without a SAMA-issued licence, and ongoing licence conditions require continuous SAMA approval of systems, governance documents, and instructions.
- **This node (Page 2 / Article 3):** "obtain SAMA approval on the computer system used in provision of the credit information services … comply with the instructions and business rules issued by SAMA."
- **Related node (Page 2 / Article 2):** "A natural or juridical person shall not provide credit information services before obtaining a license from SAMA pursuant to the provisions of Law and its Implementing Regulations."
- **Implication:** A credit information company's licence management workflow must include tracked SAMA approvals for its Articles of Association, IT systems, and any material changes thereto; absence of documented SAMA sign-off on the core platform is a direct licensing breach, not merely a procedural gap.

### [[Implementing Regulations of Credit Information Law]] — `references` [EXTRACTED]
- **Why:** The Implementing Regulations repeatedly designate SAMA as the competent authority that approves, supervises, and issues binding working rules for credit information companies, making SAMA an integral regulatory actor named within the Regulations' operative provisions.
- **This node (Page 1 / Article 1):** "SAMA: Saudi Central Bank (SAMA)*. Governor: Governor of Saudi Central Bank."
- **Related node (Page 9 / Article 25):** "gather credit information from members in line with the criteria approved by the company and which include administrative, technical and legal requirements as well as the working rules approved by SAMA"
- **Implication:** Credit information companies must be able to evidence that their data-collection criteria and working rules have received SAMA approval; an audit trail of SAMA-approved rule versions and the dates of approval is a mandatory supervisory artefact.

### [[Saudi Central Bank]] — `semantically_similar_to` [INFERRED]
- **Why:** Both nodes refer to the same regulatory authority—'Saudi Central Bank (SAMA)'—but appear in two distinct regulatory instruments: the Credit Information Law Implementing Regulations (document2) and the Systemically Important Financial Institutions Law (document3). The semantic similarity is the shared supervisory identity, not substantive overlap in regulatory obligations.
- **This node (Page 1 / Art 1 / document2.md):** "SAMA: Saudi Central Bank (SAMA)*. [...] 'Saudi Arabian Monetary Agency' was replaced by the 'Saudi Central Bank' in accordance with The Saudi Central Bank Law No. (M/36), dated 11/04/1442H."
- **Related node (Page 1 / Art 1 / document3.md):** "Competent Authority: The Saudi Central Bank or the Capital Market Authority, each with respect to financial institutions falling under its supervision."
- **Implication:** A RegTech system mapping supervisory authority must resolve 'SAMA' as 'Saudi Central Bank' uniformly across both regimes, but note that document3 splits competence between SAMA and CMA depending on institution type, while document2 assigns sole supervisory authority to SAMA for credit information companies.
- **Caveat:** Relation is INFERRED: the two nodes are linked by shared institutional identity across different regulatory instruments, not by a cross-reference or explicit legal link between the two documents.

#graphify/concept #graphify/EXTRACTED #community/SAMA_Supervision__Enforcement #graphify/enriched
