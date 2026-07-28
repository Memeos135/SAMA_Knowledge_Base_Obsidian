---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Risk-Weighted Assets Overview"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Risk-Weighted_Assets_Overview
  - graphify/enriched
---

# RWA for Credit Risk

## Connections

### [[Off-Balance Sheet Items  CCFs|Off-Balance Sheet Items / CCFs]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** If you are reconciling how a bank's off-balance-sheet items feed capital, note that the two documents use the same standardized-credit-risk machinery for different regulatory purposes and should not be conflated. The Leverage ratio's OBS treatment (para 7.4.2) applies the standardized approach for credit risk's credit conversion factors to bring commitments and credit substitutes into the leverage exposure measure, while the Output Floor document's RWA-for-credit-risk (para 5.4) uses that same credit-risk framework to build the risk-weighted denominator — a leverage (non-risk-based) metric versus a risk-based capital metric. This link appears to reflect shared reliance on the SAMA Minimum Capital Requirements for Credit Risk rather than a direct cross-reference; verify the primary text of each instrument before treating a CCF or risk-weight computed for one purpose as valid for the other.
- **Grounding — this node (Page 5 / Para 5.4):** "RWA for credit risk and counterparty credit risk is calculated as the sum of the following: Credit RWA for banking book exposures... using the standardized approach... or the IRB approach."
- **Grounding — related node (Page 29 / Para 7.4.2):** "The standardized approach for credit risk as it applies to individual claims and the standardized approach for [OBS items inclusion in the Leverage ratio exposure measure]."
- **Caveat:** Relation is INFERRED: the two provisions share the underlying SAMA credit-risk standard but serve distinct metrics (leverage vs risk-based RWA); confirm each document's own text before relying on cross-use.

### [[Output Floor (72.5% RWA)]] — `references` [EXTRACTED]
- **What this link tells you:** When assembling the output floor, recognize that credit-risk RWA is the largest input element and that the floor changes which credit-risk method is admissible. Para 5.3 requires the floor comparator to be built from the credit-risk RWA of para 5.4, but para 5.8 prohibits the IRB approach and SEC-IRBA from the floor base — so a bank on IRB for its nominated RWA must recompute credit-risk RWA on the standardized approach solely for the 72.5% calculation. Conclude that the credit-risk figure entering the floor may differ materially from the credit-risk figure in the bank's own capital calculation, and both must be produced.
- **Grounding — this node (Page 5 / Para 5.4(1)):** "Credit RWA for banking book exposures... calculated using: (a) The standardized approach... or (b) The internal ratings-based (IRB) approach."
- **Grounding — related node (Page 4 / Para 5.3 & Page 8 / Para 5.8):** "RWA for credit risk (as calculated in paragraphs 5.4)... the following approaches are not permitted... IRB approach to credit risk; SEC-IRBA."

#graphify/concept #graphify/EXTRACTED #community/Risk-Weighted_Assets_Overview #graphify/enriched
