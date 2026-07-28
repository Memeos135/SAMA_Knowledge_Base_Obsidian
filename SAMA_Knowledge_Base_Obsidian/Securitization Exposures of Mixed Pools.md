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

# Securitization Exposures of Mixed Pools

## Connections

### [[KIRB Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When capping capital on a securitization backed by a mixed pool, you cannot use a single KIRB across the whole pool; 18.54(2)(c) requires an exposure-weighted average using KIRB only for the portion where you can calculate it and KSA for the remainder. Note the threshold at 18.47: if you cannot calculate KIRB on at least 95% of the underlying exposures, you must instead use the SA-pool hierarchy, which affects whether the pool is treated as mixed or SA. Conclude that for a mixed pool you must document which exposures qualify for KIRB, blend the charges accordingly, and confirm you meet the 95% KIRB coverage test before treating the pool under the IRB-based route.
- **Grounding — this node (Page 247 / 18.47):** "Where the bank cannot calculate KIRB on at least 95% of the underlying exposures, the bank must use the hierarchy for securitization exposures of SA pools"
- **Grounding — related node (Page 249 / 18.54(2)(c)):** "For a mixed pool, KP equals the exposure-weighted average capital charge ... using KSA ... where the bank cannot calculate KIRB, and KIRB ... where a bank can calculate KIRB"

### [[KSA Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the maximum capital charge (cap) for a securitization exposure, do not apply a single approach across the whole pool if it is a mixed pool. Paragraph 18.52-18.53 define the KSA-based capital charge as a component that, for mixed pools, must be added to the IRB portion — KP equals the exposure-weighted average using KSA for the part where KIRB cannot be calculated and KIRB for the part where it can (18.55). Conclude that a mixed-pool cap requires splitting the underlying pool and computing the SA and IRB components separately, not using KSA alone.
- **Grounding — this node (Page 248 / 18.52):** "In the case of mixed pools, the overall cap should be calculated by adding up the capital before securitization"
- **Grounding — related node (Page 249 / 18.55(2)(c)):** "For a mixed pool, KP equals the exposure-weighted average capital charge of the underlying pool using KSA ... and KIRB"

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
