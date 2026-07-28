---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Counterparty Credit Risk Approaches"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Counterparty_Credit_Risk_Approaches
  - graphify/enriched
---

# Non-DvP (Free Deliveries)

## Connections

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the IRB credit-risk row of the RWA overview, be aware it does not capture unsettled/failed-trade exposures: the standardised-approach definition expressly folds in 'failed trades and non-delivery-versus-payment transactions as set out in SCRE25,' while the IRB row (cell 1/a) excludes settlement-risk positions, which are reported separately. A reviewer should therefore check that non-DvP (free delivery) exposures are capitalised under the unsettled-transactions rules (SCRE25) and reported in the settlement-risk line, not swept into the IRB credit-risk figures. Do not assume IRB modelling covers free deliveries.
- **Grounding — this node (Page 339 / Art 25.1):** "unsettled transactions must be taken into account for regulatory capital requirements purposes."
- **Grounding — related node (Page 755):** "This also includes failed trades and non-delivery-versus-payment transactions as set out in SCRE25."

### [[Unsettled Transactions and Failed Trades]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank pays or delivers without simultaneous receipt of the corresponding leg, treat non-DvP (free deliveries) as the higher-risk sub-category of the Chapter 25 unsettled-transactions regime. The parent principle (25.1) requires all unsettled transactions to be capitalized regardless of accounting treatment, while 25.4 flags that non-DvP exposes the firm to loss on the full amount paid/delivered — a materially larger exposure than the mark-to-market difference under DvP — with a capital requirement triggered if the second leg is unreceived by end of business day and escalating after five business days. The consequence: distinguish DvP from non-DvP when scoping settlement risk, because the exposure base and timing triggers differ, and remember the same CCR/CVA scope carve-out excludes derivatives and SFTs from this chapter.
- **Grounding — this node (Page 339-340 / para 25.4):** "non-DvP, or free deliveries... expose firms to a risk of loss on the full amount of cash paid or deliverables de[livered]"
- **Grounding — related node (Page 339 / para 25.1):** "unsettled transactions must be taken into account for regulatory capital requirements purposes."

#graphify/concept #graphify/EXTRACTED #community/Counterparty_Credit_Risk_Approaches #graphify/enriched
