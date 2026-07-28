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

# Fraud Detection Systems

## Connections

### [[Detect Domain]] — `references` [EXTRACTED]
- **Why:** The Detect domain is defined as the organisational capability whose primary operational expression is Fraud Detection Systems; the domain's standards mandate that Member Organisations define, implement, and maintain the systems and technology used to detect fraud, making Fraud Detection Systems the principal technical instrument of the Detect domain.
- **This node (Page 46 / §5.1g):** "Fraud detection standards should include at a minimum: [...] 4. Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."
- **Related node (Page 45 / §5):** "Fraud detection systems and controls are risk-based measures to identify fraud by looking for indicators in customer behaviours, transactional and non-transactional information. [...] Detective controls [...] typically [...] rely on technology to perform automated monitoring."
- **Implication:** Member Organisations must maintain documented fraud detection standards that specify each system or technology deployed, its data sources, calibration methodology, and rationale for adequacy relative to identified fraud risks — all subject to periodic effectiveness measurement and examiner review.

### [[Fraud Risk Assessment]] — `references` [EXTRACTED]
- **Why:** The Framework explicitly requires that fraud detection standards be aligned to, and their focus determined by, the output of the Fraud Risk Assessment, making the Assessment the risk-based input that calibrates detection system design, thresholds, and scope.
- **This node (Page 45 / Section 5.1, Control Requirement e):** "The output of the Fraud Risk Assessment should be used to determine where detection activity is focused, and controls should be proportionate to the risk appetite of the organisation."
- **Related node (Page 28 / Section 4.1.2):** "Member Organisations should conduct a Fraud Risk Assessment to identify fraud risks to which they or their customers are subject and assess the effectiveness of controls in place to mitigate the risks."
- **Implication:** Detection system configuration (alert thresholds, monitored data sources, ML model scope) must be traceable to documented Fraud Risk Assessment outputs; any material change to the risk assessment must trigger a review and update of detection standards.

### [[Intelligence Monitoring]] — `references` [EXTRACTED]
- **Why:** Fraud Detection Systems explicitly feed outputs into the Intelligence Monitoring process: detected fraud typologies are listed as a mandatory minimum intelligence source, and Intelligence Monitoring findings must loop back to periodically recalibrate detection scenarios and parameters.
- **This node (Page 46 / Section 5.1.g):** "Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."
- **Related node (Page 49 / Section 5 (tuning requirements)):** "Periodically review scenarios and parameters to ensure they remain appropriate in view of the insights gathered in Intelligence Monitoring and/or the outcome of the Fraud Risk Assessment."
- **Implication:** A RegTech architecture must implement a documented feedback loop where alert/detection outputs are ingested as structured intelligence inputs, and Intelligence Monitoring findings trigger scenario recalibration with an auditable change-log.

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
