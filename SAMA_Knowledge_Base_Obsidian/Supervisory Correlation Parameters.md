---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "SA-CCR Supervisory Parameters"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR_Supervisory_Parameters
  - graphify/enriched
---

# Supervisory Correlation Parameters

## Connections

### [[Add-on for Commodity Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When validating a commodity-derivative add-on under this SAMA standard, treat the supervisory correlation parameter as a mandatory prescribed input, not a modeling choice: step 5 of the commodity add-on formula (6.73) weights systematic versus idiosyncratic components using ρ, and 6.57 confirms these correlation parameters apply specifically to equity, credit and commodity asset classes. The correlation values are fixed in Table 2 under 6.75. Conclude that a commodity add-on using any correlation other than the supervisory-prescribed figure is non-compliant, and check the value against Table 2 rather than accepting a bank-derived estimate.
- **Grounding — this node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."
- **Grounding — related node (Page 44 / 6.73(5)):** "𝜌 is the supervisory prescribed correlation factor corresponding to the commodity type."

### [[Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a credit-derivative add-on, note that the offsetting/hedging benefit between reference entities is governed entirely by the supervisory correlation factor: 6.65–6.66 weight the systematic and idiosyncratic components by this correlation, and 6.57 confirms the correlation parameters apply to the credit asset class and are prescribed in Table 2. A higher correlation increases systematic offset but does not always reduce the charge (it can increase it for one-directional portfolios). Conclude that the correct capital outcome depends on using the prescribed correlation for the correct rating/subclass, so verify the value against Table 2 rather than assuming a directional effect.
- **Grounding — this node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."
- **Grounding — related node (Page 41 / 6.65):** "These two components are weighted by a correlation factor which determines the degree of offsetting / hedging benefit within the credit derivatives asset class."

### [[Add-on for Equity Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When checking an equity-derivative add-on, remember the standard bars banks from any modeling assumptions (6.71) and forces use of prescribed inputs: the supervisory correlation parameters under 6.57 apply to the equity asset class alongside its two fixed supervisory factors for single names and indices. The correlation weights the systematic versus idiosyncratic offset in the same way as for credit and commodity. Conclude that an equity add-on relying on internally estimated correlation or beta is non-compliant, and confirm the correlation figure used matches Table 2 under 6.75.
- **Grounding — this node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."
- **Grounding — related node (Page 43 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons, including estimating individual volatilities or taking publicly available estimates of beta."

### [[Table 2 Summary of Supervisory Parameters|Table 2: Summary of Supervisory Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the supervisory correlation parameters, treat Table 2 as the authoritative source of the actual numeric values: 6.57 states the parameters are 'set out in Table 2 under 6.75', and 6.75 confirms Table 2 lists supervisory factors, correlations and option-volatility add-ons per asset class and subclass (e.g. 50% correlation for single-name credit). Conclude that no correlation input is validly used unless it is drawn from the Table 2 figure for the correct asset class/subclass, and read the two provisions together rather than relying on the descriptive text of 6.57 alone.
- **Grounding — this node (Page 37 / 6.57):** "...are set out in Table 2 under 6.75."
- **Grounding — related node (Page 45 / 6.75):** "Table 2 includes the supervisory factors, correlations and supervisory option volatility add-ons for each asset class and subclass."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Supervisory_Parameters #graphify/enriched
