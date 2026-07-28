---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Real Estate Credit Mitigation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Real_Estate_Credit_Mitigation
  - graphify/enriched
---

# Loan Splitting Approach

## Connections

### [[Loan-to-Value Ratio (LTV)]] — `references` [INFERRED]
- **What this link tells you:** If you are assessing how a real estate exposure is split for capital purposes, the connection between a loan-splitting approach and the LTV concept appears plausible but is not established by the provided text — the node A context on this page concerns IRB phased rollout, not loan splitting, and does not state a link to LTV. The LTV mechanics (loan amount over property value, bucketing) are the natural input to any whole-loan versus loan-splitting treatment, so this is a reasonable lead. Before relying on it, verify the actual loan-splitting provision (the whole-loan approach referenced in 7.79) and confirm how it consumes the LTV, since the supplied excerpts do not evidence the relationship.
- **Grounding — this node (Page 106 / 10.44–10.46):** "it may not be practicable... to implement the IRB approach for an entire asset class... a phased rollout of the IRB approach across an asset class."
- **Grounding — related node (Page 37 / 7.66):** "The LTV is the amount of the loan divided by the value of the property."
- **Caveat:** INFERRED: node A context is about IRB phased rollout, not loan splitting; the provided text does not directly connect a loan-splitting approach to LTV. Verify the whole-loan/loan-splitting provision in the primary text before relying.

### [[Real Estate Exposure Class]] — `references` [EXTRACTED]
- **What this link tells you:** This edge appears to relate a 'loan splitting approach' to the real estate exposure class, which is plausible because real estate risk-weighting under the standardized approach can be applied either as a whole-loan or a loan-splitting method keyed to LTV; the real estate context shows LTV-based tables (e.g. Table 12) that such methods use. However, the provided context for the loan-splitting node does not actually contain the loan-splitting text (it shows securitization contents, IRB rollout and LTV definition paragraphs), so the substance of the link is not directly grounded here. Treat this as a lead: confirm in the primary real estate provisions (around paras 7.66 onward) whether loan splitting is the prescribed method and how it partitions the secured/unsecured portions before relying on it.
- **Grounding — this node (Page 37 / Art 7.66):** "The LTV is the amount of the loan divided by the value of the property. When calculating the LTV, the loan amount will be reduced as the loan amortizes."
- **Grounding — related node (Page 44 / Art 7.79 (Table 12)):** "the risk weight to be assigned to the total exposure amount will be determined based on the exposure’s LTV in Table 12 below."
- **Caveat:** The loan-splitting node's supplied context does not contain the loan-splitting methodology text; the link is inferred from the shared LTV/real-estate subject matter and should be verified against the primary provisions.

#graphify/concept #graphify/EXTRACTED #community/Real_Estate_Credit_Mitigation #graphify/enriched
