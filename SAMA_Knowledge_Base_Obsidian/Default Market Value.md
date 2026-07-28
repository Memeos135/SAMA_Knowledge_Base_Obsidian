---
source_file: "markdown/SAMA_EN_6073_VER1.md"
type: "concept"
community: "Default & Margin Terms"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default__Margin_Terms
  - graphify/enriched
---

# Default Market Value

## Connections

### [[Event of Default]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying close-out exposure after a counterparty fails, read Default Market Value as the valuation mechanism that only becomes operative once an Event of Default has triggered an Early Termination Date. The enumerated Events of Default (insolvency, failure to perform, untrue representations, etc.) allow the non-Defaulting Party to designate early termination, at which point the Default Market Value of the Second Purchased or Equivalent Margin Securities is determined using dealer quotations or actual sale/purchase prices. You would conclude that no Default Market Value calculation is available absent a designated close-out, and would trace the specific default limb and termination notice before relying on any close-out figure.
- **Grounding — this node (Page 29 / para 12):** "the non-Defaulting Party may elect to treat as the Default Market Value of such Securities... the price quoted... by market makers"
- **Grounding — related node (Page 26 / para 12):** "If at any time an Event of Default has occurred and is continuing the non-Defaulting Party may... designate... an Early Termination Date"

### [[Margin Maintenance]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating close-out amounts under this master agreement, treat Default Market Value and Margin Maintenance as parts of one exposure-and-valuation chain, because the Default Market Value provisions in paragraph 12 apply not only to Second Purchased Securities but expressly to 'Equivalent Margin Securities' delivered or receivable under the margin regime. Margin Maintenance (paragraph 6) governs Net Exposure, Margin Transfers and Cash/Margin Securities during the life of the transaction, and those same margin positions feed into the Deliverable/Receivable Securities that must be valued at default. For anyone quantifying a termination claim, conclude that outstanding margin balances are not settled separately from default valuation: unrepaid Cash Margin and undelivered Equivalent Margin Securities are valued and netted through the Default Market Value methodology.
- **Grounding — this node (Page 29):** "the amount of the Second Purchased Securities or Equivalent Margin Securities as the Default Market Value"
- **Grounding — related node (Page 20):** "If at any time either party has a Net Exposure in respect of the other party it may by notice ... require ... a Margin Transfer"

#graphify/concept #graphify/EXTRACTED #community/Default__Margin_Terms #graphify/enriched
