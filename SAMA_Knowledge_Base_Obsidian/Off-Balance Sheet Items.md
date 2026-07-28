---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Credit Conversion & EAD"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Credit_Conversion__EAD
  - graphify/enriched
---

# Off-Balance Sheet Items

## Connections

### [[Credit Conversion Factors]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's regulatory capital and leverage/disclosure exposures, off-balance sheet items and credit conversion factors must be read together: the disclosure and measurement rules require off-balance sheet exposures (guarantees, irrevocable loan commitments) to be measured gross of any CCF before mitigation is applied. This link tells you the CCF is the conversion mechanism that turns a notional off-balance sheet commitment into a credit-equivalent exposure amount. When scoping capital calculations, check that CCF treatment is applied to the off-balance sheet population identified in templates like CR1 and the leverage-ratio conversion rows, not applied inconsistently across regimes.
- **Grounding — this node (Page 797 (Template CR1)):** "Irrevocable loan commitments - total amount that the bank has committed to lend. The amount must be gross of any CCF or CRM techniques."
- **Grounding — related node (Page 126 (SAMA_EN_3487)):** "In the foundation approach, EAD is calculated as the committed but undrawn amount multiplied by a credit conversion factor (CCF)."

### [[Leverage Ratio Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When checking whether the leverage ratio denominator is complete, off-balance sheet items cannot be omitted: the LR2 template explicitly folds them in as row 22 (sum of rows 19-21) and includes that figure in total exposures at row 24. The framework requires off-balance sheet exposures to be converted to credit-equivalent amounts and to have specific/general provisions deducted from Tier 1 capital netted out. A reviewer should confirm guarantees and irrevocable loan commitments have been captured (gross of CCF/CRM per the CR1 definitions) so the leverage exposure is not understated.
- **Grounding — this node (Page 797 / Template CR1 Definitions):** "Off-balance sheet items must be measured according to the following criteria: (a) guarantees given... Irrevocable loan commitments"
- **Grounding — related node (Page 873 / rows 19-24):** "Off-balance sheet items (sum of rows 19 to 21)... Total exposures (sum of rows 7, 13, 18 and 22)"

### [[SCRE - Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying credit risk exposures, off-balance sheet items are not excluded — they must be measured (guarantees at maximum callable amount, irrevocable loan commitments at total committed amount, gross of CCF/CRM) and give rise to a credit risk exposure under the SCRE credit risk standard. SCRE governs the RWA and capital treatment of these exposures via the standardised (SCRE5–9) or IRB (SCRE10–16) approaches. In scoping which OBS items attract capital charges, apply the SCRE definitions and note that revocable loan commitments are excluded while irrevocable ones must be captured gross.
- **Grounding — this node (Page 797 / CR1):** "Off-balance sheet items that give rise to a credit risk exposure according to the Basel framework ... gross of any credit conversion factor (CCF) or credit risk mitigation (CRM) techniques"
- **Grounding — related node (Page 751):** "Credit risk (excluding counterparty credit risk): RWA and capital requirements according to the credit risk standard of the Basel framework (SCRE)"

#graphify/concept #graphify/EXTRACTED #community/Credit_Conversion__EAD #graphify/enriched
