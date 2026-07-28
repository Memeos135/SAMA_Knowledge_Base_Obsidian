---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Credit & Securitization Templates"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Credit__Securitization_Templates
  - graphify/enriched
---

# SCRE Credit Risk Framework

## Connections

### [[Minimum Capital Requirements for Credit Risk]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two documents appear to describe the same regime from different angles: 'Minimum Capital Requirements for Credit Risk' (SAMA_EN_3502) sets the substantive standardised/IRB credit-risk and CRM rules, while the SCRE references in the Pillar 3 framework (SAMA_EN_3487) are the disclosure-side citations to that same credit-risk standard. Note that 3502 itself points to Pillar 3 ("The requirements of chapter 19 in Pillar 3 Disclosure Requirements Framework must be fulfilled for banks to obtain capital relief"), which is the very section housing SCRE-referenced templates. Treat this as a lead: the capital-calculation obligations in 3502 and the disclosure obligations tagged SCRE are two halves of one requirement, so confirm the paragraph correspondence before relying on it for compliance.
- **Grounding — this node (Page 751 / row 2):** "RWA and capital requirements according to the standardised approach to credit risk (as specified in SCRE5 to SCRE9)."
- **Grounding — related node (Page 61 / para 9.4):** "The requirements of chapter 19 in Pillar 3 Disclosure Requirements Framework must be fulfilled for banks to obtain capital relief in respect of any CRM techniques."
- **Caveat:** Relation is INFERRED/conceptual — the documents are not shown to cross-cite each other directly. Verify that SCRE labels in 3487 map to the substantive rules in 3502 before relying on the equivalence.

### [[Template CR10 IRB specialised lending slotting approach|Template CR10: IRB specialised lending slotting approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how specialised-lending exposures must be disclosed and capitalised, read CR10 as subordinate to the SCRE credit risk framework: CR10 covers the IRB supervisory slotting approach, which the framework specifies is governed by SCRE13 (an explicit exception carved out of the general F-IRB/A-IRB rules in SCRE10–SCRE16). This anchors CR10's slotting figures to a specific substantive standard rather than the general IRB modelling rules. For a compliance check, confirm that specialised-lending RWA disclosed in CR10 is computed under SCRE13's slotting criteria and reported in the corresponding slotting row, not merged with modelled IRB portfolios.
- **Grounding — this node (Page 751):** "supervisory slotting approach: RWA and capital requirements according to the supervisory slotting approach (as specified in SCRE13)"
- **Grounding — related node (Page 755):** "supervisory slotting approaches of the credit risk framework"

### [[Template CR3 Credit risk mitigation techniques overview|Template CR3: Credit risk mitigation techniques overview]] — `references` [INFERRED]
- **What this link tells you:** When disclosing credit risk mitigation via Template CR3, note that the template appears to operate within the SCRE credit risk framework, which defines the standardised and IRB approaches (SCRE5–SCRE9, SCRE10–SCRE16, SCRE25) that determine how mitigated exposures are risk-weighted. CR3 sits in the Pillar 3 disclosure section covering RWA for credit risk, while SCRE supplies the underlying capital calculation and mitigation-recognition rules the disclosure reports on. Verify the primary SCRE paragraphs governing the specific mitigant before concluding a CR3 figure is correct, since the link here is inferred from the shared credit-risk scope rather than an explicit CR3-to-SCRE citation.
- **Grounding — this node (Page 751 / row 2):** "RWA and capital requirements according to the standardised approach to credit risk (as specified in SCRE5 to SCRE9)."
- **Grounding — related node (Page 794 / section 19.2.2):** "Credit risk mitigation: ... Template CR3 - Credit risk mitigation techniques – overview"
- **Caveat:** Link is INFERRED from shared credit-risk scope; CR3 does not explicitly cite SCRE by number. Confirm the applicable SCRE paragraphs in the primary text.

### [[Template CR5 Standardised approach exposures by asset classes and risk weights|Template CR5: Standardised approach exposures by asset classes and risk weights]] — `references` [EXTRACTED]
- **What this link tells you:** When completing CR5, treat the SCRE credit-risk framework as the controlling calculation authority that the template merely reports. CR5 discloses standardised-approach exposures by asset class and risk weight, and its own instructions repeatedly anchor to SCRE — the standardised approach 'as specified in SCRE5 to SCRE9', excluded positions 'subject to SCRE18 to SCRE23', and failed-trade treatment 'as set out in SCRE25.' A reader should conclude that asset-class definitions, risk weights and scope exclusions in CR5 are not discretionary but are fixed by the cited SCRE paragraphs, which must be consulted to populate the template correctly.
- **Grounding — this node (Page 751):** "Of which: standardised approach: RWA and capital requirements according to the standardised approach to credit risk (as specified in SCRE5 to SCRE9)."
- **Grounding — related node (Page 755):** "This also includes failed trades and non-delivery-versus-payment transactions as set out in SCRE25."

