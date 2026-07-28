---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB Retail & Corporate Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_Retail__Corporate_Exposures
  - graphify/enriched
---

# Micro Small and Medium-Sized Entities (MSME)

## Connections

### [[Exposures to Corporates]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a corporate counterparty, you must test whether it is an MSME because the corporate exposure class carves out MSMEs for distinct treatment rather than the general corporate risk weights. Paragraph 7.40 defines corporate MSMEs (consolidated-group revenues ≤ SAR 200 million) and assigns 85% for unrated corporate MSMEs, while MSMEs meeting the regulatory-retail criteria of 7.57 drop to 75% retail treatment; the IRB firm-size adjustment uses a different SAR 223 million threshold. Conclude that MSME status changes both the applicable risk weight and possibly the exposure class (corporate vs regulatory retail), so check revenue thresholds and the 7.57 criteria — and note the standardized (SAR 200m) versus IRB (SAR 223m) definitions differ.
- **Grounding — this node (Page 25 / 7.40):** "corporate MSMEs... are defined as corporate exposures where the reported annual revenues... is less than or equal to SAR 200 million... an 85% risk weight will be applied."
- **Grounding — related node (Page 23 / 7.37):** "The corporate exposure class does not include exposures to individuals. The corporate exposure class differentiates between the following subcategories."

### [[IRB Approach Overview]] — `references` [EXTRACTED]
- **What this link tells you:** When applying IRB risk-weight functions to corporate credits, do not treat MSME borrowers identically to large firms, because the framework mandates a distinct firm-size adjustment. The IRB overview covers the corporate asset class, and within it banks are permitted to separately distinguish MSME borrowers (consolidated group revenues below SAR 223 million) and apply the 0.04 x (1 – (S – 5)/45) adjustment to the corporate risk-weight formula. You would conclude that identifying MSME status is a required step in IRB corporate capital calculation, and should verify the revenue/total-assets thresholds and the failsafe substitution before deriving risk weights. Note the MSME threshold under IRB (SAR 223m) differs from the standardized-approach MSME definition (SAR 200m) and from the SAMA Circular referenced there.
- **Grounding — this node (Page 111 / 11.8):** "Under the IRB approach for corporate credits, banks will be permitted to separately distinguish exposures to MSME borrowers... A firm-size adjustment... is made to the corporate risk weight formula."
- **Grounding — related node (Page 102 / 10.30):** "For each of the asset classes covered under the IRB framework, there are three key elements: Risk components... Risk-weight functions... Minimum requirements."

### [[Retail Exposure Class]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying an MSME exposure for risk-weighting, do not assume the corporate MSME treatment applies automatically: whether an MSME sits in the corporate class or the retail class turns on the 'regulatory retail' criteria in para 7.57. The retail exposure class expressly includes MSMEs (as defined in 7.40) that meet those criteria, and MSMEs failing them fall back to the corporate MSME treatment under 7.40 — a difference that changes the risk weight (e.g. 75% regulatory retail vs 85% corporate MSME). You would conclude that MSME classification is a two-step test cross-referencing both provisions, and should check the 7.57 product, value and granularity criteria before applying a risk weight.
- **Grounding — this node (Page 25 / Art 7.40):** "Exposures to MSMEs that meet the criteria in paragraphs 7.57 will be treated as regulatory retail MSME exposures and risk weighted at 75%."
- **Grounding — related node (Page 32 / Art 7.55):** "Exposures to MSMEs (as defined in paragraph 7.40) that meet the “regulatory retail” criteria set out in paragraph 7.57... Exposures to MSMEs that do not meet these criteria will be treated as corporate MSMEs exposures"

#graphify/concept #graphify/EXTRACTED #community/IRB_Retail__Corporate_Exposures #graphify/enriched
