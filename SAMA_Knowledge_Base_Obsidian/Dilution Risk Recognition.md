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

# Dilution Risk Recognition

## Connections

### [[KIRB Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** This appears to be a weak link: the dilution-risk provisions cross-reference the securitisation IRB chapters (para 22 series), and KIRB is a defined parameter within that same SEC-IRBA machinery, so dilution mitigants ultimately feed into the KIRB/capital-charge computation for a securitised receivables pool. However, the node-B context provided (CDC capital-distribution template and Tier 2 rows) does not itself ground KIRB, so the connection rests on the shared SEC-IRBA framework rather than a direct textual reference. Verify against Chapter 22 (Definition of KIRB) before relying on this link for a capital-charge determination.
- **Grounding — this node (Page 180 / Para 14.11):** "they may also be treated as first loss protection under the securitization chapters (see paragraph 22.10)"
- **Grounding — related node (Page 13 / TOC ch.22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB"
- **Caveat:** Node-B context does not contain KIRB text (it shows CDC/Tier 2 disclosure pages); the link is inferred from the shared SEC-IRBA chapter reference and should be checked against Chapter 22.

### [[RWA for Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how purchased-receivable exposures feed into your OV1/RWA disclosure, note that dilution-risk recognition sits inside the same credit-risk capital framework that produces those RWA figures. Paragraphs 14.11–14.12 govern how mitigants and guarantees reduce the pool's default and dilution risk weights, and the resulting risk weights are what populate the standardised/IRB credit-risk rows of the RWA templates. In practice you would confirm that any dilution-risk capital charge computed under these mitigation rules is correctly classified into the credit-risk (non-securitisation) rows rather than the securitisation rows, since the template explicitly carves securitisation exposures out into a separate row.
- **Grounding — this node (Page 180 / Para 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"
- **Grounding — related node (Page 751 / Row 1):** "Credit risk (excluding counterparty credit risk): RWA and capital requirements according to the credit risk standard of the Basel framework (SCRE)"

### [[SEC-IRBA (Securitization Internal Ratings-Based Approach)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing how a mitigant covering both default and dilution risk affects your capital charge for purchased receivables, the dilution-risk recognition rules and the SEC-IRBA are directly linked: para 14.11 requires banks using SEC-IRBA that can calculate an exposure-weighted LGD to do so per para 22.21, and the framework even provides illustrative examples for recognising dilution risk under SEC-IRBA. So a bank's chosen securitisation approach constrains how it treats dilution mitigants. You would check whether your SEC-IRBA eligibility and LGD-calculation capability trigger the specific treatment in 22.21 rather than a general mitigation rule.
- **Grounding — this node (Page 180 / Para 14.11):** "banks using the Securitization Internal Ratings-Based Approach (SEC-IRBA) that are able to calculate an exposure-weighted LGD must do so as defined in paragraph 22.21"
- **Grounding — related node (Page 13 / TOC ch.22 & 27):** "Illustrative examples for recognition of dilution risk when applying the Securitization Internal Ratings-Based Approach (SEC-IRBA)"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
