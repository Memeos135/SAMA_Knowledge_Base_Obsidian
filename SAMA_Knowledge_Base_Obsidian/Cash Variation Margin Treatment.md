---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Leverage Ratio Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Leverage_Ratio_Exposures
  - graphify/enriched
---

# Cash Variation Margin Treatment

## Connections

### [[Derivative Exposures (Leverage Ratio)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the derivatives component of the leverage exposure measure, the cash variation margin treatment is a conditional offset you can only apply if the enumerated criteria (daily mark-to-market, unrestricted use of cash received, single MNA, full amount exchanged, specified currency) are met. Under SLEV7.2.4, qualifying cash VM received reduces the replacement cost (but not the PFE) of the derivative asset, and VM provided may be deducted from the exposure measure. Before netting VM against derivative exposures, confirm each condition is satisfied — otherwise the reduction is not permitted and the derivative exposure must be reported gross of that margin.
- **Grounding — this node (Page 710 / 7.2.4):** "the cash portion of variation margin received may be used to reduce the replacement cost portion of the Leverage ratio exposure measure"
- **Grounding — related node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions ... net of cash variation margin"

#graphify/concept #graphify/EXTRACTED #community/Leverage_Ratio_Exposures #graphify/enriched
