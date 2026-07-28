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

# RWA for Purchased Receivables

## Connections

### [[Dilution Risk Recognition]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how purchased-receivable exposures feed into your OV1/RWA disclosure, note that dilution-risk recognition sits inside the same credit-risk capital framework that produces those RWA figures. Paragraphs 14.11–14.12 govern how mitigants and guarantees reduce the pool's default and dilution risk weights, and the resulting risk weights are what populate the standardised/IRB credit-risk rows of the RWA templates. In practice you would confirm that any dilution-risk capital charge computed under these mitigation rules is correctly classified into the credit-risk (non-securitisation) rows rather than the securitisation rows, since the template explicitly carves securitisation exposures out into a separate row.
- **Grounding — this node (Page 751 / Row 1):** "Credit risk (excluding counterparty credit risk): RWA and capital requirements according to the credit risk standard of the Basel framework (SCRE)"
- **Grounding — related node (Page 180 / Para 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"

### [[Qualifying Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When computing RWA for a purchased-receivables programme, the classification decisions in the purchased-receivables node directly drive which RWA line applies — corporate receivables may use F-IRB or A-IRB (retail eligible only for A-IRB), and these are the modelled IRB approaches the RWA/OV1 template reports separately from the standardised approach. The receivables node sets eligibility (arm's-length, third-party seller, claim on proceeds) and SAMA's power to impose concentration limits or deny top-down, while the RWA node confirms IRB-derived RWA is only recognised for approaches the bank has SAMA approval to use. Conclude that an ineligible or SAMA-denied programme cannot be reported under the IRB RWA cells and must fall back to standardised treatment, so confirm eligibility and approval before selecting the RWA methodology.
- **Grounding — this node (Page 755 / cell 1/a):** "RWA for modelled approaches that banks have SAMA approval to use... subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB)...)"
- **Grounding — related node (Page 112 / para 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available... For eligible retail receivables... only the A-IRB approach is available."

### [[Securitization General Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping exposures to the correct RWA disclosure row, treat securitisation exposures as a distinct bucket: the RWA template explicitly excludes securitisation positions from the general credit-risk row and reports them separately, and the securitisation general provisions define what counts as a 'securitization exposure'. This matters because whether a transaction is captured by the securitisation framework (based on economic substance, not legal form) determines which row and which capital treatment applies. You would verify the classification against the Chapter 18 scope test before allocating exposures to credit-risk versus securitisation rows.
- **Grounding — this node (Page 751 / Row 1 & Row 16):** "(iv) securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book (reported in row 16)"
- **Grounding — related node (Page 237 / Para 18.1):** "the capital treatment of a securitization exposure must be determined on the basis of its economic substance rather than its legal form"

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