### [[Template CR6 IRB credit risk exposures by portfolio and PD range|Template CR6: IRB credit risk exposures by portfolio and PD range]] — `references` [EXTRACTED]
- **What this link tells you:** When completing CR6, treat the SCRE framework — specifically its IRB chapters — as the governing rule set that determines whether the template applies and how its parameters are derived. CR6 discloses IRB credit-risk exposures by portfolio and PD range, and the SCRE mapping ties IRB reporting to 'the F-IRB approach and/or A-IRB approach (as specified in SCRE10 to SCRE16 with the exception of SCRE13)', with the slotting approach under SCRE13. A reader should conclude that CR6 is only required where SAMA has approved IRB use, and that PD, LGD and portfolio definitions must follow the cited SCRE IRB paragraphs rather than the template's presentation alone.
- **Grounding — this node (Page 751):** "Of which: (foundation/advanced) internal rating based approaches: RWA and capital requirements according to the F-IRB approach and/or A-IRB approach (as specified in SCRE10 to SCRE16 with the exception of SCRE13)."
- **Grounding — related node (Page 755):** "RWA for modelled approaches ... subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) and supervisory slotting approaches"

### [[Template SEC1 Securitisation exposures in the banking book|Template SEC1: Securitisation exposures in the banking book]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a bank must place in Pillar 3 securitisation templates versus ordinary credit-risk templates, treat the SCRE credit-risk framework as the scoping boundary: SCRE18–SCRE23 (the securitisation framework) is carved out of the general credit-risk disclosures. Template SEC1 explicitly ties its terms to SCRE18 ('all terms used in section 21 are used consistently with the definitions in SCRE18') and covers all securitisation exposures, whereas credit-risk sections exclude positions subject to the securitisation regulatory framework. For a compliance decision, use SCRE definitions to classify an exposure before choosing the template — SEC1 captures every securitisation exposure (even those failing risk-transfer recognition), so do not assume a position belongs in credit-risk templates simply because it did not qualify for the securitisation framework.
- **Grounding — this node (Page 794 / 19.1.1):** "All positions subject to the securitization regulatory framework ... are reported in section 21"
- **Grounding — related node (Page 829 / para 21.2):** "all terms used in section 21 are used consistently with the definitions in SCRE18 ... Covers all securitisation exposures in Table SECA and in templates SEC1 and SEC2"

### [[Template SEC3 Securitisation banking book originatorsponsor|Template SEC3: Securitisation banking book originator/sponsor]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether originator/sponsor securitisation exposures qualify for SEC3 capital treatment, the SCRE framework is determinative: SEC3 is limited to exposures the bank treats under the securitisation framework (SCRE18–SCRE22), which for originators requires meeting the risk-transfer recognition criteria in SCRE18.24–SCRE18.29. The Page 755 instruction confirms that credit-risk row 1 'excludes all positions subject to SCRE18 to SCRE23, including securitisation exposures in the banking book (which are reported in row 4).' A compliance reader should conclude that failure to meet the SCRE risk-transfer criteria removes an exposure from SEC3 (and its favourable securitisation capital treatment), pushing it back into the general credit-risk framework — verify the SCRE18.24–18.29 tests before reporting under SEC3.
- **Grounding — this node (Page 755):** "The row excludes all positions subject to SCRE18 to SCRE23, including securitisation exposures in the banking book (which are reported in row 4)"
- **Grounding — related node (markdown/SAMA_EN_3487_VER1.md (Template SEC3 scope)):** "Only securitisation exposures that the bank treats under the securitisation framework (SCRE18 to SCRE22) are disclosed in templates SEC3 and SEC4"

### [[Template SEC4 Securitisation banking book investor|Template SEC4: Securitisation banking book investor]] — `references` [EXTRACTED]
- **What this link tells you:** For an investing bank classifying purchased securitisation positions, the SCRE framework again fixes the boundary: SEC4 (banking-book investor) is confined to exposures treated under the securitisation framework (SCRE18–SCRE22), and the credit-risk instructions expressly exclude SCRE18–SCRE23 positions from row 1. This means an investor cannot dual-report the same exposure under both general credit-risk and securitisation frameworks — the SCRE definitions route it to one or the other. A compliance reader should apply the SCRE securitisation definitions first to determine whether an investor position belongs in SEC4 rather than the ordinary credit-risk templates.
- **Grounding — this node (Page 755):** "The row excludes all positions subject to SCRE18 to SCRE23, including securitisation exposures in the banking book"
- **Grounding — related node (markdown/SAMA_EN_3487_VER1.md (Template SEC4 scope)):** "securitisation exposures that the bank treats under the securitisation framework (SCRE18 to SCRE22) are disclosed in templates SEC3 and SEC4"

#graphify/concept #graphify/EXTRACTED #community/Credit__Securitization_Templates #graphify/enriched
