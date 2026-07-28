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

# Real Estate Exposure Class

## Connections

### [[Credit Risk Mitigation Framework]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears to connect the Credit Risk Mitigation framework with the real estate exposure class, but the provided CRM context (paras 14.11–14.12) addresses recognition of guarantees and collateral for purchased receivables and securitization, not real estate collateral specifically. The real estate provisions here (LTV-based risk weights, 'materially dependent on cash flows') set exposure classification and risk weights rather than invoke CRM substitution. Treat this as a general framework relationship — real estate exposures are secured lending to which CRM concepts can be relevant — and verify in the primary text whether the CRM chapter actually modifies real estate risk weights before relying on any interaction.
- **Grounding — this node (Page 34 / Art 7.61):** "Exposures secured by real estate that are classified as “regulatory real estate” exposures."
- **Grounding — related node (Page 173 / Art 14.12):** "Credit risk mitigants will be recognized generally using the same type of framework as set forth in paragraphs 12.21 to 12.28"
- **Caveat:** The supplied CRM excerpts concern receivables/securitization, not real estate collateral; the direct cross-reference between these two nodes is not evidenced in context and should be verified against the CRM chapter.

### [[Land Acquisition Development and Construction Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting a property-financing loan, recognise that land ADC exposures are a defined sub-component of the real estate exposure class, not a free-standing regime: para 7.61 lists ADC as one of the three constituents of the real estate asset class, and para 7.82 supplies the ADC definition and its 150% base risk weight (reducible to 100% only if the 7.83 residential criteria are met). The 'other real estate' residual definition in 7.80 also expressly carves out ADC exposures. You would conclude that a loan financing land acquisition, development or construction must first be tested against the ADC definition before any regulatory/other real estate treatment can apply.
- **Grounding — this node (Page 34 / Art 7.61):** "The real estate exposure asset class consists of:... 3. Exposures that are classified as “land acquisition, development and construction” (ADC) exposures."
- **Grounding — related node (Page 45 / Art 7.82):** "Land ADC exposures refers to loans to companies or SPVs financing any of the land acquisition for development and construction purposes... ADC exposures will be risk-weighted at 150%, unless they meet the criteria in paragraph 7.83."

### [[Loan Splitting Approach]] — `references` [EXTRACTED]
- **What this link tells you:** This edge appears to relate a 'loan splitting approach' to the real estate exposure class, which is plausible because real estate risk-weighting under the standardized approach can be applied either as a whole-loan or a loan-splitting method keyed to LTV; the real estate context shows LTV-based tables (e.g. Table 12) that such methods use. However, the provided context for the loan-splitting node does not actually contain the loan-splitting text (it shows securitization contents, IRB rollout and LTV definition paragraphs), so the substance of the link is not directly grounded here. Treat this as a lead: confirm in the primary real estate provisions (around paras 7.66 onward) whether loan splitting is the prescribed method and how it partitions the secured/unsecured portions before relying on it.
- **Grounding — this node (Page 44 / Art 7.79 (Table 12)):** "the risk weight to be assigned to the total exposure amount will be determined based on the exposure’s LTV in Table 12 below."
- **Grounding — related node (Page 37 / Art 7.66):** "The LTV is the amount of the loan divided by the value of the property. When calculating the LTV, the loan amount will be reduced as the loan amortizes."
- **Caveat:** The loan-splitting node's supplied context does not contain the loan-splitting methodology text; the link is inferred from the shared LTV/real-estate subject matter and should be verified against the primary provisions.

### [[Loan-to-Value Ratio (LTV)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital treatment of a real estate exposure, you cannot fix a risk weight without first computing the LTV, because the real estate exposure class subdivides into buckets whose risk weights (e.g. 70%/90%/110% for commercial exposures materially dependent on property cash flows) are keyed directly to the LTV ratio. The LTV concept supplies the numerator/denominator rules — loan amount gross of provisions, property value fixed at origination subject to defined downward adjustments — that drive placement into a bucket. Conclude that for any real estate exposure you must apply the LTV calculation methodology in 7.66–7.67 before selecting the risk weight, and note the LTV bucket must be set before any credit risk mitigation is applied.
- **Grounding — this node (Page 44 / 7.79):** "the risk weight to be assigned to the total exposure amount will be determined based on the exposure's LTV in Table 12 below."
- **Grounding — related node (Page 37 / 7.66):** "The LTV is the amount of the loan divided by the value of the property. When calculating the LTV, the loan amount will be reduced as the loan amortizes."

#graphify/concept #graphify/EXTRACTED #community/Standardized_Credit_Risk_Approach #graphify/enriched
