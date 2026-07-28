---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Operational Risk Standardized Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Operational_Risk_Standardized_Approach
  - graphify/enriched
---

# Loss Component (LC)

## Connections

### [[Internal Loss Multiplier (ILM)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating how a bank's own loss history feeds into its capital, note that the ILM is directly derived from the Loss Component: the LC equals 15 times average annual operational risk losses over the previous 10 years, and the ILM's value turns on whether the LC exceeds, equals, or falls below the BIC. A high LC relative to BIC pushes the ILM above one (more capital); a low LC pushes it below one. Because the LC drives the ILM, verify the loss-data observation window (10 years, or 5 on an exceptional transitional basis with SAMA approval) before relying on any ILM figure.
- **Grounding — this node (Page 7 / Art 7.3.1):** "the Loss Component (LC) is equal to 15 times average annual operational risk losses incurred over the previous 10 years"
- **Grounding — related node (Page 7 / Art 7.3.2):** "The ILM is equal to one where the Loss Component (LC) and Business Indicator Component (BIC) are equal"

### [[Standardized Approach Loss Data Set]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's LC is validly calculated, recognise that the LC is computed from the standardized approach loss data set — the two are linked by construction, since the LC's 10-year average losses draw on the losses captured in that data set. The data set must be built to specific inclusion/exclusion rules (gross loss items, pending and timing losses in; insurance premiums and enhancement costs out) and use net-of-recovery figures only after payment is received. Before relying on an LC figure, verify the underlying data set meets the sections 8–10 collection standards, because non-compliant data forces a BIC-only capital floor.
- **Grounding — this node (Page 7 / Art 7.3.3):** "The calculation of average losses in the Loss Component must be based on 10 years of high-quality annual loss data"
- **Grounding — related node (Page 10 / Art 9.1):** "In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures"

#graphify/concept #graphify/EXTRACTED #community/Operational_Risk_Standardized_Approach #graphify/enriched
