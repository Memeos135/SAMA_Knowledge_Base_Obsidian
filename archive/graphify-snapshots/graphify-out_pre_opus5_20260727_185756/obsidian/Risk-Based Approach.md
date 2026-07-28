---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "concept"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Risk-Based Approach

## Connections

### [[AMLCTF Guide|AML/CTF Guide]] — `references` [EXTRACTED]
- **Why:** The AML/CTF Guide structurally embeds the risk-based approach as the organising framework for all AML/CTF programme obligations: ML/TF risk assessment is identified as the primary step, customer classification drives the intensity of due diligence, and the programme must be commensurate with the nature and size of the institution's business—meaning the Guide references and operationalises the risk-based approach throughout.
- **This node (Page 20 / Section 1 ML/TF Risk Assessment):** "The main step for a financial institution to adopt a risk-based approach is to assess, understand and document its ML/TF risks … The risk assessment shall be comprehensive and include an analysis of the risks arising from: Customers and beneficial owners; The nature of products,…"
- **Related node (Page 25 / Para 2.1):** "The financial institution shall develop an AML/CTF program … to mitigate ML/TF risks in line with the risk assessment results approved by it … commensurate with the nature and size of the financial institution's business."
- **Implication:** The AML/CTF programme document and its supporting risk assessment must be maintained as linked, board-approved artefacts—with the risk assessment explicitly driving control calibration—so that an examiner can trace each control's intensity directly to a documented risk rating for customers, products, channels, and geographies.

### [[Due Diligence Measures]] — `references` [EXTRACTED]
- **Why:** Due diligence intensity and scope are explicitly calibrated to ML/TF risk assessment outputs; the risk-based approach (RBA) is the governing framework that determines whether standard, simplified, or enhanced CDD applies to a given customer or relationship.
- **This node (Page 20 / Section 1 preamble):** "The main step for a financial institution to adopt a risk-based approach is to assess, understand and document its ML/TF risks and to identify the weaknesses that could be used to carry out ML/TF transactions."
- **Related node (Page 36 / Section 4 preamble):** "Customer classification according to the level of risks is a key element in the financial institution's risk-based approach. The financial institution shall identify the risk factors to be taken into consideration when classifying a customer in the high-risk customer category."
- **Implication:** Customer risk scores produced by the RBA engine must feed directly into the CDD tier-selection logic, and the risk assessment documentation must be updatable at least every two years or upon change in risk factors, demonstrable to a SAMA examiner.

### [[MLTF Risk Assessment|ML/TF Risk Assessment]] — `references` [EXTRACTED]
- **Why:** The ML/TF Risk Assessment is explicitly described as 'the main step' for adopting a Risk-Based Approach; the output of the assessment (risk classification, identified weaknesses, factor analysis) directly parameterises the calibration, scope, and update cycle of the RBA, making assessment the logical and regulatory antecedent of the approach.
- **This node (Page 20 / Chapter IX):** "The financial institution shall ensure that the risk-based approach is updated once every two years at a minimum or when risk factors change."
- **Related node (Page 20 / Section 1: ML/TF Risk Assessment):** "The main step for a financial institution to adopt a risk-based approach is to assess, understand and document its ML/TF risks and to identify the weaknesses that could be used to carry out ML/TF transactions."
- **Implication:** Any change to product, channel, geography, or technology must trigger a risk assessment refresh before RBA controls are recalibrated; the system architecture should link new-product approval workflows to a mandatory risk assessment update gate, with evidence retained for SAMA review.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
