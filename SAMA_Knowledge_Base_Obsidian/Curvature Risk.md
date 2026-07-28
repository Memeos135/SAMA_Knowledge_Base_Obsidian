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

# Curvature Risk

## Connections

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When computing SbM capital, treat curvature risk as one of the three mandated components of the Sensitivities-Based Method (alongside delta and vega), not an optional add-on. The framework defines curvature as capturing incremental risk not captured by delta for optionality, requires it for all instruments with non-linear payoffs, and specifies its own correlation aggregation (delta correlations squared, with a CTP carve-out). Conclude that any portfolio with options or non-linear cash flows must include a curvature charge in its SbM calculation, using curvature-specific correlation parameters rather than the plain delta parameters.
- **Grounding — this node (Page 30):** "all options are subject to vega risk and curvature risk. Instruments whose cash flows can be written as a linear function ... are not subject to vega risk nor [curvature]"
- **Grounding — related node (Page 27):** "Curvature: a risk measure which captures the incremental risk not captured by the delta risk measure for price changes in an option."

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
