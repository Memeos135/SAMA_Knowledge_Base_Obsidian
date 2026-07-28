---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "Securitization IRB Approach"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_IRB_Approach
  - graphify/enriched
---

# Securitization of Non-Performing Loans

## Connections

### [[Caps for Securitization Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When applying capital caps to a securitization, first check whether the underlying pool qualifies as an NPL securitization (W ≥ 90% under 23.1), because Chapter 23 overrides the ordinary treatment for such pools. Paragraph 18.48 directs that exposures to securitizations of non-performing loans be handled with the adjustments in Chapter 23, and 23.3 even precludes SEC-IRBA where the foundation approach is used. Conclude that the general caps section does not stand alone for NPL pools — you must apply the Chapter 23 adjustments and eligibility restrictions before relying on the standard cap.
- **Grounding — this node (Page 323 / 23.1):** "A non-performing loan securitization (NPL securitization) means a securitization where the underlying pool's variable W ... is equal to or higher than 90%"
- **Grounding — related node (Page 247 / 18.48):** "For exposures to securitizations of non-performing loans as defined in paragraph 23.1, banks must apply the framework with the adjustments laid out in ... chapter 23"

### [[Look-Through Approach for Senior Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When selecting a capital approach for an NPL securitization exposure, note that the look-through approach is one of the permitted methods listed in Chapter 23, alongside SEC-IRBA and SEC-SA, but its use is constrained by the NPL-specific rules. Paragraph 23.4 references the look-through approach as an applicable route for NPL securitization risk-weighting. Conclude that where a pool meets the NPL definition, look-through remains available but must be applied within the Chapter 23 adjustments rather than as the ordinary senior-exposure cap.
- **Grounding — this node (Page 323 / 23.1):** "A non-performing loan securitization (NPL securitization) means a securitization where the underlying pool's variable W ... is equal to or higher than 90%"
- **Grounding — related node (Page 323 / 23.4):** "The risk weight applicable to exposures to NPL securitizations according to ... or the look-through approach"
- **Caveat:** NPL page 23.4 text is truncated in the source; verify the full list of permitted approaches and any risk-weight floor for NPL look-through in the primary text.

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for an exposure to a non-performing loan securitization, the NPL rules directly scope and limit SEC-IRBA availability. Para 23.3 precludes applying SEC-IRBA to an NPL securitization exposure where the bank uses the foundation approach to calculate the KIRB of the underlying pool, and 23.4 lists SEC-IRBA (chapter 22), SEC-SA (chapter 19) and the look-through approach as the eligible routes. Conclude that for NPL securitizations you must first check the F-IRB carve-out in 23.3: if the underlying KIRB was computed under the foundation approach, SEC-IRBA is unavailable and you fall to SEC-SA or LTA.
- **Grounding — this node (Page 323 / Art 23.3):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach... to calculate the KIRB"
- **Grounding — related node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"

### [[Securitization Standardized Approach (SEC-SA)]] — `references` [EXTRACTED]
- **What this link tells you:** When setting the risk weight for an exposure to a non-performing-loan securitization, SEC-SA is one of the permitted calculation routes: paragraph 23.4 expressly lists the SEC-SA 'outlined in chapter 19' alongside SEC-IRBA and the look-through approach as the methods applicable to NPL securitization exposures. Note the constraint next door — 23.3 precludes SEC-IRBA where the bank uses the foundation approach for the pool's KIRB — so SEC-SA may be the fallback in that case. You would conclude the choice of approach for an NPL securitization is governed by the Ch.23 hierarchy and its carve-outs, and should confirm which of SEC-IRBA/SEC-SA/LTA is actually available before applying a risk weight.
- **Grounding — this node (Page 323 / 23.4):** "The risk weight applicable to exposures to NPL securitizations according to ... Standardized approach (SEC-SA) outlined in chapter 19"
- **Grounding — related node (Page 6 / Ch.19):** "Standardized approach (SEC-SA) outlined in chapter 19"

#graphify/document #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
