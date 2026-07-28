---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "CCP Exposure Calculation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCP_Exposure_Calculation
  - graphify/enriched
---

# Alpha Multiplier

## Connections

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing an SA-CCR capital figure, note that alpha is a fixed scaling factor applied to the whole exposure, not an optional adjustment: EAD = alpha × (RC + PFE) with alpha set at 1.4. Under 7.15 SAMA may impose a higher alpha for banks with high wrong-way risk or concentrated counterparties, and under 7.16 banks may only use internal estimates (floored at 1.2) with SAMA approval. When assessing a bank's EAD, confirm which alpha applies — the default 1.4, a SAMA-imposed higher figure, or an approved internal estimate — because it directly multiplies the entire exposure.
- **Grounding — this node (Page 51 / 7.14–7.16):** "Alpha (α) is set equal to 1.4. SAMA may require a higher alpha ... Banks should seek approval from SAMA to compute internal estimates of alpha subject to a floor of 1.2"
- **Grounding — related node (Page 19 / 6.2):** "alpha = 1.4 ... EAD = alpha ∗ (RC + PFE)"

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a bank's IMM EAD figure, check the alpha parameter as a distinct supervisory lever, because IMM does not merely output an exposure — it multiplies Effective EPE by alpha to produce regulatory EAD. Alpha is fixed at 1.4 by default, but SAMA may impose a higher value for concentrated or wrong-way-risk exposures, and internal alpha estimates require SAMA approval and are floored at 1.2. You would therefore confirm which alpha applies and whether any own-estimate was formally approved before relying on the bank's IMM capital number.
- **Grounding — this node (Page 51 / 7.14–7.16):** "Alpha (α) is set equal to 1.4. SAMA may require a higher alpha... Banks should seek approval from SAMA to compute internal estimates of alpha subject to a floor of 1.2"
- **Grounding — related node (Page 48 / 7.1):** "A bank that wishes to adopt an internal models method to measure exposure or exposure at default (EAD) for regulatory capital purposes must seek SAMA approval."

#graphify/concept #graphify/EXTRACTED #community/CCP_Exposure_Calculation #graphify/enriched
