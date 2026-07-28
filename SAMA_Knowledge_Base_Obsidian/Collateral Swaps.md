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

# Collateral Swaps

## Connections

### [[Level 1 Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When determining LCR treatment of a collateral swap (a securities-lending/borrowing transaction where one asset class is lent and another borrowed), you must check the specific asset composition, because whether Level 1 assets are lent or borrowed drives whether the transaction generates an inflow/outflow adjustment. The reporting reflects that Level 1 collateral received (e.g. lines 290, 216) is treated most favourably — Level 1 securities posted for derivatives margin need no additional HQLA buffer — whereas swaps out of Level 1 into lower-quality assets change the required HQLA. Conclude that you cannot classify a collateral swap without first identifying which side is Level 1, and verify the exact line item (216/290/415) against the transaction's actual asset legs.
- **Grounding — this node (Page 33 / Row 290):** "Transactions backed by Level 1 assets... In column E: The market value of the Level 1 collateral received in these transactions."
- **Grounding — related node (Page 46 / Row 415):** "Level 2B RMBS assets are lent and Level 1 assets are borrowed... swapped Level 2B RMBS assets (lent) for Level 1 assets (borrowed)."

### [[Level 2B Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When reporting collateral swaps in the LCR return, note that Level 2B assets (RMBS and non-RMBS) are an explicit leg category in the swap matrix, so their presence changes the run-off/roll-over assumption applied. The framework distinguishes swaps into Level 2B assets — and whether the borrowed Level 2B collateral meets HQLA operational requirements (paragraphs 28–40) and is reported in panel Ac — from swaps into ineligible 'other' assets. Conclude that a swap's treatment turns on both the eligibility grade (Level 1 vs 2A vs 2B vs other) and HQLA operational compliance; check each swap leg's Level 2B status and its panel Ac eligibility before assigning the line.
- **Grounding — this node (Page 45 / Rows 398, 400):** "Other assets are lent and Level 2B non-RMBS assets are borrowed... the Level 2B non-RMBS collateral borrowed is reported in panel Ac of the "LCR" worksheet."
- **Grounding — related node (Page 4 / Rows 37-40):** "Total stock of Level 2B RMBS assets... Total outright holdings of Level 2B RMBS assets plus all borrowed securities... after applying haircuts."

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
