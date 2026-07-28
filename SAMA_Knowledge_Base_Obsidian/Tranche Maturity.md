---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Securitization Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Tranche Maturity

## Connections

### [[Resecuritization Exposure]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting a resecuritization exposure, note that tranche maturity is a required input to the risk-weight formulas even though resecuritizations attract more conservative treatment, so the maturity parameter (floored at one year, capped at five) still feeds the calculation. The framework captures the material effects of differing tranche maturities through maturity adjustments on securitization risk weights, and resecuritizations are a defined subset of securitization exposures. Conclude that you must still determine effective tranche maturity per 18.22–18.23 when applying the SEC-SA to a resecuritization, and verify how the resecuritization-specific adjustments in 19.16 modify that base treatment.
- **Grounding — this node (SAMA_EN_3502 Page 236 / 18.22):** "tranche maturity (𝑀𝑇) is the tranche’s remaining effective maturity in years... will have a floor of one year and a cap of five years"
- **Grounding — related node (SAMA_EN_3487 Page 238 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure"
- **Caveat:** Nodes are drawn from two document versions (3487 and 3502); confirm the tranche-maturity definition applies unchanged to the resecuritization treatment in the version you are relying on.

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
