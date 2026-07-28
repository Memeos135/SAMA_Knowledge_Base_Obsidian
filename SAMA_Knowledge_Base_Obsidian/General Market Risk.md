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

# General Market Risk

## Connections

### [[Duration Method]] — `references` [EXTRACTED]
- **What this link tells you:** When electing a method to measure general market risk for interest-rate positions, note that the duration method is an alternative, more granular measurement of general market risk that requires SAMA's consent and must be used continuously once adopted. The provision expressly frames the duration method as a way to measure 'all of their general market risk' by calculating each position's price sensitivity separately, subject to SAMA monitoring. Conclude that using the duration method is not a free choice: it needs prior SAMA approval, binds the bank to consistent application, and any switch back requires further SAMA approval.
- **Grounding — this node (Page 146 / [14.29]):** "Banks must elect and use the method on a continuous basis (unless a change in method is approved by SAMA)"
- **Grounding — related node (Page 146 / [14.29]):** "banks with the necessary capability may, with SAMA' consent, use a more accurate method of measuring all of their general market risk by calculating the price sensitivity of each position separately"

### [[Equity Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the equity charge under the standardised approaches, understand that equity risk is one of the defined risk classes that feeds the overall general market risk measurement, and that under the simplified standardised approach equity, interest rate, FX and commodities charges are summed arithmetically. The framework lists equity risk within the enumerated risk classes and directs that these component risk measures be aggregated for the capital requirement. Conclude that the equity charge is not standalone but part of the summed general market risk total, and check [14.1]–[14.73] for the applicable equity computation.
- **Grounding — this node (Page 134 / [14.1]):** "the measures of risk obtained ... summed arithmetically"
- **Grounding — related node (Page 134 / [14.1]):** "[14.3] to [14.73] deal with interest rate, equity, foreign exchange (FX) and commodities risk"

### [[Interest Rate Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When distinguishing risk types for market risk capital, understand that general market risk is a cross-cutting component (broad market-wide price movement) that applies to interest-rate instruments alongside specific risk, and interest rate risk is one of the defined risk classes to which it attaches. The glossary anchors 'general interest rate risk' as a listed risk class, and the simplified-approach text (14.75) confirms option carve-outs generate capital incorporating 'both general market risk and specific risk' added back to the interest-rate category. For a capital calculation you would therefore treat general market risk and interest rate risk as related layers — general market risk is measured within the interest-rate class, not as a substitute for it — and ensure both the general and specific components are captured for interest-rate positions.
- **Grounding — this node (Page 162 / 14.75):** "subject to separately calculated capital requirements that incorporate both general market risk and specific risk."
- **Grounding — related node (Page 5 (glossary)):** "Risk class: A defined list of risks... general interest rate risk, credit spread risk (non-securitisation)... FX risk, equity risk and commodity risk."

### [[Maturity Method]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's market risk capital charge for interest-rate and options positions under the simplified standardised approach, do not treat general market risk and the maturity method as independent inputs — the maturity method is one of the mechanics through which the general market risk charge is measured. The same instrument (SAMA_EN_3553) links them by requiring delta-weighted and derivative positions to be slotted into maturity time bands (with sub-three-month positions floored at a three-month weighting) before the general market risk charge is applied. Conclude that any assessment of the general market risk requirement for these positions must confirm correct maturity treatment, since the maturity determination feeds directly into the capital number.
- **Grounding — this node (Page 26 / 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach"
- **Grounding — related node (Page 78 / 8.17-8.18):** "the maturity of the derivative contract is considered in determining the offsetting criterion, not the maturity of the underlying instrument"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
