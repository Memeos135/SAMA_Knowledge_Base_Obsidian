---
source_file: "markdown/SAMA_EN_2217_VER1.md"
type: "concept"
community: "Counter-Fraud Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Fraud Risk Assessment

## Connections

### [[Fraud Detection Systems]] — `references` [EXTRACTED]
- **Why:** The Framework explicitly requires that fraud detection standards be aligned to, and their focus determined by, the output of the Fraud Risk Assessment, making the Assessment the risk-based input that calibrates detection system design, thresholds, and scope.
- **This node (Page 28 / Section 4.1.2):** "Member Organisations should conduct a Fraud Risk Assessment to identify fraud risks to which they or their customers are subject and assess the effectiveness of controls in place to mitigate the risks."
- **Related node (Page 45 / Section 5.1, Control Requirement e):** "The output of the Fraud Risk Assessment should be used to determine where detection activity is focused, and controls should be proportionate to the risk appetite of the organisation."
- **Implication:** Detection system configuration (alert thresholds, monitored data sources, ML model scope) must be traceable to documented Fraud Risk Assessment outputs; any material change to the risk assessment must trigger a review and update of detection standards.

### [[Fraud Risk Appetite]] — `references` [EXTRACTED]
- **Why:** The Framework mandates a direct dependency: Fraud Risk Appetite must be based on the outcome of the Fraud Risk Assessment, and KRIs monitoring appetite exposure must reference risks identified in that same Assessment, creating a required evidence chain from risk identification to tolerance calibration.
- **This node (Page 28 / Section 4.1.2, Control Requirement c.5):** "The development of action plans to address residual risk that is outside of risk appetite."
- **Related node (Page 30 / Section 4.1.3, Control Requirement b):** "The Member Organisation Fraud Risk Appetite should be based on the outcome of the Fraud Risk Assessment and aligned to the overall risk appetite of the organisation."
- **Implication:** Governance evidence must demonstrate a documented audit trail from Fraud Risk Assessment residual-risk outputs to Board-endorsed Fraud Risk Appetite thresholds, with KRI breach escalation procedures referencing specific appetite limits set through this cycle.

### [[Prevent Domain]] — `references` [EXTRACTED]
- **Why:** The Fraud Risk Assessment is the primary input that determines the focus, proportionality, limits and thresholds of all controls within the Prevent Domain, creating a mandatory feed from assessment outputs into prevention standard design and update cycles.
- **This node (Page 28 / Section 4.1.2):** "Member Organisations should conduct a Fraud Risk Assessment to identify fraud risks to which they or their customers are subject and assess the effectiveness of controls in place to mitigate the risks."
- **Related node (Page 40 / Section 4.6 (Prevent Domain controls)):** "The output of the Fraud Risk Assessment should be used to determine where prevention activity is focused, and controls should be proportionate to the risk appetite of the organisation."
- **Implication:** RegTech workflow must ensure that each refresh of the Fraud Risk Assessment triggers a documented review of fraud prevention standards, limits and thresholds, with a traceable audit trail linking residual risk ratings to specific preventive control updates or accepted risk decisions.

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
