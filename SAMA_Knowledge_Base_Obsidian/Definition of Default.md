---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "IRB Credit Risk Approach"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Definition of Default

## Connections

### [[Own-LGD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When validating an own-LGD model, confirm it uses the framework's reference definition of default, because LGD estimation is functionally dependent on that definition. Paragraph 16.71 requires banks to use the reference definition of default for estimating PDs and, where relevant, LGDs and EADs, and 16.72 links default status directly to how LGD is estimated for defaulted versus non-defaulted facilities. You would therefore not accept LGD estimates built on an inconsistent internal default trigger; any external data not aligned to the reference definition must satisfy the adjustment conditions in 16.77.
- **Grounding — this node (Page 199 / 16.71):** "A bank must also use the reference definition for its estimation of PDs, and (where relevant) LGDs and EADs."
- **Grounding — related node (Page 200 / 16.72):** "the bank must rate the borrower and estimate LGD as they would for a non-defaulted facility. Should the reference definition subsequently be triggered, a second default would be deemed to have occurred."

### [[Risk Quantification]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying IRB risk parameters you cannot use an internal or ad hoc default trigger, because the framework mandates that PD, and where relevant LGD and EAD, be estimated using the same reference definition of default set out in the definition-of-default provisions. Paragraph 16.71 expressly ties actual default recording and parameter estimation to that reference definition, permitting external data only subject to the mapping conditions. For a compliance decision, conclude that your quantification inputs must be reconciled to the reference default definition (including the unlikeliness-to-pay indicators and the retail facility-level option in 16.70) and verify that any external data has been mapped consistently before relying on the estimates.
- **Grounding — this node (Page 199 / Para 16.71):** "A bank must also use the reference definition for its estimation of PDs, and (where relevant) LGDs and EADs"
- **Grounding — related node (Page 173 / Para 14.12):** "Credit risk mitigants will be recognized generally using the same type of framework as set forth in paragraphs 12.21 to 12.28"
- **Caveat:** Node B's tagged context spans several quantification/CRM pages; the definition-of-default linkage is grounded in 16.71, but confirm the exact quantification paragraphs (16.x PD/LGD/EAD standards) that consume the default definition.

#graphify/document #graphify/INFERRED #community/IRB_Credit_Risk_Approach #graphify/enriched
