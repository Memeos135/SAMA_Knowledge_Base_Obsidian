---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "CCR & CVA Disclosure Templates"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCR__CVA_Disclosure_Templates
  - graphify/enriched
---

# SCCR Counterparty Credit Risk Framework

## Connections

### [[Template CCR1 Analysis of CCR exposures by approach|Template CCR1: Analysis of CCR exposures by approach]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping a bank's Pillar 3 CCR disclosure obligations, treat Template CCR1 as the reporting vehicle for the substantive capital rules in the SCCR framework rather than a standalone requirement. The disclosure section expressly lists CCR1 among the mandatory CCR templates and points to 'SCCR3 to SCCR9 and SCCR11' as the underlying Basel-based rules, so the exposures and RWA shown in CCR1 must be computed under those SCCR chapters. A compliance reviewer should therefore reconcile CCR1 figures against the SCCR calculation methodology, not merely check that the template is filed.
- **Grounding — this node (Page 751):** "Counterparty credit risk: RWA and capital charges according to the counterparty credit risk chapters of the Basel framework (SCCR3 to SCCR10)."
- **Grounding — related node (Page 819):** "20.2.2 Template CCR1 – Analysis of CCR exposures by approach ... The relevant sections of the Basel framework are in SCCR3 to SCCR9 and SCCR11."

### [[Template CCR4 IRB CCR exposures by portfolio and PD scale|Template CCR4: IRB CCR exposures by portfolio and PD scale]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying a bank's IRB-based CCR disclosures, treat Template CCR4 as reporting output governed by the SCCR framework: it applies only where the bank uses A-IRB or F-IRB to compute RWA for exposures 'subject to the counterparty credit risk framework.' The disclosure list ties CCR4 to the same SCCR3–SCCR9/SCCR11 basis, and CCR4 explicitly excludes CVA charges and CCP-cleared exposures (reported elsewhere). A reviewer should check that CCR4's PD-scale breakdown covers only IRB CCR exposures and that scope exclusions align with the SCCR rules, rather than assuming the template captures all CCR.
- **Grounding — this node (Page 751):** "Counterparty credit risk: RWA and capital charges according to the counterparty credit risk chapters of the Basel framework (SCCR3 to SCCR10)."
- **Grounding — related node (Page 823):** "RWA and parameters used in RWA calculations for exposures subject to the counterparty credit risk framework (excluding CVA charges or exposures cleared through a CCP)"

### [[Template CCR5 Composition of collateral for CCR exposures|Template CCR5: Composition of collateral for CCR exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing collateral disclosure for CCR, treat CCR5 as reporting the credit-risk-mitigation inputs to the SCCR capital calculation rather than a general collateral inventory. It is listed among the mandatory CCR templates tied to SCCR3–SCCR9/SCCR11, so the collateral it reports is that recognised in computing the counterparty credit risk charge for the transaction types (OTC/exchange-traded derivatives, long settlement, securities financing) captured by the SCCR scope. A reviewer should confirm the collateral figures are consistent with the exposure/EAD basis used elsewhere in the CCR framework.
- **Grounding — this node (Page 563):** "Banks must calculate a counterparty credit risk charge for all exposures that give rise to counterparty credit risk, with the exception of those transactions listed in 5.15"
- **Grounding — related node (Page 819):** "20.2.5 Template CCR5 – Composition of collateral for CCR exposures"

### [[Template CCR8 Exposures to central counterparties|Template CCR8: Exposures to central counterparties]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping CCP-exposure reporting, treat CCR8 as the SCCR-governed template for the specific sub-charge on central counterparty exposures. The CCR disclosure section covers 'exposures to central counterparties (CCPs)' within the counterparty credit risk charge and points to the SCCR chapters, and CCR8 breaks these into QCCP/non-QCCP, margin and default-fund components. A reviewer should confirm CCP exposures are reported here (not in the general CCR templates) and that qualifying-CCP classification follows the SCCR definitions, since risk-weighting differs by that status.
- **Grounding — this node (Page 819):** "This section includes all exposures in the banking book and trading book that are subject to a counterparty credit risk charge, including the charges applied to exposures to central counterparties (CCPs)."
- **Grounding — related node (Page 827):** "Template CCR8: Exposures to central counterparties ... the template includes all types of exposures (due to operations, margins, contributions to default funds) and related capital requirements."

### [[Template CVA1 Reduced basic approach for CVA|Template CVA1: Reduced basic approach for CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When completing or reviewing Template CVA1, read its figures as computed outputs of the SCCR11 CVA methodology, not as free-standing disclosure numbers. Every row of CVA1 (systematic aggregation, idiosyncratic aggregation, and Kreduced × 12.5) is defined by reference to SCCR11.14, and the disclosure obligation itself is triggered only when the materiality threshold in the CCR framework paragraph 11.9 is met. Confirm both that the threshold is satisfied and that the reported RWA reconcile to the underlying SCCR11 calculation before relying on the template as evidence of compliance.
- **Grounding — this node (Page 751 / OV1 row 10):** "Credit valuation adjustment: RWA and capital charge requirements according to SCCR11."
- **Grounding — related node (Page 849 / Template CVA1 rows 1-3):** "Aggregation of systematic components of CVA risk: RWA under perfect correlation assumption ... as per SCCR11.14."

### [[Template CVA2 Full basic approach for CVA|Template CVA2: Full basic approach for CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether Template CVA2 (full BA-CVA) applies and what it must contain, treat the SCCR counterparty credit risk / CVA framework as the governing source of both scope and computation. The CVA capital requirement under SCCR11 must be calculated by all banks involved in covered transactions across banking and trading book, and disclosure is required once the CCR materiality threshold (para 11.9) is met. Conclude that CVA2's contents are defined by the SCCR11 full basic approach; verify the covered-transaction scope (derivatives except QCCP-facing, plus qualifying SFTs) before treating the template as complete.
- **Grounding — this node (Page 751 / OV1 row 10):** "Credit valuation adjustment: RWA and capital charge requirements according to SCCR11."
- **Grounding — related node (Page 636 / SCCR 11.5):** "The capital requirement for CVA risk must be calculated by all banks involved in covered transactions in both banking book and trading book."

#graphify/concept #graphify/EXTRACTED #community/CCR__CVA_Disclosure_Templates #graphify/enriched
