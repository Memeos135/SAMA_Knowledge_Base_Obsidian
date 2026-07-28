---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Net Independent Collateral Amount (NICA)

## Connections

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining regulatory capital for margined derivatives under SA-CCR, you cannot treat NICA and Replacement Cost as separate inputs — NICA is an explicit term inside the RC formula. Under paragraph 6.20/6.21, RC = max{V − C; TH + MTA − NICA; 0}, so the net independent collateral posted by the counterparty (less unsegregated collateral the bank posted) directly reduces the exposure figure that feeds EAD. When validating an RC calculation, confirm NICA excludes segregated/bankruptcy-remote collateral the bank posted and correctly nets the IA differential, because misclassifying collateral changes the capital charge.
- **Grounding — this node (Page 23 / 6.19):** "net independent collateral amount (NICA), to describe the amount of collateral that a bank may use to offset its exposure on the default of the counterparty"
- **Grounding — related node (Page 24 / 6.21):** "TH + MTA – NICA represents the largest exposure that would not trigger a VM call ... NICA is subtracted from TH + MTA"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
