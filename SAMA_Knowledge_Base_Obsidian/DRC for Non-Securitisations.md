---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Default Risk Capital"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Default_Risk_Capital
  - graphify/enriched
---

# DRC for Non-Securitisations

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When computing DRC, treat 'DRC for non-securitisations' as one of three self-contained sub-buckets that must be aggregated with no cross-category netting. The framework states 'No diversification benefit is recognised between the DRC requirements for' non-securitisations, securitisations (non-CTP), and securitisations (CTP), and that the total for non-securitisations is a simple sum of bucket-level requirements. For the capital number, this means you cannot offset a non-securitisation long against a securitisation short to reduce DRC — verify positions are assigned to the correct category before aggregating.
- **Grounding — this node (SAMA_EN_3553 / Page 81, [8.26]):** "the total DRC requirement for non-securitisations must be calculated as a simple sum of the bucket level capital requirements"
- **Grounding — related node (SAMA_EN_3553 / Page 74, [8.4]):** "No diversification benefit is recognised between the DRC requirements for: (1) non-securitisations; (2) securitisations (non-CTP); and (3) securitisations (CTP)"

### [[Hedge Benefit Ratio (HBR)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the DRC requirement for non-securitisations, note that the hedge benefit ratio (HBR) operates only within a bucket and gives partial, not full, offset for short exposures against distinct obligors. Section 8.26 confirms that no hedging is recognised between different buckets, so the total non-securitisation DRC is a simple sum of bucket-level requirements after the within-bucket HBR is applied. A reviewer should check that any hedge benefit claimed reflects the HBR-limited partial recognition and was not extended across buckets, since cross-bucket 'hedging' is not permitted.
- **Grounding — this node (Page 81 / 8.26):** "No hedging is recognised between different buckets - the total DRC requirement for non- securitisations must be calculated as a simple sum of the bucket level capital requirements."
- **Grounding — related node (Page 83 / 8.33(1)):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket."
- **Caveat:** HBR grounding excerpt is drawn from the securitisation subsection; the non-securitisation HBR definition sits at [8.23] which is referenced but not fully quoted in the provided context.

#graphify/document #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
