---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "IRB Credit Risk Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# IRB Risk Components (PD, LGD, EAD, M)

## Connections

### [[Credit Risk Mitigation Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing how a bank may capitalize purchased receivables covered by a seller or third-party guarantee, don't treat credit risk mitigation as a standalone adjustment: paragraphs 14.11-14.12 route mitigant recognition back through the IRB risk-component machinery (PD, LGD, EAD, M), substituting the guarantor's risk weight for the pool's default and/or dilution risk weight. The link tells you that whether a guarantee is recognized, and how, depends on which risk component it covers and on the underlying IRB estimates (e.g. exposure-weighted LGD under SEC-IRBA). Conclude that CRM eligibility cannot be evaluated without confirming the bank's IRB approval and the relevant risk-component treatment; partial-cover guarantees leave the uncovered component capitalized under ordinary CRM rules.
- **Grounding — this node (Page 91 / 10.1):** "The risk components include measures of the probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)"
- **Grounding — related node (Page 173 / 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"

### [[IRB Approach Overview]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may use the IRB approach, understand that its defining feature is reliance on internal estimates of the risk components (PD, LGD, EAD, M) subject to SAMA approval. The IRB overview identifies risk components as the first of the three key elements and states that approved banks may rely on their own internal estimates, while in some cases a supervisory value must be used. You would conclude that permission to self-estimate each component is not automatic — it depends on approach (F-IRB vs A-IRB) and the minimum requirements — so check which components carry supervisory values before relying on a bank's own estimates.
- **Grounding — this node (Page 91 / 10.1):** "In some cases, banks may be required to use a supervisory value as opposed to an internal estimate for one or more of the risk components."
- **Grounding — related node (Page 91 / 10.1):** "banks that have received SAMA's approval to use the IRB approach may rely on their own internal estimates of risk components... probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)."

### [[IRB Risk Weight Functions]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing an IRB capital output, understand that the risk components (PD, LGD, EAD, M) are the inputs and the risk-weight functions are the formula that converts them into risk-weighted assets — the two chapters are operationally inseparable. The text states banks 'may rely on their own internal estimates of risk components in determining the capital requirement,' and those measures of PD, LGD, EAD and M are what the chapter 11 functions consume. Conclude that validating a capital figure requires checking both the integrity of the component estimates and their correct feed into the applicable risk-weight function; a defect in either invalidates the result.
- **Grounding — this node (Page 91 / Para 10.1):** "The risk components include measures of the probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)."
- **Grounding — related node (Page 3 (TOC) / Chapter 11):** "11. IRB Approach: Risk Weight Functions ... Risk-weighted assets for corporate, sovereign and bank exposures that are not in default"

### [[Supervisory Haircuts]] — `references` [EXTRACTED]
- **What this link tells you:** When computing EAD under the IRB approach for collateralised or SFT exposures, do not treat the IRB risk components (PD, LGD, EAD, M) as fully bank-estimated in isolation: the EAD input for such exposures is derived using the standardized-approach collateral machinery, including supervisory haircuts. Chapter 12 provides that for SFTs banks calculate E* (the exposure used for EAD) applying the standard-haircut / netting rules of the standardized approach unless a VaR-models alternative is approved. You should conclude that even an A-IRB bank's own EAD estimate for collateralised transactions incorporates the supervisory haircut framework, so the two chapters must be read together when validating EAD figures.
- **Grounding — this node (Page 91 / para 10.1):** "The risk components include measures of the probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)"
- **Grounding — related node (Page 128 / para 12.38-12.39):** "As an alternative to the use of standard haircuts for the calculation of the counterparty credit risk requirement for SFTs... banks may be permitted to use a value-at-risk (VaR) models approach"

#graphify/concept #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
