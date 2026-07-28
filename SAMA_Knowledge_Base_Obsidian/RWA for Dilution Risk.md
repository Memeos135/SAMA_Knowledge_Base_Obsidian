---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Securitization IRB Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_IRB_Approach
  - graphify/enriched
---

# RWA for Dilution Risk

## Connections

### [[Eligible Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for a purchased-receivables or securitization portfolio, do not scope dilution-risk RWA as a stand-alone calculation — it only arises within the 'eligible purchased receivables' treatment and its recognition of mitigants feeds directly into the purchased-receivables/securitization capital chain (SEC-IRBA, KIRB). The dilution-risk provisions govern how collateral or guarantees covering dilution or default losses are recognized, while the purchased-receivables definition (paras 10.25–10.29) sets which retail/corporate receivables and top-down approaches even qualify. Conclude that you must confirm the receivables meet the eligibility and operational requirements before applying any dilution-risk mitigant treatment; the two provisions must be read together for a defensible RWA figure.
- **Grounding — this node (Page 173 / 14.11):** "When collateral or partial guarantees obtained on receivables provide first loss protection ... and these mitigants cover default losses, dilution losses, or both"
- **Grounding — related node (Page 313 / 22.6):** "the treatment for eligible purchased receivables described in paragraphs 10.25 to 10.29, 14.2 to 14.7 ... may be used"

### [[KIRB Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalizing purchased receivables with non-immaterial dilution risk that are also securitized, treat the dilution capital charge as an input to KIRB, not a standalone add-on. The worked example computes KIRB,Pool as KIRB,Dilution + KIRB,Default (13.47% + 6.69% = 20.16%), and para 14.5 requires EAD for default risk to be reduced by the dilution capital requirement — so the two components feed the single KIRB used in the SEC-IRBA capital-charge cap under chapter 22. Conclude that dilution-risk RWA must be quantified before KIRB can be finalized, and that omitting or double-counting it distorts both the pool capital charge and the securitization cap.
- **Grounding — this node (Page 338 / para 27.5):** "KIRB, Pool = KIRB, Dilution + KIRB, Default = 13.47% + 6.69% = 20.16%"
- **Grounding — related node (Page 249 / para 18.54):** "For an IRB pool, KP equals KIRB as defined in 22.2 to 22.13."

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When first-loss mitigants cover dilution risk (alone or with default risk) on securitized receivables, apply the SEC-IRBA LGD rule, not just the receivables chapter. Para 14.11 states that where the same mitigant covers both default and dilution risk, banks using SEC-IRBA that can calculate an exposure-weighted LGD must do so as defined in para 22.21, and chapter 27 gives illustrative examples specifically for recognizing dilution risk under SEC-IRBA. Conclude that the dilution-risk treatment and the securitization approach are linked through the LGD calculation, so you should determine the SEC-IRBA LGD inputs before finalizing dilution capital where these mitigants exist.
- **Grounding — this node (Page 173 / para 14.11):** "When the same mitigant covers both default and dilution risk, banks using the Securitization Internal Ratings-Based Approach (SEC-IRBA) that are able to calculate an exposure-weighted LGD must do so as defined in paragraph 22.21."
- **Grounding — related node (Page 6 / chapter 27 heading):** "Illustrative examples for recognition of dilution risk when applying the Securitization Internal Ratings-Based Approach (SEC-IRBA) to securitization"

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
