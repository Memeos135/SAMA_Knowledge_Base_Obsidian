---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "CCR Collateral & Mitigation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCR_Collateral__Mitigation
  - graphify/enriched
---

# Supervisory Haircuts

## Connections

### [[Comprehensive Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how much collateral relief a bank may claim under the credit risk mitigation rules, treat the comprehensive approach and supervisory haircuts as a single mechanism: the comprehensive approach mandates adjusting exposure and collateral values, and supervisory haircuts are the prescribed factors used to do so. Chapter 9 states banks 'must use the applicable supervisory haircuts to adjust both the amount of the exposure to the counterparty and the value of any collateral,' with haircut size driven by holding period, instrument type, maturity and remargining frequency. You should conclude that any RWA reduction from eligible collateral must be net of these haircuts (volatility-adjusted), and cannot be based on nominal collateral values.
- **Grounding — this node (Page 71 / para 9.41-9.42):** "The size of the haircuts that banks must use depends on the prescribed holding period... type of instrument, type of transaction, residual maturity and the frequency of marking to market and remargining"
- **Grounding — related node (Page 71 / para 9.40):** "In the comprehensive approach... banks must use the applicable supervisory haircuts to adjust both the amount of the exposure to the counterparty and the value of any collateral received"

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing EAD under the IRB approach for collateralised or SFT exposures, do not treat the IRB risk components (PD, LGD, EAD, M) as fully bank-estimated in isolation: the EAD input for such exposures is derived using the standardized-approach collateral machinery, including supervisory haircuts. Chapter 12 provides that for SFTs banks calculate E* (the exposure used for EAD) applying the standard-haircut / netting rules of the standardized approach unless a VaR-models alternative is approved. You should conclude that even an A-IRB bank's own EAD estimate for collateralised transactions incorporates the supervisory haircut framework, so the two chapters must be read together when validating EAD figures.
- **Grounding — this node (Page 128 / para 12.38-12.39):** "As an alternative to the use of standard haircuts for the calculation of the counterparty credit risk requirement for SFTs... banks may be permitted to use a value-at-risk (VaR) models approach"
- **Grounding — related node (Page 91 / para 10.1):** "The risk components include measures of the probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)"

#graphify/concept #graphify/EXTRACTED #community/CCR_Collateral__Mitigation #graphify/enriched
