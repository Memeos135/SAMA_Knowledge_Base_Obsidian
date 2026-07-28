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

# DRC for Securitisations (CTP)

## Connections

### [[Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating default risk capital for securitisation positions, first classify whether the exposure sits in the correlation trading portfolio (CTP), because that classification selects a distinct DRC treatment. Within the same SAMA framework, [8.2] lists CTP securitisations as a separate default-risk category, and the DRC-for-securitisations (CTP) rules ([8.36]+) build on the non-CTP method but apply their own offsetting and bucketing (each index defined as a bucket; no netting across series or index families). Conclude that CTP membership is a gating determination that changes hedge recognition and bucket construction, so verify the CTP definition in [6.5] before applying either the CTP or non-CTP DRC path.
- **Grounding — this node (Page 85 / 8.40):** "For default risk of securitisations (CTP), each index is defined as a bucket of..."
- **Grounding — related node (Page 73 / 8.2):** "The DRC requirement must be calculated for instruments subject to default risk: ... Securitisation (correlation trading portfolio, or CTP)"

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the market-risk capital charge for a bank holding correlation-trading-portfolio (CTP) securitisation tranches, treat the general DRC framework and the CTP-specific rules as one continuous methodology rather than separate charges. Both sit within SAMA's Minimum Capital Requirements for Market Risk: the DRC concept sets the jump-to-default architecture (bucket-level capital, no cross-bucket hedging), and the CTP provisions (8.36 onward) build on that by referencing the non-CTP securitisation approach for gross JTD. You should therefore compute CTP DRC only by reading it against the base DRC and non-CTP rules it incorporates, not in isolation.
- **Grounding — this node (SAMA_EN_3553_VER1.md / Page 83 (8.36)):** "For the computation of gross JTD on securitisations (CTP), the same approach must be followed as for default risk-securitisations (non-CTP) as described in [8.27]."
- **Grounding — related node (SAMA_EN_3487_VER1.md / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book"

### [[Hedge Benefit Ratio (HBR)]] — `references` [EXTRACTED]
- **What this link tells you:** For securitisations in the correlation trading portfolio (CTP), the hedge benefit ratio governs how much offset short positions attract within an index-defined bucket, since [8.40] defines each index as a bucket for CTP default risk. Because DRC for CTP is built on the same gross/net JTD machinery ([8.36] mirrors [8.27]) and HBR provides only partial hedge recognition, a reviewer should verify that offsetting respected the strict CTP netting limits — no offset across different tranches, series or index families — before the HBR discount was applied. Do not assume CTP hedging benefit is broader than the bucket-and-HBR structure allows.
- **Grounding — this node (Page 85 / 8.40):** "For default risk of securitisations (CTP), each index is defined as a bucket of"
- **Grounding — related node (Page 83 / 8.33(1)):** "The hedge benefit discount HBR, as defined in [8.23], is applied to net short securitisation exposures in that bucket."
- **Caveat:** The HBR definition ([8.23]) is cross-referenced rather than reproduced in the provided context; verify the exact HBR formula and its CTP application in the primary text.

#graphify/document #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
