---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "document"
community: "CCP Exposure Calculation"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/CCP_Exposure_Calculation
  - graphify/enriched
---

# Exposures to Central Counterparties (CCPs)

## Connections

### [[Default Fund Contribution Capital (KCMiKCCP)|Default Fund Contribution Capital (KCMi/KCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a clearing-member bank's capital for CCP exposures, treat the default-fund contribution charge as a distinct, mandatory component of the overall CCP exposure regime rather than an optional add-on. Chapter 8 requires banks to capitalize both trade exposures and default-fund contributions to a QCCP, with the risk-sensitive KCMi/KCCP formula (8.25–8.37) being the prescribed method for the latter, subject to the overall QCCP cap (8.40) and the punitive 1250% risk weight for non-qualifying CCPs (8.42). Conclude that a bank cannot capitalize CCP trade exposure in isolation — the default-fund calculation, its quarterly KCCP inputs, and the non-QCCP fallback must all be checked together.
- **Grounding — this node (Page 70 / 8.4):** "This assessment will include potential future or contingent exposures resulting from future drawings on default fund commitments"
- **Grounding — related node (Page 77 / 8.25-8.26):** "Whenever a bank is required to capitalize for exposures arising from default fund contributions to a QCCP, clearing member banks will apply the following approach."

### [[Qualifying CCP (QCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital treatment for cleared trades, first determine whether the CCP is a QCCP, because that classification drives the risk weight applied to trade exposures (e.g. the 2% weight for a clearing member's exposures to a QCCP), while non-qualifying CCPs fall to paragraphs 8.41–8.42. The QCCP definition depends on the CCP being subject to a regulator applying the PFMI (or a SAMA determination) and on the 8.37 requirements being met. For a compliance decision, verify the CCP's QCCP status and note the transitional rule: if a CCP ceases to qualify, trades may continue to be capitalized as QCCP exposures for three months unless SAMA requires otherwise—but adequate-capital responsibility under Pillar 2 persists regardless of QCCP status.
- **Grounding — this node (Page 70 / 8.3):** "Regardless of whether a central counterparty (CCP) is classified as a qualifying CCP (QCCP), a bank retains the responsibility to ensure that it maintains adequate capital for its exposures."
- **Grounding — related node (Page 71 / 8.7):** "a risk weight of 2% must be applied to the bank's trade exposure to the CCP in respect of OTC derivatives, exchange-traded derivative transactions, SFTs and long settlement transactions."

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating exposures to central counterparties, do not assume the ordinary bilateral SA-CCR netting rules apply unchanged — Chapter 8 recognises that CCP netting arrangements are less standardized and makes specific adjustments. Net replacement cost for CCP trade exposures may be used only where close-out netting meets the requirements cross-referenced in 8.10, which expressly incorporate SA-CCR provisions 6.9–6.10 for derivative transactions. Conclude that CCP exposure treatment borrows SA-CCR's netting-eligibility tests as a precondition, so those SA-CCR clauses must be satisfied before netting benefit is claimed against CCP exposures.
- **Grounding — this node (Page 72 / 8.10(2)):** "the total replacement cost of all contracts relevant to the trade exposure determination can be calculated as a net replacement cost if the applicable close-out netting sets meet the requirements set out in: ...6.9 and 6.10 of the SA-CCR"
- **Grounding — related node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions."

#graphify/document #graphify/EXTRACTED #community/CCP_Exposure_Calculation #graphify/enriched
