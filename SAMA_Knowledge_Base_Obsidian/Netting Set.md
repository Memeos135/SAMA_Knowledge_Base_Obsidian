---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Netting Set

## Connections

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** When checking IMM exposure figures, confirm the unit of measurement is the netting set as defined in the framework, because IMM measures CCR exposure or EAD at netting-set level, not per trade. Paragraph 7.6 states EAD is measured at the netting set defined in Chapter 4 and 7.61–7.71, so an incorrectly constituted netting set (or improper aggregation of collateral and margin agreements) directly distorts the capital outcome. You would therefore verify that trades are validly grouped into legally enforceable netting sets before relying on the aggregated IMM EAD.
- **Grounding — this node (Page 47 / 6.79):** "Where a single margin agreement applies to several netting sets... collateral will be exchanged based on mark-to-market values that are netted across all transactions"
- **Grounding — related node (Page 49 / 7.6):** "CCR exposure or EAD is measured at the level of the netting set as defined in Chapter 4 of this framework and 7.61 to 7.71 of this framework."

### [[Minimum Haircut Floors for SFTs]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether the SFT minimum haircut floors bite, keep in mind they operate on a different unit of account than the SA-CCR netting-set machinery: the haircut floors in Chapter 10 apply per in-scope SFT (with defined scope and exemptions for central banks and certain cash-collateralized lending), whereas the netting-set concept governs how counterparty credit-risk exposure (EAD/RC) is aggregated. The link is a cross-reference within the same framework, not an obligation flowing from one to the other. Check the Chapter 10 scope and exemption tests (10.3–10.5) to confirm a transaction is in-scope before applying floors, and treat netting-set aggregation as a separate exposure-measurement step.
- **Grounding — this node (Page 47 / 6.79-6.80):** "Where a single margin agreement applies to several netting sets... the PFE add-on must be calculated according to the unmargined methodology."
- **Grounding — related node (Page 82-83 / 10.1-10.6):** "This chapter specifies the treatment of certain non-centrally cleared securities financing transactions (SFTs)... the haircut floors for SFTs referred to above (herein referred to as 'in-scope SFTs')"
- **Caveat:** The two concepts belong to different SA-CCR chapters (SFT haircut floors vs netting-set aggregation); the relationship is contextual co-reference, not a direct obligation chain.

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
