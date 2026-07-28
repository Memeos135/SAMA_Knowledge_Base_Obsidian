---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Leverage Ratio Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Leverage_Ratio_Exposures
  - graphify/enriched
---

# Derivative Exposures (Leverage Ratio)

## Connections

### [[CCR Stress Testing Program]] — `references` [AMBIGUOUS]
- **What this link tells you:** This link between the CCR stress-testing program and the leverage-ratio derivative-exposures rules appears thematic rather than a direct cross-reference, so treat it as a lead to verify. The stress-testing program requires complete trade capture and exposure aggregation 'across all forms of counterparty credit risk (not just OTC derivatives)', while the leverage-ratio derivatives section governs how replacement cost and derivative exposures enter the exposure measure—both bear on how derivative counterparty exposures are measured, but they serve different capital regimes (risk-based CCR versus the non-risk-based leverage ratio). Before relying on any interdependence, confirm in the primary text whether either provision actually references the other, since the connection here is inferred from shared subject matter (derivative counterparty exposure) rather than an explicit citation.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions... Where applicable, this amount should be net of cash variation margin"
- **Grounding — related node (Page 611 / 7.46(1)):** "Banks must ensure complete trade capture and exposure aggregation across all forms of counterparty credit risk (not just OTC derivatives)"
- **Caveat:** Relation is AMBIGUOUS; the two provisions address derivative exposures under different regimes (CCR stress testing vs leverage ratio) and no direct cross-reference is evident in the provided context.

### [[Cash Variation Margin Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the derivatives component of the leverage exposure measure, the cash variation margin treatment is a conditional offset you can only apply if the enumerated criteria (daily mark-to-market, unrestricted use of cash received, single MNA, full amount exchanged, specified currency) are met. Under SLEV7.2.4, qualifying cash VM received reduces the replacement cost (but not the PFE) of the derivative asset, and VM provided may be deducted from the exposure measure. Before netting VM against derivative exposures, confirm each condition is satisfied — otherwise the reduction is not permitted and the derivative exposure must be reported gross of that margin.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions ... net of cash variation margin"
- **Grounding — related node (Page 710 / 7.2.4):** "the cash portion of variation margin received may be used to reduce the replacement cost portion of the Leverage ratio exposure measure"

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **What this link tells you:** When building or reviewing the leverage ratio denominator, derivative exposures must be included in the exposure measure per the prescribed method: replacement cost plus a potential future exposure add-on, both reported with the 1.4 alpha factor and computed under SLEV7.2.2. The exposure measure template (rows 8-9) treats these derivative amounts as additive components of total exposures, subject to netting and cash variation margin rules. A reviewer should confirm the alpha factor has been applied and that netting/margin treatment follows SLEV7.2.2 and 7.2.4 before accepting the derivative contribution to the reported leverage exposure.
- **Grounding — this node (Page 874 / rows 8-9):** "Replacement cost (RC) associated with all derivatives transactions... Add-on amount for the potential future exposure (PFE)... 1.4 alpha factor applied as specified in SLEV7.2.2 (ii) and (v)"
- **Grounding — related node (Page 870 / Template LR1):** "To reconcile the total assets in the published financial statements with the leverage ratio exposure measure."

### [[Qualifying CCP (QCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the leverage-ratio exposure measure for a bank's derivative book, do not treat CCP-cleared derivatives as automatically low-exposure: the leverage ratio's derivative-exposure component captures replacement cost of all derivative transactions, including exposures where the bank guarantees clients' derivative trades to a CCP. The QCCP classification governs the risk-weighted (CCR) treatment, but SLEV computes exposure regardless of QCCP status, and a bank retains responsibility for adequate capital under Pillar 2 even where a CCP qualifies as a QCCP. Conclude that QCCP status reduces risk weights on trade exposures (e.g. 2%) but does not shrink the leverage-ratio exposure measure — the two regimes must be run in parallel, not substituted.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions (including exposures resulting from direct transactions between a client and a CCP where the bank guarantees the performance of its clients' derivative trade exposures to the CCP)."
- **Grounding — related node (Page 619, s.8.3):** "Regardless of whether a central counterparty (CCP) is classified as a qualifying CCP (QCCP), a bank retains the responsibility to ensure that it maintains adequate capital for its exposures."

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the leverage-ratio exposure measure for derivatives, replacement cost is a defined constituent input you must include, not a separate credit-risk-only concept. The leverage-ratio derivative treatment requires reporting the RC associated with all derivatives transactions (net of eligible cash variation margin, and including client-cleared CCP-guaranteed trades), drawing on the same RC construct defined in the SA-CCR sections (6.5–6.21). You would conclude that the RC figure feeding the leverage measure must be derived consistently with the SA-CCR replacement-cost formula rather than an ad hoc mark-to-market number.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions (including exposures resulting from direct transactions between a client and a CCP where the bank guarantees the performance of its clients' derivative trade exposures to the CCP)."
- **Grounding — related node (Page 568 / 6.2):** "RC = the replacement cost calculated according to 6.5 to 6.21"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the leverage ratio exposure measure for derivatives, recognize that the leverage framework relies on the same SA-CCR mechanics used for risk-based CCR capital, so the two are methodologically linked rather than independent. The leverage measure captures replacement cost associated with all derivatives transactions (net of eligible cash variation margin) consistent with SA-CCR replacement-cost and add-on logic. Conclude that a bank's derivative exposure inputs should be consistent between the risk-based CCR charge and the leverage exposure measure, and check that the SA-CCR components (RC plus add-ons) feed the leverage denominator per the SLEV rules.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions... this amount should be net of cash variation margin"
- **Grounding — related node (Page 819 / 20.2.3):** "Template CCR3 – Standardised approach – CCR exposures by regulatory portfolio and risk weights"
- **Caveat:** The leverage-ratio derivative treatment and SA-CCR are related through shared replacement-cost/add-on methodology; confirm the exact SLEV cross-reference to SA-CCR in the primary text before relying on the equivalence.

### [[Written Credit Derivatives Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring derivative exposures for the leverage ratio, written credit derivatives are a distinct sub-category where the bank effectively sells credit protection and must include the effective notional in its exposure — offsetting is only allowed under the strict conditions of paragraphs 7.2.9–7.2.13. The definition is broad (not limited to CDS/TRS) and offset against purchased protection requires same-or-more-conservative material terms, identical reference names, and matching seniority/maturity. In deciding whether to net a purchased credit derivative against a sold one, verify these pari passu, notional, and maturity conditions are met before recognising any reduction to the exposure figure.
- **Grounding — this node (Page 874):** "Replacement cost (RC) associated with all derivatives transactions"
- **Grounding — related node (Page 716 / 7.2.11):** "Written credit derivative refers to a broad range of credit derivatives through which a bank effectively provides credit protection and is not limited solely to credit default swaps"

#graphify/document #graphify/EXTRACTED #community/Leverage_Ratio_Exposures #graphify/enriched
