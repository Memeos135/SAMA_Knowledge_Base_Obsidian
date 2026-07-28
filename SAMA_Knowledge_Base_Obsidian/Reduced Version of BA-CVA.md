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

# Reduced Version of BA-CVA

## Connections

### [[Basic Approach for CVA (BA-CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's CVA capital charge, treat the reduced BA-CVA as one of two selectable forms within the single BA-CVA regime rather than a separate method. Paragraph 11.13-11.14 establishes that the reduced version 'eliminates the element of hedging recognition' and applies a 0.65 discount scalar, and it is 'also part of the full BA-CVA capital calculations.' Conclude that a bank on the reduced version cannot claim hedge offsets, and that Template CVA1 (reduced BA-CVA) governs its disclosure obligation.
- **Grounding — this node (Page 639 / 11.14):** "The reduced version eliminates the element of hedging recognition from the full version... designed to simplify BA-CVA implementation for less sophisticated banks that do not hedge CVA."
- **Grounding — related node (Page 636 / 11.7):** "Two approaches are available for calculating CVA capital: the standardized approach (SA-CVA) and the basic approach (BA-CVA)."

### [[Full Version of BA-CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When choosing between the two BA-CVA variants, understand they are nested, not independent: the reduced version is a component of the full version's calculation, used 'as a conservative means to limit hedging recognition.' The full version recognizes counterparty spread hedges and suits banks that hedge CVA, while the reduced version zeroes out hedge recognition for non-hedging banks. Conclude that a bank claiming hedge benefits must run the full BA-CVA and its more demanding inputs, and that the reduced figure acts as a floor on how much hedging benefit the full version can deliver.
- **Grounding — this node (Page 639):** "the reduced BA-CVA is also part of the full BA-CVA capital calculations as a conservative means to limit hedging recognition."
- **Grounding — related node (Page 639 / 11.13):** "The full version recognizes counterparty spread hedges and is intended for banks that hedge CVA risk."

### [[SA-CVA Delta and Vega Risk Classes]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** This link appears to connect two alternative CVA capital methodologies rather than a defining or subordinating relationship. The reduced BA-CVA (a simplified, hedge-blind formula with a 0.65 scalar) and the SA-CVA delta/vega six-risk-class approach both measure CVA risk capital, but they are distinct regimes with different eligibility and approval requirements — SA-CVA requires SAMA approval per 11.7. Before relying on any equivalence, verify against the primary text that a bank may not mix them within a netting set except under the carve-out rules; they are parallel options, not interchangeable inputs.
- **Grounding — this node (Page 639 / 11.14):** "The capital requirement for CVA risk under the reduced version of the BA-CVA... where the discount scalar = 0.65."
- **Grounding — related node (Page 652 / 11.43):** "The capital requirements for delta risk are calculated as the simple sum of delta capital requirements calculated independently for the following six risk classes."
- **Caveat:** INFERRED link; the two are alternative CVA approaches (BA-CVA vs SA-CVA), not a definitional relationship — confirm scope and approval conditions in the primary text before treating them as related.

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
