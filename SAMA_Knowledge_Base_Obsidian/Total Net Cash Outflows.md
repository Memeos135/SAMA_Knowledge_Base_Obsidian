---
source_file: "markdown/SAMA_EN_2788_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Total Net Cash Outflows

## Connections

### [[Cash Inflows]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the LCR denominator, treat Cash Inflows and Total Net Cash Outflows as a single linked calculation, not independent figures, because the standard defines net outflows precisely as outflows minus inflows and caps recognised inflows at 75% of total expected outflows. The formula (outflows minus the lesser of inflows or 75% of outflows) means excess inflows cannot fully offset outflows, and the no-double-counting rule bars counting an HQLA-included asset's inflows again. Conclude that inflow recognition is bounded by this 75% cap and the anti-double-counting constraint, so a bank cannot reduce its net outflow figure below 25% of gross outflows through inflows alone.
- **Grounding — this node (Page 26, para 69):** "total expected cash inflows ... up to an aggregate cap of 75% of total expected cash outflows"
- **Grounding — related node (Page 43, para 158):** "Derivatives cash inflows: the sum of all net cash inflows should receive a 100% inflow factor"

### [[Cash Outflows]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the LCR denominator for a SAMA-supervised bank, treat 'Cash Outflows' as a component of, not a synonym for, 'Total Net Cash Outflows': the net figure is total expected outflows minus capped inflows over the 30-day stress horizon. Paragraph 69 defines the net measure and its inflow cap at 75% of total expected outflows, so gross outflow categories feed directly into it. You should conclude that any outflow category (retail, wholesale, secured, derivatives) must be aggregated and then netted against eligible inflows, subject to the 75% floor on inflow offset, before assessing LCR compliance.
- **Grounding — this node (Page 26 / para 69):** "total net cash outflows... is defined as the total expected cash outflows minus total expected cash inflows in the specified stress scenario for the subsequent 30 calendar days"
- **Grounding — related node (Page 26 / para 69):** "Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off"

### [[Liquidity Coverage Ratio (LCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the LCR you must apply Total Net Cash Outflows as the denominator, and its precise formula constrains the outcome. The standard defines it as 'total expected cash outflows minus total expected cash inflows' over 30 days, with inflows capped at 75% of outflows, and prohibits double-counting (an asset in the HQLA stock cannot also count its inflows). For decision purposes, verify the run-off/draw-down and inflow factors in Annex 4 and the 75% cap, since misapplying either the cap or the no-double-count rule directly distorts the ratio.
- **Grounding — this node (Page 26 / para 69):** "total net cash outflows … total expected cash outflows minus total expected cash inflows … up to an aggregate cap of 75% of total expected cash outflows"
- **Grounding — related node (Page 13 / para 23):** "banks must hold a stock of unencumbered HQLA to cover the total net cash outflows (as defined below) over a 30-day period"

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
