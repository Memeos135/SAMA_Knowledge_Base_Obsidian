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

# KIRB Capital Charge

## Connections

### [[RWA for Dilution Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalizing purchased receivables with non-immaterial dilution risk that are also securitized, treat the dilution capital charge as an input to KIRB, not a standalone add-on. The worked example computes KIRB,Pool as KIRB,Dilution + KIRB,Default (13.47% + 6.69% = 20.16%), and para 14.5 requires EAD for default risk to be reduced by the dilution capital requirement — so the two components feed the single KIRB used in the SEC-IRBA capital-charge cap under chapter 22. Conclude that dilution-risk RWA must be quantified before KIRB can be finalized, and that omitting or double-counting it distorts both the pool capital charge and the securitization cap.
- **Grounding — this node (Page 249 / para 18.54):** "For an IRB pool, KP equals KIRB as defined in 22.2 to 22.13."
- **Grounding — related node (Page 338 / para 27.5):** "KIRB, Pool = KIRB, Dilution + KIRB, Default = 13.47% + 6.69% = 20.16%"

### [[Securitization Exposures of Mixed Pools]] — `references` [EXTRACTED]
- **What this link tells you:** When capping capital on a securitization backed by a mixed pool, you cannot use a single KIRB across the whole pool; 18.54(2)(c) requires an exposure-weighted average using KIRB only for the portion where you can calculate it and KSA for the remainder. Note the threshold at 18.47: if you cannot calculate KIRB on at least 95% of the underlying exposures, you must instead use the SA-pool hierarchy, which affects whether the pool is treated as mixed or SA. Conclude that for a mixed pool you must document which exposures qualify for KIRB, blend the charges accordingly, and confirm you meet the 95% KIRB coverage test before treating the pool under the IRB-based route.
- **Grounding — this node (Page 249 / 18.54(2)(c)):** "For a mixed pool, KP equals the exposure-weighted average capital charge ... using KSA ... where the bank cannot calculate KIRB, and KIRB ... where a bank can calculate KIRB"
- **Grounding — related node (Page 247 / 18.47):** "Where the bank cannot calculate KIRB on at least 95% of the underlying exposures, the bank must use the hierarchy for securitization exposures of SA pools"

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying SEC-IRBA, KIRB is the pool-level capital charge that anchors the whole calculation, so a bank cannot use SEC-IRBA at all unless it can compute KIRB for the underlying exposures. The framework lists 'Definition of KIRB' under the SEC-IRBA chapter, and the caps provision fixes KP=KIRB (per 22.2–22.13) for an IRB pool. Conclude that inability to calculate KIRB for part of a mixed pool forces exposure-weighted use of KSA for that portion, changing which capital approach is even available.
- **Grounding — this node (Page 249 / 18.54(2)(a)):** "For an IRB pool, KP equals KIRB as defined in 22.2 to 22.13."
- **Grounding — related node (Page 6 / ch.22):** "Internal ratings-based approach (SEC-IRBA)... Definition of KIRB"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
