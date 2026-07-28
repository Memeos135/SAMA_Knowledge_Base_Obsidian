---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB Default & Provisions"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_Default__Provisions
  - graphify/enriched
---

# Supervisory Slotting Approach for Specialized Lending

## Connections

### [[Expected Loss for SL under Slotting]] — `references` [EXTRACTED]
- **What this link tells you:** When computing expected loss (EL) for specialized-lending exposures under slotting, do not apply the general IRB EL = PD × LGD formula: Chapter 15 expressly carves out slotting exposures and routes their EL calculation back to the slotting chapter (paragraphs 13.8 to 13.12). The general slotting approach therefore governs both RWA and EL for these exposures, and the difference between EL and provisions is then treated under the Chapter 15 / Basel III capital rules (Circular No. 341000015689). Conclude that for SL slotting exposures you determine EL via the slotting-specific method (13.8–13.12), then feed the result into the EL-versus-provisions capital adjustment, rather than the standard PD×LGD route used for corporate/retail exposures.
- **Grounding — this node (Page 138 / Art 13.1):** "This chapter sets out the calculation of risk weighted assets and expected losses for specialized lending (SL) exposures subject to the supervisory slotting approach"
- **Grounding — related node (Page 174 / Art 15.3):** "For exposures subject to the supervisory slotting criteria EL is calculated as described in the chapter on the supervisory slotting approach (paragraphs 13.8 to 13.12)"

### [[High-Volatility Commercial Real Estate (HVCRE)]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a commercial real-estate exposure as HVCRE, recognise that this definition feeds directly into the supervisory slotting approach — HVCRE is a specialized-lending sub-type with its own slotting risk weights, distinct from the PF/OF/CF/IPRE table. The link matters because HVCRE (higher loss-rate volatility, including ADC financing) is carved out for a separate slotting treatment, so correct identification of an exposure as HVCRE changes which supervisory-category risk weights apply. Confirm whether an ADC or high-volatility CRE exposure meets the HVCRE definition in 10.15 before applying the slotting weights, since HVCRE and other SL exposures are slotted under different tables.
- **Grounding — this node (Page 3 / Chapter 13 contents):** "Risk weights for specialized lending (HVCRE) 139"
- **Grounding — related node (Page 95 / Para 10.15):** "HVCRE lending is the financing of commercial real estate that exhibits higher loss rate volatility (i.e. higher asset correlation) compared to other types of SL."

### [[Rating Criteria]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank cannot meet the IRB rating-system requirements for estimating PD on specialized lending, note that the supervisory slotting approach is the fallback that substitutes standardized supervisory categories for the bank's own rating criteria. The link tells you these two are alternatives within the same IRB chapter: the general rating-criteria documentation and differentiation standards (16.34–16.36) apply where a bank uses internal PD estimates, whereas slotting (chapter 13) maps internal grades to five supervisory categories precisely for banks that 'do not meet the requirements for the estimation of PD.' Determine first whether the bank meets the rating-system minimums; if not, RWA for PF/OF/CF/IPRE/HVCRE must be set via the slotting risk weights rather than own estimates.
- **Grounding — this node (Page 138 / Para 13.2):** "banks that do not meet the requirements for the estimation of probability of default (PD) under the corporate internal ratings-based (IRB) approach will be required to map their internal grades to five supervisory categories"
- **Grounding — related node (Page 188 / Para 16.34):** "A bank must document the rationale for its choice of internal rating criteria and must be able to provide analyses demonstrating that rating criteria... meaningfully differentiate risk."

