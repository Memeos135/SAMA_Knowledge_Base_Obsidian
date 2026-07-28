---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Market Risk Backtesting"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Market_Risk_Backtesting
  - graphify/enriched
---

# Actual P&L (APL)

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating a bank's backtesting compliance, understand that Actual P&L (APL) is one of the defined inputs the backtesting process compares against model-generated VaR to test model conservatism. The standard defines APL as the daily P&L including intraday trading, time effects and new/modified deals but excluding fees, commissions and specified valuation adjustments — and it is APL loss (alongside HPL) that determines whether a desk-level exception can be disregarded. For a compliance decision you would check that APL is constructed to the [12.26]-[12.28] exclusions, because a mis-specified APL directly distorts exception counts and therefore the backtesting-zone outcome and any add-on.
- **Grounding — this node (Page 7 (definitions) / [12.25]):** "The actual P&L derived from the daily P&L process. It includes intraday trading as well as time effects and new and modified deals, but excludes fees and commissions"
- **Grounding — related node (Page 110):** "an SES capital requirement that is in excess of the maximum of the APL loss or HPL loss for that day, it is permitted to be disregarded"

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
