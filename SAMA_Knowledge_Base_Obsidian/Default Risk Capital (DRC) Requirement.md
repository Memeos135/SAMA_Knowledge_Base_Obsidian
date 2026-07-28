---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Default Risk Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default_Risk_Capital
  - graphify/enriched
---

# Default Risk Capital (DRC) Requirement

## Connections

### [[Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the DRC calculation, treat the Correlation Trading Portfolio (CTP) as a distinct DRC risk class rather than folding it into general default-risk treatment. The market risk framework requires the DRC requirement to be computed separately for non-securitisations, securitisations (non-CTP), and securitisations (CTP), with no diversification benefit recognised across those categories. Confirm which portfolios meet the CTP definition, because misclassifying a securitisation position as non-CTP (or vice versa) changes the applicable buckets, correlations and JTD treatment and therefore the capital charge.
- **Grounding — this node (SAMA_EN_3487 / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book"
- **Grounding — related node (SAMA_EN_3553 / Page 73, [8.2]):** "(3) Securitisation (correlation trading portfolio, or CTP)"

### [[DRC for Non-Securitisations]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping a bank's market-risk capital charge, treat DRC for non-securitisations as a distinct, self-contained computation within the overall DRC requirement — not a subset that can be netted against other DRC classes. The parent DRC provision requires the charge to be calculated separately for non-securitisation portfolios, and this node fixes the aggregation rule: no hedging is recognised between buckets, so the non-securitisation total is a simple sum of bucket-level requirements. For a capital-adequacy assessment you would conclude that any diversification or hedge benefit sought across non-securitisation and securitisation buckets is disallowed and must be checked against [8.4] and [8.26].
- **Grounding — this node (Page 429 / 8.2):** "The DRC requirement must be calculated for instruments subject to default risk: (1) Non-securitisation portfolios"
- **Grounding — related node (Page 437 / 8.26):** "the total DRC requirement for non-securitisations must be calculated as a simple sum of the bucket level capital requirements"

### [[DRC for Non-Securitisations]] — `references` [EXTRACTED]
- **What this link tells you:** When computing DRC, treat 'DRC for non-securitisations' as one of three self-contained sub-buckets that must be aggregated with no cross-category netting. The framework states 'No diversification benefit is recognised between the DRC requirements for' non-securitisations, securitisations (non-CTP), and securitisations (CTP), and that the total for non-securitisations is a simple sum of bucket-level requirements. For the capital number, this means you cannot offset a non-securitisation long against a securitisation short to reduce DRC — verify positions are assigned to the correct category before aggregating.
- **Grounding — this node (SAMA_EN_3553 / Page 74, [8.4]):** "No diversification benefit is recognised between the DRC requirements for: (1) non-securitisations; (2) securitisations (non-CTP); and (3) securitisations (CTP)"
- **Grounding — related node (SAMA_EN_3553 / Page 81, [8.26]):** "the total DRC requirement for non-securitisations must be calculated as a simple sum of the bucket level capital requirements"

### [[DRC for Securitisations (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating DRC for a correlation trading portfolio, treat securitisations (CTP) as a third, ring-fenced DRC class governed by its own offsetting logic. The parent DRC provision lists CTP as a separate portfolio type, and this node sets the restrictive netting rules — perfect replication is required for offsetting, and different tranches, series or index families of the same index may not be netted. For capital purposes you would conclude that CTP positions cannot be pooled with non-securitisation or non-CTP securitisation DRC, and that any claimed offset must satisfy the strict replication/equivalence tests in [8.40] and surrounding paragraphs.
- **Grounding — this node (Page 429 / 8.2):** "(3) Securitisation (correlation trading portfolio, or CTP)"
- **Grounding — related node (Page 441 / 8.40):** "Different tranches of the same index or series may not be offset (netted), different series of the same index may not be offset, and different index families may not be offset."

### [[DRC for Securitisations (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the market-risk capital charge for a bank holding correlation-trading-portfolio (CTP) securitisation tranches, treat the general DRC framework and the CTP-specific rules as one continuous methodology rather than separate charges. Both sit within SAMA's Minimum Capital Requirements for Market Risk: the DRC concept sets the jump-to-default architecture (bucket-level capital, no cross-bucket hedging), and the CTP provisions (8.36 onward) build on that by referencing the non-CTP securitisation approach for gross JTD. You should therefore compute CTP DRC only by reading it against the base DRC and non-CTP rules it incorporates, not in isolation.
- **Grounding — this node (SAMA_EN_3487_VER1.md / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book"
- **Grounding — related node (SAMA_EN_3553_VER1.md / Page 83 (8.36)):** "For the computation of gross JTD on securitisations (CTP), the same approach must be followed as for default risk-securitisations (non-CTP) as described in [8.27]."

### [[DRC for Securitisations (non-CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the default-risk charge for ordinary (non-CTP) securitisation tranches, read the general DRC concept together with the non-CTP securitisation rules, because the latter deliberately modify the base default-risk methodology. Both derive from SAMA's Market Risk minimum capital framework: the non-CTP rules borrow the DRC approach but drop the LGD ratio (LGD is already embedded in securitisation risk weights) and restrict offsetting to tranches sharing the same underlying asset pool. You would conclude that the securitisation charge cannot be computed by plain application of the non-securitisation DRC rules; the tranche-specific carve-outs in 8.27–8.35 govern.
- **Grounding — this node (SAMA_EN_3487_VER1.md / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book (reported in row 16)"
- **Grounding — related node (SAMA_EN_3553_VER1.md / Page 81 (8.27)):** "the same approach must be followed as for default risk (non-securitisations), except that an LGD ratio is not applied to the exposure"

### [[Jump-to-Default (JTD) Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what the DRC requirement is designed to capture, read it as the mechanism for jump-to-default (JTD) risk — the risk of a sudden default not picked up by credit-spread shocks under the sensitivities-based method. This node defines JTD and sets the step-by-step method (gross JTD per exposure, offsetting of long/short to the same obligor, allocation to buckets, hedge-benefit ratio) that the whole DRC framework operates on. For a capital assessment you would conclude that DRC and JTD are two views of one requirement, and that the definitions of offsetting (same-obligor netting) versus hedging (partial benefit across distinct obligors) in [8.1] govern every DRC class.
- **Grounding — this node (Page 429 / 8.1):** "The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-based method."
- **Grounding — related node (Page 429 / 8.3):** "The gross JTD risk of each exposure is computed separately... the JTD amounts of long and short exposures are offset (where permissible)"

### [[Jump-to-Default (JTD) Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what the DRC requirement is meant to capture, read it as the charge for jump-to-default (JTD) risk — the loss from a sudden default that the sensitivities-based method's credit spread shocks do not capture. The framework states DRC 'is intended to capture jump-to-default (JTD) risk' and the calculation is built on gross and net JTD positions per obligor. For a capital decision, this means DRC and JTD are not independent charges: JTD is the underlying exposure measure that drives the DRC number, so verify the JTD computation before relying on any DRC output.
- **Grounding — this node (SAMA_EN_3553 / Page 73, [8.1]):** "The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks"
- **Grounding — related node (SAMA_EN_3553 / Page 6 (Definitions)):** "The risk of a sudden default. JTD exposure refers to the loss that could be incurred from a JTD event."

### [[Residual Risk Add-On (RRAO)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two appear to be parallel, additive components of the standardised market risk charge rather than overlapping tests: DRC covers jump-to-default risk while the Residual Risk Add-On (RRAO) is introduced to ensure 'sufficient coverage of market risks' not otherwise captured. The link is inferred from the shared standardised-approach structure (both feature in the internal risk transfer recognition rule at [5.33] alongside curvature). Before relying on this, verify in the primary text which specific instruments fall under RRAO versus DRC, since the framework scopes each separately and a position should not be double-counted or omitted.
- **Grounding — this node (SAMA_EN_3487 / Page 382, [5.33]):** "Internal CVA risk transfers that are subject to curvature, default risk or residual risk add-on as set out in [6] through [9]"
- **Grounding — related node (SAMA_EN_3487 / Page 382, [6.1]):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"
- **Caveat:** Relationship is INFERRED from shared standardised-approach structure; confirm the distinct instrument scopes of DRC versus RRAO in the primary text before treating them as strictly non-overlapping.

### [[SAMA Minimum Capital Requirements for Credit Risk]] — `cites` [EXTRACTED]
- **What this link tells you:** When setting default risk weights for DRC purposes, do not derive them independently — the market-risk DRC framework imports risk weights and zero-risk-weight treatments from SAMA's Minimum Capital Requirements for Credit Risk. The DRC provisions expressly apply sovereign/PSE/MDB zero-weight treatment 'in line with paragraphs 7.1 through 7.11 in the SAMA Minimum Capital Requirements for Credit Risk framework,' and securitisation DRC weights are based on the banking-book securitisation weights in that same document. For a capital calculation you would conclude that DRC risk-weight inputs must be sourced from and reconciled against the credit-risk framework, including SAMA's non-zero weighting of certain foreign-government securities.
- **Grounding — this node (Page 430 / 8.7):** "subject to a zero default risk weight in line with paragraphs 7.1 through 7.11 in the SAMA Minimum Capital Requirements for Credit Risk framework"
- **Grounding — related node (Page 142):** "The capital requirement for specific risk for a first-to-default credit derivative is the lesser of... the maximum possible credit event payment under the contract."
- **Caveat:** Node B context shown is specific-risk/credit-derivative material rather than the exact para 7.1–7.11 sovereign weighting cited; verify the precise cross-referenced paragraphs in the credit-risk framework before relying.

### [[SMAR - Minimum Capital Requirements for Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When locating the DRC requirement in the rulebook, treat it as a component chapter of SMAR (Minimum Capital Requirements for Market Risk), not a standalone regime — DRC is the standardised-approach default-risk charge sitting alongside SMAR's sensitivities-based, residual-risk and internal-models measures. The SMAR document supplies the defined terms and cross-referenced paragraphs (e.g. expected shortfall under SMAR13) that frame where DRC contributes to the total market-risk capital charge. For scoping you would conclude that DRC obligations must be read together with the broader SMAR framework and cannot be assessed in isolation from the overall market-risk capital calculation.
- **Grounding — this node (Page 429 / 8):** "8- Standardised approach: default risk capital requirement"
- **Grounding — related node (Page 845):** "Unconstrained expected shortfall: Expected shortfall (ES) as defined in SMAR13.1 to SMAR13.12"

### [[Sensitivities-Based Method]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When building the standardised market risk capital charge, treat the DRC requirement and the sensitivities-based method as complementary components, not substitutes. The framework introduces DRC precisely to capture jump-to-default risk 'that may not be captured by credit spread shocks under the sensitivities-based method,' meaning the two address different risk dimensions of the same credit instruments. For the capital total, you would add both (plus RRAO) rather than choose between them, and should confirm that credit positions are run through both to avoid a coverage gap.
- **Grounding — this node (SAMA_EN_3553 / Page 73, [8.1]):** "jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-based method"
- **Grounding — related node (SAMA_EN_3553 / Page 27):** "a bank must calculate three sensitivities-based method capital requirement values, based on three different scenarios on the specified values for the correlation parameters"

### [[Standardised Approach (Market Risk)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating market-risk capital under the mandatory standardised approach, treat the Default Risk Capital (DRC) requirement as one of the required components of that approach, not an optional add-on. The framework describes the standardised approach as built from sensitivities-based, DRC and RRAO components ([6] to [9]), with DRC capturing jump-to-default risk calibrated to the banking-book credit treatment. A reader should conclude that a complete standardised market-risk charge must include the DRC element and cannot be omitted when assessing capital adequacy.
- **Grounding — this node (Page 383 / para (2)):** "The DRC requirement captures the jump-to-default risk for instruments subject to credit risk ... calibrated based on the credit risk treatment in the banking book"
- **Grounding — related node (Page 382 / para 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"

### [[Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the output-floor calculation, note that the Default Risk Capital requirement links to the Standardized Approach through the floor's prescribed base: para 5.7 lists 'the standardized approach for credit risk' and the securitization DRC component among the standardized approaches used to compute the output floor. This means DRC treatment for securitization exposures feeds the floor via SA/SEC-SA methods, tying an otherwise trading-book/market-risk concept back to SA credit-risk mechanics under the same SAMA framework. Conclude that a bank computing the output floor must apply the standardized DRC methodology (or the specified SEC hierarchy) rather than internal models, and should confirm which nominated approach applies for its securitization positions.
- **Grounding — this node (Page 733 / 5.7(3)):** "For securitization exposures in the banking book and when determining the default risk charge component for securitization exposures in the trading book"
- **Grounding — related node (Page 733 / 5.7(1)):** "The standardized approaches to be used to calculate the base of the output floor... (1) The standardized approach for credit risk"

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
