---
source_file: "markdown/SAMA_EN_3343_VER1.md"
type: "concept"
community: "PSIA Liquidity Requirements"
tags:
  - graphify/concept
  - graphify/AMBIGUOUS
  - community/PSIA_Liquidity_Requirements
  - graphify/enriched
---

# Weighted Denominator Calculation

## Connections

### [[Assets and Liabilities Reporting Categories]] — `shares_data_with` [AMBIGUOUS]
- **What this link tells you:** If you are reconciling prudential returns, treat these two as distinct reporting regimes rather than a shared data feed. The Interest Rates on Assets and Liabilities guidelines classify assets/liabilities by product, sector and Sharia type at a domestic level, while the LDR guidelines define a separate net-loan numerator and weighted-deposit denominator reported monthly on a consolidated basis with different inclusion rules (e.g. interbank and SAMA transactions excluded). The claimed data-sharing link is not established in the text — the definitions, scope and periodicity differ. Before mapping figures across the two returns, verify each item's definition in its own guideline, as balances qualifying for one report will not necessarily match the LDR components.
- **Grounding — this node (SAMA_EN_3343_VER1 Page 5 / 4.3-4.4):** "interbank transactions and transactions with SAMA should not be included in the LDR calculation, unless specifically stated by SAMA"
- **Grounding — related node (SAMA_EN_3276_VER1 Page 4-5):** "Assets and Liabilities Weighted Average (W.A) rates and balances... Reports should be completed at a domestic level only"
- **Caveat:** Relation is AMBIGUOUS; no textual basis for actual data-sharing between the two returns — verify definitions independently before cross-mapping.

### [[Loans to Deposits Ratio (LDR)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When computing the LDR you cannot apply the sub-90% limit correctly without first building the weighted denominator, because the ratio is defined as net loans over weighted deposits. Section 5 sets the maturity-bucket weights (100% to 190%) applied to denominator components, and 4.5 conditions the ratio on the numerator not exceeding the unweighted denominator — so both the weighted and unweighted deposit bases matter. Conclude that the weighting mechanism directly determines whether a bank breaches the LDR expectation; check maturity classification (original vs residual per 5.2) since it changes the applicable weight.
- **Grounding — this node (SAMA_EN_3343_VER1 Page 5 / 5.1):** "Banks will apply the weights below to the denominator components (as applicable) in order to compute the weighted amount"
- **Grounding — related node (SAMA_EN_3343_VER1 Page 4 / 4.1):** "net loans divided by deposits after applying weights: Net loans / LDR Weighted Deposits"

#graphify/concept #graphify/AMBIGUOUS #community/PSIA_Liquidity_Requirements #graphify/enriched
