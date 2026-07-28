---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Trading Book Policy"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Trading_Book_Policy
  - graphify/enriched
---

# Internal Risk Transfer

## Connections

### [[Banking Book  Trading Book Boundary|Banking Book / Trading Book Boundary]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding how a hedge moving risk across the banking/trading book boundary is capitalised, apply the internal risk transfer rules [5.18]–[5.29] as the operative mechanism for that boundary. The framework only recognises transfers from banking book to trading book (not the reverse) and only where documented external-hedge matching conditions are met, so the boundary is not just a classification but a set of conditions that govern capital recognition. You would conclude that mischaracterising or under-documenting an internal risk transfer causes the transfer to be excluded from capital recognition, changing the market-risk capital outcome.
- **Grounding — this node (Page 23 / 5.18):** "An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book."
- **Grounding — related node (Page 23 / 5.19):** "There will be no regulatory capital recognition for internal risk transfers from the trading book to the banking book."

### [[Credit Valuation Adjustment (CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what enters the P&L series used for market-risk backtesting and internal-model eligibility, treat CVA and internal risk transfers as separately-carved-out items rather than ordinary trading positions. Both are addressed in the same SAMA market risk framework (SAMA_EN_3553): CVA has its own separate regulatory capital approach so it must be excluded from APL/HPL, while internal risk transfers only receive capital recognition under the constraints in [5.25]–[5.27]. Conclude that you cannot fold either into standard trading-book P&L or hedge recognition without applying its distinct rule; verify the specific paragraph before claiming an offset or exclusion.
- **Grounding — this node (Page 25 / 5.28):** "Internal risk transfers between the internal risk transfer desk and other trading desks will only receive regulatory capital recognition if the constraints in [5.25] to [5.27] are fulfilled."
- **Grounding — related node (Page 114 / 12.26):** "valuation adjustments for which separate regulatory capital approaches have been otherwise specified... (eg credit valuation adjustment and its associated eligible hedges)"

### [[SAMA Minimum Capital Requirements for Credit Risk]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing whether a banking-book credit or equity exposure is deemed hedged by an internal risk transfer, do not evaluate the market-risk conditions in isolation: [5.21] cross-refers to specific paragraphs (9.73–9.74, 9.76–9.77) of the SAMA credit-risk capital framework that the external hedge must satisfy vis-à-vis the banking-book exposure. This makes credit-risk recognition of the hedge dependent on both frameworks being met simultaneously. You would conclude that you must verify the external hedge against the cited credit-risk provisions before treating the banking-book exposure as hedged for capital purposes.
- **Grounding — this node (Page 24 / 5.22):** "the banking book exposure is deemed to be hedged by the banking book leg of the internal risk transfer for capital purposes in the banking book"
- **Grounding — related node (Page 24 / 5.21(1)(b)):** "The external hedge meets the requirements of paragraphs 9.73 to 9.74 and 9.76 9.77 of the SAMA Minimum Capital Requirements for Market Risk vis-à-vis the banking book exposure"
- **Caveat:** The [5.21](1)(b) reference names 'Market Risk' provisions 9.73–9.77; whether these are the credit-risk framework paragraphs is ambiguous in the extract, so verify the cross-referenced document before relying on the credit-risk linkage.

#graphify/concept #graphify/EXTRACTED #community/Trading_Book_Policy #graphify/enriched
