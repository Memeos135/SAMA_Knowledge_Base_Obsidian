---
source_file: "markdown/SAMA_EN_4376_VER1.md"
type: "concept"
community: "Leverage & SA-CCR Requirements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Leverage__SA-CCR_Requirements
  - graphify/enriched
---

# Output Floor (72.5% RWA)

## Connections

### [[RWA for CCR and CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the output floor base, treat CCR and CVA RWA as components that must be recalculated on standardized approaches, not carried in at the bank's internal-model values. Para 5.3 builds the floor from the sum of credit, market and operational RWA (with CCR/CVA falling within the credit-risk element and its own chapter 8/11 rules), but para 5.8 expressly bars the VaR models approach and IMM for counterparty credit risk from the floor base. Conclude that even where a bank is SAMA-approved to use internal models for CCR/CVA in its nominated-approach RWA, those same exposures must be re-derived under standardized/BA-CVA methods for the 72.5% comparison.
- **Grounding — this node (Page 8 / Para 5.8):** "the following approaches are not permitted to be used, directly or by cross reference, in the calculation of the base of the output floor: ... VaR models approach to counterparty credit risk; and IMM for counterparty credit risk."
- **Grounding — related node (Page 6 / Para 5.4(2),(5) & 5.5(2)):** "RWA for counterparty credit risk arising from banking book exposures and from trading book instruments... RWA for credit valuation adjustment (CVA) risk... methods set out in chapter 11 of SAMA CCR and CVA Framework."

### [[RWA for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When assembling the output floor, recognize that credit-risk RWA is the largest input element and that the floor changes which credit-risk method is admissible. Para 5.3 requires the floor comparator to be built from the credit-risk RWA of para 5.4, but para 5.8 prohibits the IRB approach and SEC-IRBA from the floor base — so a bank on IRB for its nominated RWA must recompute credit-risk RWA on the standardized approach solely for the 72.5% calculation. Conclude that the credit-risk figure entering the floor may differ materially from the credit-risk figure in the bank's own capital calculation, and both must be produced.
- **Grounding — this node (Page 4 / Para 5.3 & Page 8 / Para 5.8):** "RWA for credit risk (as calculated in paragraphs 5.4)... the following approaches are not permitted... IRB approach to credit risk; SEC-IRBA."
- **Grounding — related node (Page 5 / Para 5.4(1)):** "Credit RWA for banking book exposures... calculated using: (a) The standardized approach... or (b) The internal ratings-based (IRB) approach."

### [[RWA for Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a bank's capital ratios comply with SAMA's Output Floor Requirements, you cannot look at RWA for market risk in isolation: the floor operates on the aggregate RWA, of which market risk RWA is one of three named components (credit, market, operational). Paragraph 5.3 sets total RWA as the higher of the sum computed under nominated approaches or 72.5% of that sum recomputed using only standardised approaches, so market-risk RWA feeds both legs of the calculation. Note the exclusion in paragraph 5.8: the IMA for market risk may not be used to build the floor base, so for the 72.5% leg you must recompute market risk on the standardised or simplified-standardised approach. Conclude that market-risk RWA is not a standalone figure but a mandatory input whose approach differs between the nominated and floor calculations.
- **Grounding — this node (Page 4 / para 5.3):** "72.5% of the sum of the elements listed in point (1) above, calculated using only the sta[ndardised approaches]"
- **Grounding — related node (Page 6 / para 5.5):** "RWA for market risk is calculated as the sum of the following: (1) RWA for market risk for instruments in the trading book..."

### [[SAMA Output Floor Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the Output Floor Requirements, read the document as the issuing/scoping instrument and the 72.5% floor as its central operative obligation. The document, issued under the Central Bank Law and Banking Control Law and effective 1 January 2023, sets the scope (all domestic banks, consolidated and standalone; not foreign-bank branches) and phase-in, while para 5.3 fixes the binding requirement that RWA must be the higher of the bank's nominated-approach RWA or 72.5% of standardized-approach RWA. Conclude that eligibility, timing and the transitional calibration table in para 5.10 govern when and at what percentage the floor bites — a bank in the phase-in period is not yet at the full 72.5% figure.
- **Grounding — this node (Page 4 / Para 5.3(2)):** "72.5% of the sum of the elements listed in point (1) above, calculated using only the sta[ndardized approaches]."
- **Grounding — related node (Page 3 / Sections 1.2, 2.1, 3.1):** "The output floor requirements are issued by SAMA in exercise of the authority vested in SAMA under the Central Bank Law... These requirements apply to all domestic banks."

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
