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

# Hedging Set

## Connections

### [[Add-on for Commodity Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the commodity add-on, you must first allocate trades into the four prescribed hedging sets (energy, metals, agriculture, other) as defined in 6.48(5), because the commodity add-on calculation (6.72 onward) proceeds hedging-set by hedging-set with limited offsetting between them. This link tells you the hedging-set definitions are a mandatory structural input, not a modelling choice, and that SAMA may require more refined commodity definitions where basis risk is material. When reviewing a commodity add-on, verify trades are mapped to the correct hedging set and that any within-set offsetting respects the prescribed correlation factors.
- **Grounding — this node (Page 34 / 6.48(5)):** "Commodity derivatives consist of four hedging sets defined for broad categories of commodity derivatives: energy, metals, agricultural and other commodities"
- **Grounding — related node (Page 44 / Step 2):** "Allocate the trades in commodity derivative asset class to hedging sets... four hedging sets consisting of derivatives that reference: energy, metals, agriculture and other commodities"

### [[Add-on for Foreign Exchange Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the FX add-on, note the hedging-set definition governs the aggregation: 6.48(2) requires a separate hedging set for each currency pair, and 6.62 builds the FX add-on by allocating trades to those per-currency-pair hedging sets, summing effective notionals within each, then applying the 4% supervisory factor. This link tells you offsetting is only permitted within a currency pair, not across pairs. When checking an FX add-on, confirm trades are grouped strictly by currency pair before the 4% factor is applied.
- **Grounding — this node (Page 34 / 6.48(2)):** "FX derivatives consist of a separate hedging set for each currency pair"
- **Grounding — related node (Page 39 / 6.62(2)):** "In the foreign exchange derivative asset class the hedging sets consist of all the derivatives that reference the same currency pair"

### [[Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the SA-CCR PFE add-on for interest rate derivatives under this SAMA capital standard, you cannot apply the interest-rate add-on formula without first applying the hedging-set definitions: paragraph 6.48 fixes that IR derivatives form a separate hedging set per currency, which controls where offsetting is (and is not) permitted. The IR add-on section (6.59) then operates inside those hedging sets, using maturity buckets to allow full offset within a bucket and only limited offset across buckets. Conclude that any IR add-on calculation you review must be checked against the correct per-currency hedging-set allocation before its offsetting treatment can be relied upon.
- **Grounding — this node (Page 34 / 6.48):** "Interest rate derivatives consist of a separate hedging set for each currency."
- **Grounding — related node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Derivative_Add-ons #graphify/enriched
