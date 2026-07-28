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

# RWA for CCR and CVA

## Connections

### [[Output Floor (72.5% RWA)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the output floor base, treat CCR and CVA RWA as components that must be recalculated on standardized approaches, not carried in at the bank's internal-model values. Para 5.3 builds the floor from the sum of credit, market and operational RWA (with CCR/CVA falling within the credit-risk element and its own chapter 8/11 rules), but para 5.8 expressly bars the VaR models approach and IMM for counterparty credit risk from the floor base. Conclude that even where a bank is SAMA-approved to use internal models for CCR/CVA in its nominated-approach RWA, those same exposures must be re-derived under standardized/BA-CVA methods for the 72.5% comparison.
- **Grounding — this node (Page 6 / Para 5.4(2),(5) & 5.5(2)):** "RWA for counterparty credit risk arising from banking book exposures and from trading book instruments... RWA for credit valuation adjustment (CVA) risk... methods set out in chapter 11 of SAMA CCR and CVA Framework."
- **Grounding — related node (Page 8 / Para 5.8):** "the following approaches are not permitted to be used, directly or by cross reference, in the calculation of the base of the output floor: ... VaR models approach to counterparty credit risk; and IMM for counterparty credit risk."

### [[SAMA CCR and CVA Minimum Capital Requirements]] — `cites` [EXTRACTED]
- **What this link tells you:** When assembling total RWA under the output-floor / capital-adequacy rules, note that the RWA aggregation document (SAMA_EN_4376) does not itself define CCR/CVA methodology but points to this CCR and CVA Framework as the authoritative source: RWA for CVA risk is calculated using BA-CVA, SA-CVA, or the 100%-of-CCR-RWA fallback set out in Chapter 11 here. This establishes a hierarchy where 4376 governs how the CVA/CCR figure enters the capital ratio, while 4283 governs how it is computed. For a compliance decision, verify the CVA/CCR numbers used in the RWA total are produced strictly per the methods and materiality threshold in the referenced CCR and CVA Framework.
- **Grounding — this node (SAMA_EN_4376 Page 6 / 5.4(2)):** "RWA for credit valuation adjustment (CVA) risk ... calculated using one of the following methods set out in chapter 11 of SAMA CCR and CVA Framework"
- **Grounding — related node (Page 87 / 11.7):** "Two approaches are available for calculating CVA capital: the standardized approach (SA-CVA) and the basic approach (BA-CVA). Banks must use the BA-CVA unless they receive approval ... to use the SA-CVA."

#graphify/concept #graphify/EXTRACTED #community/Leverage__SA-CCR_Requirements #graphify/enriched
