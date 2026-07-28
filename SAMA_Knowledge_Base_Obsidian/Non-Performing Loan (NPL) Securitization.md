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

# Non-Performing Loan (NPL) Securitization

## Connections

### [[Look-Through Approach (LTA)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the capital charge on an NPL securitisation exposure, note that the look-through approach is one of the permitted methods, but its availability is constrained by the NPL-specific rules. Chapter 23 states NPL securitisation exposures may be treated under SEC-IRBA, SEC-SA, or the look-through approach, while also precluding SEC-IRBA where the bank uses the foundation approach for KIRB and allowing SAMA to impose a stricter W-threshold definition. Conclude that you cannot assume unrestricted LTA use for NPL pools — verify the method-selection limits in 23.3-23.4 and any stricter SAMA definition before relying on a look-through result.
- **Grounding — this node (Page 330 / 23.4):** "The risk weight applicable to exposures to NPL securitizations according to Internal ratings-based approach (SEC-IRBA)... Standardized approach (SEC-SA)... or the look-through approach"
- **Grounding — related node (Page 406 / 7.34):** "A look-through approach must always be used for indices that do not meet the criteria set out in [7.31]"
- **Caveat:** Node A's LTA excerpt is from the market-risk index look-through (ch.7), whereas 23.4 refers to the securitisation LTA (ch.24); confirm the correct LTA definition applies to NPL securitisations.

### [[SEC-IRBA (Securitization Internal Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing the capital approach for an exposure to an NPL securitization (a pool where variable W ≥ 90%), check the explicit SEC-IRBA carve-out before assuming internal-model treatment applies. The NPL provisions state that risk weights may be derived under SEC-IRBA, SEC-SA or the look-through approach, but expressly preclude SEC-IRBA where the bank uses the foundation approach to calculate the underlying pool's KIRB. Conclude that for a foundation-approach bank, SEC-IRBA is off the table for NPL securitizations, and you must fall back to another permitted approach — so confirm which KIRB method the bank uses before selecting SEC-IRBA.
- **Grounding — this node (Page 330 / 23.3):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach... to calculate the KIRB"
- **Grounding — related node (Page 13 / ch.22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"

### [[SEC-SA (Standardized Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting an exposure to a non-performing loan securitization, note that the NPL rules do not create a standalone method but route the calculation into the existing approaches — SEC-IRBA (ch 22), SEC-SA (ch 19), or the look-through approach — subject to NPL-specific constraints. Crucially, a bank using the foundation IRB approach for the underlying pool is precluded from applying SEC-IRBA to that NPL exposure, which pushes it toward SEC-SA. Conclude that you must first classify the pool as an NPL securitization (W ≥ 90%), then check the eligibility restrictions before choosing SEC-SA versus other methods, and note SAMA may impose a stricter NPL definition.
- **Grounding — this node (Page 330 / 23.3-23.4):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach ... The risk weight applicable ... Standardized approach (SEC-SA) outlined in chapter 19"
- **Grounding — related node (Page 755):** "RWA for portfolios where standardised approaches are used (cell 1/b): RWA which result from applying the above-described standardised approach"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
