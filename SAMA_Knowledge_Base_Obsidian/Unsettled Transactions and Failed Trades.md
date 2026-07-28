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

# Unsettled Transactions and Failed Trades

## Connections

### [[Delivery-versus-Payment (DvP) Transactions]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalizing settlement exposures, treat DvP as a defined sub-category within the Chapter 25 'unsettled transactions and failed trades' regime rather than a separate rule set. Para 25.1 establishes the overarching obligation that unsettled transactions must be taken into account for capital purposes irrespective of accounting; para 25.3 then specifies that DvP transactions attract a capital requirement only once payments have not taken place five business days after settlement date. Crucially, check scope: Chapter 25 does not apply to instruments already covered by the CCR/CVA requirements (OTC derivatives, ETDs, long settlement transactions, SFTs), so classify the transaction first to avoid double- or mis-capitalization.
- **Grounding — this node (Page 339 / para 25.1):** "Irrespective of the booking or the accounting of the transaction, unsettled transactions must be taken into account for regulatory capital requirements purposes."
- **Grounding — related node (Page 339 / para 25.3):** "Banks must calculate a capital requirement for such exposures if the payments have not yet taken place five business days after the settlement date"

### [[Non-DvP (Free Deliveries)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank pays or delivers without simultaneous receipt of the corresponding leg, treat non-DvP (free deliveries) as the higher-risk sub-category of the Chapter 25 unsettled-transactions regime. The parent principle (25.1) requires all unsettled transactions to be capitalized regardless of accounting treatment, while 25.4 flags that non-DvP exposes the firm to loss on the full amount paid/delivered — a materially larger exposure than the mark-to-market difference under DvP — with a capital requirement triggered if the second leg is unreceived by end of business day and escalating after five business days. The consequence: distinguish DvP from non-DvP when scoping settlement risk, because the exposure base and timing triggers differ, and remember the same CCR/CVA scope carve-out excludes derivatives and SFTs from this chapter.
- **Grounding — this node (Page 339 / para 25.1):** "unsettled transactions must be taken into account for regulatory capital requirements purposes."
- **Grounding — related node (Page 339-340 / para 25.4):** "non-DvP, or free deliveries... expose firms to a risk of loss on the full amount of cash paid or deliverables de[livered]"

#graphify/concept #graphify/EXTRACTED #community/Counterparty_Credit_Risk_Approaches #graphify/enriched
