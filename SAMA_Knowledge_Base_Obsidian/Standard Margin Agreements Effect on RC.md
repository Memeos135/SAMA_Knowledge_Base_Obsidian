---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Standard Margin Agreements Effect on RC

## Connections

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining counterparty credit risk EAD under SA-CCR, do not compute replacement cost the same way for every netting set: whether a margin agreement is in place is the switch that changes which RC formula applies. The margin-agreement provisions expressly drive the margined RC formula RC = max{V−C; TH+MTA−NICA; 0}, whereas unmargined sets use RC per 6.5–6.21 — both feeding EAD = 1.4 × (RC + PFE). Conclude that you must first classify each netting set as margined or unmargined, and confirm the specific margin terms (threshold, MTA, margin period of risk), because that classification materially changes the capital exposure figure.
- **Grounding — this node (Page 602 / 7.22):** "If the netting set is subject to a margin agreement and the internal model captures the effects of margining when estimating EE, the model's EE measure may be used directly"
- **Grounding — related node (Page 568 / 6.4):** "The replacement cost (RC) and the potential future exposure (PFE) components are calculated differently for margined and unmargined netting sets."

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining CCR capital treatment for a derivatives netting set, you must first classify it as margined or unmargined, because SA-CCR calculates the replacement cost (RC) and potential future exposure (PFE) components differently for each. The margin-agreement provisions define what makes a netting set 'margined' and impose supervisory floors on the margin period of risk (e.g. five business days for repo-style netting sets, higher floors above 5000 trades), which feed directly into the EAD formula EAD = alpha × (RC + PFE). Conclude that you cannot apply SA-CCR to a collateralised set without first verifying the margin-agreement terms (unilateral/bilateral, thresholds, minimum transfer amount, re-margining frequency) that drive the applicable floor.
- **Grounding — this node (Page 602 / para 7.24):** "a supervisory floor of five business days for netting sets consisting only of repo style transactions, and 10 business days for all other netting sets is imposed on the margin period of risk"
- **Grounding — related node (Page 568 / para 6.4):** "The replacement cost (RC) and the potential future exposure (PFE) components are calculated differently for margined and unmargined netting sets."

#graphify/document #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
