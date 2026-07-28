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

# Internal Models Approach (IMA)

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may keep using its internal models for market risk capital, treat backtesting not as an optional diagnostic but as a condition of continued IMA eligibility, because the framework mandates ongoing backtesting of both trading-desk and bank-wide internal models and ties SAMA responses (add-ons, multiplier increases, or model disallowance) directly to backtesting outcomes. The 'green/amber/red zone' regime and the one-year backtesting report required for SAMA model approval make backtesting the mechanism by which IMA use is validated and priced. Conclude that a compliance assessment of IMA status must confirm the bank runs, documents, and explains all backtesting exceptions — failure exposes the bank to a backtesting add-on or loss of model approval.
- **Grounding — this node (Page 92 / 10.7):** "The bank must also conduct regular backtesting of its bank-wide internal models used for determining market risk capital requirements."
- **Grounding — related node (Page 111 / 12.14-12.15):** "in the case of severe problems with the basic integrity of the model, SAMA may consider whether to disallow the bank's use of the model for market risk capital requirement purposes altogether"

### [[DRC Requirement Internal Model]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping what a bank must build and validate to run the IMA, do not treat the default risk charge (DRC) internal model as a standalone product — it is one of the internal models that must be independently validated at least annually under the IMA qualitative criteria before SAMA will permit its use for capital purposes. The framework requires that all internal models used to determine market risk capital, including the DRC model, satisfy the [10.5]–[10.16] qualitative evaluation and obtain SAMA model approval. Conclude that DRC-model outputs cannot be relied upon for regulatory capital unless the DRC model itself has passed the IMA validation and approval gates that govern the broader internal-models regime.
- **Grounding — this node (Page 11 / 3.9):** "internal models approach (IMA) for market risk as described in [10] to [13]. SAMA approval is required before using the IMA approach."
- **Grounding — related node (Page 92 / 10.8):** "The model validation unit must validate all internal models used for purposes of the IMA on at least an annual basis."

### [[Expected Shortfall (ES)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how IMA capital is actually calculated, recognise that the IMA is not VaR-based at the capital-requirement level: the framework states the internal models approach capital calculation is built on Expected Shortfall (ES) techniques, so ES is the core measure a bank's IMA model must produce. This distinction matters because VaR still governs the backtesting comparison while ES drives the capital number. Conclude that any review of an IMA capital figure must confirm the ES model meets the minimum standards in chapter 13, and must not assume the capital charge is derived from the VaR used for backtesting.
- **Grounding — this node (Page 11 / 3.9):** "internal models approach (IMA) for market risk as described in [10] to [13]. SAMA approval is required before using the IMA approach."
- **Grounding — related node (Page 118 / Section 13):** "The internal models approach is based on the use Expected Shortfall (ES) techniques."

### [[Minimum Capital Requirements for Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which capital methodology a bank may use for market risk, treat the IMA not as a free choice but as a conditional exception to the default Standardised Approach within the Market Risk framework. The framework requires all banks to compute the standardised charge and makes IMA use contingent on prior SAMA approval, per-trading-desk nomination, and qualitative and backtesting criteria; desks not approved must fall back to the standardised approach. Conclude that reliance on internal models is only defensible for specifically approved, nominated desks, and the standardised calculation remains a mandatory baseline.
- **Grounding — this node (Page 90 / 10.4):** "The bank must nominate individual trading desks ... for which the bank seeks model approval in order to use the internal models approach (IMA)."
- **Grounding — related node (Page 11 / 3.9):** "a bank may choose between two broad methodologies: the standardised approach ... and internal models approach (IMA) ... SAMA approval is required before using the IMA approach."

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating whether a given trading desk may remain in-scope for the IMA, treat the P&L Attribution (PLA) test as a gating requirement operating alongside backtesting, because a desk in the PLA amber zone is subject to a capital surcharge and can only return to green after producing green-zone outcomes and satisfying its backtesting exceptions requirements. The framework requires PLA assessments at desk level and a one-year PLA report for SAMA model approval, and updates the backtesting portfolio scope quarterly based on PLA results. Conclude that IMA desk eligibility must be checked against both PLA and backtesting status — a passing backtest alone does not keep a desk in-scope if it fails PLA.
- **Grounding — this node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level."
- **Grounding — related node (Page 118 / 12.44):** "If a trading desk is in the PLA test amber zone, it is not considered an out-of-scope trading desk for use of the IMA."

### [[SAMA (Supervisory Authority)]] — `references` [EXTRACTED]
- **What this link tells you:** When advising a bank on whether it can adopt or continue the IMA, treat SAMA prior approval as a hard precondition, not a formality — the framework expressly requires SAMA approval before IMA use and empowers SAMA to insist on live testing, impose backtesting add-ons and multiplier increases, or disallow the model outright. This supervisory authority is grounded in the Central Bank Law (Royal Decree M/36) and the Banking Control Law under which the framework is issued. Conclude that IMA status is at all times contingent on SAMA consent and ongoing oversight; a bank cannot self-certify eligibility, and any capital benefit from the IMA is revocable by the supervisor.
- **Grounding — this node (Page 11 / 3.9):** "SAMA approval is required before using the IMA approach. ... The use of the simplified alternative is subject to SAMA approval and oversight."
- **Grounding — related node (Page 4 / Section 1):** "issued by SAMA in exercise of the authority vested in SAMA under the Central Bank Law issued via Royal Decree No. M/36 ... and the Banking Control Law"

### [[Standardized Approach]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When deciding market-risk capital methodology, treat the Standardized Approach and the Internal Models Approach (IMA) as the two mutually-exclusive alternatives SAMA permits per trading desk, with IMA requiring prior SAMA approval and the standardized approach as the mandatory fallback. Under SAMA_EN_3553, out-of-scope desks 'must use the standardised approach,' and a bank may not exclude desks from IMA merely because the standardised charge is lower. Note the SA node quoted here is drawn from the credit-risk document, so verify that the standardized approach you are comparing against IMA is the market-risk standardized approach ([6]–[9]) before relying on this equivalence.
- **Grounding — this node (SAMA_EN_3553 Page 90 / 10.4):** "The bank must use the standardised approach to determine the market risk capital requirements for trading desks that are out-of-scope for model approval."
- **Grounding — related node (SAMA_EN_3553 Page 11 / 3.9):** "a bank may choose between two broad methodologies: the standardised approach...and internal models approach (IMA) for market risk...SAMA approval is required before using the IMA approach."
- **Caveat:** The 'Standardized Approach' node excerpt is sourced from the credit-risk document (3487), while IMA is market-risk (3553); the meaningful relationship is with the market-risk standardised approach — confirm the intended framework before treating them as the paired alternatives.

### [[Stress Testing Programme]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank qualifies to use the Internal Models Approach for market risk capital, treat the stress testing programme as a mandatory qualitative condition, not an optional add-on. Para 10.19 makes a 'rigorous and comprehensive stress testing programme' at both trading-desk and bank-wide level a precondition for IMA use, sitting inside the same section [10] that defines IMA eligibility. You would conclude that IMA approval cannot be relied upon unless stress scenarios cover low-probability events across market, credit and operational risk and results are escalated to senior management and the board.
- **Grounding — this node (Page 11 / 3.9):** "internal models approach (IMA) for market risk as described in [10] to [13]. SAMA approval is required before using the IMA approach."
- **Grounding — related node (Page 96 / 10.19):** "Banks that use the IMA for determining market risk capital requirements must have in place a rigorous and comprehensive stress testing programme both at the trading desk level and at the bank-wide level."

#graphify/concept #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
