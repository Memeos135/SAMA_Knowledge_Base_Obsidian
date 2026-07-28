---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "CCR & CVA Disclosure Templates"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCR__CVA_Disclosure_Templates
  - graphify/enriched
---

# Template TLAC1 - TLAC Composition

## Connections

### [[Template CC1 - Composition of Regulatory Capital]] — `references` [EXTRACTED]
- **What this link tells you:** For a G-SIB reviewer, CC1 and TLAC1 are directly coupled at the resolution-group level: for single-point-of-entry G-SIBs where the resolution group coincides with the regulatory scope of consolidation, TLAC1 rows referring to regulatory capital before adjustments coincide with information provided under CC1. TLAC1 applies only to G-SIB resolution groups, whereas CC1 is mandatory for all banks, so the overlap holds only for that G-SIB subset. This means a reviewer can cross-check TLAC1's capital-element rows against CC1 for SPE G-SIBs, but for MPE G-SIBs should not expect aggregation across resolution groups to equal CC1 values.
- **Grounding — this node (Page 774 / Instructions):** "those rows that refer to regulatory capital before adjustments coincide with information provided under Template CC1. For MPE G-SIBs ... will not necessarily equal ... values reported ... under Template CC1."
- **Grounding — related node (Page 760 / 14.3.2):** "Template CC1 details the composition of a bank's regulatory capital."

### [[Template KM2 - TLAC Key Metrics]] — `references` [EXTRACTED]
- **What this link tells you:** When preparing G-SIB resolution-group disclosures, read Template KM2 (key TLAC metrics) and Template TLAC1 (composition of TLAC) as two views of the same underlying figures, so the summary ratios in KM2 must reconcile to the detailed composition reported in TLAC1. Both templates are mandatory only for G-SIB resolution groups and are built on the same defined base — TLAC available, RWA and leverage exposure measured at resolution-group level per the FSB TLAC Term Sheet. Conclude that inconsistency between the KM2 headline metrics and the TLAC1 breakdown signals an error, and that both are governed by the same scope trigger (G-SIB / TLAC conformance date) rather than applying to all banks.
- **Grounding — this node (Page 773 / Template TLAC1):** "Provide details of the composition of a G-SIB's TLAC. ... mandatory for all G-SIBs. It should be completed at the level of each resolution group"
- **Grounding — related node (Page 748 / Template KM2):** "Provide summary information about total loss-absorbing capacity (TLAC) available, and TLAC requirements applied, at resolution group level"

#graphify/concept #graphify/EXTRACTED #community/CCR__CVA_Disclosure_Templates #graphify/enriched
