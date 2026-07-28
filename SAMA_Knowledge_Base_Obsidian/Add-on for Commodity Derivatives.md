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

# Add-on for Commodity Derivatives

## Connections

### [[Hedging Set]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the commodity add-on, you must first allocate trades into the four prescribed hedging sets (energy, metals, agriculture, other) as defined in 6.48(5), because the commodity add-on calculation (6.72 onward) proceeds hedging-set by hedging-set with limited offsetting between them. This link tells you the hedging-set definitions are a mandatory structural input, not a modelling choice, and that SAMA may require more refined commodity definitions where basis risk is material. When reviewing a commodity add-on, verify trades are mapped to the correct hedging set and that any within-set offsetting respects the prescribed correlation factors.
- **Grounding — this node (Page 44 / Step 2):** "Allocate the trades in commodity derivative asset class to hedging sets... four hedging sets consisting of derivatives that reference: energy, metals, agriculture and other commodities"
- **Grounding — related node (Page 34 / 6.48(5)):** "Commodity derivatives consist of four hedging sets defined for broad categories of commodity derivatives: energy, metals, agricultural and other commodities"

### [[Supervisory Correlation Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When validating a commodity-derivative add-on under this SAMA standard, treat the supervisory correlation parameter as a mandatory prescribed input, not a modeling choice: step 5 of the commodity add-on formula (6.73) weights systematic versus idiosyncratic components using ρ, and 6.57 confirms these correlation parameters apply specifically to equity, credit and commodity asset classes. The correlation values are fixed in Table 2 under 6.75. Conclude that a commodity add-on using any correlation other than the supervisory-prescribed figure is non-compliant, and check the value against Table 2 rather than accepting a bank-derived estimate.
- **Grounding — this node (Page 44 / 6.73(5)):** "𝜌 is the supervisory prescribed correlation factor corresponding to the commodity type."
- **Grounding — related node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
