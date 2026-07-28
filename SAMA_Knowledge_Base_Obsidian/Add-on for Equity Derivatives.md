---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR Derivative Add-ons"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR_Derivative_Add-ons
  - graphify/enriched
---

# Add-on for Equity Derivatives

## Connections

### [[Add-on for Credit Derivatives]] — `semantically_similar_to` [EXTRACTED]
- **What this link tells you:** When scoping the add-on methodology for different derivative asset classes, do not assume the credit and equity add-ons are interchangeable, even though the framework itself notes the equity calculation is 'very similar' to the credit one. Both share the same effective-notional structure (adjusted notional × supervisory delta × maturity factor) and use supervisory correlation parameters splitting systematic and idiosyncratic components, but the calibration differs — equity uses only two prescribed supervisory factors (single-entity and index) with no modelling permitted. Treat the shared mechanics as a reason to read the two sections in parallel, but apply each asset class's own supervisory factors and hedging-set rules rather than porting parameters across.
- **Grounding — this node (Page 43 / 6.68, 6.71):** "The calculation of the add-on for the equity derivative asset class is very similar... bank must only use the two values of supervisory factors that are defined for equity derivatives"
- **Grounding — related node (Page 41 / 6.65-6.67):** "These two components are weighted by a correlation factor which determines the degree of offsetting / hedging benefit within the credit derivatives asset class."

### [[Supervisory Correlation Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When checking an equity-derivative add-on, remember the standard bars banks from any modeling assumptions (6.71) and forces use of prescribed inputs: the supervisory correlation parameters under 6.57 apply to the equity asset class alongside its two fixed supervisory factors for single names and indices. The correlation weights the systematic versus idiosyncratic offset in the same way as for credit and commodity. Conclude that an equity add-on relying on internally estimated correlation or beta is non-compliant, and confirm the correlation figure used matches Table 2 under 6.75.
- **Grounding — this node (Page 43 / 6.71):** "Banks are not permitted to make any modelling assumptions in the calculation of the PFE add-ons, including estimating individual volatilities or taking publicly available estimates of beta."
- **Grounding — related node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
