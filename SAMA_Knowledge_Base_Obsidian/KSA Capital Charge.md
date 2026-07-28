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

# KSA Capital Charge

## Connections

### [[Securitization Exposures of Mixed Pools]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the maximum capital charge (cap) for a securitization exposure, do not apply a single approach across the whole pool if it is a mixed pool. Paragraph 18.52-18.53 define the KSA-based capital charge as a component that, for mixed pools, must be added to the IRB portion — KP equals the exposure-weighted average using KSA for the part where KIRB cannot be calculated and KIRB for the part where it can (18.55). Conclude that a mixed-pool cap requires splitting the underlying pool and computing the SA and IRB components separately, not using KSA alone.
- **Grounding — this node (Page 249 / 18.55(2)(c)):** "For a mixed pool, KP equals the exposure-weighted average capital charge of the underlying pool using KSA ... and KIRB"
- **Grounding — related node (Page 248 / 18.52):** "In the case of mixed pools, the overall cap should be calculated by adding up the capital before securitization"

### [[Securitization Standardized Approach (SEC-SA)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the capital charge cap for a bank holding securitization exposures over an SA pool, you must use KSA as the underlying-pool capital charge (KP) feeding the SEC-SA calculation. Paragraph 18.54(2)(b) fixes KP equal to KSA as defined in 19.2 to 19.5 for an SA pool, and 18.53 confirms SEC-SA users may cap capital at the pre-securitization charge. Conclude that the SEC-SA output cannot be assessed without first deriving KSA on the underlying exposures, and for mixed pools you blend KSA and KIRB on an exposure-weighted basis per 18.54(2)(c).
- **Grounding — this node (Page 249 / 18.54(2)(b)):** "For an SA pool, KP equals KSA as defined in 19.2 to 19.5."
- **Grounding — related node (Page 248 / 18.53):** "An originating or sponsor bank using the SEC-ERBA or SEC-SA ... may apply a maximum capital requirement ... equal to the capital requirement that would have been assessed against the underlying exposures"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
