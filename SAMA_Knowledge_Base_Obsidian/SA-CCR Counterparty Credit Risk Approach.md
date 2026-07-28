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

# SA-CCR Counterparty Credit Risk Approach

## Connections

### [[Collateralized Transactions]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating exposure for OTC derivatives, exchange-traded derivatives, long settlement transactions and SFTs, don't apply the collateralized-transaction/haircut rules in isolation: paragraphs 12.37-12.39 direct that EAD for counterparty-credit-risk exposures be computed under the CCR framework, and offer a VaR-models alternative to standard haircuts for SFTs. The link tells you the collateralized-transaction maturity and haircut treatment feeds into, but is subordinate to, the counterparty-credit-risk EAD rules and their master-netting and daily-revaluation conditions. Conclude that you must confirm which transactions trigger counterparty credit risk and apply CCR-framework EAD (or approved VaR models) rather than treating collateral haircuts as the endpoint.
- **Grounding — this node (Page 127 / 12.37):** "For exposures that give rise to counterparty credit risk ... the EAD is to be calculated under the rules set in chapters 3 to 8 of the Counterparty Credit Risk (CCR) framework"
- **Grounding — related node (Page 131 / 12.51):** "fully or nearly-fully collateralized capital market-driven transactions ... and repo-style transactions ... where the documentation contains daily remargining clauses"

### [[Counterparty Credit Risk (CCR) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating exposure amounts for derivatives, long settlement transactions and SFTs, treat SA-CCR as the default computation method sitting inside the broader CCR Framework rather than as a stand-alone rule. The credit risk chapters direct that exposures giving rise to counterparty credit risk 'is to be calculated under the rules set out in chapters 3 to 8 in The Counterparty Credit Risk (CCR) Framework,' and SA-CCR uses RC and PFE defined in those CCR chapters (paras 6.5–6.76). You should conclude that SA-CCR inputs and any internal-models alternative are governed by the CCR Framework, so you must cross-check the CCR Framework text before relying on any SA-CCR figure.
- **Grounding — this node (Page 82 / para 9.65-9.66):** "Under the standardized approach for Counterparty Credit Risk Framework (SA-CCR)... RC = the replacement cost... PFE = the amount for potential future exposure calculated according to paragraphs 6.23 to 6.76 in the CCR framework"
- **Grounding — related node (Page 48 / para 7.94):** "For exposures that give rise to counterparty credit risk... the exposure amount... is to be calculated under the rules set out in chapters 3 to 8 in The Counterparty Credit Risk (CCR) Framework"

### [[Equity Investment in Funds LTA Example]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the look-through approach to a bank's equity investment in a fund that holds derivatives, note that counterparty credit risk on the fund's derivative exposures is captured via the CCR/SA-CCR machinery, with a specific overlay: the CCR exposure must be multiplied by 1.5 before applying the counterparty risk weight in lieu of a CVA charge. This links the funds chapter (Ch. 24) to the SA-CCR/CCR exposure calculation used generally for derivatives. You should conclude that fund look-through capital cannot ignore embedded derivative counterparty exposure and must fold in the 1.5 multiplier where the CVA charge is not separately determined.
- **Grounding — this node (Page 82 / para 9.65):** "Under the standardized approach for Counterparty Credit Risk Framework (SA-CCR), the calculation of the counterparty credit risk charge for an individual contract will be calculated using the following formula"
- **Grounding — related node (Page 328 / para 24.x (funds)):** "Instead of determining a CVA charge... banks must multiply the CCR exposure by a factor of 1.5 before applying the risk weight associated with the counterparty"

#graphify/concept #graphify/EXTRACTED #community/CCR_Collateral__Mitigation #graphify/enriched
