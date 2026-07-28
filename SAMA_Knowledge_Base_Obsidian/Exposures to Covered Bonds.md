---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "Bank & ECAI Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank__ECAI_Exposures
  - graphify/enriched
---

# Exposures to Covered Bonds

## Connections

### [[External Credit Risk Assessment Approach (ECRA)]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears to connect the covered-bonds exposure class to the external-ratings-based approach, but the provided context does not contain the covered-bond risk-weight text itself — the node A extract shows only the contents listing and the retail exposure class. Both sit within the same SAMA credit-risk framework, and covered bonds are typically weighted by reference to the issue's or issuer's external rating, which would draw in ECRA/ECAI eligibility. Treat this as a lead: verify the actual covered-bonds paragraphs (around page 20 per the contents) to confirm whether and how external ratings drive the risk weight before relying on an ECRA linkage.
- **Grounding — this node (Page 2 / Contents):** "Exposures to covered bonds 20"
- **Grounding — related node (Page 301 / para 20.8(2)):** "The external credit assessments must be from an eligible external credit assessment institution (ECAI) as recognized by SAMA"
- **Caveat:** Node A's provided context does not include the covered-bond substantive text; the ECRA connection is inferred from the framework structure and not verified against the covered-bonds paragraphs — confirm in the primary text.

### [[Standardized Credit Risk Assessment Approach (SCRA)]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting a covered-bond exposure, note that the surrounding standardized-approach framework for bank exposures relies on the SCRA for unrated counterparties, and both regimes impose the same conservative due-diligence override. The covered-bond due-diligence rule (7.35) mirrors the bank-exposure/SCRA due-diligence discipline (7.16): due diligence can push a risk weight one bucket higher but must never lower the weight below the external rating. Conclude that where a covered bond or its issuing bank is unrated, you fall into the SCRA classification logic, and that due diligence is a floor-raising, never floor-lowering, exercise.
- **Grounding — this node (Page 23 / 7.35):** "Due diligence analysis must never result in the application of a lower risk weight than that determined by the external rating."
- **Grounding — related node (Page 17 / 7.16-7.17):** "Banks will apply the SCRA to all their unrated bank exposures... classify bank exposures into one of three risk-weight buckets (i.e. Grades A, B and C)."

#graphify/document #graphify/EXTRACTED #community/Bank__ECAI_Exposures #graphify/enriched
