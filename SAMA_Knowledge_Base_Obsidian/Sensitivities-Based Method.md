---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Sensitivities"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# Sensitivities-Based Method

## Connections

### [[Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the Sensitivities-Based Method to credit-spread positions, recognise that the Correlation Trading Portfolio (CTP) is a defined sub-category that alters the standard SbM correlation treatment rather than a separate regime. The framework introduces a specific definition of the correlation trading portfolio and, for CSR securitisations (CTP), disapplies the ordinary basis and tenor correlation parameters, using only a same-name correlation instead. Conclude that CTP-classified positions must be run through the SbM with these modified correlation rules, and standard bucket correlations cannot be assumed for them.
- **Grounding — this node (Page 27):** "the risk-weighted sensitivities are aggregated using specified correlation parameters ... a bank must calculate three sensitivities-based method capital requirement values"
- **Grounding — related node (Page 27 / 6.5):** "Definition of correlation trading portfolio ... CSR securitisations (CTP)"

### [[Curvature Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When computing SbM capital, treat curvature risk as one of the three mandated components of the Sensitivities-Based Method (alongside delta and vega), not an optional add-on. The framework defines curvature as capturing incremental risk not captured by delta for optionality, requires it for all instruments with non-linear payoffs, and specifies its own correlation aggregation (delta correlations squared, with a CTP carve-out). Conclude that any portfolio with options or non-linear cash flows must include a curvature charge in its SbM calculation, using curvature-specific correlation parameters rather than the plain delta parameters.
- **Grounding — this node (Page 27):** "Curvature: a risk measure which captures the incremental risk not captured by the delta risk measure for price changes in an option."
- **Grounding — related node (Page 30):** "all options are subject to vega risk and curvature risk. Instruments whose cash flows can be written as a linear function ... are not subject to vega risk nor [curvature]"

### [[Default Risk Capital (DRC) Requirement]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When building the standardised market risk capital charge, treat the DRC requirement and the sensitivities-based method as complementary components, not substitutes. The framework introduces DRC precisely to capture jump-to-default risk 'that may not be captured by credit spread shocks under the sensitivities-based method,' meaning the two address different risk dimensions of the same credit instruments. For the capital total, you would add both (plus RRAO) rather than choose between them, and should confirm that credit positions are run through both to avoid a coverage gap.
- **Grounding — this node (SAMA_EN_3553 / Page 27):** "a bank must calculate three sensitivities-based method capital requirement values, based on three different scenarios on the specified values for the correlation parameters"
- **Grounding — related node (SAMA_EN_3553 / Page 73, [8.1]):** "jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-based method"

### [[Delta Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's standardised market-risk capital charge under SAMA_EN_3553, treat delta risk as one of the three mandatory components of the sensitivities-based method (SbM), not as a standalone calculation. The framework defines the SbM capital requirement as an aggregation of delta, vega and curvature capital requirements ([7.3]), with delta being the sensitivity-based risk position for each regulatory risk factor. For a compliance check, confirm that any SbM capital number includes a properly-computed delta component across all applicable risk classes, since omitting it would understate the standardised charge SAMA requires.
- **Grounding — this node (Page 30 / [7.3]):** "the capital requirement under the sensitivities-based method is calculated by aggregating delta, vega and curvature capital [requirements]"
- **Grounding — related node (Page 27 / [6.4]):** "Delta: a risk measure based on sensitivities of a bank's trading book to regulatory delta risk factors"

### [[Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping a bank's capital methodologies across risk types, recognize that 'Standardized Approach' is used in two distinct SAMA frameworks: credit risk (SAMA_EN_3487) and market risk (SAMA_EN_3553), where the Sensitivities-Based Method is the core building block of the market-risk standardised approach. The link connects the credit-risk standardized concept to the market-risk SbM component, which measures delta, vega and curvature risk. You would conclude these are separate capital charges with different rules, and should not treat credit-risk standardized methodology and the market-risk SbM as interchangeable — confirm which framework governs the instrument in question.
- **Grounding — this node (Page 27):** "a bank must calculate three sensitivities-based method capital requirement values, based on three different scenarios on the specified values for the correlation parameters"
- **Grounding — related node (Page 733 / 5.7):** "The standardized approaches to be used to calculate the base of the output floor...(1) The standardized approach for credit risk."
- **Caveat:** Cross-document 'references' link rests on the shared 'standardised approach' label spanning two different risk frameworks; confirm which regime (credit vs market risk) applies before relying on it.

### [[Vega Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the SbM capital calculation, vega risk must be included for all instruments with optionality, alongside delta and curvature. The framework defines vega as a risk measure based on sensitivities to regulatory vega risk factors and states that the SbM requirement is the aggregation of delta, vega and curvature; critically, instruments whose cash flows cannot be written as a linear function of underlying notional (all options) are subject to vega risk, while linear instruments are not. For a compliance conclusion, verify that optionality-bearing positions carry a vega charge and that non-optional instruments are correctly excluded, since misclassification changes the SbM total.
- **Grounding — this node (Page 30 / [7.3]):** "the capital requirement under the sensitivities-based method is calculated by aggregating delta, vega and curvature capita[l]"
- **Grounding — related node (Page 30 / [7.2](3)):** "all options are subject to vega risk and curvature risk ... instruments without optionality ... are not subject to vega risk nor curvature risk capital requirements"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
