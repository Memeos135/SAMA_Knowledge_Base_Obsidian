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

# Vega Risk

## Connections

### [[Delta-plus Method]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses the simplified standardised approach for options rather than the full SbM, note that vega risk is handled differently: the delta-plus method carves out options and applies separate capital requirements to their gamma and vega risks. This is a distinct regime from the SbM's vega treatment — the delta-equivalent position enters the general market-risk charge while gamma and vega are charged separately under [14.74] onward. For a compliance decision, confirm which options methodology the bank is entitled to use (simplified approach is limited to firms without significant trading activity) before validating how vega is captured, since the two regimes are not interchangeable.
- **Grounding — this node (Page 30 / [7.2](3)):** "all options are subject to vega risk and curvature risk"
- **Grounding — related node (Page 162 / [14.75]):** "Separate capital requirements are then applied to the gamma and vega risks of the option positions"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the SbM capital calculation, vega risk must be included for all instruments with optionality, alongside delta and curvature. The framework defines vega as a risk measure based on sensitivities to regulatory vega risk factors and states that the SbM requirement is the aggregation of delta, vega and curvature; critically, instruments whose cash flows cannot be written as a linear function of underlying notional (all options) are subject to vega risk, while linear instruments are not. For a compliance conclusion, verify that optionality-bearing positions carry a vega charge and that non-optional instruments are correctly excluded, since misclassification changes the SbM total.
- **Grounding — this node (Page 30 / [7.2](3)):** "all options are subject to vega risk and curvature risk ... instruments without optionality ... are not subject to vega risk nor curvature risk capital requirements"
- **Grounding — related node (Page 30 / [7.3]):** "the capital requirement under the sensitivities-based method is calculated by aggregating delta, vega and curvature capita[l]"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
