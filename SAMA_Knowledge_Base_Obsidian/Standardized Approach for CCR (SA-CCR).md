---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Standardized Approach for CCR (SA-CCR)

## Connections

### [[Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When computing potential future exposure under SA-CCR, the interest rate derivative add-on is a component within that method, not a standalone regime — so its maturity-bucket allocation and aggregation rules only bite once you are inside SA-CCR (i.e. no IMM approval for the relevant trades). The add-on for interest rate derivatives (6.59) feeds the netting-set aggregate add-on described in SA-CCR's PFE section, and note that supervisory correlation parameters do not apply to interest rate derivatives — a scope carve-out you must respect. Practical consequence: apply the IR add-on only within the SA-CCR EAD calculation and confirm you are using the correct maturity-bucket offsetting rather than importing the equity/credit/commodity correlation treatment.
- **Grounding — this node (Page 18 / 6.1):** "Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions must use SA-CCR, as set out in this chapter."
- **Grounding — related node (Page 37 / 6.59):** "The calculation of the add-on for the interest rate derivative asset class captures the risk of interest rate derivatives of different maturities being imperfectly correlated."

### [[Default Fund Contribution Capital (KCMiKCCP)|Default Fund Contribution Capital (KCMi/KCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping capital requirements for a clearing member bank's CCP exposures, treat default fund contributions as a distinct workstream governed by Chapter 8, not the SA-CCR chapter — the two are linked but sequential. SA-CCR (Chapter 6) computes counterparty credit risk EAD for OTC derivatives and long settlement transactions, while default fund contributions to a QCCP are capitalized via the separate risk-sensitive KCMi formula in Chapter 8 which itself draws on the hypothetical capital requirement KCCP. The practical consequence: verify you have applied Chapter 8's formulae (and the QCCP cap in 8.40) to fund contributions rather than defaulting to SA-CCR, and confirm you have the CCP-supplied inputs (KCCP, prefunded contributions) required under 8.37.
- **Grounding — this node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions."
- **Grounding — related node (Page 77 / 8.26-8.27):** "Clearing member banks will apply a risk weight to their default fund contributions determined according to a risk sensitive formula"

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining counterparty credit risk RWA, understand that EAD is the output SA-CCR produces and the input the credit-risk approaches consume — they are chained, not interchangeable. SA-CCR calculates EAD per netting set (EAD = alpha × (RC + PFE)), and that EAD is then risk-weighted under the standardized or IRB approach (5.12), unless the bank has SAMA approval for IMM as an alternative EAD method. Practical consequence: confirm which EAD method applies (SA-CCR by default, IMM only with SAMA approval) before applying risk weights, and check the exemptions in 5.15 where EAD is zero for certain hedged/guarantee transactions.
- **Grounding — this node (Page 19 / 6.2):** "EAD is to be calculated separately for each netting set"
- **Grounding — related node (Page 16 / 5.10):** "the exposure amount or EAD for a given counterparty is equal to the sum of the exposure amounts"

### [[Exposures to Central Counterparties (CCPs)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating exposures to central counterparties, do not assume the ordinary bilateral SA-CCR netting rules apply unchanged — Chapter 8 recognises that CCP netting arrangements are less standardized and makes specific adjustments. Net replacement cost for CCP trade exposures may be used only where close-out netting meets the requirements cross-referenced in 8.10, which expressly incorporate SA-CCR provisions 6.9–6.10 for derivative transactions. Conclude that CCP exposure treatment borrows SA-CCR's netting-eligibility tests as a precondition, so those SA-CCR clauses must be satisfied before netting benefit is claimed against CCP exposures.
- **Grounding — this node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions."
- **Grounding — related node (Page 72 / 8.10(2)):** "the total replacement cost of all contracts relevant to the trade exposure determination can be calculated as a net replacement cost if the applicable close-out netting sets meet the requirements set out in: ...6.9 and 6.10 of the SA-CCR"

### [[Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the default CCR measurement method, treat SA-CCR as the mandatory fallback: this framework requires banks without IMM approval to use SA-CCR for OTC derivatives, exchange-traded derivatives and long settlement transactions. The framework also links the CVA regime to SA-CCR outputs — the IRB maturity-adjustment cap at 1 applies per netting set for which BA-CVA/SA-CVA capital is calculated. Conclude that unless a bank holds IMM approval, SA-CCR governs its derivative EAD, and CVA-related maturity caps must be applied consistently across the CCR and CVA calculations.
- **Grounding — this node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives... Banks that do not have approval to apply the internal model method (IMM)... must use SA-CCR"
- **Grounding — related node (Page 89 / 11.12):** "Banks that use the BA-CVA or the SA-CVA for calculating CVA capital requirements may cap the maturity adjustment factor at 1 for all netting sets"

### [[Qualifying CCP (QCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalizing CCP-cleared derivatives, whether a counterparty is a QCCP determines the capital track — but SA-CCR still supplies the underlying EAD before preferential QCCP treatment applies. QCCP status triggers the favorable 2% trade-exposure risk weight and Chapter 8 default-fund treatment, while a non-qualifying CCP attracts the standardized approach for trade exposure and a 1250% weight on fund contributions (8.41-8.42); the QCCP definition (4.2) also conditions on the CCP meeting 8.37's data-sharing requirements. Practical consequence: verify QCCP status (including SAMA's determination where no compliant CCP regulator exists) and note the three-month grace window when a CCP loses QCCP status, then confirm SA-CCR EAD is computed as the basis before applying the QCCP risk weights.
- **Grounding — this node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions."
- **Grounding — related node (Page 70 / 8.3):** "Regardless of whether a central counterparty (CCP) is classified as a qualifying CCP (QCCP), a bank retains the responsibility to ensure that it maintains adequate capital for its exposures."

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating SA-CCR EAD, replacement cost is one of its two defining inputs (EAD = alpha × (RC + PFE)) and must be computed differently for margined versus unmargined netting sets. For margined trades RC uses the formula RC = max{V − C; TH + MTA − NICA; 0} (6.20), where the third zero term prevents a negative RC and margin agreement terms (threshold, MTA, NICA) directly reduce or increase the figure. Practical consequence: confirm you have correctly classified each netting set as margined or unmargined — a one-way agreement where only the bank posts VM is treated as unmargined — and that collateral and independent amounts are fed into the correct RC term rather than double-counted.
- **Grounding — this node (Page 19 / 6.2-6.4):** "The replacement cost (RC) and the potential future exposure (PFE) components are calculated differently for margined and unmargined netting sets."
- **Grounding — related node (Page 142 / 13.1):** "they relate to the formulation of replacement cost for margined trades, as set out in 6.20: RC = max{V − C; RH + MTA − MHXA; 0}"

### [[SA-CCR Sample Portfolio Examples]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank has correctly computed EAD under SA-CCR, treat the sample portfolio section as the authoritative worked illustration of the same rules, not as a separate standard. Both sit within the one CCR framework: the SA-CCR chapter (6.1) sets the binding methodology for OTC, exchange-traded and long settlement transactions, and Section 12 explicitly applies that method to five sample portfolios using the EAD formula with alpha=1.4. For a compliance review you would use the examples to test the bank's calculation logic against SAMA's intended application, but the enforceable obligation remains the SA-CCR chapter itself.
- **Grounding — this node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions."
- **Grounding — related node (Page 123 / 12.1):** "This section sets out the calculation of exposure at default (EAD) for five sample portfolios using SA-CCR."

#graphify/document #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
