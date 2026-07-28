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

# Event of Default

## Connections

### [[Default Market Value]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying close-out exposure after a counterparty fails, read Default Market Value as the valuation mechanism that only becomes operative once an Event of Default has triggered an Early Termination Date. The enumerated Events of Default (insolvency, failure to perform, untrue representations, etc.) allow the non-Defaulting Party to designate early termination, at which point the Default Market Value of the Second Purchased or Equivalent Margin Securities is determined using dealer quotations or actual sale/purchase prices. You would conclude that no Default Market Value calculation is available absent a designated close-out, and would trace the specific default limb and termination notice before relying on any close-out figure.
- **Grounding — this node (Page 26 / para 12):** "If at any time an Event of Default has occurred and is continuing the non-Defaulting Party may... designate... an Early Termination Date"
- **Grounding — related node (Page 29 / para 12):** "the non-Defaulting Party may elect to treat as the Default Market Value of such Securities... the price quoted... by market makers"

### [[Exercise Notice]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing close-out rights under this SAMA repo/securities master agreement, read the Exercise Notice mechanism and the Event of Default regime together, because the definitions in the agreement make the valuation and settlement mechanics of an Exercise Notice shift once default and an Early Termination Date arise. The Exercise Notice provisions expressly cross-refer to Default Market Value where 'an Early Termination Date has occurred', tying the ordinary exercise-of-undertakings process to the default cascade in paragraph 12 and the non-Defaulting Party's Early Termination Date designation. For a party enforcing or contesting termination, conclude that the two clauses are not independent stages: an ongoing Event of Default changes which valuation standard and settlement obligations apply, so both must be checked before asserting rights on any Exercise Date.
- **Grounding — this node (Page 26):** "If at any time an Event of Default has occurred and is continuing the non-Defaulting Party may, by not more than 20 days' notice ... designate ... an Early Termination Date"
- **Grounding — related node (Page 19):** "the Exercising Party ... will be entitled to deliver to the Undertaking Party, on each Exercise Date, an Exercise Notice with respect to that Exercise Date"
- **Caveat:** Relation is 'conceptually_related_to'; the agreement links the two through the Default Market Value definition rather than a single direct cross-reference — verify paragraphs 5, 6 and 12 before relying on the interaction.

#graphify/concept #graphify/EXTRACTED #community/Default__Margin_Terms #graphify/enriched
