---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Standardized Credit Risk Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Standardized_Credit_Risk_Approach
  - graphify/enriched
---

# Loan-to-Value Ratio (LTV)

## Connections

### [[Loan Splitting Approach]] — `references` [INFERRED]
- **What this link tells you:** If you are assessing how a real estate exposure is split for capital purposes, the connection between a loan-splitting approach and the LTV concept appears plausible but is not established by the provided text — the node A context on this page concerns IRB phased rollout, not loan splitting, and does not state a link to LTV. The LTV mechanics (loan amount over property value, bucketing) are the natural input to any whole-loan versus loan-splitting treatment, so this is a reasonable lead. Before relying on it, verify the actual loan-splitting provision (the whole-loan approach referenced in 7.79) and confirm how it consumes the LTV, since the supplied excerpts do not evidence the relationship.
- **Grounding — this node (Page 37 / 7.66):** "The LTV is the amount of the loan divided by the value of the property."
- **Grounding — related node (Page 106 / 10.44–10.46):** "it may not be practicable... to implement the IRB approach for an entire asset class... a phased rollout of the IRB approach across an asset class."
- **Caveat:** INFERRED: node A context is about IRB phased rollout, not loan splitting; the provided text does not directly connect a loan-splitting approach to LTV. Verify the whole-loan/loan-splitting provision in the primary text before relying.

### [[Real Estate Exposure Class]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital treatment of a real estate exposure, you cannot fix a risk weight without first computing the LTV, because the real estate exposure class subdivides into buckets whose risk weights (e.g. 70%/90%/110% for commercial exposures materially dependent on property cash flows) are keyed directly to the LTV ratio. The LTV concept supplies the numerator/denominator rules — loan amount gross of provisions, property value fixed at origination subject to defined downward adjustments — that drive placement into a bucket. Conclude that for any real estate exposure you must apply the LTV calculation methodology in 7.66–7.67 before selecting the risk weight, and note the LTV bucket must be set before any credit risk mitigation is applied.
- **Grounding — this node (Page 37 / 7.66):** "The LTV is the amount of the loan divided by the value of the property. When calculating the LTV, the loan amount will be reduced as the loan amortizes."
- **Grounding — related node (Page 44 / 7.79):** "the risk weight to be assigned to the total exposure amount will be determined based on the exposure's LTV in Table 12 below."

#graphify/concept #graphify/EXTRACTED #community/Standardized_Credit_Risk_Approach #graphify/enriched
