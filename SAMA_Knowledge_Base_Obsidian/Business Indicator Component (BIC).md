---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Operational Risk Standardized Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Operational_Risk_Standardized_Approach
  - graphify/enriched
---

# Business Indicator Component (BIC)

## Connections

### [[Business Indicator (BI)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's minimum operational risk capital under SAMA's standardized approach, you cannot treat the BI and BIC as interchangeable inputs: the BIC is a derived quantity built on top of the BI through a tiered coefficient schedule. The framework defines the BI as the financial-statement-based proxy and the BIC as the result of multiplying that BI by regulatory marginal coefficients (12% up to SAR 4.46bn, +3% for excess amounts). For any capital calculation you should confirm the correct BI figure first, then apply the bracketed coefficients, since an error in the BI propagates directly into the BIC and the final ORC.
- **Grounding — this node (Page 5 / Art 7.1(a)):** "Business Indicator Component (BIC) is calculated as the sum of: (i) 12% of the Bank's BI"
- **Grounding — related node (Page 4 / section 4 definitions):** "the Business Indicator (BI) ... a financial-statement-based proxy for operational risk"

### [[Operational Risk Capital (ORC)]] — `references` [EXTRACTED]
- **What this link tells you:** When you assess a bank's minimum capital compliance, the BIC is not a standalone charge — it is one of two multiplicands producing the ORC (ORC = BIC × ILM). This matters because a bank that fails the loss-data standards must hold capital at least equal to 100% of the BIC, effectively flooring ORC at the BIC even where internal losses are low. Confirm both which figure (BIC vs BIC×ILM) applies and whether SAMA has imposed an ILM greater than 1 before concluding on the capital requirement.
- **Grounding — this node (Page 5 / Art 7.1):** "The Banks must calculate minimum ORC requirements ... by multiplying the BIC and the ILM: ORC = BIC x ILM"
- **Grounding — related node (Page 3 / section 1 Introduction):** "the revised standardized approach as the sole approach for calculating operational risk capital requirements"

### [[The Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating minimum operational risk capital, the BIC is not a standalone metric — it is a required multiplicand in the Standardized Approach formula (ORC = BIC x ILM), so any dispute over the BIC calculation is a dispute over the capital charge itself. The framework defines the BIC via marginal coefficients on the Business Indicator and makes it the floor even where loss data is deficient (minimum 100% of BIC). A reader should conclude the BIC and the Standardized Approach cannot be assessed independently, and that BIC inputs directly drive regulatory capital adequacy.
- **Grounding — this node (Page 5 / sec 7.1):** "Business Indicator Component (BIC) is calculated as the sum of: (i) 12% of the Bank's BI..."
- **Grounding — related node (Page 5 / sec 7.1):** "The Banks must calculate minimum ORC requirements based on the Standardized Approach by multiplying the BIC and the ILM: ORC = BIC x ILM"

#graphify/concept #graphify/EXTRACTED #community/Operational_Risk_Standardized_Approach #graphify/enriched
