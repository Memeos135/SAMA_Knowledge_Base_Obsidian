---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "document"
community: "CCR & CVA Capital Requirements"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/CCR__CVA_Capital_Requirements
  - graphify/enriched
---

# Minimum Capital Requirements for CCR and CVA

## Connections

### [[Counterparty Credit Risk (CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which SAMA capital rules bind a bank's derivatives and SFT book, treat 'Counterparty Credit Risk' as a defined concept whose obligations live inside this framework document — the framework both defines CCR (Chapter 3) and sets the mandatory measurement, reporting and effective-date requirements around it. The framework fixes the go-live (01 January 2023) and the Q17 quarterly reporting duty within 30 days of quarter-end, so the concept is not free-standing guidance but an enforceable regime. Conclude that any CCR compliance position must be anchored to this document's provisions rather than to the abstract term.
- **Grounding — this node (Page 12 / 4.1-4.2):** "This framework will be effective on 01 January 2023... report the Counterparty credit risk (CCR) and Credit Valuation Adjustment (CVA) Risk-Weighted Assets (RWA)... within 30 days"
- **Grounding — related node (Page 12 / 5.1):** "Counterparty credit risk is defined in Chapter 3 of this framework. It is the risk that the counterparty to a transaction could default before the final settlement"

### [[Credit Valuation Adjustment (CVA) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping capital obligations under this document, do not treat CCR and CVA as one undifferentiated charge — the framework carries a separate, mandatory CVA regime (Chapter 11) with its own covered-transaction scope and its own approach hierarchy. All banks with covered derivatives/SFTs must calculate a CVA risk capital requirement, and BA-CVA is the default unless SAMA approves SA-CVA; a materiality carve-out exists only below the SAR 446 billion notional threshold. Conclude that CVA capital is an independent standalone requirement (calculated on a 'CVA portfolio') that must be assessed on its own terms even after CCR EAD is measured.
- **Grounding — this node (Page 87 / 11.5):** "The capital requirement for CVA risk must be calculated by all banks involved in covered transactions in both banking book and trading book."
- **Grounding — related node (Page 86-87 / 11.7):** "Two approaches are available for calculating CVA capital... Banks must use the BA-CVA unless they receive approval from Saudi Central Bank (SAMA) to use the SA-CVA."

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** When advising on whether a bank may use its own internal exposure models for CCR, note that IMM is a permission-gated method inside this framework, not a default option — a bank must obtain SAMA approval, meet the qualifying standards (7.6–7.60), and generally apply IMM to all exposures subject to CCR except long settlement transactions. Reversion to the standardized approach is only allowed under exceptional circumstances or for immaterial exposures and must not enable regulatory-capital arbitrage. Conclude that IMM use should be verified against an actual SAMA approval and the use-test/track-record conditions before relying on internally-modelled EAD.
- **Grounding — this node (Page 89 / 11.12):** "Banks that use the BA-CVA or the SA-CVA for calculating CVA capital requirements may cap the maturity adjustment factor at 1... when they calculate CCR capital requirements under the Internal Ratings Based (IRB) app[roach]"
- **Grounding — related node (Page 48 / 7.1):** "A bank that wishes to adopt an internal models method to measure exposure or exposure at default (EAD) for regulatory capital purposes must seek SAMA approval."

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the default CCR measurement method, treat SA-CCR as the mandatory fallback: this framework requires banks without IMM approval to use SA-CCR for OTC derivatives, exchange-traded derivatives and long settlement transactions. The framework also links the CVA regime to SA-CCR outputs — the IRB maturity-adjustment cap at 1 applies per netting set for which BA-CVA/SA-CVA capital is calculated. Conclude that unless a bank holds IMM approval, SA-CCR governs its derivative EAD, and CVA-related maturity caps must be applied consistently across the CCR and CVA calculations.
- **Grounding — this node (Page 89 / 11.12):** "Banks that use the BA-CVA or the SA-CVA for calculating CVA capital requirements may cap the maturity adjustment factor at 1 for all netting sets"
- **Grounding — related node (Page 18 / 6.1):** "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives... Banks that do not have approval to apply the internal model method (IMM)... must use SA-CCR"

#graphify/document #graphify/EXTRACTED #community/CCR__CVA_Capital_Requirements #graphify/enriched
