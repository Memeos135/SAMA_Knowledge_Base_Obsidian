---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Default Risk Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default_Risk_Capital
  - graphify/enriched
---

# Hedge Benefit Ratio (HBR)

## Connections

### [[DRC for Non-Securitisations]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the DRC requirement for non-securitisations, note that the hedge benefit ratio (HBR) operates only within a bucket and gives partial, not full, offset for short exposures against distinct obligors. Section 8.26 confirms that no hedging is recognised between different buckets, so the total non-securitisation DRC is a simple sum of bucket-level requirements after the within-bucket HBR is applied. A reviewer should check that any hedge benefit claimed reflects the HBR-limited partial recognition and was not extended across buckets, since cross-bucket 'hedging' is not permitted.
- **Grounding — this node (Page 83 / 8.33(1)):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket."
- **Grounding — related node (Page 81 / 8.26):** "No hedging is recognised between different buckets - the total DRC requirement for non- securitisations must be calculated as a simple sum of the bucket level capital requirements."
- **Caveat:** HBR grounding excerpt is drawn from the securitisation subsection; the non-securitisation HBR definition sits at [8.23] which is referenced but not fully quoted in the provided context.

### [[DRC for Securitisations (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** For securitisations in the correlation trading portfolio (CTP), the hedge benefit ratio governs how much offset short positions attract within an index-defined bucket, since [8.40] defines each index as a bucket for CTP default risk. Because DRC for CTP is built on the same gross/net JTD machinery ([8.36] mirrors [8.27]) and HBR provides only partial hedge recognition, a reviewer should verify that offsetting respected the strict CTP netting limits — no offset across different tranches, series or index families — before the HBR discount was applied. Do not assume CTP hedging benefit is broader than the bucket-and-HBR structure allows.
- **Grounding — this node (Page 83 / 8.33(1)):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket."
- **Grounding — related node (Page 85 / 8.40):** "For default risk of securitisations (CTP), each index is defined as a bucket of"
- **Caveat:** The HBR definition ([8.23]) is cross-referenced rather than reproduced in the provided context; verify the exact HBR formula and its CTP application in the primary text.

### [[DRC for Securitisations (non-CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** For non-CTP securitisation DRC, the hedge benefit ratio applies to net short securitisation exposures within a bucket, but only after the tightly constrained offsetting of [8.29] is respected. Section 8.33(1) applies the HBR discount, while 8.35 confirms no hedging is recognised across buckets, so total DRC is a simple sum of bucket-level requirements. A reviewer should check that offsetting was limited to tranches with the same underlying asset pool (no netting across different pools or different tranches of the same pool) before any HBR benefit is claimed.
- **Grounding — this node (Page 83 / 8.33(1); 8.35):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket... No hedging is recognised between different buckets."
- **Grounding — related node (Page 81 / 8.29):** "For default risk of securitisations (non-CTP), offsetting is limited to a specific securitisation exposure (ie tranches with the same underlying asset pool)."
- **Caveat:** The HBR is defined at [8.23], which is referenced but not fully quoted here; confirm the definition and its risk-weight interaction in the primary text.

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
