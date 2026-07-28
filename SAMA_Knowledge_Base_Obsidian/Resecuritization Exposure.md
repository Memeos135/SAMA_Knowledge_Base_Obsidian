---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Securitization Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Resecuritization Exposure

## Connections

### [[SEC-SA (Standardized Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge on a resecuritization exposure, apply the SEC-SA — the standard directs banks to use the SEC-SA methodology (19.1–19.15) for resecuritizations, with specified modifications. This means resecuritizations do not get an independent method; they inherit the standardized approach's formula and its floor risk weight, adjusted upward. Conclude that you should compute the resecuritization risk weight through SEC-SA as modified by 19.16 (rather than an external-ratings or IRB path), and check the specific adjustments that raise the charge relative to a plain securitization.
- **Grounding — this node (Page 238 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure"
- **Grounding — related node (Page 304 / 19.16):** "For resecuritization exposures, banks must apply the SEC-SA specified in 19.1 to 19.15, with the fo[llowing adjustments]"

### [[Securitization General Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for a resecuritization position, do not treat it as a self-contained regime: 18.5 defines a resecuritization exposure as a species of securitization exposure whose underlying pool contains at least one securitization exposure, so the general securitization framework's scope and definitions govern it. Under 19.16 the resecuritization RWA is calculated by applying the standard SEC-SA rules with specific adjustments (delinquencies set to zero, supervisory parameter p set to 1.5), and the underlying securitization exposures' capital is itself computed using the securitization framework. For a capital decision you would first classify the position under the framework's definitions, then apply the modified SEC-SA parameters rather than ordinary securitization parameters.
- **Grounding — this node (Page 238 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure."
- **Grounding — related node (Page 237 / 18.1):** "Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizations"

### [[Securitization General Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the regulatory capital treatment of a resecuritization exposure, you cannot treat it in isolation: SAMA's rules define it as a securitization exposure whose underlying pool itself contains at least one securitization exposure, so it is a subset of the general securitization framework. The general provisions (18.4–18.6) supply the definitions of securitization exposure and originator that anchor the resecuritization concept, and the SEC-SA adjustments (19.16) explicitly require the underlying securitization exposures' capital to be computed using the securitization framework. Conclude that resecuritization capital calculations must be read against the general securitization provisions — check both the resecuritization-specific parameters (e.g. p=1.5, W set to zero) and the base framework definitions before applying a risk weight.
- **Grounding — this node (Page 297 / 19.16):** "For resecuritization exposures, banks must apply the SEC-SA specified in 19.1 to 19.15, with the following adjustments"
- **Grounding — related node (Page 231 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure."

### [[Tranche Maturity]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting a resecuritization exposure, note that tranche maturity is a required input to the risk-weight formulas even though resecuritizations attract more conservative treatment, so the maturity parameter (floored at one year, capped at five) still feeds the calculation. The framework captures the material effects of differing tranche maturities through maturity adjustments on securitization risk weights, and resecuritizations are a defined subset of securitization exposures. Conclude that you must still determine effective tranche maturity per 18.22–18.23 when applying the SEC-SA to a resecuritization, and verify how the resecuritization-specific adjustments in 19.16 modify that base treatment.
- **Grounding — this node (SAMA_EN_3487 Page 238 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure"
- **Grounding — related node (SAMA_EN_3502 Page 236 / 18.22):** "tranche maturity (𝑀𝑇) is the tranche’s remaining effective maturity in years... will have a floor of one year and a cap of five years"
- **Caveat:** Nodes are drawn from two document versions (3487 and 3502); confirm the tranche-maturity definition applies unchanged to the resecuritization treatment in the version you are relying on.

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
