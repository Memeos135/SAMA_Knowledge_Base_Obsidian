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

# Credit Spread Risk (CSR)

## Connections

### [[CS01 Sensitivity]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for Credit Spread Risk, treat CS01 as the prescribed sensitivity input for the CSR class: [7.20] defines the delta CSR sensitivity for non-securitisation and both securitisation categories as CS01, measured by a one-basis-point credit-spread shift. The link tells you CSR capital is built from CS01 figures fed into the same net/risk-weight/aggregate steps of [7.4], and that where counterparty-specific curves are unavailable the bank may proxy PV01 to CS01. For a review you would confirm the CSR charge traces to properly computed CS01 sensitivities and that any PV01-to-CS01 proxy is used only in the permitted absence of money-market curves.
- **Grounding — this node (Page 361):** "credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securitisation: correlation trading portfolio)"
- **Grounding — related node (Page 402 / [7.20]):** "Delta CSR non-securitisation, securitisation (non-CTP) and securitisation (CTP): the sensitivity is defined as CS01"

### [[Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the CSR charge, recognise that CTP (correlation trading portfolio) is one of the defined sub-classes of Credit Spread Risk, so a correlation-trading position is not capitalised under a generic CSR bucket but under the specific CSR securitisation (CTP) treatment. The risk-class definition on Page 361 lists CSR (securitisation: correlation trading portfolio) as a distinct class, and [7.100] applies different correlation-parameter rules to CSR securitisations (CTP) than to ordinary buckets. In practice you would verify that CTP positions are assigned to the correct CSR sub-class and that the CTP-specific curvature/correlation carve-outs are applied rather than the general CSR parameters.
- **Grounding — this node (Page 361):** "credit spread risk (securitisation: correlation trading portfolio)"
- **Grounding — related node (Page 428 / [7.100]):** "For CSR non-securitisations and CSR securitisations (CTP)... the correlation parameter is determined by whether the two names of weighted sensitivities are the same"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising credit-sensitive trading positions, treat Credit Spread Risk as one of the defined risk classes processed through the sensitivities-based method rather than as an independent capital line. The framework defines CSR risk factors (including CSR non-securitisation delta, vega and curvature along issuer credit spread curves) and feeds them into the SBM's delta/vega/curvature measures, with bond and CDS spreads treated as distinct risk factors. For a capital decision this means CSR sensitivities must be captured, risk-weighted and aggregated within the SBM, so you should verify CSR positions are mapped into the correct SBM buckets and that curvature is computed where instruments have optionality.
- **Grounding — this node (Page 396 / 7.10):** "the CSR non-securitisation curvature risk factors are defined along one dimension: the relevant issuer credit spread curves (bond and CDS)"
- **Grounding — related node (Page 385):** "Methodologies to calculate risk positions for delta, vega and curvature risks are set out in [7.3] to [7.5] and [7.15] to [7.26]"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
