---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Default Risk Capital"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Default_Risk_Capital
  - graphify/enriched
---

# Jump-to-Default (JTD) Risk

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what the DRC requirement is meant to capture, read it as the charge for jump-to-default (JTD) risk — the loss from a sudden default that the sensitivities-based method's credit spread shocks do not capture. The framework states DRC 'is intended to capture jump-to-default (JTD) risk' and the calculation is built on gross and net JTD positions per obligor. For a capital decision, this means DRC and JTD are not independent charges: JTD is the underlying exposure measure that drives the DRC number, so verify the JTD computation before relying on any DRC output.
- **Grounding — this node (SAMA_EN_3553 / Page 6 (Definitions)):** "The risk of a sudden default. JTD exposure refers to the loss that could be incurred from a JTD event."
- **Grounding — related node (SAMA_EN_3553 / Page 73, [8.1]):** "The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks"

### [[Gross JTD Risk Position]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the DRC requirement, treat 'gross JTD risk position' as the first computational step that operationalises the broader JTD (jump-to-default) risk concept. In the same SAMA framework, [8.1] defines DRC as capturing JTD risk, and [8.3] prescribes that the gross JTD of each exposure is computed first, before offsetting into net JTD and bucketing. Conclude that gross JTD is a defined input within the JTD-risk regime, so the general JTD definition ([Page 6]) governs its meaning while [8.9]+ governs its measurement — apply both when determining the capital charge.
- **Grounding — this node (Page 73 / 8.1):** "The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks"
- **Grounding — related node (Page 73 / 8.3(1)):** "The gross JTD risk of each exposure is computed separately."

#graphify/document #graphify/EXTRACTED #community/Default_Risk_Capital #graphify/enriched
