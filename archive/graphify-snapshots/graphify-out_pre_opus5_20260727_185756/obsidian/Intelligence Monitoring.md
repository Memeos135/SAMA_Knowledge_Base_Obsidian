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

# Intelligence Monitoring

## Connections

### [[Fraud Detection Systems]] — `references` [EXTRACTED]
- **Why:** Fraud Detection Systems explicitly feed outputs into the Intelligence Monitoring process: detected fraud typologies are listed as a mandatory minimum intelligence source, and Intelligence Monitoring findings must loop back to periodically recalibrate detection scenarios and parameters.
- **This node (Page 49 / Section 5 (tuning requirements)):** "Periodically review scenarios and parameters to ensure they remain appropriate in view of the insights gathered in Intelligence Monitoring and/or the outcome of the Fraud Risk Assessment."
- **Related node (Page 46 / Section 5.1.g):** "Systems and technology implemented to detect potential fraud (e.g., fraud detection software, alerts on high-value events or transactions, access monitoring, link analysis)."
- **Implication:** A RegTech architecture must implement a documented feedback loop where alert/detection outputs are ingested as structured intelligence inputs, and Intelligence Monitoring findings trigger scenario recalibration with an auditable change-log.

### [[Prevent Domain]] — `references` [EXTRACTED]
- **Why:** Intelligence Monitoring is explicitly listed as a mandatory component of the Fraud Risk Management Framework within the Prevent domain; the Framework requires it to be addressed at a minimum alongside Fraud Risk Assessment, Fraud Risk Appetite, and KRIs, making it a structural sub-domain of Prevent.
- **This node (Page 27 / §4.1.1):** "The fraud Intelligence Monitoring process should be defined, approved, and implemented. [...] The Intelligence Monitoring process should include: Scanning, collation, analysis, assessment and dissemination of information on existing and emerging threats."
- **Related node (Page 26 / §4.1):** "The Fraud Risk Management Framework should address at a minimum: 1. Intelligence Monitoring. 2. Fraud Risk Assessment. 3. Fraud Risk Appetite. 4. Key Risk Indicators (KRIs)."
- **Implication:** Auditors should expect a documented, Board-approved Fraud Risk Management Framework that explicitly maps Intelligence Monitoring as a named sub-process with defined sources, dissemination paths (including to SAMA), and a periodic effectiveness evaluation cadence.

### [[Sectorial Anti-Fraud Committee]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Department — which hosts or coordinates the Sectorial Anti-Fraud Committee function — is explicitly required to share Counter-Fraud Intelligence with SAMA and other sector organisations, directly linking the Intelligence Monitoring output to the inter-organisational committee mechanism.
- **This node (Page 27 / Section 4.1.1.d.4):** "Sharing relevant intelligence with internal and external stakeholders (e.g., Cyber, Business Operations or SAMA)."
- **Related node (Page 20 / Section 4.1 Control Requirement a.5):** "Sharing Counter-Fraud Intelligence with SAMA and other organisations in the sector."
- **Implication:** Member Organisations must build an outbound intelligence-dissemination workflow — with defined classification, packaging, and dispatch controls — that can evidence timely sharing of fraud typologies and TTPs to SAMA and peer institutions via the sectorial committee channel.
- **Caveat:** The source context does not render a discrete 'Sectorial Anti-Fraud Committee' article; the node is inferred from the Counter-Fraud Department's sector-sharing obligation. Locator for node B is therefore the Counter-Fraud Department control requirement rather than a standalone committee article.

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
