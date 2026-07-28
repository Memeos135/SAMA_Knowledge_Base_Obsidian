---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Securitization Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Securitization General Provisions

## Connections

### [[Resecuritization Exposure]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the regulatory capital treatment of a resecuritization exposure, you cannot treat it in isolation: SAMA's rules define it as a securitization exposure whose underlying pool itself contains at least one securitization exposure, so it is a subset of the general securitization framework. The general provisions (18.4–18.6) supply the definitions of securitization exposure and originator that anchor the resecuritization concept, and the SEC-SA adjustments (19.16) explicitly require the underlying securitization exposures' capital to be computed using the securitization framework. Conclude that resecuritization capital calculations must be read against the general securitization provisions — check both the resecuritization-specific parameters (e.g. p=1.5, W set to zero) and the base framework definitions before applying a risk weight.
- **Grounding — this node (Page 231 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure."
- **Grounding — related node (Page 297 / 19.16):** "For resecuritization exposures, banks must apply the SEC-SA specified in 19.1 to 19.15, with the following adjustments"

### [[Synthetic Securitization]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether the securitization capital framework applies to a given structure, treat synthetic securitizations as squarely in scope: paragraph 18.1 requires banks to apply the securitization framework to both traditional and synthetic securitizations, and 18.3 defines synthetic securitization as a tranched structure. The general provisions (definitions of securitization exposure, originator, resecuritization) therefore govern synthetic deals directly, not by analogy. Conclude that a synthetic transaction cannot escape the framework on the basis of legal form — 18.1 mandates treatment on economic substance — so verify tranching and credit-risk transfer features against the 18.x definitions rather than the transaction's label.
- **Grounding — this node (Page 230 / 18.1):** "Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizations"
- **Grounding — related node (Page 230 / 18.3):** "A synthetic securitization is a structure with at least two different stratified risk positions or tranches that reflect different degre[es]"

### [[Traditional Securitization]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a transaction under the securitization framework, use the traditional securitization definition in 18.2 as the reference test: the general provisions in 18.1 bring both traditional and synthetic securitizations into scope, and 18.2 fixes the distinguishing feature — cash flows from an underlying pool servicing at least two stratified tranches where junior tranches absorb losses without interrupting senior payments. This link establishes that the framework's defined terms (securitization exposure, originator) attach to structures meeting the 18.2 traditional test. Conclude that the tranching/loss-absorption characteristic, not the senior/subordinated priority typical of ordinary debt, is what triggers framework application; check the deal against 18.2 before applying the capital treatment.
- **Grounding — this node (Page 230 / 18.1):** "the capital treatment of a securitization exposure must be determined on the basis of its economic substance rather than its legal form"
- **Grounding — related node (Page 230 / 18.2):** "A traditional securitization is a structure where the cash flow from an underlying pool of exposures is used to service at least two different stratified risk positions or tranches"

### [[Treatment of Purchase Price Discounts]] — `references` [EXTRACTED]
- **What this link tells you:** When a purchased-receivables transaction carries a purchase price discount that provides first-loss protection, decide the capital treatment by reference to the securitization framework, not solely the receivables rules. Para 14.10 directs that a refundable portion of such a discount be recognized as first-loss protection and treated under securitization chapters 18–23 by the purchaser, with the seller treating the refundable amount as a first-loss position — invoking the chapter 18 framework where treatment turns on economic substance rather than legal form. Conclude that you must characterize the discount (refundable vs non-refundable) and apply the securitization first-loss treatment accordingly, rather than assuming ordinary receivables capital rules govern.
- **Grounding — this node (Page 230 / para 18.1):** "the capital treatment of a securitization exposure must be determined on the basis of its economic substance rather than its legal form."
- **Grounding — related node (Page 172 / para 14.10):** "the purchaser may recognize this refundable amount as first-loss protection and hence treat this exposure under the securitization chapters 18 to 23, while the seller ... must treat the refundable amount as a first-loss position"

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
