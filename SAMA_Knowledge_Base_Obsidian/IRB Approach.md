---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Counterparty Credit Risk Approaches"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Counterparty_Credit_Risk_Approaches
  - graphify/enriched
---

# IRB Approach

## Connections

### [[DRC Requirement Internal Model]] — `references` [EXTRACTED]
- **What this link tells you:** This cross-reference between the IRB credit-risk regime (capital adequacy document) and the DRC internal model (market-risk document) appears to reflect the conceptual overlap in modelling default risk across the banking and trading books rather than a direct textual obligation link. The provided excerpts for the DRC node concern independent model validation and backtesting generally, not an explicit IRB citation, so the connection reads as thematic. Treat this as a lead only and verify the primary DRC text (SMAR default-risk-charge provisions) for any actual IRB parameter cross-reference before relying on it.
- **Grounding — this node (Page 755):** "subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB)"
- **Grounding — related node (Page 92 / Art 10.8):** "must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements"
- **Caveat:** Relation inferred from thematic model-risk overlap; provided DRC excerpts do not textually cite the IRB approach. Verify the primary DRC provisions before relying on a direct link.

### [[DRC Requirement Model (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are reconciling market-risk and credit-risk capital treatment of the same positions, note that the DRC requirement under the IMA and the IRB approach are analytically related but govern different books: the DRC measures 'the default risk of trading book positions' under SMAR13.18, whereas IRB governs default risk in the banking book, and both draw on default-risk (PD/LGD-type) modelling permitted only with SAMA approval. The reference reflects shared modelling concepts (default risk, internal models subject to supervisory validation) across the same rulebook. For a compliance decision, keep the boundary clear — trading-book default risk falls under the DRC/IMA regime, not the IRB credit-risk regime — and confirm each internal model carries its own SAMA approval, since neither approval transfers to the other.
- **Grounding — this node (Page 755 / row 1):** "subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) ...)"
- **Grounding — related node (Page 845 / row for DRC):** "Default risk capital (DRC) requirement: ... measure of the default risk of trading book positions, except those subject to standardised capital requirements."
- **Caveat:** Link rests on shared 'default risk' modelling concepts across market-risk (IMA/DRC) and credit-risk (IRB) chapters; the two apply to different books. Verify each regime's approval scope separately.

### [[IRB Asset Classes]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how a bank must apply the IRB approach, treat asset-class categorization as the mandatory entry gate, not an afterthought: the IRB rules operate by requiring banks to sort banking-book exposures into corporate, sovereign, bank, retail and equity classes, and rollout obligations attach at the asset-class level. Because 10.4 fixes the taxonomy and 10.44–10.46 require that adoption of IRB for an asset class in a business unit be applied to ALL exposures in that class in that unit under a SAMA-agreed plan, the two provisions are read together to scope the obligation. A compliance reviewer should conclude that IRB commitments cannot be cherry-picked within an asset class, and that the equity class is excluded from IRB entirely.
- **Grounding — this node (Page 113 / 10.45):** "when a bank adopts an IRB approach for an asset class within a particular business unit, it must apply the IRB approach to all exposures within that asset class in that unit."
- **Grounding — related node (Page 99 / 10.4):** "banks must categorize banking-book exposures into broad classes of assets... (a) corporate, (b) sovereign, (c) bank, (d) retail, and (e) equity."

