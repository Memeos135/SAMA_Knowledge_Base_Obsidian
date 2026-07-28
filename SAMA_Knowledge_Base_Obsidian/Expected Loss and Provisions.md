---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "IRB Credit Risk Approach"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Expected Loss and Provisions

## Connections

### [[Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **What this link tells you:** When distinguishing operational-risk 'net loss' figures from the credit-risk LGD parameter, keep them separate: the LGD node governs credit-risk IRB estimation, while the linked expected-loss material concerns operational-risk loss data collection net of recoveries. Both live in the same SAMA capital rulebook but under different regimes — own-LGD estimates (para 16.82) must reflect a long-run default-weighted average loss rate and downturn conditions, whereas the operational loss dataset nets recoveries only after payment is received. Conclude that operational net-loss data is not an LGD input; verify which regime a 'loss net of recoveries' figure belongs to (SCRE IRB vs operational-risk framework) before using it in capital calculations.
- **Grounding — this node (Page 541 / 9.2.1):** "Banks should use losses net of recoveries (including insurance recoveries) in the loss dataset."
- **Grounding — related node (Page 211 / 16.82):** "This LGD cannot be less than the long-run default-weighted average loss rate given default calculated based on the average economic loss of all observed defaults"
- **Caveat:** The 'references' link crosses regimes (operational-risk loss data vs credit-risk LGD); the shared 'loss/recovery' vocabulary is not a direct dependency — treat as a co-location lead and confirm the applicable framework.

### [[Probability of Default (PD)]] — `references` [EXTRACTED]
- **What this link tells you:** Do not conflate operational-risk 'expected loss/provisions' with the credit-risk PD parameter when scoping which capital rules apply to a portfolio: the loss-data material here concerns operational-risk capital, whereas PD is a credit-risk IRB input. Both are computed under the same SAMA capital rulebook but through separate calculation streams, and the source itself excludes credit-risk-driven operational events accounted for in credit RWAs from the operational loss set. Conclude that provisioning/loss figures for operational risk should not be used as, or mixed with, PD-based credit capital inputs; check which risk category and template a figure belongs to before relying on it.
- **Grounding — this node (Page 540):** "Operational loss events related to credit risk and that are accounted for in credit risk RWAs should not be included in the loss data set."
- **Grounding — related node (Page 816 / Template CR9):** "the model that is used to assign a risk rating to an obligor, and/or the model that calibrates the internal ratings to the PD scale."
- **Caveat:** The 'references' relation is weak — the two nodes address different risk regimes (operational vs credit) within the same rulebook; treat as a co-location lead, not a direct dependency.

### [[Supervisory Slotting Approach]] — `references` [EXTRACTED]
- **What this link tells you:** If you are mapping which capital regime governs a given exposure, treat operational-risk loss provisioning and the supervisory slotting approach as distinct components of the same Basel/SCRE-derived capital framework rather than interchangeable methods. The linked material sits within one SAMA capital rulebook: operational-risk loss data feeds the operational-risk capital calculation, while supervisory slotting (SCRE13) produces credit-risk RWA reported separately in the OV1 template. Conclude that provisioning inputs for operational losses do not migrate into the slotting credit-risk numbers; verify the SCRE13 cross-reference before attributing any exposure's RWA to the slotting approach.
- **Grounding — this node (Page 540):** "Operational loss events related to credit risk and that are accounted for in credit risk RWAs should not be included in the loss data set."
- **Grounding — related node (Page 751):** "Of which: supervisory slotting approach: RWA and capital requirements according to the supervisory slotting approach (as specified in SCRE13)."
- **Caveat:** The 'references' link is thin — the two topics co-occur in the same capital rulebook but no direct textual cross-reference between them is shown; confirm against SCRE13 and the operational-risk sections.

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
