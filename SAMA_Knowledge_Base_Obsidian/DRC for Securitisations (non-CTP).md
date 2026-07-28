---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "concept"
community: "Default Risk Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default_Risk_Capital
  - graphify/enriched
---

# DRC for Securitisations (non-CTP)

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the default-risk charge for ordinary (non-CTP) securitisation tranches, read the general DRC concept together with the non-CTP securitisation rules, because the latter deliberately modify the base default-risk methodology. Both derive from SAMA's Market Risk minimum capital framework: the non-CTP rules borrow the DRC approach but drop the LGD ratio (LGD is already embedded in securitisation risk weights) and restrict offsetting to tranches sharing the same underlying asset pool. You would conclude that the securitisation charge cannot be computed by plain application of the non-securitisation DRC rules; the tranche-specific carve-outs in 8.27–8.35 govern.
- **Grounding — this node (SAMA_EN_3553_VER1.md / Page 81 (8.27)):** "the same approach must be followed as for default risk (non-securitisations), except that an LGD ratio is not applied to the exposure"
- **Grounding — related node (SAMA_EN_3487_VER1.md / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book (reported in row 16)"

### [[Hedge Benefit Ratio (HBR)]] — `references` [EXTRACTED]
- **What this link tells you:** For non-CTP securitisation DRC, the hedge benefit ratio applies to net short securitisation exposures within a bucket, but only after the tightly constrained offsetting of [8.29] is respected. Section 8.33(1) applies the HBR discount, while 8.35 confirms no hedging is recognised across buckets, so total DRC is a simple sum of bucket-level requirements. A reviewer should check that offsetting was limited to tranches with the same underlying asset pool (no netting across different pools or different tranches of the same pool) before any HBR benefit is claimed.
- **Grounding — this node (Page 81 / 8.29):** "For default risk of securitisations (non-CTP), offsetting is limited to a specific securitisation exposure (ie tranches with the same underlying asset pool)."
- **Grounding — related node (Page 83 / 8.33(1); 8.35):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket... No hedging is recognised between different buckets."
- **Caveat:** The HBR is defined at [8.23], which is referenced but not fully quoted here; confirm the definition and its risk-weight interaction in the primary text.

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
