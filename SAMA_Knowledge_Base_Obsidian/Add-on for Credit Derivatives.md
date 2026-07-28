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

# Add-on for Credit Derivatives

## Connections

### [[Add-on for Equity Derivatives]] — `semantically_similar_to` [EXTRACTED]
- **What this link tells you:** When scoping the add-on methodology for different derivative asset classes, do not assume the credit and equity add-ons are interchangeable, even though the framework itself notes the equity calculation is 'very similar' to the credit one. Both share the same effective-notional structure (adjusted notional × supervisory delta × maturity factor) and use supervisory correlation parameters splitting systematic and idiosyncratic components, but the calibration differs — equity uses only two prescribed supervisory factors (single-entity and index) with no modelling permitted. Treat the shared mechanics as a reason to read the two sections in parallel, but apply each asset class's own supervisory factors and hedging-set rules rather than porting parameters across.
- **Grounding — this node (Page 41 / 6.65-6.67):** "These two components are weighted by a correlation factor which determines the degree of offsetting / hedging benefit within the credit derivatives asset class."
- **Grounding — related node (Page 43 / 6.68, 6.71):** "The calculation of the add-on for the equity derivative asset class is very similar... bank must only use the two values of supervisory factors that are defined for equity derivatives"

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the SA-CCR add-on for the credit derivative asset class, Step 1 is to compute each trade's effective notional (adjusted notional × supervisory delta × maturity factor) exactly as defined in 6.35–6.56, then aggregate per referenced entity/index before applying the supervisory factor. So the credit add-on cannot be built without first producing the effective notional per trade. For a calculation-review decision, confirm the effective-notional step is completed and correctly signed before entity-level aggregation and correlation weighting are applied; errors upstream in effective notional propagate directly into the credit derivatives add-on and hence PFE.
- **Grounding — this node (Page 40 / 6.63 Step 1):** "Calculate the effective notional for each trade in the netting set that is in the credit derivative asset class... 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖, where each term is as defined in 6.35 to 6.56."
- **Grounding — related node (Page 130 / 12.31):** "The effective notional for each trade in the netting set (𝐴�𝑖) is calculated using the formula 𝐴�𝑖 = 𝑐�𝑖 ∗ 𝑀𝐴�𝑖 ∗ 𝛼�𝑖"

### [[SA-CCR Sample Portfolio Examples]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying how the credit-derivative add-on rules translate into an EAD figure, consult the Chapter 12 sample portfolios as the framework's own illustration of the aggregation formula (EAD = alpha × (RC + multiplier × aggregate add-on)) into which the credit add-on components feed. The connection is grounded in both sections belonging to the SA-CCR chapter and sharing the effective-notional and asset-class-level add-on constructs. Note, however, that the provided sample context is Example 1, an interest-rate portfolio — confirm which worked example (if any) covers credit derivatives before treating it as a direct illustration of the 6.63+ rules; otherwise rely on the substantive credit add-on text.
- **Grounding — this node (Page 40 / 6.63):** "The calculation of the add-on for the credit derivative asset class only gives full recognition [of offsetting]... Each separate credit index... should be treated as a separate entity."
- **Grounding — related node (Page 123 / 12.2):** "The EAD for all netting sets in SA-CCR is given by the following formula, where alpha is assigned a value of 1.4"
- **Caveat:** Provided sample-portfolio context shows an interest-rate example; verify whether a credit-derivative worked example exists before relying on it to illustrate the credit add-on.

### [[Supervisory Correlation Parameters]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a credit-derivative add-on, note that the offsetting/hedging benefit between reference entities is governed entirely by the supervisory correlation factor: 6.65–6.66 weight the systematic and idiosyncratic components by this correlation, and 6.57 confirms the correlation parameters apply to the credit asset class and are prescribed in Table 2. A higher correlation increases systematic offset but does not always reduce the charge (it can increase it for one-directional portfolios). Conclude that the correct capital outcome depends on using the prescribed correlation for the correct rating/subclass, so verify the value against Table 2 rather than assuming a directional effect.
- **Grounding — this node (Page 41 / 6.65):** "These two components are weighted by a correlation factor which determines the degree of offsetting / hedging benefit within the credit derivatives asset class."
- **Grounding — related node (Page 37 / 6.57):** "The supervisory correlation parameters (ρi) only apply to the PFE add-on calculation for equity, credit and commodity derivatives."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
