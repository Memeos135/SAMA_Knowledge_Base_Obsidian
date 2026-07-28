---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "CCR & CVA Capital Requirements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCR__CVA_Capital_Requirements
  - graphify/enriched
---

# Standardized Approach for CVA (SA-CVA)

## Connections

### [[Credit Valuation Adjustment (CVA) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which CVA capital methodology a bank may lawfully use, treat SA-CVA as a permission-gated option under the overarching CVA Framework, not a free choice. Chapter 11 of the Framework establishes the CVA regime and expressly makes BA-CVA the default, allowing SA-CVA only where SAMA has approved its use. A compliance reviewer should therefore verify that any SA-CVA reliance is backed by an actual SAMA approval and note that approval may be partial (limited to certain transactions within a netting set).
- **Grounding — this node (Page 87 / Art 11.7):** "Banks must use the BA-CVA unless they receive approval from Saudi Central Bank (SAMA) to use the SA-CVA."
- **Grounding — related node (Page 87 / Art 11.7):** "Two approaches are available for calculating CVA capital: the standardized approach (SA-CVA) and the basic approach (BA-CVA)."

### [[Eligible CVA Hedges]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing hedge offsets claimed by a bank on SA-CVA, note that eligibility of CVA hedges under SA-CVA is governed by a distinct set of criteria (11.37–11.39) from those applying to BA-CVA (11.17–11.19). Art 11.10 assigns separate eligibility rules per approach, so a hedge recognized under one approach is not automatically recognized under the other. A reviewer should confirm the bank applied the SA-CVA-specific eligibility conditions before treating hedges as reducing the SA-CVA capital charge.
- **Grounding — this node (Page 87 / Art 11.7):** "the standardized approach (SA-CVA) ... Banks must use the BA-CVA unless they receive approval ... to use the SA-CVA."
- **Grounding — related node (Page 89 / Art 11.10):** "Eligibility criteria for CVA hedges are specified in 11.17 to 11.19 for the BA-CVA and in 11.37 to 11.39 for the SA-CVA."

### [[Regulatory CVA Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which CVA capital methodology a bank must apply, treat 'regulatory CVA' as the required input measure that feeds the SA-CVA, not as an interchangeable concept. The framework defines regulatory CVA (excluding the bank's own default, with best-practice accounting constraints) and then states the SA-CVA uses as inputs the sensitivities of that regulatory CVA to credit spreads and market risk factors; SA-CVA use is conditional on SAMA approval, otherwise BA-CVA applies. A reader should conclude that eligibility for SA-CVA depends on being able to compute regulatory CVA and its sensitivities per Chapter 11, and should not assume SA-CVA can be used without both SAMA approval and a compliant regulatory CVA calculation.
- **Grounding — this node (Page 97 / 11.29):** "The SA-CVA uses as inputs the sensitivities of regulatory CVA to counterparty credit spreads and market risk factors driving the values of covered transactions."
- **Grounding — related node (Page 87 / 11.31-11.32):** "A bank must calculate regulatory CVA for each counterparty with which it has at least one covered position for the purpose of the CVA risk capital requirements."

### [[SA-CVA Delta and Vega Sensitivities]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping what a bank must be able to compute before it can use SA-CVA, note that the delta and vega sensitivities are the operative measurement inputs the approach depends on, not an optional add-on. The framework states the SA-CVA uses sensitivities of regulatory CVA as inputs, and eligibility requires the bank to calculate CVA and CVA sensitivities at least monthly; the sensitivity provisions (11.46-11.53) then specify that vega sensitivities are always material and must be calculated regardless of whether the portfolio contains options. A reader should conclude that a bank cannot qualify for or apply SA-CVA without producing both delta and vega sensitivities per these paragraphs, and vega cannot be omitted on the grounds of no options exposure.
- **Grounding — this node (Page 87 / 11.30(1)):** "A bank must be able to model exposure and calculate, on at least a monthly basis, CVA and CVA sensitivities to the market risk factors specified..."
- **Grounding — related node (Page 104 / 11.48):** "CVA sensitivities for vega risk are always material and must be calculated regardless of whether or not the portfolio includes options."

### [[Saudi Central Bank (SAMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether a bank may use SA-CVA rather than the default BA-CVA, treat SAMA as the gatekeeper: use of SA-CVA is not a bank election but requires prior SAMA approval, which may also be limited in scope. The framework provides that banks must use BA-CVA unless they receive SAMA approval for SA-CVA, and separately allows SAMA to determine materiality and to grant partial approvals covering only some transactions in a netting set. A reader should conclude that any reliance on SA-CVA must be backed by documented SAMA approval and should verify the exact scope of that approval before applying SA-CVA across a portfolio.
- **Grounding — this node (Page 87 / 11.7):** "Banks must use the BA-CVA unless they receive approval from Saudi Central Bank (SAMA) to use the SA-CVA."
- **Grounding — related node (Page 88 / 11.8):** "SAMA approval to use the SA-CVA is limited and does not cover all transactions within a legal netting set."

### [[Template CVA3 Standardised Approach SA-CVA|Template CVA3: Standardised Approach SA-CVA]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When assessing SA-CVA disclosure obligations, read Template CVA3 as the reporting face of the SA-CVA capital regime whose eligibility is conditional: the substantive rule (para 11.7) permits SA-CVA only where SAMA has granted approval, otherwise BA-CVA is the default. CVA3 therefore does not become applicable simply because a bank wishes to report under SA-CVA — it presupposes the underlying SAMA approval documented in SAMA_EN_4283. The link appears sound but is inferred from the shared CVA framework rather than an explicit named cross-reference. Conclude that before scoping CVA3 you must confirm SAMA approval status and note that split netting-set treatment (partial SA-CVA approval) affects which template captures which exposures.
- **Grounding — this node (Page 88 / para 11.8):** "SAMA approval to use the SA-CVA is limited and does not cover all transactions within a legal netting set."
- **Grounding — related node (Page 113 / 23.2.3):** "Template CVA3 - The standardised approach for CVA (SA-CVA)"
- **Caveat:** Relation is INFERRED from a shared CVA framework; confirm the approval-conditional link in the primary SCCR11 text before relying on CVA3 scope.

#graphify/concept #graphify/EXTRACTED #community/CCR__CVA_Capital_Requirements #graphify/enriched
