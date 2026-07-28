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

# Probability of Default (PD)

## Connections

### [[Definition of Default]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When assessing a bank's IRB capital reporting, read the definition of default and the PD parameter as tightly coupled: the reliability of PD is validated against realised default rates, so an inconsistent default definition undermines PD backtesting. Template CR9 explicitly compares the PD used in IRB capital calculations with effective default rates of obligors, and the CR2/CR1 default definition (e.g. past due more than 90 days for the standardised approach) sets what counts as a default event. This appears to link the two, but the connection is inferred rather than a stated cross-reference — confirm the bank's internal default definition (paras 16.67–16.75) aligns with the reference definition before relying on PD validation results.
- **Grounding — this node (Page 816 / Template CR9):** "the template compares the PD used in IRB capital calculations with the effective default rates of bank obligors."
- **Grounding — related node (Page 798 / Table CR2):** "the default exposures in Templates CR1 and CR2 should correspond to exposures that are "past due for more than 90 days", as stated in SCRE7.96."
- **Caveat:** Relation is INFERRED — the documents share the default concept but no explicit cross-reference is quoted; verify the reference default definition (16.67–16.75) and PD calibration text before relying on the link.

### [[Expected Loss and Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** Do not conflate operational-risk 'expected loss/provisions' with the credit-risk PD parameter when scoping which capital rules apply to a portfolio: the loss-data material here concerns operational-risk capital, whereas PD is a credit-risk IRB input. Both are computed under the same SAMA capital rulebook but through separate calculation streams, and the source itself excludes credit-risk-driven operational events accounted for in credit RWAs from the operational loss set. Conclude that provisioning/loss figures for operational risk should not be used as, or mixed with, PD-based credit capital inputs; check which risk category and template a figure belongs to before relying on it.
- **Grounding — this node (Page 816 / Template CR9):** "the model that is used to assign a risk rating to an obligor, and/or the model that calibrates the internal ratings to the PD scale."
- **Grounding — related node (Page 540):** "Operational loss events related to credit risk and that are accounted for in credit risk RWAs should not be included in the loss data set."
- **Caveat:** The 'references' relation is weak — the two nodes address different risk regimes (operational vs credit) within the same rulebook; treat as a co-location lead, not a direct dependency.

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing IRB capital calculations, treat PD not as a standalone metric but as one of the defined risk components (alongside LGD, EAD and M) that feed the risk-weight functions. The corpus defines PD as a modelling parameter used in IRB capital calculations and subject to backtesting against effective default rates, so it is a subordinate input within the broader IRB risk-component framework. A reader validating capital adequacy should therefore check PD estimation and its five-year backtesting evidence as part of the integrated risk-component set, not in isolation.
- **Grounding — this node (Page 816):** "compares the PD used in IRB capital calculations with the effective default rates of bank obligors. A minimum five-year average annual default rate is required"
- **Grounding — related node (Page 361 / risk components):** "Modelling parameters used in IRB calculation"

### [[Rating System Design]] — `references` [EXTRACTED]
- **What this link tells you:** If you are evaluating an IRB bank's compliance, treat rating system design as the governing framework that produces PD, not a separate topic: PD is one of the estimates the rating system must generate and document. The rating-system section defines the 'rating system' as the methods, processes and controls supporting the quantification of default and loss estimates, with a borrower-default dimension, and requires documentation of the specific default definition consistent with the reference definitions. Conclude that a bank's PD estimates are only valid to the extent its rating system meets the Section 3 minimum requirements; check rating-system documentation and the borrower-grade dimension before accepting PD outputs.
- **Grounding — this node (Page 816 / Template CR9):** "the model that is used to assign a risk rating to an obligor, and/or the model that calibrates the internal ratings to the PD scale."
- **Grounding — related node (Page 187 / 16.9):** "the assessment of credit risk, the assignment of internal risk ratings, and the quantification of default and loss estimates."

#graphify/concept #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
