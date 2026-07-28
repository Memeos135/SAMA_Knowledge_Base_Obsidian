---
source_file: "markdown/SAMA_EN_3417_VER1.md"
type: "document"
community: "LCR & NSFR Metrics"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/LCR__NSFR_Metrics
  - graphify/enriched
---

# BCBS LCR Document Jan 2013

## Connections

### [[Cap on Level 2 Assets Calculation]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining how much of a bank's HQLA buffer can be composed of Level 2/2B assets in collateral-swap and securities-financing transactions, do not treat the SAMA prudential-return line items as self-standing rules — they are operationalisations of the underlying BCBS LCR standard. The return's cap-calculation rows repeatedly point back to Basel III LCR paragraphs (28–40, 48, 113, 146, Annex 1) as the source of the operational-requirement and eligibility tests each swapped asset must meet. For a compliance decision, treat the cited BCBS paragraphs as controlling substance: confirm the asset genuinely satisfies the HQLA operational requirements before reporting it in the relevant panel, rather than relying on the row label alone.
- **Grounding — this node (Page 40 / rows 349–353):** "would be unencumbered and would meet the operational requirements for HQLA as specified in paragraphs 28 to 40 of the Basel III LCR standards"
- **Grounding — related node (Page 46 / rows 412–419):** "Such transactions in which the bank has swapped Level 2A assets (lent) for Level 2B RMBS assets (borrowed). 48, 113, 146, Annex 1"

### [[Concentration of Funding Metric]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining how the concentration-of-funding metric must be calculated and reported, read it as SAMA's adoption of the Basel III LCR standards (Jan 2013) rather than a purely domestic construct — the entire document is built on 'Basel III LCR standards reference' columns and the framework expressly follows BCBS scope and definitions. This matters because thresholds like the 1% 'significant counterparty' test and the 5% 'significant currency' test derive their authority and interpretation from the cited BCBS text. A reader should conclude that where SAMA guidance is silent or ambiguous, the underlying BCBS LCR document is the interpretive source, and should check the referenced Basel paragraphs before finalising a reporting position.
- **Grounding — this node (Page 48 / para 164):** "The application of the requirements in this document follow the existing scope of application set out in Part I (Scope of Application) of the Basel II Framework."
- **Grounding — related node (Page 53 / paras 188-191):** "This metric is meant to identify those sources of wholesale funding... The metric thus encourages the diversification of funding sources recommended in the Committee's Sound Principles."

### [[LCR by Significant Currency]] — `cites` [EXTRACTED]
- **What this link tells you:** When reporting the LCR-by-significant-currency monitoring tool, treat its definitions as inheriting from the cited Basel III LCR standards (Jan 2013) — the framework states the stock of high-quality FX assets and total net FX cash outflows 'should mirror those of the LCR for common currencies.' Note this tool is a monitoring metric, not a binding standard, so it carries no internationally defined minimum threshold, though SAMA may set an alert ratio. A reader should conclude that the currency LCR follows BCBS LCR mechanics (including the 5% significant-currency test and Option 2 FX haircuts) but that any minimum trigger is supervisor-set rather than a hard pass/fail limit.
- **Grounding — this node (Page 56 / para 210):** "The definition of the stock of high-quality foreign exchange assets and total net foreign exchange cash outflows should mirror those of the LCR for common currencies."
- **Grounding — related node (Page 56 / para 212):** "As the foreign currency LCR is not a standard but a monitoring tool, it does not have an internationally defined minimum required threshold."

### [[Market-related Monitoring Tools]] — `cites` [EXTRACTED]
- **What this link tells you:** When scoping the market-related monitoring tools, read them as part of the Basel III LCR monitoring suite adopted by SAMA — the document consistently maps each line to a 'Basel III LCR standards reference' and follows BCBS scope. These are early-warning indicators using high-frequency market data, not a pass/fail standard, so they impose observation and supervisory-alert functions rather than a fixed compliance ratio. A reader should conclude that the authority and definitional content for this tool trace to the cited BCBS LCR document, and should verify the referenced Basel paragraphs before relying on any specific treatment.
- **Grounding — this node (Page 40 / Basel III LCR standards reference column):** "...would meet the operational requirements for HQLA as specified in paragraphs 28 to 40 of the Basel III LCR standards."
- **Grounding — related node (Page 56 / para 214):** "High frequency market data with little or no time lag can be used as early warning indicators in monitoring potential liquidity difficulties at banks."

### [[Net Stable Funding Ratio (NSFR)]] — `references` [INFERRED]
- **What this link tells you:** These two SAMA guidance documents appear to be complementary but distinct minimum standards, and should not be conflated when scoping a bank's liquidity obligations: the LCR (3417) addresses 30-day short-term resilience via HQLA, while the NSFR (3467) addresses stable funding over a one-year horizon. The NSFR document itself frames the pair as 'two separate but complementary objectives,' with the LCR promoting short-term resilience and the NSFR reducing funding risk over a longer horizon. For a compliance decision, treat them as cumulative — meeting the LCR does not discharge NSFR obligations — but verify the specific reporting frequency and scope in each primary document, since the cross-reference here is inferred rather than a direct citation from the LCR text to the NSFR.
- **Grounding — this node (Page 48 / para 162):** "The LCR should be used on an ongoing basis to help monitor and control liquidity risk. The LCR should be reported to supervisors at least monthly"
- **Grounding — related node (3467 / Page 4):** "These standards are designed to achieve two separate but complementary objectives... the net stable funding ratio (NSFR), which SAMA has also implemented"
- **Caveat:** Relation is INFERRED — the linkage is a conceptual LCR/NSFR pairing described in the NSFR document; there is no direct citation from the LCR document (3417) to the NSFR. Confirm against each primary text.

#graphify/document #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
