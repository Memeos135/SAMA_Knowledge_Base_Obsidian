---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# SA-CVA Delta and Vega Risk Classes

## Connections

### [[Reduced Version of BA-CVA]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** This link appears to connect two alternative CVA capital methodologies rather than a defining or subordinating relationship. The reduced BA-CVA (a simplified, hedge-blind formula with a 0.65 scalar) and the SA-CVA delta/vega six-risk-class approach both measure CVA risk capital, but they are distinct regimes with different eligibility and approval requirements — SA-CVA requires SAMA approval per 11.7. Before relying on any equivalence, verify against the primary text that a bank may not mix them within a netting set except under the carve-out rules; they are parallel options, not interchangeable inputs.
- **Grounding — this node (Page 652 / 11.43):** "The capital requirements for delta risk are calculated as the simple sum of delta capital requirements calculated independently for the following six risk classes."
- **Grounding — related node (Page 639 / 11.14):** "The capital requirement for CVA risk under the reduced version of the BA-CVA... where the discount scalar = 0.65."
- **Caveat:** INFERRED link; the two are alternative CVA approaches (BA-CVA vs SA-CVA), not a definitional relationship — confirm scope and approval conditions in the primary text before treating them as related.

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank has SAMA approval to use SA-CVA, understand that its CVA capital is built from delta and vega risk-class charges that must be mapped consistently with the underlying counterparty exposures produced under the CCR framework. SA-CVA capital is the sum of delta charges across six risk classes (including counterparty and reference credit spread) plus vega across five, with an eligible credit-spread hedge assigned entirely to one class and never split. You would conclude that classifying an instrument into the wrong risk class, or splitting a hedge, misstates the capital charge, so the risk-class mapping must be checked before relying on any SA-CVA figure.
- **Grounding — this node (Page 652 / 11.43-11.44):** "delta capital requirements calculated independently for the following six risk classes... Instruments must not be split between the two risk classes"
- **Grounding — related node (Page 636 / 11.7):** "Two approaches are available for calculating CVA capital: the standardized approach (SA-CVA) and the basic approach (BA-CVA)"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
