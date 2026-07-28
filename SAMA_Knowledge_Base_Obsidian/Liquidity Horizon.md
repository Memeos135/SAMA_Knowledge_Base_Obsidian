---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Backtesting"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Backtesting
  - graphify/enriched
---

# Liquidity Horizon

## Connections

### [[Expected Shortfall (ES)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's internal models approach (IMA) capital figure is computed correctly, treat the ES calculation and liquidity horizons as a single mandated computation, not separate topics. Article 13.4 requires the ES to be liquidity-adjusted by scaling a 10-day base-horizon result using the liquidity horizons prescribed in [13.12]/Table 2, so the assigned horizon per risk factor category directly drives the regulatory ES output. A compliance reviewer should therefore verify that each risk factor's liquidity horizon has been mapped to the correct category and applied in the ES scaling — an ES number produced without the prescribed horizon adjustment does not meet the SAMA minimum standard.
- **Grounding — this node (Page 123 / Table 2):** "Liquidity horizon n by risk factor ... Interest rate: specified currencies ... 10 ... Credit spread: volatility 120"
- **Grounding — related node (Page 118-119 / Art 13.1, 13.4):** "the liquidity horizons described in [13.12] must be reflected by scaling an ES calculated on a base horizon"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