### [[IRB Minimum Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may lawfully use the IRB approach, do not treat the approach and its minimum requirements as separable — use of IRB is conditional on continuing satisfaction of the Chapter 16 minimum requirements for entry and on-going use. The IRB rows in the reporting/RWA framework only recognize IRB-computed RWA where the bank has SAMA approval, and that approval rests on the minimum-requirement set (rating system design, governance, validation, risk quantification, disclosure). A reviewer should conclude that a bank failing any minimum requirement cannot rely on its IRB numbers, and that these requirements cut across asset classes rather than applying class-by-class.
- **Grounding — this node (Page 755):** "RWA for modelled approaches that banks have SAMA approval to use... subject to the credit risk IRB approaches (F-IRB, A-IRB and supervisory slotting)."
- **Grounding — related node (Page 184 / 16.1–16.2):** "This chapter presents the minimum requirements for entry and on-going use of the internal ratings-based (IRB) approach... cut across asset classes."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating an IRB implementation, focus on the risk components (PD, LGD, EAD, M) because the distinction between foundation and advanced IRB turns entirely on which of these a bank estimates itself. The IRB rollout rule expressly ties advancement to 'own estimates of LGD and EAD' and moving 'from the foundation approach to the advanced approach for certain risk components.' A reviewer should conclude that data limitations on specific components (e.g., LGD/EAD) can lawfully restrict a bank to F-IRB for some exposures even within an IRB-approved asset class.
- **Grounding — this node (Page 113 / 10.44):** "banks can meet the standards for the use of own estimates of LGD and EAD for some but not all of their exposures within an asset class."
- **Grounding — related node (Page 361 (definitions)):** "Risk factor: A principal determinant of the change in value of an instrument (eg an exchange rate or interest rate)."
- **Caveat:** Node B is a broad 'risk components' concept node populated from market-risk/CVA definition pages; the PD/LGD/EAD/M link to IRB is grounded in the IRB rollout text (10.44), not in the quoted definition page. Verify the specific IRB risk-quantification chapter for component definitions.

### [[Interest Rate Risk (Simplified SA)]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the SAMA_EN_3487 capital framework, note that the simplified standardised approach to interest-rate (market) risk and the IRB approach to credit risk are distinct methodologies addressing different risk classes within the same rulebook — 'general interest rate risk' is a defined market-risk class, while IRB governs credit RWA. The reference reflects their co-location in one comprehensive capital document rather than an operative dependency between them. For a compliance decision, do not treat interest-rate-risk measurement under the simplified SA as governed by IRB rules or vice versa; verify each methodology's own eligibility and SAMA-approval conditions against its own chapter before relying.
- **Grounding — this node (Page 755 / row 1):** "the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) ...)"
- **Grounding — related node (Page 361 / definitions):** "Risk class: ... general interest rate risk, credit spread risk (non-securitisation) ... FX risk, equity risk and commodity risk."
- **Caveat:** The two nodes address different risk classes (market interest-rate risk vs credit risk); the link appears to reflect shared-document co-location rather than a substantive cross-obligation. Confirm against each respective chapter.

### [[Look-Through Approach (LTA)]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears weaker than the label suggests and should be treated as a lead rather than a direct dependency. The Look-Through Approach is a treatment for indices, multi-underlying instruments and equity investments in funds (market-risk/equity context), while the IRB rows on Page 755 concern credit-risk RWA computation; the two share the same defved-terms glossary but the excerpts do not establish that IRB reliance depends on LTA. Before relying on this connection, verify the primary text: LTA is most relevant to fund/index exposures and equity treatment, whereas IRB credit-risk categorization is a separate mechanism, and equity is excluded from IRB entirely.
- **Grounding — this node (Page 755):** "subject to the credit risk IRB approaches (F-IRB, A-IRB and supervisory slotting approaches of the credit risk framework)."
- **Grounding — related node (Page 406 / 7.34–7.35):** "A look-through approach must always be used for indices... banks must apply a look-through approach and treat the underlying positions of the fund as if held directly."
- **Caveat:** Relationship is thin/indirect — LTA (index/fund/equity treatment) and IRB credit-risk categorization operate in different parts of the framework; confirm any dependency in the primary text before relying on it.

### [[Mandate-Based Approach (MBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how a bank capitalises its equity investments in funds, note that the IRB credit-risk regime and the mandate-based approach (MBA) are linked parts of one framework: the MBA is one of the look-through methods for fund exposures, and this document explicitly addresses 'Application of the LTA and MBA to banks using the IRB approach.' A compliance reviewer should therefore not treat MBA as free-standing — a bank on IRB that holds fund exposures must apply MBA within the constraints set for IRB banks. Verify the specific paragraphs governing that interaction (the cross-referenced fund-exposure section) before concluding a given fund position is correctly risk-weighted.
- **Grounding — this node (Page 755):** "subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) and supervisory slotting approaches"
- **Grounding — related node (Page 13):** "The mandate-based approach ... Application of the LTA and MBA to banks using the IRB approach"

