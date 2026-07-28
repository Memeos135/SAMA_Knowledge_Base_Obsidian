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

# Trading Book

## Connections

### [[Banking Book]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When classifying a position, the banking book and trading book are mutually exclusive regulatory 'books' whose boundary drives the entire capital outcome — market risk capital applies to the trading book, and moving exposure across the boundary changes which capital rules bite. The framework fixes classification via a presumptive list ([5.9]) and permits deviation only with SAMA written approval, and internal transfers between the two books receive capital recognition only under strict conditions. Conclude that book assignment is not a free accounting choice: verify against the presumptive list and obtain SAMA approval before reclassifying, because the boundary determines the applicable capital regime.
- **Grounding — this node (Page 380 / 5.22):** "the trading book leg of the internal risk transfer and the external hedge must be included in the market risk capital requirements"
- **Grounding — related node (Page 376 / 5.10):** "Banks are allowed to deviate from the presumptive list specified in [5.9] ... it must submit a request to SAMA and receive Written approval."

### [[Internal Risk Transfer]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can claim capital relief for an internal hedge, treat the internal risk transfer and the trading book as legally interdependent: the trading-book leg of an internal risk transfer only earns regulatory capital recognition where the constraints in [5.25]-[5.27] are met, and that leg must satisfy the same trading-book requirements under [25] as any other trading-book instrument. The market risk framework treats the transfer as a defined 'internal written record of a transfer of risk' whose booking side determines capital treatment. Conclude that you cannot assess the internal risk transfer's capital effect in isolation — check that its trading-book leg meets the full trading-book instrument requirements before relying on any hedge recognition.
- **Grounding — this node (Page 379 / 5.18):** "An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book"
- **Grounding — related node (Page 381 / 5.29):** "The trading book leg of internal risk transfers must fulfil the same requirements under [25] as instruments in the trading b[ook]"

### [[Trading Book Policy Statement (TPS)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's market-risk obligations, note that having a Trading Book Policy Statement is a mandatory prerequisite tied directly to trading-book/market-risk exposure: all banks with market risk exposures 'are required to have a Trading Book Policy Statement (TPS).' The TPS is the governing document that documents trading-desk structure and how positions are assigned to the trading book for the market-risk capital framework. Conclude that any bank with trading-book positions must maintain a TPS, and that classification and desk decisions should be checked against it rather than treated as informal.
- **Grounding — this node (Page 379 / 5.18):** "a transfer of risk within the banking book, between the banking and the trading book or within the trading book (between different desks)"
- **Grounding — related node (Page 368 / 4.1):** "All banks with market risk exposures are required to have a Trading Book Policy Statement (TPS)."

### [[Trading Desk]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When mapping how trading-book positions are governed, understand the trading desk as the mandatory organisational unit into which trading-book activity is grouped for the regulatory capital charge — 'an unambiguously defined group of traders or trading accounts' with a defined risk scope. Desk definitions must meet the [4.7] key attributes and be SAMA-checked, and internal-model (IMA) eligibility is granted desk-by-desk. Conclude that trading-book capital treatment and any model approval depend on a compliant, SAMA-approved desk structure; a bank cannot claim IMA or clean market-risk treatment without demonstrating its desk definitions satisfy [4.7].
- **Grounding — this node (Page 379 / 5.18):** "within the trading book (between different desks)"
- **Grounding — related node (Page 370 / 4.7(1)):** "A trading desk for the purposes of the regulatory capital charge is an unambiguously defined group of traders or trading accounts."

#graphify/concept #graphify/EXTRACTED #community/Trading_Book_Policy #graphify/enriched
