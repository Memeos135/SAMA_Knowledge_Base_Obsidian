---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Securitization Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Supervisory Parameter p

## Connections

### [[Resecuritization Exposures Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When determining SEC-IRBA capital for a securitization tranche, you must confirm whether the exposure is a resecuritization before applying parameter p, because the definition in 18.5 governs which capital formula and inputs apply. The link connects the classification rule (what counts as a resecuritization) to the risk-weight machinery (the supervisory p and its floor of 0.3). Practically, conclude that mislabeling a resecuritization as an ordinary securitization would feed the wrong p-parameter into the risk-weight calculation, so classification under 18.5 must be settled first.
- **Grounding — this node:** _(source text unavailable / OCR-garbled — consult original)_
- **Grounding — related node:** _(source text unavailable / OCR-garbled — consult original)_

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing a SEC-IRBA risk weight, the supervisory parameter p is a defined, non-discretionary input whose value derives from N, KIRB, LGD, MT and the A–E lookup table by pool type (wholesale/retail, senior/non-senior, granular/non-granular). The framework defines p 'in the context of the SEC-IRBA' with a 0.3 floor. Conclude that a bank must first classify the pool correctly to pick the right A–E row, since misclassification changes p and therefore the reported capital charge.
- **Grounding — this node (Page 317 / 22.17):** "The supervisory parameter p in the context of the SEC-IRBA is expressed as follows, where: (1) 0.3 denotes the p-parameter floor"
- **Grounding — related node (Page 6 / ch.22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"

### [[Securitization Standardized Approach (SEC-SA)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying SEC-SA to a securitization exposure, the supervisory parameter p is an integral input to the risk-weight formula, so you cannot compute the SEC-SA risk weight without fixing p for that exposure. Note the corpus specifies p differently by approach: the p-formula with floor 0.3 shown at 22.17 is the SEC-IRBA context, while under SEC-SA p is set to a supervisory value (e.g. 0.5 for STC exposures per 19.21). Conclude that you must apply the SEC-SA-specific p value in chapter 19 and not carry over the SEC-IRBA p-formula from 22.17.
- **Grounding — this node (Page 317 / 22.17):** "The supervisory parameter p in the context of the SEC-IRBA is expressed as follows, where: (1) 0.3 denotes the p-parameter floor"
- **Grounding — related node (Page 6 / Ch 19-22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Caveat:** The quoted p-formula at 22.17 is SEC-IRBA-specific; the SEC-SA value of p is set separately (e.g. 19.21). Verify the chapter 19 SEC-SA provision for the applicable p.

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