### [[Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping credit-risk capital obligations, read the IRB approach as a subordinate, permissioned alternative within the overarching Minimum Capital Requirements for Credit Risk, not a separate regime — the parent framework's disclosure rows expressly split credit RWA into 'standardised approach' (SCRE5–9) and 'foundation/advanced internal rating based approaches' (SCRE10–16), and IRB use requires an implementation plan 'agreed with SAMA.' The reference tells you that a bank cannot elect IRB unilaterally: SAMA approval, phased rollout and the no-capital-relief constraint on intra-group transactions all condition its use. For a compliance decision, confirm SAMA has approved the specific asset-class rollout before treating any IRB-based RWA as validly reported under the credit-risk framework.
- **Grounding — this node (Page 113 / para 10.46):** "it must produce an implementation plan ... The plan ... must be agreed with the SAMA."
- **Grounding — related node (Page 751 / rows 3 and 5):** "Of which: (foundation/advanced) internal rating based approaches: RWA and capital requirements according to the F-IRB approach and/or A-IRB approach"

### [[Non-DvP (Free Deliveries)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the IRB credit-risk row of the RWA overview, be aware it does not capture unsettled/failed-trade exposures: the standardised-approach definition expressly folds in 'failed trades and non-delivery-versus-payment transactions as set out in SCRE25,' while the IRB row (cell 1/a) excludes settlement-risk positions, which are reported separately. A reviewer should therefore check that non-DvP (free delivery) exposures are capitalised under the unsettled-transactions rules (SCRE25) and reported in the settlement-risk line, not swept into the IRB credit-risk figures. Do not assume IRB modelling covers free deliveries.
- **Grounding — this node (Page 755):** "This also includes failed trades and non-delivery-versus-payment transactions as set out in SCRE25."
- **Grounding — related node (Page 339 / Art 25.1):** "unsettled transactions must be taken into account for regulatory capital requirements purposes."

### [[Output Floor Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's use of the IRB approach delivers actual capital relief, the Output Floor Requirements are decisive: they cap modelled RWA at a percentage of standardised-approach RWA, and paragraph 5.8 expressly bars the IRB credit-risk approach from being used, directly or by cross-reference, in the floor base calculation. A compliance reviewer should conclude that IRB outputs cannot be relied on in isolation — the floored figure (effective 1 January 2023, subject to phase-in) governs the minimum. Check the floor calibration and reporting obligation alongside any IRB RWA number.
- **Grounding — this node (Page 755):** "RWA for modelled approaches that banks have SAMA approval to use ... subject to the credit risk IRB approaches"
- **Grounding — related node (Page 734 / Art 5.8):** "the following approaches are not permitted to be used, directly or by cross reference ... IRB approach to credit risk"

### [[Saudi Central Bank (SAMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When planning any IRB adoption, treat it as a supervisory-approval regime, not a self-election: SAMA is the approving and gatekeeping authority for use of internal models and for the rollout plan. The framework recognizes IRB-based RWA only for 'approaches that banks have SAMA approval to use,' and the rollout plan 'must be agreed with the SAMA,' which will also deny capital relief for intra-group transactions designed to reduce the group charge. A reviewer should conclude that no IRB reliance is defensible without documented SAMA approval, and that SAMA retains discretion over the phasing, floors and anti-arbitrage conditions.
- **Grounding — this node (Page 113 / 10.46):** "The plan should be realistic, and must be agreed with the SAMA... SAMA will ensure that no capital relief is granted for intra-group transactions..."
- **Grounding — related node (Page 3 (Introduction)):** "SAMA applies the framework to all local banks on a consolidated level and at every tier within the bank group."

### [[Specific Risk]] — `references` [EXTRACTED]
- **What this link tells you:** The link between the IRB credit-risk approach (capital adequacy) and the 'Specific Risk' concept in the market-risk framework appears to be a conceptual bridge — both address issuer/credit-spread risk, but across different books and regimes. The supplied market-risk excerpts cover internal risk transfers and defined terms, not an explicit IRB cross-reference, so the connection is thematic rather than an obligation chain. Use this only as a signpost that credit-related risk is capitalised under distinct regimes; confirm the actual specific-risk provisions in the market-risk text before treating them as linked to IRB.
- **Grounding — this node (Page 755):** "the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB)"
- **Grounding — related node (Page 5):** "a bond ... has risk positions in general interest rate risk, credit spread"
- **Caveat:** Relation inferred from conceptual overlap in credit-related risk; no explicit IRB citation in the provided specific-risk excerpts. Verify primary text before relying on the link.

#graphify/document #graphify/EXTRACTED #community/Counterparty_Credit_Risk_Approaches #graphify/enriched
