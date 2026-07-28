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

# Replacement Cost (RC)

## Connections

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing EAD under the SA-CCR, treat replacement cost as a defined component of the EAD formula, not a separate calculation: EAD equals alpha (1.4) times the sum of RC and PFE. The framework defines RC per paragraphs 6.5 to 6.21 and current exposure/RC as the loss that would occur on immediate counterparty default, and the EAD formula incorporates that RC directly. A reader should conclude that any EAD figure depends on a correctly derived RC (margined vs unmargined) and should trace the RC inputs before relying on the EAD output.
- **Grounding — this node (Page 19 / 6.5):** "For unmargined transactions, the RC intends to capture the loss that would occur if a counterparty were to default and were closed out of its transactions immediately."
- **Grounding — related node (Page 19 / 6.2):** "RC = the replacement cost calculated according to 6.5 to 6.21 ... EAD = alpha * (RC + PFE)"

### [[Margin Agreement  NICA|Margin Agreement / NICA]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating RC, first determine whether a margin agreement applies, because it changes the RC formula: margined netting sets use the max{V-C; TH+MTA-NICA; 0} formulation while unmargined sets use a simpler close-out measure. The framework classifies a netting set as margined only where the counterparty must post variation margin (one-way agreements where only the bank posts are treated as unmargined), and NICA feeds directly into the margined RC formula illustrated in the worked examples. A reader should conclude that RC and thus EAD turn on the correct characterization of the margin agreement and the NICA computation, and should check whether the agreement obliges the counterparty to post VM before applying the margined formula.
- **Grounding — this node (Page 142 / 13.1, 6.20):** "RC = max{V - C; TH + MTA - NICA; 0} ... relate to the formulation of replacement cost for margined trades."
- **Grounding — related node (Page 19 / 6.4):** "Margined netting sets are netting sets covered by a margin agreement under which the bank's counterparty has to post variation margin; all other netting sets ... are treated as unmargined."

### [[Net Independent Collateral Amount (NICA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining regulatory capital for margined derivatives under SA-CCR, you cannot treat NICA and Replacement Cost as separate inputs — NICA is an explicit term inside the RC formula. Under paragraph 6.20/6.21, RC = max{V − C; TH + MTA − NICA; 0}, so the net independent collateral posted by the counterparty (less unsegregated collateral the bank posted) directly reduces the exposure figure that feeds EAD. When validating an RC calculation, confirm NICA excludes segregated/bankruptcy-remote collateral the bank posted and correctly nets the IA differential, because misclassifying collateral changes the capital charge.
- **Grounding — this node (Page 24 / 6.21):** "TH + MTA – NICA represents the largest exposure that would not trigger a VM call ... NICA is subtracted from TH + MTA"
- **Grounding — related node (Page 23 / 6.19):** "net independent collateral amount (NICA), to describe the amount of collateral that a bank may use to offset its exposure on the default of the counterparty"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating SA-CCR EAD, replacement cost is one of its two defining inputs (EAD = alpha × (RC + PFE)) and must be computed differently for margined versus unmargined netting sets. For margined trades RC uses the formula RC = max{V − C; TH + MTA − NICA; 0} (6.20), where the third zero term prevents a negative RC and margin agreement terms (threshold, MTA, NICA) directly reduce or increase the figure. Practical consequence: confirm you have correctly classified each netting set as margined or unmargined — a one-way agreement where only the bank posts VM is treated as unmargined — and that collateral and independent amounts are fed into the correct RC term rather than double-counted.
- **Grounding — this node (Page 142 / 13.1):** "they relate to the formulation of replacement cost for margined trades, as set out in 6.20: RC = max{V − C; RH + MTA − MHXA; 0}"
- **Grounding — related node (Page 19 / 6.2-6.4):** "The replacement cost (RC) and the potential future exposure (PFE) components are calculated differently for margined and unmargined netting sets."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
