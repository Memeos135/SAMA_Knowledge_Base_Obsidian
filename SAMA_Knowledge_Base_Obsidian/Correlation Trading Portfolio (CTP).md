---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Sensitivities"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# Correlation Trading Portfolio (CTP)

## Connections

### [[DRC for Securitisations (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating default risk capital for securitisation positions, first classify whether the exposure sits in the correlation trading portfolio (CTP), because that classification selects a distinct DRC treatment. Within the same SAMA framework, [8.2] lists CTP securitisations as a separate default-risk category, and the DRC-for-securitisations (CTP) rules ([8.36]+) build on the non-CTP method but apply their own offsetting and bucketing (each index defined as a bucket; no netting across series or index families). Conclude that CTP membership is a gating determination that changes hedge recognition and bucket construction, so verify the CTP definition in [6.5] before applying either the CTP or non-CTP DRC path.
- **Grounding — this node (Page 73 / 8.2):** "The DRC requirement must be calculated for instruments subject to default risk: ... Securitisation (correlation trading portfolio, or CTP)"
- **Grounding — related node (Page 85 / 8.40):** "For default risk of securitisations (CTP), each index is defined as a bucket of..."

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the DRC calculation, treat the Correlation Trading Portfolio (CTP) as a distinct DRC risk class rather than folding it into general default-risk treatment. The market risk framework requires the DRC requirement to be computed separately for non-securitisations, securitisations (non-CTP), and securitisations (CTP), with no diversification benefit recognised across those categories. Confirm which portfolios meet the CTP definition, because misclassifying a securitisation position as non-CTP (or vice versa) changes the applicable buckets, correlations and JTD treatment and therefore the capital charge.
- **Grounding — this node (SAMA_EN_3553 / Page 73, [8.2]):** "(3) Securitisation (correlation trading portfolio, or CTP)"
- **Grounding — related node (SAMA_EN_3487 / Page 751):** "securitisation positions subject to the securitisation regulatory framework, including securitisation exposures in the banking book"

### [[Other Residual Risks]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which instruments attract the residual risk add-on (RRAO), note that CTP membership directly pulls instruments into 'other residual risks' — the two concepts are linked by definition, not just theme. In the same SAMA framework, [9.4](2) treats instruments falling under the CTP definition in [6.5] as bearing other residual risks, except those recognised as eligible hedges of risks within the CTP. Conclude that classifying a position as CTP is not the end of the capital analysis: you must also test it against the RRAO criteria and check the eligible-hedge carve-out before excluding it.
- **Grounding — this node (Page 87 / 9.4(2)):** "Instruments which fall under the definition of the correlation trading portfolio (CTP) in [6.5], except for those instruments that are recognised... as eligible hedges of risks within the CTP."
- **Grounding — related node (Page 87 / 9.4):** "Instruments bearing other residual risks are those that meet criteria (1) and (2) below"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the Sensitivities-Based Method to credit-spread positions, recognise that the Correlation Trading Portfolio (CTP) is a defined sub-category that alters the standard SbM correlation treatment rather than a separate regime. The framework introduces a specific definition of the correlation trading portfolio and, for CSR securitisations (CTP), disapplies the ordinary basis and tenor correlation parameters, using only a same-name correlation instead. Conclude that CTP-classified positions must be run through the SbM with these modified correlation rules, and standard bucket correlations cannot be assumed for them.
- **Grounding — this node (Page 27 / 6.5):** "Definition of correlation trading portfolio ... CSR securitisations (CTP)"
- **Grounding — related node (Page 27):** "the risk-weighted sensitivities are aggregated using specified correlation parameters ... a bank must calculate three sensitivities-based method capital requirement values"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
