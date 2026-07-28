---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "document"
community: "Trading Book Boundary"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Trading_Book_Boundary
  - graphify/enriched
---

# SAMA Minimum Capital Requirements for Credit Risk

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `cites` [EXTRACTED]
- **What this link tells you:** When setting default risk weights for DRC purposes, do not derive them independently — the market-risk DRC framework imports risk weights and zero-risk-weight treatments from SAMA's Minimum Capital Requirements for Credit Risk. The DRC provisions expressly apply sovereign/PSE/MDB zero-weight treatment 'in line with paragraphs 7.1 through 7.11 in the SAMA Minimum Capital Requirements for Credit Risk framework,' and securitisation DRC weights are based on the banking-book securitisation weights in that same document. For a capital calculation you would conclude that DRC risk-weight inputs must be sourced from and reconciled against the credit-risk framework, including SAMA's non-zero weighting of certain foreign-government securities.
- **Grounding — this node (Page 142):** "The capital requirement for specific risk for a first-to-default credit derivative is the lesser of... the maximum possible credit event payment under the contract."
- **Grounding — related node (Page 430 / 8.7):** "subject to a zero default risk weight in line with paragraphs 7.1 through 7.11 in the SAMA Minimum Capital Requirements for Credit Risk framework"
- **Caveat:** Node B context shown is specific-risk/credit-derivative material rather than the exact para 7.1–7.11 sovereign weighting cited; verify the precise cross-referenced paragraphs in the credit-risk framework before relying.

### [[Internal Risk Transfer]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing whether a banking-book credit or equity exposure is deemed hedged by an internal risk transfer, do not evaluate the market-risk conditions in isolation: [5.21] cross-refers to specific paragraphs (9.73–9.74, 9.76–9.77) of the SAMA credit-risk capital framework that the external hedge must satisfy vis-à-vis the banking-book exposure. This makes credit-risk recognition of the hedge dependent on both frameworks being met simultaneously. You would conclude that you must verify the external hedge against the cited credit-risk provisions before treating the banking-book exposure as hedged for capital purposes.
- **Grounding — this node (Page 24 / 5.21(1)(b)):** "The external hedge meets the requirements of paragraphs 9.73 to 9.74 and 9.76 9.77 of the SAMA Minimum Capital Requirements for Market Risk vis-à-vis the banking book exposure"
- **Grounding — related node (Page 24 / 5.22):** "the banking book exposure is deemed to be hedged by the banking book leg of the internal risk transfer for capital purposes in the banking book"
- **Caveat:** The [5.21](1)(b) reference names 'Market Risk' provisions 9.73–9.77; whether these are the credit-risk framework paragraphs is ambiguous in the extract, so verify the cross-referenced document before relying on the credit-risk linkage.

### [[Minimum Capital Requirements for Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping capital treatment of internal risk transfers and hedges, do not read the Credit Risk and Market Risk frameworks in isolation: the same instrument (e.g. an external hedge or a banking-book credit position moved to the trading book) can shift between the two regimes depending on whether the [5.21] matching conditions are met. The Market Risk framework expressly conditions capital recognition of CVA/credit-derivative hedges on requirements that straddle both books, so a hedge that reduces a credit-risk capital charge only qualifies if the parallel market-risk treatment is also satisfied. Conclude that eligibility must be checked against both frameworks together, and that failing the market-risk condition removes the credit-risk offset.
- **Grounding — this node (Page 142):** "the bank is allowed to reduce, with respect to the hedged amount, both the capital requirement for specific risk for the reference credit instrument and that part of the capital requirement for specific risk for the credit derivative"
- **Grounding — related node (Page 26 / 5.33):** "Internal CVA risk transfers ... may be recognised in the CVA portfolio capital requirement and market risk capital requirement only if the trading book additionally enters into an external hedge with an eligible third-party protection provider that exactly matches the internal r…"

### [[Specific Risk]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining specific-risk capital for credit derivatives, this document itself sets out the specific-risk charges and offsets for reference credit instruments, so specific risk here is a market-risk (trading-book) concept computed within these minimum capital requirements. The provisions on first-to-default and nth-to-default derivatives prescribe the specific-risk charge as the lesser of aggregated component charges or the maximum credit event payment. Conclude that these specific-risk rules govern trading-book credit-derivative positions; do not conflate them with the separate credit-risk (banking-book) capital framework without confirming which book the position sits in.
- **Grounding — this node (Page 142):** "The capital requirement for specific risk for a first-to-default credit derivative is the lesser of: (a) the sum of the specific risk capital requirements ...; and (b) the maximum possible credit event payment"
- **Grounding — related node (Page 142):** "the bank is allowed to reduce ... both the capital requirement for specific risk for the reference credit instrument and that part of the capital requirement for specific risk for the credit derivative"

#graphify/document #graphify/EXTRACTED #community/Trading_Book_Boundary #graphify/enriched
