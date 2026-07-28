---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "IRB Retail & Corporate Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_Retail__Corporate_Exposures
  - graphify/enriched
---

# IRB Approach Overview

## Connections

### [[Advanced IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding which IRB variant a bank may use, treat the Advanced IRB approach as a subordinate option within the broader IRB Approach framework, not a separate regime. The IRB overview defines that under A-IRB banks 'provide their own estimates of PD, LGD and EAD, and their own calculation of M,' but the same chapter imposes overriding constraints — SAMA approval, phased rollout, the all-exposures-within-an-asset-class-in-a-unit rule, and outright A-IRB prohibitions (e.g. equities, large corporates above SAR 2,230m, bank/financial exposures). You should conclude that A-IRB eligibility is gated by the IRB Approach's scope limits and minimum requirements, so verify both before assuming a bank can use own estimates of LGD/EAD.
- **Grounding — this node (Page 102 / para 10.30 & 10.32):** "Minimum requirements: the minimum standards that must be met in order for a bank to use the IRB approach... the A-IRB approach cannot be used for the following"
- **Grounding — related node (Page 102 / para 10.31):** "Under the advanced approach (A-IRB approach), banks provide their own estimates of PD, LGD and EAD, and their own calculation of M, subject to meeting minimum standards"

### [[Eligible Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying purchased receivables for capital purposes, recognise that they are a distinct asset class within the IRB framework whose treatment straddles corporate and retail rules. The IRB overview lists corporate purchased receivables and retail purchased receivables as separate asset classes for the roll-out obligation, and specifies that eligible corporate receivables can use F-IRB or A-IRB (A-IRB only for obligors otherwise eligible), while retail receivables are A-IRB only. You would conclude that the available approach depends on both the receivable type and whether individual obligor default risk can be assessed, and should check paragraphs 10.25–10.29 and 14.6–14.7 before assuming the top-down treatment applies.
- **Grounding — this node (Page 105 / 10.43):** "the relevant assets classes are as follows... (5) Corporate purchased receivables... (9) Retail purchased receivables."
- **Grounding — related node (Page 105 / 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available... For eligible retail receivables... only the A-IRB approach is available."

### [[Foundation IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which risk parameters a bank may self-estimate for a given asset class, treat the Foundation IRB approach as one option nested inside the overall IRB framework rather than a standalone regime. The IRB overview establishes the three key elements (risk components, risk-weight functions, minimum requirements) and permits banks, subject to SAMA approval and a phased rollout, to move from foundation to advanced treatment; under F-IRB a bank supplies its own PD but relies on supervisory estimates for LGD and EAD. You would conclude that F-IRB eligibility and any migration to A-IRB is governed by the overview's rollout and approval conditions, so check the implementation plan and asset-class scope rules before assuming a bank can apply own estimates of LGD/EAD.
- **Grounding — this node (Page 106 / 10.45):** "move from the foundation approach to the advanced approach for certain risk components where use of the advanced approach is permitted."
- **Grounding — related node (Page 102 / 10.31):** "Under the foundation approach (F-IRB approach), as a general rule, banks provide their own estimates of PD and rely on supervisory estimates for other risk components."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may use the IRB approach, understand that its defining feature is reliance on internal estimates of the risk components (PD, LGD, EAD, M) subject to SAMA approval. The IRB overview identifies risk components as the first of the three key elements and states that approved banks may rely on their own internal estimates, while in some cases a supervisory value must be used. You would conclude that permission to self-estimate each component is not automatic — it depends on approach (F-IRB vs A-IRB) and the minimum requirements — so check which components carry supervisory values before relying on a bank's own estimates.
- **Grounding — this node (Page 91 / 10.1):** "banks that have received SAMA's approval to use the IRB approach may rely on their own internal estimates of risk components... probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)."
- **Grounding — related node (Page 91 / 10.1):** "In some cases, banks may be required to use a supervisory value as opposed to an internal estimate for one or more of the risk components."

### [[IRB Risk Weight Functions]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's IRB capital calculation for credit risk, treat the IRB approach chapter and the risk-weight functions chapter as one linked mechanism: the approach lets banks use internal risk-component estimates, but those estimates feed directly into the risk-weight functions that produce the actual capital requirement. The text ties them explicitly — the IRB approach is 'based on measures of unexpected losses (UL)' and 'the risk-weight functions, as outlined in chapter 11, produce capital requirements for the UL portion.' Conclude that IRB approval alone is not enough; a compliance reviewer must verify the correct risk-weight function is applied to each asset class before relying on the resulting capital figure.
- **Grounding — this node (Page 91 / Para 10.2):** "The IRB approach is based on measures of unexpected losses (UL) and expected losses. The risk-weight functions, as outlined in chapter 11, produce capital requirements for the UL po..."
- **Grounding — related node (Page 3 (TOC) / Chapter 11):** "11. IRB Approach: Risk Weight Functions ... Explanation of the risk-weight functions"

### [[Micro Small and Medium-Sized Entities (MSME)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying IRB risk-weight functions to corporate credits, do not treat MSME borrowers identically to large firms, because the framework mandates a distinct firm-size adjustment. The IRB overview covers the corporate asset class, and within it banks are permitted to separately distinguish MSME borrowers (consolidated group revenues below SAR 223 million) and apply the 0.04 x (1 – (S – 5)/45) adjustment to the corporate risk-weight formula. You would conclude that identifying MSME status is a required step in IRB corporate capital calculation, and should verify the revenue/total-assets thresholds and the failsafe substitution before deriving risk weights. Note the MSME threshold under IRB (SAR 223m) differs from the standardized-approach MSME definition (SAR 200m) and from the SAMA Circular referenced there.
- **Grounding — this node (Page 102 / 10.30):** "For each of the asset classes covered under the IRB framework, there are three key elements: Risk components... Risk-weight functions... Minimum requirements."
- **Grounding — related node (Page 111 / 11.8):** "Under the IRB approach for corporate credits, banks will be permitted to separately distinguish exposures to MSME borrowers... A firm-size adjustment... is made to the corporate risk weight formula."

### [[Qualifying Revolving Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When segmenting retail exposures under IRB, treat QRRE as a mandatory separately-identified sub-class, not a discretionary category. The IRB overview requires banks to identify three retail sub-classes, and the QRRE definition sets cumulative criteria (revolving, unsecured, uncommitted exposures with fluctuating balances) that must all be satisfied at sub-portfolio level. You would conclude that QRRE classification drives a distinct risk-weight treatment, so verify each defining criterion at the sub-portfolio level before assigning an exposure to the QRRE pool. Note the retail/QRRE definitions here differ from the standardized-approach 'regulatory retail' and 'transactor' concepts on pages 32–33.
- **Grounding — this node (Page 98 / 10.21):** "banks are required to identify separately three sub-classes of exposures... (2) Qualifying revolving retail exposures, as defined in the following paragraph."
- **Grounding — related node (Page 98 / 10.22):** "All of the following criteria must be satisfied for a sub-portfolio to be treated as a qualifying revolving retail exposure (QRRE)."

### [[Supervisory Slotting Criteria Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how a bank must capitalise specialized-lending (SL) exposures under IRB, note that the supervisory slotting approach is a distinct sub-track within the IRB framework, not the general internal-estimate route. Banks using slotting must assign exposures to internal grades and then map them into the five supervisory rating categories set out in chapter 13, rather than deriving their own PD/LGD. For a compliance decision, check whether the bank's SL portfolio is running on slotting (supervisory categories/tables) versus own estimates, because the qualification standards and mapping-integrity obligations differ.
- **Grounding — this node (Page 106 / Para 10.45):** "move from the foundation approach to the advanced approach for certain risk components where use of the advanced approach is permitted"
- **Grounding — related node (Page 185 / Para 16.27):** "Banks using the supervisory slotting criteria must assign exposures to their internal rating grades ... Banks must then map these internal rating grades into the five supervisory rating categories."

#graphify/document #graphify/EXTRACTED #community/IRB_Retail__Corporate_Exposures #graphify/enriched
