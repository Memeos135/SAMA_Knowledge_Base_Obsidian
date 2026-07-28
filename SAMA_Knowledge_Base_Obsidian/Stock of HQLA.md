---
source_file: "markdown/SAMA_EN_3417_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Stock of HQLA

## Connections

### [[Level 1 Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating a bank's stock of HQLA under this guidance, treat Level 1 assets as the foundational, uncapped component and the base against which the Level 2 caps are measured. The guidance is explicit that the 40% Level 2 cap equals two-thirds of the adjusted Level 1 amount after haircuts, so the size and eligibility of Level 1 holdings (coins, banknotes, qualifying central-bank reserves) directly constrain how much Level 2 can count toward HQLA. Conclude that misclassifying an asset as Level 1 versus Level 2 changes not only that asset's own treatment but the admissible amount of all Level 2 assets in the ratio.
- **Grounding — this node (Page 58 / Annex 1 para 2):** "The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets after haircuts have been applied."
- **Grounding — related node (Page 1):** "A)a) Level 1 assets — Coins and banknotes currently held by the bank that are immediately available to meet obligations."

### [[Level 2 Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a bank's LCR numerator is correctly composed, treat the Level 2 asset definition and the HQLA-stock reporting rules as one calculation, not two: the SAMA LCR standard (2788) defines Level 2 assets and imposes the 40% cap (and 15% Level 2B sub-cap) on the total HQLA stock, while the reporting return (3417) operationalises the same caps through the adjusted-amount and cap line items and Annex 1 methodology. The link matters because the caps are binding only after haircuts and after unwinding short-term securities-financing and collateral-swap transactions maturing within 30 days. Conclude that eligibility of a Level 2 holding cannot be assessed in isolation from the stock-level cap arithmetic in the return; verify both the qualifying-asset criteria and the cap adjustment before treating an asset as HQLA.
- **Grounding — this node (Page 58 / Annex 1):** "the calculation of the 40% cap on Level 2 assets should take into account the impact on the stock of HQLA ... The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets"
- **Grounding — related node (Page 12 / para 46-48):** ""Level 2" assets can only comprise up to 40% of the total (level 1 and level 2) stock ... the 15% cap on Level 2B assets should be determined after the application of required haircuts"

### [[Level 2B Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When building the HQLA stock, treat Level 2B assets (AA-rated RMBS, BBB- to A+ non-financial corporate bonds, qualifying common equity) as the most tightly restricted eligible category: the guidance caps adjusted Level 2B at 15/85 of the sum of adjusted Level 1 and Level 2 assets, and this 15% cap interacts with the overall 40% Level 2 cap. Each Level 2B sub-class requires haircuts and must satisfy the specific paragraph 54(a)/(b)/(c) eligibility conditions before inclusion. Conclude that Level 2B inclusion is doubly constrained — by asset-level eligibility and by two nested caps — so overstated Level 2B holdings will be reduced in the HQLA total regardless of their market value.
- **Grounding — this node (Page 58 / Annex 1 para 3):** "The maximum amount of adjusted Level 2B assets in the stock of HQLA is equal to 15/85 of the sum of the adjusted amounts of Level 1 and Level 2 assets..."
- **Grounding — related node (Page 4 / rows 37-40):** "Total stock of Level 2B RMBS assets — Total outright holdings of Level 2B RMBS assets plus all borrowed securities of Level 2B RMBS assets, after applying haircuts."

### [[Liquidity Coverage Ratio]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the LCR, understand that the stock of HQLA is the numerator of the ratio: its composition, caps, and haircuts directly determine whether a bank meets the 100% LCR requirement. The guidance's HQLA rules — Level 1 uncapped, Level 2 subject to the 40% cap, Level 2B within the 15% cap — feed straight into the LCR calculation reported to SAMA. Conclude that any adjustment to eligible HQLA (through the caps in Annex 1 or exclusion of transfer-restricted assets) mechanically changes the reported LCR, so HQLA classification decisions are LCR-compliance decisions, not separate exercises.
- **Grounding — this node (Page 58 / Annex 1 para 2):** "the calculation of the 40% cap on Level 2 assets should take into account the impact on the stock of HQLA..."
- **Grounding — related node (Page 24):** "Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools – Jan 2013"

### [[SAMA Specific Guidance for Amended LCR Prudential Returns]] — `references` [EXTRACTED]
- **What this link tells you:** When reporting under the amended LCR returns, understand that the Specific Guidance is structured around building and adjusting the 'stock of HQLA'—the numerator of the ratio—so its row-by-row instructions govern which assets enter the stock, at what haircut, and how Level 2 and Level 2B caps reduce it. The guidance ties HQLA composition and cap adjustments (40% Level 2, 15% Level 2B) to the operational requirements in Basel III LCR paragraphs 28-40 and Annex 1. Conclude that any determination of eligible HQLA for the return must apply both the guidance's line-item treatment and the underlying Basel operational/eligibility tests, and that assets failing those tests (e.g. encumbered collateral) must be excluded from the stock.
- **Grounding — this node (Page 4):** "Total outright holdings of Level 2B RMBS assets plus all borrowed securities of Level 2B RMBS assets, after applying haircuts"
- **Grounding — related node (Page 58 / Annex 1):** "The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets after haircuts have been applied."

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
