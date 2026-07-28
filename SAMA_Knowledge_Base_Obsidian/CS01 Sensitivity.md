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

# CS01 Sensitivity

## Connections

### [[Credit Spread Risk (CSR)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for Credit Spread Risk, treat CS01 as the prescribed sensitivity input for the CSR class: [7.20] defines the delta CSR sensitivity for non-securitisation and both securitisation categories as CS01, measured by a one-basis-point credit-spread shift. The link tells you CSR capital is built from CS01 figures fed into the same net/risk-weight/aggregate steps of [7.4], and that where counterparty-specific curves are unavailable the bank may proxy PV01 to CS01. For a review you would confirm the CSR charge traces to properly computed CS01 sensitivities and that any PV01-to-CS01 proxy is used only in the permitted absence of money-market curves.
- **Grounding — this node (Page 402 / [7.20]):** "Delta CSR non-securitisation, securitisation (non-CTP) and securitisation (CTP): the sensitivity is defined as CS01"
- **Grounding — related node (Page 361):** "credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securitisation: correlation trading portfolio)"

### [[Delta Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the delta component of the sensitivities-based market-risk charge, note that CS01 is the prescribed sensitivity metric feeding delta risk for credit-spread (CSR) instruments, so the two are inputs and framework, not separate concepts. Within the same SAMA Market Risk standard, delta risk (7.4) requires banks to determine each instrument's sensitivity to prescribed risk factors, and 7.20 defines that sensitivity as CS01 for delta CSR non-securitisation, securitisation (non-CTP) and securitisation (CTP). You should conclude that delta CSR capital cannot be derived without the CS01 definition, and that CS01 outputs must be netted and risk-weighted per the delta-risk procedure.
- **Grounding — this node (SAMA_EN_3487_VER1.md / Page 402 (7.20)):** "Delta CSR non-securitisation, securitisation (non-CTP) and securitisation (CTP): the sensitivity is defined as CS01."
- **Grounding — related node (SAMA_EN_3487_VER1.md / Page 387 (7.4)):** "a bank must determine its instruments' sensitivity to a set of prescribed risk factors, risk weight those sensitivities, and aggregate ... for delta and vega risk"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
