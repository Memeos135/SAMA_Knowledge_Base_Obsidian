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

# Credit Conversion Factors

## Connections

### [[EAD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When estimating EAD for off-balance-sheet items under the advanced IRB approach, understand that CCFs are the mechanism by which undrawn commitments are converted into exposure, so the own-EAD estimation requirements directly govern how a bank derives its CCFs. Para 16.88–16.95 require EAD to reflect additional drawings up to and after default and warn against the instability of the undrawn-limit-factor (ULF) CCF method, prohibiting capping of reference data. Conclude that a bank on the advanced approach must derive CCFs within the EAD-estimation standards — check that estimates are default-weighted, conservative, and not artificially capped, rather than applying fixed supervisory CCFs.
- **Grounding — this node (Page 216 / 16.94 footnote 66):** "undrawn limit factor (ULF) approach ... a specific type of CCF, where predicted additional drawings in the lead-up to default are expressed as a percentage of the undrawn limit."
- **Grounding — related node (Page 213 / 16.88):** "the additional minimum requirements for internal estimation of EAD under the advanced approach ... focus on the estimation of EAD for off-balance sheet items."

### [[EAD under Foundation Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When estimating exposure at default for off-balance sheet commitments, the CCF concept and the foundation EAD approach are directly coupled: under the foundation approach EAD equals the committed-but-undrawn amount multiplied by a CCF, so the two documents describe the same computation across the two circulars. This link tells you that CCF definitions in SAMA_EN_3487 and the EAD-estimation standards in SAMA_EN_3502 form one continuous methodology. When choosing between foundation and advanced treatment, verify which CCF/EAD basis applies and note the advanced-approach constraints (e.g. EAD reference data must not be capped, and instability near fully-drawn limits must be quarantined).
- **Grounding — this node (Page 126 (SAMA_EN_3487)):** "In the foundation approach, EAD is calculated as the committed but undrawn amount multiplied by a credit conversion factor (CCF)."
- **Grounding — related node (Page 209 / 16.94-16.95 (SAMA_EN_3502)):** "undrawn limit factor (ULF) approach... to estimating CCFs... EAD reference data must not be capped to the principal amount outstanding or facility limits."

### [[Off-Balance Sheet Items]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's regulatory capital and leverage/disclosure exposures, off-balance sheet items and credit conversion factors must be read together: the disclosure and measurement rules require off-balance sheet exposures (guarantees, irrevocable loan commitments) to be measured gross of any CCF before mitigation is applied. This link tells you the CCF is the conversion mechanism that turns a notional off-balance sheet commitment into a credit-equivalent exposure amount. When scoping capital calculations, check that CCF treatment is applied to the off-balance sheet population identified in templates like CR1 and the leverage-ratio conversion rows, not applied inconsistently across regimes.
- **Grounding — this node (Page 126 (SAMA_EN_3487)):** "In the foundation approach, EAD is calculated as the committed but undrawn amount multiplied by a credit conversion factor (CCF)."
- **Grounding — related node (Page 797 (Template CR1)):** "Irrevocable loan commitments - total amount that the bank has committed to lend. The amount must be gross of any CCF or CRM techniques."

### [[Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how off-balance-sheet items convert into credit exposure for capital purposes, treat Credit Conversion Factors as a sub-component of the Standardized Approach rather than a free-standing method: the disclosure templates report off-balance-sheet amounts 'before credit conversion factors (CCF) and CRM' precisely because CCFs are applied within the SA computation of RWA. Both concepts sit inside SAMA's Minimum Capital Requirements for Credit Risk framework, so the CCF you select is dictated by the SA exposure-class rules, not chosen independently. Conclude that a bank on the SA must apply the SA-prescribed CCFs to convert commitments and derivatives before risk-weighting, and should verify the specific CCF against the SA exposure treatment for each item type.
- **Grounding — this node (Page 714 / para 7.2.x):** "The resulting amount may be further reduced by the effective notional amount of a purchased credit derivative on the same reference name"
- **Grounding — related node (Page 755 / row 1):** "Definition of standardised approach: The standardised approach for credit risk... banks must use the simple approach or the comprehensive approach with standard supervisory haircuts"

#graphify/concept #graphify/EXTRACTED #community/Credit_Conversion__EAD #graphify/enriched
