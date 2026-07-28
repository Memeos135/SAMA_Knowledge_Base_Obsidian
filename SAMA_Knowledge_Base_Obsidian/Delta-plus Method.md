---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Market Risk Sensitivities"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# Delta-plus Method

## Connections

### [[Gamma Risk Capital Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the delta-plus method, do not treat delta capture as sufficient — the same instrument requires that gamma and vega risks be separately measured and charged on top of the delta-equivalent position. SAMA_EN_3553 states delta does not sufficiently cover options risk, so banks writing options must additionally measure gamma and vega to arrive at the total capital requirement. Conclude that a delta-plus capital calculation is incomplete unless the separate gamma (and vega) capital requirements are also computed and added.
- **Grounding — this node (Page 162 / 14.75):** "Separate capital requirements are then applied to the gamma and vega risks of the option positions"
- **Grounding — related node (Page 163 / 14.77):** "since delta does not sufficiently cover the risks associated with options positions, banks will also be required to measure gamma ... and vega ... sensitivities"

### [[Scenario Approach]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When a bank writes options, understand delta-plus and the scenario approach as the two alternative methods offered for the same purpose under the simplified standardised approach — a bank chooses one, not both. The same instrument (SAMA_EN_3553) presents them together: delta-plus uses Greek-letter sensitivities while the scenario approach uses simulation over a scenario grid, and for both the specific risk charge is derived by applying specific risk weights to the delta-equivalent. Conclude that a compliance review should confirm which single method the bank has adopted for its written-option positions and that the associated (gamma/vega or scenario-grid) computations are consistent with the chosen method.
- **Grounding — this node (Page 162 / 14.75):** "The delta-plus method uses the sensitivity parameters or Greek letters associated with options to measure their market risk"
- **Grounding — related node (Page 162 / 14.75):** "The scenario approach uses simulation techniques ... the general market risk charge is determined by the scenario grid ... that produces the largest loss"

### [[Simplified Approach for Options]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When establishing which options capital methodology a bank may use, treat the delta-plus method as a component within the simplified approach for options, not as a standalone alternative regime — the delta-plus method is one of the permissible methods offered under the simplified standardised approach at SAMA's discretion. The instrument (SAMA_EN_3553) states that banks solely holding purchased options may use the basic simplified treatment, while banks that write options are expected to use the delta-plus method or scenario approach. Conclude that eligibility turns on whether the bank writes options; a written-option book cannot rely on the basic simplified treatment and must apply delta-plus (with gamma and vega add-ons) or the scenario approach.
- **Grounding — this node (Page 162 / 14.75):** "the delta-equivalent position of each option becomes part of the simplified standardised approach set out in [14.3] to [14.73]"
- **Grounding — related node (Page 161 / 14.74):** "Those banks which also write options are expected to use the delta-plus method or scenario app[roach]"

### [[Vega Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses the simplified standardised approach for options rather than the full SbM, note that vega risk is handled differently: the delta-plus method carves out options and applies separate capital requirements to their gamma and vega risks. This is a distinct regime from the SbM's vega treatment — the delta-equivalent position enters the general market-risk charge while gamma and vega are charged separately under [14.74] onward. For a compliance decision, confirm which options methodology the bank is entitled to use (simplified approach is limited to firms without significant trading activity) before validating how vega is captured, since the two regimes are not interchangeable.
- **Grounding — this node (Page 162 / [14.75]):** "Separate capital requirements are then applied to the gamma and vega risks of the option positions"
- **Grounding — related node (Page 30 / [7.2](3)):** "all options are subject to vega risk and curvature risk"

#graphify/document #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
