---
source_file: "markdown/SAMA_EN_3343_VER1.md"
type: "concept"
community: "PSIA Liquidity Requirements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/PSIA_Liquidity_Requirements
  - graphify/enriched
---

# Loans to Deposits Ratio (LDR)

## Connections

### [[LCRNSFR Liquidity Ratios|LCR/NSFR Liquidity Ratios]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** If you are mapping a bank's regulatory liquidity obligations, note that the LDR referenced in the ILAAP guideline appears to be the same ratio governed in detail by the standalone Loans to Deposits Ratio Guidelines — the two documents seem to connect through the shared LDR metric rather than one defining the other. The ILAAP guideline lists LDR alongside LCR, NSFR and the SAMA Liquidity Ratio as regulatory limits to be reported, while the LDR Guidelines supply the actual definition, weighted-denominator method and the sub-90% expectation. Verify the primary LDR Guidelines (effective June 2023, superseding the earlier circulars) for the binding calculation rules before relying on the ILAAP text, since the ILAAP document only names LDR as one of several reporting benchmarks.
- **Grounding — this node (Page 4-5 / Sections 4.1, 4.5):** "The Loans to Deposits Ratio is defined as net loans divided by deposits after applying weights... SAMA expects banks to maintain total LDR below 90%."
- **Grounding — related node (Page 13 / Section 6.2):** "Regulatory Liquidity requirements under LCR, NSFR, LDR, and SAMA Liquidity Ratio."
- **Caveat:** Relation is INFERRED: the ILAAP guideline only names LDR among several ratios; it does not cite the LDR Guidelines document. Confirm the current LDR Guidelines version for binding calculation rules.

### [[Loans to Deposits Ratio Guidelines]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what obligation this instrument imposes, note the LDR is the operative regulatory ratio the guidelines exist to define and cap. The document defines LDR as net loans divided by weighted deposits and states SAMA expects banks to maintain total LDR below 90%, subject to the numerator not exceeding the unweighted denominator, reportable monthly on a consolidated basis. Treat the sub-90% expectation and the reporting frequency as the enforceable core; the surrounding definitions of numerator/denominator scope what counts toward it.
- **Grounding — this node (SAMA_EN_3343_VER1 Page 5 / 4.5):** "SAMA expects banks to maintain total LDR below 90%, Subject to numerator not exceeding unweighted denominator"
- **Grounding — related node (SAMA_EN_3343_VER1 Page 4 / 4.1):** "The Loans to Deposits Ratio is defined as net loans divided by deposits after applying weights"

### [[Weighted Denominator Calculation]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When computing the LDR you cannot apply the sub-90% limit correctly without first building the weighted denominator, because the ratio is defined as net loans over weighted deposits. Section 5 sets the maturity-bucket weights (100% to 190%) applied to denominator components, and 4.5 conditions the ratio on the numerator not exceeding the unweighted denominator — so both the weighted and unweighted deposit bases matter. Conclude that the weighting mechanism directly determines whether a bank breaches the LDR expectation; check maturity classification (original vs residual per 5.2) since it changes the applicable weight.
- **Grounding — this node (SAMA_EN_3343_VER1 Page 4 / 4.1):** "net loans divided by deposits after applying weights: Net loans / LDR Weighted Deposits"
- **Grounding — related node (SAMA_EN_3343_VER1 Page 5 / 5.1):** "Banks will apply the weights below to the denominator components (as applicable) in order to compute the weighted amount"

#graphify/concept #graphify/EXTRACTED #community/PSIA_Liquidity_Requirements #graphify/enriched
