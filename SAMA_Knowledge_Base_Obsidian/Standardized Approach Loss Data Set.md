---
source_file: "markdown/SAMA_EN_4041_VER1.md"
type: "concept"
community: "Operational Risk Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Operational_Risk_Capital
  - graphify/enriched
---

# Standardized Approach Loss Data Set

## Connections

### [[Detailed Loss Event Type Classification]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a bank must capture in its operational-risk loss data set under the standardized approach, treat the gross/net loss classification rules (inclusions, exclusions, reference dates) as an integral part of building the data set, not a separate exercise. Both provisions sit in section 9 of the same operational-risk framework (SAMA_EN_4041), where 9.1 requires policies to build the data set and 9.2 defines how gross loss, recoveries, pending and timing losses are classified. For a capital-calculation decision you should conclude that a data set omitting the mandatory gross-loss items (e.g. legal expenses, provisions, pending losses) or misapplying the exclusion list would not meet the loss-data standards SAMA requires.
- **Grounding — this node (Page 10 / 9.1):** "In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures to address several features, including gross loss definition, reference date and grouped losses."
- **Grounding — related node (Page 10 / 9.2.2):** "The following items must be included in the gross loss computation of the loss data set: a) Direct charges, including impairments and settlements..."

### [[Loss Component (LC)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's LC is validly calculated, recognise that the LC is computed from the standardized approach loss data set — the two are linked by construction, since the LC's 10-year average losses draw on the losses captured in that data set. The data set must be built to specific inclusion/exclusion rules (gross loss items, pending and timing losses in; insurance premiums and enhancement costs out) and use net-of-recovery figures only after payment is received. Before relying on an LC figure, verify the underlying data set meets the sections 8–10 collection standards, because non-compliant data forces a BIC-only capital floor.
- **Grounding — this node (Page 10 / Art 9.1):** "In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures"
- **Grounding — related node (Page 7 / Art 7.3.3):** "The calculation of average losses in the Loss Component must be based on 10 years of high-quality annual loss data"

### [[Pillar 3 Disclosure]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** If you are scoping disclosure obligations for a bank using internal loss data, note that the operational-risk loss data set appears to feed directly into Pillar 3 disclosure duties rather than remaining an internal capital-calculation artifact. SAMA_EN_4041 requires that exclusions of internal loss data and any resulting ILM multipliers 'must be publicly disclosed in Pillar 3', and the separate Pillar 3 framework (SAMA_EN_4234) governs how such disclosures must be presented, assured, and timed. This link is inferred from the cross-document reference to Pillar 3, so verify in the primary Pillar 3 templates exactly which loss-data figures and narratives are mandated before relying on the scope of the disclosure obligation.
- **Grounding — this node (Page 8 / 7.4.1):** "The exclusion of internal loss data due to non-compliance with the loss data standards, and the application of any resulting multipliers, must be publicly disclosed in Pillar 3."
- **Grounding — related node (Page 5 / 2.1):** "Disclosure requirements are an integral part of the Basel framework... the Tables and Templates are applicable to all domestic banks both on a consolidated basis... and on a standalone basis."
- **Caveat:** Relationship is INFERRED from a cross-reference to 'Pillar 3'; confirm the specific loss-data disclosure templates in SAMA_EN_4234 before treating this as the governing disclosure requirement.

#graphify/concept #graphify/EXTRACTED #community/Operational_Risk_Capital #graphify/enriched
