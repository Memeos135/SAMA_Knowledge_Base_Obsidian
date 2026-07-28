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

# Foreign Exchange (FX) Risk

## Connections

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping FX risk capital under the SAMA market-risk framework, FX risk is one of the defined risk classes measured through the sensitivities-based method's delta, vega and curvature measures, not a separate arithmetic add-on (that simpler treatment belongs to the simplified standardised approach). Because the SbM aggregates risk-weighted sensitivities across all risk classes using specified correlation parameters, FX exposures interact with the same computation. Conclude that under the full standardised approach FX positions are captured via SbM risk factors; verify whether the bank uses the SbM or the simplified standardised approach before selecting the FX treatment.
- **Grounding — this node (Page 490):** "interest rate risk, equity risk, FX risk and commodity risk ... summed arithmetically."
- **Grounding — related node (Page 383):** "a bank must calculate three sensitivities-based method capital requirement values, based on three different scenarios on the specified values for the correlation parameters."

### [[Simplified Standardised Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping FX-risk capital for a bank eligible for the simplified standardised approach, treat FX risk as one of the four prescribed risk classes that feed the aggregate charge rather than as a separate regime. Para 14.2(3) sets the FX component (CRFX) under [14.53] to [14.62] plus option add-ons, and para 14.1 requires the four class charges to be summed arithmetically to derive the total. You should conclude that the FX-risk calculation cannot be omitted or netted against other classes under this approach and must be included in the arithmetic total before deriving RWA (charge × 12.5).
- **Grounding — this node (Page 490 / para 14.2(3)):** "𝐶𝑅FX = capital requirement under [14.53] to [14.62] (FX risk), plus additional requirements for option risks from foreign exchange instruments"
- **Grounding — related node (Page 490 / para 14.1):** "[14.3] to [14.73] deal with interest rate, equity, foreign exchange (FX) and commodities risk."

### [[Simplified Standardised Approach]] — `references` [EXTRACTED]
- **What this link tells you:** This link shows FX risk as a component of the simplified standardised approach across two related SAMA market-risk documents; before relying on it, confirm that the simplified approach is available to the bank at all, because eligibility is gated. SAMA (3553, para 3.9) permits the simplified alternative only for smaller/simpler trading books subject to SAMA approval, excluding G-SIBs/D-SIBs, IMA users and correlation-trading positions, and SAMA may still mandate the full standardised approach. For a bank considering measuring FX risk this way, first verify SAMA approval and the indicative eligibility criteria; the FX-risk module (as detailed in 3487 [14.53]–[14.62]) only applies if the simplified approach is authorised.
- **Grounding — this node (SAMA_EN_3487_VER1 Page 162 / para 14.75):** "added to the capital requirements for the relevant category, ie interest rate related instruments, equities, FX and commodities as described in [14.3] to [14.73]"
- **Grounding — related node (SAMA_EN_3553_VER1 Page 11 / para 3.9):** "SAMA may allow banks that maintain smaller or simpler trading books to use the simplified alternative to the standardised approach as set out in [14]. The use of the simplified alternative is subject to SAMA approval"
- **Caveat:** The two documents appear to be parallel/versioned market-risk frameworks; confirm which version applies to the bank and that eligibility conditions in 3553 para 3.9 are met before relying on the simplified FX treatment.

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
