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

# Standardised Approach (Market Risk)

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating market-risk capital under the mandatory standardised approach, treat the Default Risk Capital (DRC) requirement as one of the required components of that approach, not an optional add-on. The framework describes the standardised approach as built from sensitivities-based, DRC and RRAO components ([6] to [9]), with DRC capturing jump-to-default risk calibrated to the banking-book credit treatment. A reader should conclude that a complete standardised market-risk charge must include the DRC element and cannot be omitted when assessing capital adequacy.
- **Grounding — this node (Page 382 / para 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"
- **Grounding — related node (Page 383 / para (2)):** "The DRC requirement captures the jump-to-default risk for instruments subject to credit risk ... calibrated based on the credit risk treatment in the banking book"

### [[Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping RWA reporting rows to capital requirements, note that the credit-risk minimum requirements identify the standardised approach as a defined sub-method ('Of which: standardised approach') specified in SCRE5 to SCRE9. The link tells you the standardised approach is not a free-standing regime but the default credit-risk measurement route, expressly including failed trades and non-DvP transactions per SCRE25. A reader should conclude that where IRB/slotting approvals do not apply, the standardised approach governs, and its scope pulls in the settlement-risk items reported separately in the disclosure templates.
- **Grounding — this node (Page 755):** "Definition of standardised approach ... This also includes failed trades and non-delivery-versus-payment transactions as set out in SCRE25"
- **Grounding — related node (Page 751):** "Of which: standardised approach: RWA and capital requirements according to the standardised approach to credit risk (as specified in SCRE5 to SCRE9)"

### [[Residual Risk Add-On (RRAO)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the mandatory standardised market-risk charge, include the Residual Risk Add-On (RRAO) as a component covering risks the sensitivities-based and DRC methods do not capture. The framework introduces the RRAO expressly 'to ensure sufficient coverage of market risks' for instruments specified in [9.2], within the standardised approach structure that all banks must use per 6.1. A reader should conclude that instruments with residual/exotic risks attract the RRAO in addition to core standardised charges, and cannot be treated as fully captured by the sensitivities-based method alone.
- **Grounding — this node (Page 382 / para 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"
- **Grounding — related node (Page 383 / para (3)):** "An RRAO is thus introduced to ensure sufficient coverage of market risks for instruments specified in [9.2]. The calculation method for the RRAO is set out in [9.8]"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When building the standardised market-risk capital charge, treat the sensitivities-based method as the core component delivering the delta, vega and curvature measures aggregated using specified correlation parameters. Since 6.1 makes the standardised approach mandatory for all banks and the framework specifies computing three sensitivities-based values under different correlation scenarios, this method is a required calculation, not a modelling choice. A reader should conclude the sensitivities-based method, alongside DRC and RRAO, forms the standardised charge, and stress-scenario correlation values must be applied as prescribed in [7.6]–[7.7].
- **Grounding — this node (Page 382 / para 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"
- **Grounding — related node (Page 383 / para (d)):** "a bank must calculate three sensitivities-based method capital requirement values, based on three different scenarios on the specified values for the correlation parameters"

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
