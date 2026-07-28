---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "concept"
community: "Expected Shortfall Modelling"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Expected_Shortfall_Modelling
  - graphify/enriched
---

# IMCC (Aggregate Capital Requirement for Modellable Risk Factors)

## Connections

### [[Expected Shortfall (ES)]] — `references` [EXTRACTED]
- **What this link tells you:** When testing IMA capital adequacy, understand that ES is not the final capital number — it is an input aggregated into the IMCC (aggregate capital requirement for modellable risk factors). The framework builds the internal-models capital requirement on ES techniques, but IMCC combines constrained and unconstrained ES measures for modellable factors, which is separate from the NMRF/SES add-ons for non-modellable factors. A reviewer should therefore confirm that a compliant ES figure has been correctly rolled up into IMCC, and not conclude that a correct ES alone satisfies the total internal-models capital requirement.
- **Grounding — this node (Page 105 / Art 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 118 / Art 13.1):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Caveat:** Node B's provided context does not contain the IMCC aggregation formula itself; the ES-to-IMCC linkage is stated conceptually — verify the IMCC definition and aggregation article ([13.43] and related) in the primary text before relying on the exact composition.

### [[Stressed Expected Shortfall (SES)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** These two concepts appear to sit on opposite sides of the same internal-models capital calculation: IMCC is the aggregate charge for modellable risk factors captured in the ES model, while SES is the add-on charge for non-modellable factors excluded from it. The provided context does not contain a direct cross-reference between the IMCC and SES nodes, so the link is inferential — the connection is that a factor either flows into the ES/IMCC calculation or, on failing modellability, into SES. Before relying on this as an authoritative cross-reference, check the aggregate market-risk capital formula (referenced around [13.43]) in the primary text to confirm how IMCC and SES are summed.
- **Grounding — this node (Page 26 / [6.1]-[6.2]):** "the risk-weighted assets for market risk under the standardised approach are determined by multiplying the capital requirements"
- **Grounding — related node (Page 107 / Principle six):** "The data used to determine stressed expected shortfall (ESR,S) must be reflective of market prices observed and/or quoted in the period of stress"
- **Caveat:** Relation is 'conceptually_related_to'; the supplied context shows no explicit IMCC-SES cross-reference, so verify the aggregation rule in the primary standard before treating the two as formally linked.

#graphify/concept #graphify/EXTRACTED #community/Expected_Shortfall_Modelling #graphify/enriched
