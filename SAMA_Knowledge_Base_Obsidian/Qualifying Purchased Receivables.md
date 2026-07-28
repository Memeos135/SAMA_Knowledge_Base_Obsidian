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

# Qualifying Purchased Receivables

## Connections

### [[IRB Asset Classes]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying purchased receivables, recognise this is a cross-cutting treatment that 'straddles two asset classes' — it applies within both the corporate and retail asset classes rather than being a standalone class, subject to eligibility and operational conditions. The corpus lists corporate and retail purchased receivables as distinct roll-out categories and permits a top-down approach only where the receivables meet arm's-length, third-party and other conditions. A reader should therefore confirm both the underlying asset class (corporate vs retail, which dictates F-IRB vs A-IRB availability) and the specific eligibility criteria before applying purchased-receivables treatment.
- **Grounding — this node (Page 112 / 10.42):** "The treatment potentially straddles two asset classes. For eligible corporate receivables, both a foundation and advanced approach are available"
- **Grounding — related node (Page 99 / 10.4):** "Within the corporate and retail asset classes, a distinct treatment for purchased receivables may also apply provided that certain conditions are met"

### [[PD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising purchased receivables under IRB, whether you must produce obligor-level PD estimates turns on which sub-track applies: for corporate receivables banks are 'in general expected to assess the default risk of individual obligors' (i.e. bottom-up PD estimation), whereas the top-down approach relaxes that only where meeting the full corporate IRB minimum requirements would be an undue burden. The link tells you PD estimation obligations are not uniform across purchased receivables — the receivables node carves out when individual obligor assessment is required versus when pool-based top-down treatment is permitted with SAMA approval. Conclude that you must first classify the receivables (retail vs corporate, top-down eligibility) before deciding whether obligor-level PD estimation is mandatory.
- **Grounding — this node (Page 107 / para 10.27):** "for purchased corporate receivables, banks are expected to assess the default risk of individual obligors... However, the top-down approach may be used"
- **Grounding — related node (Page 751 / rows 3 and 5):** "(foundation/advanced) internal rating based approaches: RWA and capital requirements according to the F-IRB approach and/or A-IRB approach (as specified in SCRE10 to SCRE16...)"
- **Caveat:** Node A's supplied context is the OV1 RWA-overview template rather than the substantive PD-estimation chapter; the PD/top-down linkage is grounded chiefly in node B's text, so verify the PD estimation minimum-requirement chapters (14/16) referenced there before relying on this.

### [[RWA for Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When computing RWA for a purchased-receivables programme, the classification decisions in the purchased-receivables node directly drive which RWA line applies — corporate receivables may use F-IRB or A-IRB (retail eligible only for A-IRB), and these are the modelled IRB approaches the RWA/OV1 template reports separately from the standardised approach. The receivables node sets eligibility (arm's-length, third-party seller, claim on proceeds) and SAMA's power to impose concentration limits or deny top-down, while the RWA node confirms IRB-derived RWA is only recognised for approaches the bank has SAMA approval to use. Conclude that an ineligible or SAMA-denied programme cannot be reported under the IRB RWA cells and must fall back to standardised treatment, so confirm eligibility and approval before selecting the RWA methodology.
- **Grounding — this node (Page 112 / para 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available... For eligible retail receivables... only the A-IRB approach is available."
- **Grounding — related node (Page 755 / cell 1/a):** "RWA for modelled approaches that banks have SAMA approval to use... subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB)...)"

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
