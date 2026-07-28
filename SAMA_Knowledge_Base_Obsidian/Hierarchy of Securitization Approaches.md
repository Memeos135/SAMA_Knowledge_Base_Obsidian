---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Securitization Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Hierarchy of Securitization Approaches

## Connections

### [[SEC-ERBA (External Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When selecting the capital approach for a securitization exposure, treat SEC-ERBA as one option positioned within a mandated hierarchy rather than a free choice: the framework requires capital to be 'calculated as determined by the hierarchy of approaches for securitization exposures' (18.59-18.62), and SEC-ERBA (chapter 20) is the external-ratings-based method that applies where a rating exists. The hierarchy also governs inferred and pari passu ratings, so ERBA's availability depends on the exposure's place in that ordering. Conclude that you must confirm ERBA is the approach the hierarchy actually assigns before applying it, rather than defaulting to it because an external rating happens to be available.
- **Grounding — this node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62."
- **Grounding — related node (Page 13 / Ch.20):** "Securitization: External-ratings-based approach (SEC-ERBA) ... Operational requirements for use of external credit assessments"

### [[SEC-IRBA (Securitization Internal Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for a securitization exposure, recognise that SEC-IRBA is the top of the mandated hierarchy of approaches referenced in 18.59-18.62: capital 'as determined by the hierarchy' must generally be computed under IRBA (chapter 22) where the bank can calculate KIRB for the underlying pool, before falling to ERBA/SA. The hierarchy also drives treatment of protected/unprotected sub-tranches and resecuritizations. Conclude that IRBA is not optional where the hierarchy assigns it, and its applicability turns on the bank's ability to derive KIRB and the defined attachment/detachment and supervisory parameters, not on preference.
- **Grounding — this node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62."
- **Grounding — related node (Page 13 / Ch.22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB ... Calculation of risk weight"

### [[SEC-SA (Standardized Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital treatment of a securitization exposure, do not select SEC-SA in isolation: it sits inside a mandatory ranking (the 'hierarchy of approaches for securitization exposures') that dictates which method a bank may use and under what conditions. The hierarchy provisions repeatedly point to SEC-SA (chapter 19) as one of the ordered options, and SEC-SA itself carries embedded constraints — a 15% floor risk weight and a rule that an unrated junior exposure cannot be risk-weighted below the next more senior rated tranche. Conclude that eligibility for SEC-SA must first be confirmed against the hierarchy, and that even once SEC-SA applies its floors are non-negotiable, so any SEC-SA output must be tested against these minimums.
- **Grounding — this node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62"
- **Grounding — related node (Page 304 / 19.15):** "The resulting risk weight is subject to a floor risk weight of 15%... shall not be lower than the risk weight for the next more senior rated exposure"

### [[Securitization Internal Assessment Approach (SEC-IAA)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank holds securitization exposures to ABCP programmes (e.g. liquidity facilities or credit enhancements), note that SEC-IAA sits within the hierarchy of approaches but is not self-selecting: 21.1 requires the bank to notify SAMA and obtain approval, hold at least one approved IRB model, and map internal assessments to ECAI-equivalent ratings before using IAA. The hierarchy provisions (18.59-18.62) determine where IAA applies relative to other approaches. Conclude that IAA cannot be relied on absent SAMA approval and the stated operational preconditions, and its use must still be consistent with the hierarchy's ordering.
- **Grounding — this node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62."
- **Grounding — related node (Page 313 / 21.1):** "banks shall notify SAMA of the transactions and seek approval to apply the IAA treatment ... provided that the bank has at least one approved IRB model"

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