### [[Specialized Lending]] — `references` [EXTRACTED]
- **What this link tells you:** When an IRB bank holds specialized-lending exposures but cannot estimate PD, this link tells you the fallback is not the general corporate IRB formula but the supervisory slotting approach in chapter 13. Para 13.2 requires banks that do not meet the PD-estimation requirements for PF, OF, CF and IPRE to map internal grades to five supervisory categories with fixed UL risk weights (70%/90%/115%/250%/0%). Conclude that eligibility for slotting turns on whether you meet the PD-estimation requirements — verify that before choosing between slotting and full IRB, and use the chapter-13 slotting criteria (13.13–13.15) for the mapping.
- **Grounding — this node (Page 138 / 13.2):** "banks that do not meet the requirements for the estimation of probability of default (PD)... will be required to map their internal grades to five supervisory categories."
- **Grounding — related node (Page 26 / 7.42):** "Exposures described in paragraph 7.41 will be classified in one of the following three subcategories of specialized lending: Project finance... Object finance... Commodities finance."

### [[Supervisory Slotting Criteria for Commodities Finance]] — `references` [EXTRACTED]
- **What this link tells you:** When determining risk weights for a bank's commodities finance (CF) book under the IRB slotting fallback, read the general slotting approach (Chapter 13) together with the CF-specific criteria table it points to: the approach sets the five supervisory categories and their UL risk weights (Strong 70% / Good 90% / Satisfactory 115% / Weak 250% / Default 0%), while the CF criteria table supplies the assessment factors that place a given exposure into a category. Paragraph 13.2 expressly cites the CF slotting criteria as the mandatory basis for mapping internal grades. Conclude that CF capital cannot be computed from the risk-weight table alone — you must apply the corresponding CF criteria table (referenced in 13.2, and see the parallel mapping-obligation in 16.27) to justify each category assignment.
- **Grounding — this node (Page 138 / Art 13.2):** "The slotting criteria on which this mapping must be based are provided in ... paragraph 013.6 for CF exposures"
- **Grounding — related node (Page 185 / Art 16.27):** "The slotting criteria tables in the supervisory slotting approach chapter 13 provide, for each sub-class of SL exposures, the general assessment factors and characteristics"

### [[Supervisory Slotting Criteria for Object Finance]] — `references` [EXTRACTED]
- **What this link tells you:** For object finance (OF) exposures that fall back to slotting, apply the general slotting approach and the OF-specific criteria table together: Chapter 13 defines the supervisory categories and their risk weights, and paragraph 13.2 directs OF mapping to paragraph 13.15. The category-to-risk-weight table has no self-executing test — the OF criteria table supplies the characteristics needed to slot each exposure. Conclude that you must evidence OF category assignment against the OF criteria table (and the mapping obligation in 16.27), not rely on the risk-weight schedule in isolation.
- **Grounding — this node (Page 138 / Art 13.2):** "The slotting criteria on which this mapping must be based are provided in ... paragraph 13.15 for OF exposures"
- **Grounding — related node (Page 185 / Art 16.27):** "Banks using the supervisory slotting criteria must assign exposures to their internal rating grades ... Banks must then map these internal rating grades into the five supervisory rating categories"

### [[Supervisory Slotting Criteria for Project Finance]] — `references` [EXTRACTED]
- **What this link tells you:** When setting capital for project finance (PF) exposures under slotting, use the general approach with the PF criteria table (Table 24 at para 13.13) that it references: Chapter 13 fixes the five categories and UL risk weights, while the PF table sets out the financial-strength, market-condition and other factors that determine which category applies. Paragraph 13.2 names 13.13 as the mandatory PF mapping basis, and note SAMA may permit preferential 50%/70% weights for 'strong'/'good' PF exposures under stated conditions. Conclude that PF slotting decisions must be grounded in the Table 24 criteria and that any preferential weighting requires the specific maturity/underwriting conditions to be met.
- **Grounding — this node (Page 138 / Art 13.2):** "The slotting criteria on which this mapping must be based are provided in paragraph 13.13 for PF exposures"
- **Grounding — related node (Page 142 / Art 13.13):** "Table 24 below sets out the supervisory rating grades for project finance exposures subject to the supervisory slotting approach"

#graphify/concept #graphify/EXTRACTED #community/IRB_Default__Provisions #graphify/enriched
