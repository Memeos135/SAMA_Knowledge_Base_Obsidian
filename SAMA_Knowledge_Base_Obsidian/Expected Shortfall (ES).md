---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "concept"
community: "Expected Shortfall Modelling"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Expected_Shortfall_Modelling
  - graphify/enriched
---

# Expected Shortfall (ES)

## Connections

### [[IMCC (Aggregate Capital Requirement for Modellable Risk Factors)]] — `references` [EXTRACTED]
- **What this link tells you:** When testing IMA capital adequacy, understand that ES is not the final capital number — it is an input aggregated into the IMCC (aggregate capital requirement for modellable risk factors). The framework builds the internal-models capital requirement on ES techniques, but IMCC combines constrained and unconstrained ES measures for modellable factors, which is separate from the NMRF/SES add-ons for non-modellable factors. A reviewer should therefore confirm that a compliant ES figure has been correctly rolled up into IMCC, and not conclude that a correct ES alone satisfies the total internal-models capital requirement.
- **Grounding — this node (Page 118 / Art 13.1):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node (Page 105 / Art 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Caveat:** Node B's provided context does not contain the IMCC aggregation formula itself; the ES-to-IMCC linkage is stated conceptually — verify the IMCC definition and aggregation article ([13.43] and related) in the primary text before relying on the exact composition.

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how IMA capital is actually calculated, recognise that the IMA is not VaR-based at the capital-requirement level: the framework states the internal models approach capital calculation is built on Expected Shortfall (ES) techniques, so ES is the core measure a bank's IMA model must produce. This distinction matters because VaR still governs the backtesting comparison while ES drives the capital number. Conclude that any review of an IMA capital figure must confirm the ES model meets the minimum standards in chapter 13, and must not assume the capital charge is derived from the VaR used for backtesting.
- **Grounding — this node (Page 118 / Section 13):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node (Page 11 / 3.9):** "internal models approach (IMA) for market risk as described in [10] to [13]. SAMA approval is required before using the IMA approach."

### [[Liquidity Horizon]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's internal models approach (IMA) capital figure is computed correctly, treat the ES calculation and liquidity horizons as a single mandated computation, not separate topics. Article 13.4 requires the ES to be liquidity-adjusted by scaling a 10-day base-horizon result using the liquidity horizons prescribed in [13.12]/Table 2, so the assigned horizon per risk factor category directly drives the regulatory ES output. A compliance reviewer should therefore verify that each risk factor's liquidity horizon has been mapped to the correct category and applied in the ES scaling — an ES number produced without the prescribed horizon adjustment does not meet the SAMA minimum standard.
- **Grounding — this node (Page 118-119 / Art 13.1, 13.4):** "the liquidity horizons described in [13.12] must be reflected by scaling an ES calculated on a base horizon"
- **Grounding — related node (Page 123 / Table 2):** "Liquidity horizon n by risk factor ... Interest rate: specified currencies ... 10 ... Credit spread: volatility 120"

### [[Risk Factor Eligibility Test (RFET)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When deciding whether a given risk factor may enter the ES model at all, treat the RFET as the gatekeeper to ES eligibility. Under Art 11.23, a risk factor that fails the RFET (or whose data SAMA deems unsuitable) must be excluded from the ES model and instead capitalised as an NMRF; passing the RFET is a precondition, not a guarantee, since [11.25]-[11.26] impose further modellability principles. A reviewer should therefore check RFET results before accepting that any risk factor is legitimately captured within ES, rather than assuming ES coverage is complete.
- **Grounding — this node (Page 118 / Art 13.1):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node (Page 105 / Art 11.23, 11.26):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Caveat:** Relation is 'conceptually_related_to'; the ES/RFET dependency is well supported textually but confirm the precise eligibility articles ([11.13], [11.23]) in the primary text before relying on scope boundaries.

#graphify/concept #graphify/EXTRACTED #community/Expected_Shortfall_Modelling #graphify/enriched
