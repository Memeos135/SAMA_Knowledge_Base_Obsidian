---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Leverage Ratio Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Leverage_Ratio_Exposures
  - graphify/enriched
---

# SFT Exposures (Leverage Ratio)

## Connections

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **What this link tells you:** When reconciling a bank's leverage ratio disclosures, treat SFT exposures as one of the four mandatory input components of the total leverage exposure measure — not a standalone metric. The exposure measure (LR2 denominator) is defined as the sum of rows 7, 13, 18 and 22, and SFT assets are separately captured (including the mean and quarter-end gross SFT values in rows 28–29) precisely because they feed that denominator. In practice you would check that reported SFT figures tie into the total exposures line and that any material difference between Pillar 1 SFT amounts and the disclosed mean values is explained, rather than reading the SFT row in isolation.
- **Grounding — this node (Page 873):** "Mean value of gross SFT assets, after adjustment for sale accounting transactions and netted of amounts of associated cash payables and cash receivables"
- **Grounding — related node (Page 873):** "Total exposures (sum of rows 7, 13, 18 and 22)"

### [[Qualifying CCP (QCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring SFT exposures for the leverage ratio, distinguish between the risk-weighted CCR treatment of SFTs cleared through a QCCP (a 2% risk weight on the clearing member's trade exposure) and the leverage-ratio treatment, which requires gross SFT assets to be disclosed after adjustment for sale accounting and netted only against associated cash payables/receivables. The QCCP definition and 2% risk weight sit in the CCR standard, whereas the SFT leverage-ratio component is a non-risk-based exposure measure. Conclude that favourable QCCP risk-weighting does not carry over to reduce the leverage-ratio SFT exposure measure — compute each separately and do not assume QCCP clearing lowers the leverage numerator.
- **Grounding — this node (Page 873, rows 28-29):** "Mean value of gross SFT assets, after adjustment for sale accounting transactions and netted of amounts of associated cash payables and cash receivables."
- **Grounding — related node (Page 620, s.8.7):** "a risk weight of 2% must be applied to the bank's trade exposure to the CCP in respect of OTC derivatives, exchange-traded derivative transactions, SFTs and long settlement transactions."

#graphify/document #graphify/EXTRACTED #community/Leverage_Ratio_Exposures #graphify/enriched
