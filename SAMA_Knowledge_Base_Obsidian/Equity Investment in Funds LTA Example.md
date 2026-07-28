---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "CCR Collateral & Mitigation"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/CCR_Collateral__Mitigation
  - graphify/enriched
---

# Equity Investment in Funds LTA Example

## Connections

### [[Leverage Adjustment Example]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When computing capital requirements for a bank's equity investment in a fund under the look-through approach (LTA), treat the leverage adjustment as an integral step of the same calculation, not a separate rule — paragraph 24.12 requires a leverage adjustment 'to the average risk weight of the fund' once total RWA is computed under the LTA or MBA. The two nodes appear to be sections of the same equity-investments-in-funds chapter (24) of SAMA_EN_3502, so the LTA output feeds directly into the leverage-adjusted RWA formula (capped at 1250%). Verify against the primary chapter 24 text, since these are inferred document fragments rather than a stated cross-reference.
- **Grounding — this node (Page 6 (TOC) / Section 24):** "24. Equity investments in funds ... The look-through approach 325 ... Leverage adjustment 329"
- **Grounding — related node (Page 329 / Para 24.12-24.13):** "a bank must apply a leverage adjustment to the average risk weight of the fund, as set out in 24.13, subject to a cap of 1250%"
- **Caveat:** Relationship inferred from shared chapter structure; confirm the LTA/leverage-adjustment sequencing in the full chapter 24 text before relying on it.

### [[Look-Through Approach for Funds]] — `semantically_similar_to` [INFERRED]
- **What this link tells you:** These two provisions both concern the look-through of funds, but they appear to sit in different capital regimes and should not be used interchangeably: SAMA_EN_3502 addresses the LTA for the credit-risk/banking-book capital treatment of equity investments in funds, while SAMA_EN_3553 (para 7.34-7.35) applies a look-through under the market-risk sensitivities-based framework, treating underlying positions as if held directly. The shared 'look-through' concept is genuine but the calculation purpose and conditions differ (banking book RWA vs market-risk sensitivities and index-netting criteria). Confirm which framework governs the specific exposure before transporting rules from one to the other.
- **Grounding — this node (Page 6 (TOC) / Section 24):** "24. Equity investments in funds ... The look-through approach 325"
- **Grounding — related node (SAMA_EN_3553 Page 50 / Para 7.35):** "banks must apply a look-through approach and treat the underlying positions of the fund as if the positions were held directly by the bank"
- **Caveat:** Link is a topical/semantic overlap only; the two documents apply look-through in different capital regimes (credit risk vs market risk). Do not assume identical scope or method — verify the governing framework.

### [[Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital treatment for a bank's equity investments in funds, treat the look-through approach (LTA) worked example as an illustrative appendix subordinate to the main Credit Risk framework rather than a free-standing rule. Both nodes are part of the same SAMA-issued Minimum Capital Requirements for Credit Risk document (issued under the Charter, Royal Decree M/36, and the Banking Control Law), where chapter 24 sets the LTA/MBA/FBA hierarchy and the example simply demonstrates it. Conclude that the binding obligations (e.g. the 1250% FBA risk weight when neither LTA nor MBA is feasible) come from the framework's operative paragraphs; use the example only to check application, not to derive obligations.
- **Grounding — this node (Page 6 / Contents ch.24):** "24. Equity investments in funds ... The look-through approach ... The mandate-based approach ... The fall-back approach"
- **Grounding — related node (Page 328 / para 24.8):** "Where neither the LTA nor the MBA is feasible, banks are required to apply the FBA. The FBA applies a 1250% risk weight to the bank's equity investment in the fund."

### [[SA-CCR Counterparty Credit Risk Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the look-through approach to a bank's equity investment in a fund that holds derivatives, note that counterparty credit risk on the fund's derivative exposures is captured via the CCR/SA-CCR machinery, with a specific overlay: the CCR exposure must be multiplied by 1.5 before applying the counterparty risk weight in lieu of a CVA charge. This links the funds chapter (Ch. 24) to the SA-CCR/CCR exposure calculation used generally for derivatives. You should conclude that fund look-through capital cannot ignore embedded derivative counterparty exposure and must fold in the 1.5 multiplier where the CVA charge is not separately determined.
- **Grounding — this node (Page 328 / para 24.x (funds)):** "Instead of determining a CVA charge... banks must multiply the CCR exposure by a factor of 1.5 before applying the risk weight associated with the counterparty"
- **Grounding — related node (Page 82 / para 9.65):** "Under the standardized approach for Counterparty Credit Risk Framework (SA-CCR), the calculation of the counterparty credit risk charge for an individual contract will be calculated using the following formula"

#graphify/document #graphify/EXTRACTED #community/CCR_Collateral__Mitigation #graphify/enriched
