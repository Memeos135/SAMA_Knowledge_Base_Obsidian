---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Credit Risk & CCP Capital"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Credit_Risk__CCP_Capital
  - graphify/enriched
---

# Minimum Haircut Floors for SFTs

## Connections

### [[Netting Set]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether the SFT minimum haircut floors bite, keep in mind they operate on a different unit of account than the SA-CCR netting-set machinery: the haircut floors in Chapter 10 apply per in-scope SFT (with defined scope and exemptions for central banks and certain cash-collateralized lending), whereas the netting-set concept governs how counterparty credit-risk exposure (EAD/RC) is aggregated. The link is a cross-reference within the same framework, not an obligation flowing from one to the other. Check the Chapter 10 scope and exemption tests (10.3–10.5) to confirm a transaction is in-scope before applying floors, and treat netting-set aggregation as a separate exposure-measurement step.
- **Grounding — this node (Page 82-83 / 10.1-10.6):** "This chapter specifies the treatment of certain non-centrally cleared securities financing transactions (SFTs)... the haircut floors for SFTs referred to above (herein referred to as 'in-scope SFTs')"
- **Grounding — related node (Page 47 / 6.79-6.80):** "Where a single margin agreement applies to several netting sets... the PFE add-on must be calculated according to the unmargined methodology."
- **Caveat:** The two concepts belong to different SA-CCR chapters (SFT haircut floors vs netting-set aggregation); the relationship is contextual co-reference, not a direct obligation chain.

#graphify/document #graphify/INFERRED #community/Credit_Risk__CCP_Capital #graphify/enriched
