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

# Hierarchy of Approaches for Securitization Exposures

## Connections

### [[Calculation of Capital Requirements and RWA]] — `references` [EXTRACTED]
- **What this link tells you:** When computing capital requirements and RWA for a securitization exposure, do not apply a calculation method in isolation — the hierarchy of approaches determines which method (SEC-IRBA, SEC-ERBA, SEC-SA, SEC-IAA) you are entitled to use for that pool type. 18.35 establishes that regulatory capital is required across the listed securitization exposure forms, while the hierarchy provisions define originator/pool status (IRB, mixed, SA pools per 18.15–18.17) that gates the applicable approach. Conclude that the correct RWA figure depends first on classifying the pool and selecting the mandated approach in the hierarchy, then applying the calculation and any risk-weight floors.
- **Grounding — this node (Page 231-233 / Art 18.4-18.17):** "Banks' exposures to a securitization are hereafter referred to as 'securitization exposures'... a mixed pool means a securitization pool for which a bank is able to calculate IRB parameters for some, but not all, underlying exposures."
- **Grounding — related node (Page 244 / Art 18.35):** "Regulatory capital is required for banks' securitization exposures, including those arising from the provision of credit risk mitigants... as set forth in the following sections."

### [[Internal Assessment Approach (SEC-IAA)]] — `references` [EXTRACTED]
- **What this link tells you:** When selecting a securitization approach, treat SEC-IAA as a conditional branch of the hierarchy, not a freely available option. Per 18.44, a bank in Saudi Arabia permitted to use SEC-ERBA may use SEC-IAA for unrated exposures (e.g. liquidity facilities and credit enhancements) to an SA pool within an ABCP programme, and 21.1 requires the bank to notify SAMA and obtain approval, hold at least one approved IRB model, and map internal assessments to ECAI ratings. Conclude that SEC-IAA is only reachable after the hierarchy conditions are satisfied and SAMA approval is granted, so it cannot be assumed as a default for unrated ABCP exposures.
- **Grounding — this node (Page 246 / Art 18.44):** "A bank operating in Saudi Arabia that permit to use the SEC-ERBA may use an Internal Assessment Approach (SEC-IAA)... for an unrated securitization exposure... to an SA pool within an ABCP programme."
- **Grounding — related node (Page 306 / Art 21.1):** "banks shall notify SAMA of the transactions and seek approval to apply the IAA treatment... provided that the bank has at least one approved IRB model."

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge for a bank's securitization exposure under this SAMA capital framework, you must first apply the mandated hierarchy of approaches, and SEC-IRBA is the top-ranked method in that sequence. The hierarchy governs whether a bank may use SEC-IRBA at all — it is only available where the bank can compute KIRB for the underlying pool; failing that, the bank falls through to SEC-ERBA/SEC-IAA and then SEC-SA. Conclude that you cannot select SEC-IRBA freely: verify eligibility against the hierarchy's ordering rules (chapters 18–22) before treating an SEC-IRBA risk weight as valid.
- **Grounding — this node (Page 244 / Art 18.35):** "Regulatory capital is required for banks' securitization exposures... as set forth in the following sections."
- **Grounding — related node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"

### [[Securitization Standardized Approach (SEC-SA)]] — `references` [EXTRACTED]
- **What this link tells you:** When you cannot qualify a securitization exposure for the higher-ranked methods, the hierarchy directs you to SEC-SA as the standardized fallback, and its computation carries specific constraints. SEC-SA is defined in chapter 19 (paras 19.1–19.17) and applies a 15% floor risk weight plus special adjustments for resecuritizations (supervisory parameter p set to 1.5). Conclude that reaching SEC-SA is not a free choice but a consequence of the hierarchy; once there, apply the floor and the resecuritization adjustments rather than the ordinary parameters.
- **Grounding — this node (Page 244 / Art 18.35):** "Regulatory capital is required for banks' securitization exposures... as set forth in the following sections."
- **Grounding — related node (Page 297 / Art 19.15):** "The resulting risk weight is subject to a floor risk weight of 15%."

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
