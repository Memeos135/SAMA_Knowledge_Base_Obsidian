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

# Residual Risk Add-On (RRAO)

## Connections

### [[Exotic Underlying Instruments]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying which trading-book instruments attract the residual risk add-on, treat 'exotic underlying' as one of the two triggering categories the RRAO is designed to capture. The framework requires the RRAO for all instruments bearing residual risk, and defines instruments with an exotic underlying as those whose underlying exposure is outside the scope of delta, vega, curvature or DRC treatment — precisely the residual gap the RRAO addresses. For a compliance conclusion, confirm that any position with a non-standard underlying (e.g. future realised volatility) is flagged for the additional RRAO charge on top of other standardised components, since it will otherwise be under-capitalised.
- **Grounding — this node (Page 86 / [9.1]-[9.2]):** "The residual risk add-on (RRAO) is to be calculated for all instruments bearing residual risk ... Instruments with an exotic underlying and instruments bearing other residual risks are subject to the RRAO"
- **Grounding — related node (Page 86 / [9.3]):** "Instruments with an exotic underlying are trading book instruments with an underlying exposure that is not within the scope of delta, vega or curvature risk treatment"

### [[Other Residual Risks]] — `references` [EXTRACTED]
- **What this link tells you:** When determining RRAO scope, 'other residual risks' is the second triggering category alongside exotic underlyings, capturing instruments with vega/curvature charges whose pay-offs cannot be replicated as a finite linear combination of vanilla options, plus CTP instruments. Note the framework's exclusions matter for the compliance conclusion: back-to-back matched transactions and listed/centrally-cleared instruments are carved out of the RRAO ([9.7]). For a decision, check both that qualifying gap, correlation and behavioural-risk instruments are included and that the specified exemptions are correctly applied, since over- or under-scoping the RRAO directly changes the standardised capital charge.
- **Grounding — this node (Page 87 / [9.7]):** "Any instrument that is listed and/or eligible for central clearing must be excluded from the RRAO"
- **Grounding — related node (Page 87 / [9.4]):** "Instruments subject to vega or curvature risk capital requirements ... with pay-offs that cannot be written or perfectly replicated as a finite linear combination of vanilla options"

### [[Standardized Approach]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** If you are mapping the components of the market-risk standardised approach, treat the RRAO as a mandatory add-on that sits inside that SA rather than as a free-standing charge — the two concepts appear linked because the market-risk SA (which parallels but is distinct from the credit-risk SA of SAMA_EN_3487) is built from the sensitivities-based method, default risk charge and residual risk add-on set out in [6] through [9]. The connection here is conceptual: 'standardised approach' is the umbrella methodology and RRAO is one of its structural sub-components. Verify against the primary text of SAMA_EN_3553 sections [6]–[9] before relying on the precise scope of instruments that attract the RRAO, and do not conflate this SA-internal add-on with anything in the credit-risk SA.
- **Grounding — this node (Page 26 / para 5.33 / section 6):** "Internal CVA risk transfers that are subject to curvature, default risk or residual risk add-on as set out in [6] through [9]"
- **Grounding — related node (Page 733 / para 5.7):** "(1) The standardized approach for credit risk. (2) The bank's nominated approach for equity investments in funds."
- **Caveat:** Relation is conceptually_related_to; the two 'standardised approaches' belong to different regimes (credit vs market risk). Confirm the RRAO's placement within the market-risk SA structure in SAMA_EN_3553 [6]-[9] before relying.

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
