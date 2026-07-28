---
source_file: "markdown/SAMA_EN_3417_VER1.md"
type: "concept"
community: "LCR & NSFR Metrics"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/LCR__NSFR_Metrics
  - graphify/enriched
---

# Cap on Level 2 Assets Calculation

## Connections

### [[BCBS LCR Document Jan 2013]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining how much of a bank's HQLA buffer can be composed of Level 2/2B assets in collateral-swap and securities-financing transactions, do not treat the SAMA prudential-return line items as self-standing rules — they are operationalisations of the underlying BCBS LCR standard. The return's cap-calculation rows repeatedly point back to Basel III LCR paragraphs (28–40, 48, 113, 146, Annex 1) as the source of the operational-requirement and eligibility tests each swapped asset must meet. For a compliance decision, treat the cited BCBS paragraphs as controlling substance: confirm the asset genuinely satisfies the HQLA operational requirements before reporting it in the relevant panel, rather than relying on the row label alone.
- **Grounding — this node (Page 46 / rows 412–419):** "Such transactions in which the bank has swapped Level 2A assets (lent) for Level 2B RMBS assets (borrowed). 48, 113, 146, Annex 1"
- **Grounding — related node (Page 40 / rows 349–353):** "would be unencumbered and would meet the operational requirements for HQLA as specified in paragraphs 28 to 40 of the Basel III LCR standards"

### [[Stock of HQLA Formula]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the stock of HQLA, treat the Level 2 cap calculation not as a separate exercise but as an adjustment that feeds directly into the HQLA total formula. The return specifies that adjusted Level 2B amounts are used 'for the purpose of calculating the adjustment to the stock of HQLA due to the cap on Level 2 assets,' and Annex 1 fixes the mechanics: adjusted Level 2 assets are capped at two-thirds of adjusted Level 1, with the 15% Level 2B cap taken into account. The practical consequence is that you cannot finalise the HQLA numerator without first applying both caps; verify the Annex 1 adjustment amounts flow into the stock-of-HQLA line items before relying on the reported ratio.
- **Grounding — this node (Page 58 / Annex 1, para 2):** "The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets after haircuts have been applied."
- **Grounding — related node (Page 4 / row 42):** "Adjusted amount of Level 2B RMBS assets used for the purpose of calculating the adjustment to the stock of HQLA due to the cap on Level 2 assets"

#graphify/concept #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
