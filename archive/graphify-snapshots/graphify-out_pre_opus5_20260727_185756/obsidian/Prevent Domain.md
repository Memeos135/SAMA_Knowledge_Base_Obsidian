---
source_file: "markdown/SAMA_EN_2217_VER1.md"
type: "document"
community: "Counter-Fraud Framework"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Prevent Domain

## Connections

### [[Authentication Standard]] — `references` [EXTRACTED]
- **Why:** The Authentication Standard is explicitly enumerated as a required system/technology control within the Prevent Domain's fraud prevention standards, making it a named sub-component of the broader prevention control architecture rather than a merely co-occurring concept.
- **This node (Page 40 / Section 4.6 (Prevent Domain controls)):** "Systems and technology implemented to prevent fraud (e.g., identity and access management, authentication, issuance of one-time-passwords, biometrics)."
- **Related node (Page 37 / Section 4.4):** "Member Organisations should define, approve, implement and maintain a standard for the authentication of customer, employee and third party credentials and instructions to ensure information is protected and unauthorised access or actions are prevented."
- **Implication:** A SAMA examiner will expect the Authentication Standard to be documented, cross-referenced within the fraud prevention standards policy, and subject to periodic review aligned to the Fraud Risk Assessment — authentication controls must appear in both the cyber-security and counter-fraud control inventories.

### [[Counter-Fraud Framework]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Framework explicitly designates 'Prevent' as one of its four structural domains, with the Framework's control requirement numbering system, governance obligations, and Fraud Risk Assessment outputs all feeding directly into the Prevent domain's standards, thresholds, and control design obligations.
- **This node (Page 26):** "An effective Counter-Fraud Programme includes fraud prevention processes and controls to facilitate the identification of threats and mitigate the risk of fraud occurring... The Fraud Risk Management Framework should be defined, approved and implemented."
- **Related node (Page 9):** "The Framework is structured around four main domains, namely: Governance, Prevent, Detect, Respond. For each domain, several sub-domains are defined... the Framework states a Principle and related Control Requirements."
- **Implication:** Compliance teams must map each Prevent-domain control requirement (e.g., authentication, transaction limits, due diligence) back to the Fraud Risk Assessment output and Fraud Risk Appetite thresholds, with documented rationale that prevention controls are proportionate—an auditor will check this linkage explicitly.

### [[Due Diligence Standards]] — `references` [EXTRACTED]
- **Why:** Due Diligence Standards are explicitly listed as a mandated control category within the Prevent Domain's fraud prevention standards, serving as the primary mechanism for preventing establishment of fraudulent relationships with employees, customers and third parties before harm occurs.
- **This node (Page 40 / Section 4.6 (Prevent Domain controls)):** "The controls implemented to prevent fraud (e.g., segregation of duties, approval and escalations, employee training, access restrictions, due diligence and integrity checks, notification of account changes, transaction limits, underwriting checks)."
- **Related node (Page 31 / Section 4.2):** "Member Organisations should define, approve and implement standards for assessing the fraud risk associated with employees, customers and third parties to prevent the establishment of relationships outside risk appetite and manage fraud risks throughout the duration of the relat…"
- **Implication:** Due Diligence Standards must be versioned artefacts that are explicitly cross-referenced in the fraud prevention standards document, with evidence of periodic review, risk-based tiering for employees/customers/third parties, and outcomes fed back into the Fraud Risk Assessment cycle.

### [[Fraud Risk Appetite]] — `references` [EXTRACTED]
- **Why:** The Prevent domain's control requirements mandate that fraud prevention control thresholds and limits be set by reference to Fraud Risk Appetite, and the Fraud Risk Appetite itself must be formally defined, Board-endorsed, and monitored — creating a bidirectional dependency between prevention control calibration and appetite governance.
- **This node (Page 40 / §4 Prevent):** "Member Organisations should define the approach to setting limits and thresholds for preventive controls (where applicable) in fraud prevention standards, considering: [...] 3. Fraud Risk Appetite."
- **Related node (Page 30 / §4.1.3):** "The Fraud Risk Appetite of the Member Organisation should be defined to state the level of fraud risk the Member Organisation is willing to tolerate. [...] Fraud Risk Appetite should be reviewed on at least an annual basis and be formally endorsed by the Board."
- **Implication:** Prevention control thresholds (e.g., transaction limits, authentication step-up triggers) must be traceable to the documented Fraud Risk Appetite statement; any Board-approved appetite revision must trigger a review and update of corresponding preventive control parameters.

### [[Fraud Risk Assessment]] — `references` [EXTRACTED]
- **Why:** The Fraud Risk Assessment is the primary input that determines the focus, proportionality, limits and thresholds of all controls within the Prevent Domain, creating a mandatory feed from assessment outputs into prevention standard design and update cycles.
- **This node (Page 40 / Section 4.6 (Prevent Domain controls)):** "The output of the Fraud Risk Assessment should be used to determine where prevention activity is focused, and controls should be proportionate to the risk appetite of the organisation."
- **Related node (Page 28 / Section 4.1.2):** "Member Organisations should conduct a Fraud Risk Assessment to identify fraud risks to which they or their customers are subject and assess the effectiveness of controls in place to mitigate the risks."
- **Implication:** RegTech workflow must ensure that each refresh of the Fraud Risk Assessment triggers a documented review of fraud prevention standards, limits and thresholds, with a traceable audit trail linking residual risk ratings to specific preventive control updates or accepted risk decisions.

### [[Intelligence Monitoring]] — `references` [EXTRACTED]
- **Why:** Intelligence Monitoring is explicitly listed as a mandatory component of the Fraud Risk Management Framework within the Prevent domain; the Framework requires it to be addressed at a minimum alongside Fraud Risk Assessment, Fraud Risk Appetite, and KRIs, making it a structural sub-domain of Prevent.
- **This node (Page 26 / §4.1):** "The Fraud Risk Management Framework should address at a minimum: 1. Intelligence Monitoring. 2. Fraud Risk Assessment. 3. Fraud Risk Appetite. 4. Key Risk Indicators (KRIs)."
- **Related node (Page 27 / §4.1.1):** "The fraud Intelligence Monitoring process should be defined, approved, and implemented. [...] The Intelligence Monitoring process should include: Scanning, collation, analysis, assessment and dissemination of information on existing and emerging threats."
- **Implication:** Auditors should expect a documented, Board-approved Fraud Risk Management Framework that explicitly maps Intelligence Monitoring as a named sub-process with defined sources, dissemination paths (including to SAMA), and a periodic effectiveness evaluation cadence.

#graphify/document #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
