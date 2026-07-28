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

# Counter-Fraud Framework

## Connections

### [[Counter-Fraud Maturity Model]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Framework mandates measurement of Member Organisations' control implementation via the Counter-Fraud Maturity Model, making the model the primary assessment instrument embedded within and referenced by the Framework. Achieving higher maturity levels (3–5) is a sequential, criteria-gated progression that governs how the Framework's control requirements are evidenced and benchmarked.
- **This node (Page 11):** "The Counter-Fraud maturity level will be measured with the help of a predefined maturity model. The Counter-Fraud Maturity Model distinguishes 6 maturity levels (0, 1, 2, 3, 4 and 5)."
- **Related node (Page 13):** "To achieve maturity level 4, Member Organisations should periodically measure and evaluate the effectiveness of the Counter-Fraud controls implemented to achieve maturity level 3... Key Risk Indicators (KRIs) should be defined."
- **Implication:** A SAMA examiner will expect Member Organisations to maintain documented, time-stamped maturity assessments mapped to specific control requirements, with evidence trails showing sequential fulfilment of criteria for each level (0–5) including KPI/KRI records for levels 4 and 5.

### [[Cyber Security Framework]] — `references` [EXTRACTED]
- **Why:** _(enrichment pending)_

### [[Detect Domain]] — `references` [EXTRACTED]
- **Why:** The Detect Domain is one of the four mandated domains within the Counter-Fraud Framework structure; the Framework explicitly names Detect as a required domain and prescribes that each domain's Principles and Control Requirements must be implemented by Member Organisations.
- **This node (Page 9 / Section 2.1):** "The Framework is structured around four main domains, namely: Governance, Prevent, Detect, Respond. For each domain, several sub-domains are defined."
- **Related node (Page 45 / Section 5):** "Fraud detection systems and controls are risk-based measures to identify fraud by looking for indicators in customer behaviours, transactional and non-transactional information."
- **Implication:** A SAMA examiner will expect Member Organisations to evidence that fraud detection standards (covering data sources, system calibration, roles, and thresholds) are formally documented as part of the overarching Counter-Fraud Framework, with maturity-model scoring applied to each Detect sub-domain.

### [[Governance Domain]] — `references` [EXTRACTED]
- **Why:** The Governance Domain is the first and foundational domain of the Counter-Fraud Framework; the Framework explicitly positions Board and Executive Leadership accountability, the Counter-Fraud Governance Committee (CFGC), and the Counter-Fraud Programme as prerequisite structural requirements that enable all other domains.
- **This node (Page 9 / Section 2.1):** "The Framework is structured around four main domains, namely: Governance, Prevent, Detect, Respond… The Control Requirements reflect the mandated Counter-Fraud controls that should be considered by Member Organisations when designing and implementing a Counter-Fraud Programme."
- **Related node (Page 14 / Section 3):** "The Board and Executive Leadership of the Member Organisation is ultimately responsible for creation of a Counter-Fraud Programme; providing leadership and direction; and projecting a Counter-Fraud culture inside and outside the organisation."
- **Implication:** Compliance officers must ensure that CFGC establishment, Board endorsement of the Counter-Fraud Strategy/Policy/Risk Appetite, and appointment of a Head of Counter-Fraud are evidenced before the organisation can claim any maturity level above 0 in any Framework domain.

### [[PreauthorizationNotification POS Fraud Circular|Preauthorization/Notification POS Fraud Circular]] — `references` [EXTRACTED]
- **Why:** The Preauthorization/Notification POS Fraud Circular explicitly cross-references the Counter-Fraud Framework (issued under SAMA circular No. 501011), requiring acquiring service providers to comply with it; the Framework thus sets the minimum control standards that the circular operationalises for preauthorization fraud scenarios.
- **This node (Page 20 / Section 3.5):** "Proactively and reactively tuning Counter-Fraud systems... developing Fraud Monitoring & Detection System capabilities."
- **Related node (Page 1):** "مع التأكيد على الالتزام التام بدليل مكافحة الاحتيال المالي المبلغ بموجب تعميم البنك المركزي رقم ٥٠١٠١١ [with full commitment to the Counter-Fraud Guide issued under SAMA circular No. 501011]"
- **Implication:** Acquiring service providers must map their preauthorization transaction monitoring and detection controls explicitly to the Counter-Fraud Framework's maturity requirements, and document this linkage to demonstrate compliance with both instruments to SAMA examiners.
- **Caveat:** The Arabic circular references circular No. 501011 as the Counter-Fraud Guide; confirmation that SAMA_EN_2217_VER1 corresponds to that circular number relies on contextual inference rather than an explicit identifier visible in the English document.

### [[Prevent Domain]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Framework explicitly designates 'Prevent' as one of its four structural domains, with the Framework's control requirement numbering system, governance obligations, and Fraud Risk Assessment outputs all feeding directly into the Prevent domain's standards, thresholds, and control design obligations.
- **This node (Page 9):** "The Framework is structured around four main domains, namely: Governance, Prevent, Detect, Respond. For each domain, several sub-domains are defined... the Framework states a Principle and related Control Requirements."
- **Related node (Page 26):** "An effective Counter-Fraud Programme includes fraud prevention processes and controls to facilitate the identification of threats and mitigate the risk of fraud occurring... The Fraud Risk Management Framework should be defined, approved and implemented."
- **Implication:** Compliance teams must map each Prevent-domain control requirement (e.g., authentication, transaction limits, due diligence) back to the Fraud Risk Assessment output and Fraud Risk Appetite thresholds, with documented rationale that prevention controls are proportionate—an auditor will check this linkage explicitly.

### [[Respond Domain]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Framework designates 'Respond' as the fourth structural domain and requires the Head of Counter-Fraud to develop systems to 'prevent, detect and respond to fraud', making the Fraud Response Plan an obligatory component of the Framework's overall programme architecture.
- **This node (Page 18):** "Developing a risk-based Counter-Fraud Programme that addresses people, process, and technology, including adequate systems to prevent, detect and respond to fraud."
- **Related node (Page 51):** "A timely and effective response to incidents of actual or suspected fraud is key to minimising losses... Member Organisations should define, approve, implement and maintain a Fraud Response Plan to outline the organisational response to an actual or suspected fraud incident."
- **Implication:** The Fraud Response Plan must be formally approved, aligned with enterprise incident management, and its compliance monitored, meaning RegTech systems should capture case timestamps, escalation decisions, and resolution outcomes to evidence prompt and competent response as required by the Framework.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Framework is issued by SAMA and imposes obligations on Member Organisations, with SAMA retaining supervisory roles including receiving intelligence, notifications of new fraud typologies, and overseeing compliance via maturity assessments. The document's authority flows directly from SAMA's regulatory mandate.
- **This node (Page 20 / Section 3.5):** "Sharing Counter-Fraud Intelligence with SAMA and other organisations in the sector."
- **Related node (Page 3):** "Counter-Fraud Framework, Saudi Central Bank, October 2022, Version 1.0"
- **Implication:** Member Organisations must build a structured channel (e.g., supervisory notification workflow) to transmit fraud intelligence and new typology alerts to SAMA, evidencing this as a documented, recurring process subject to examiner review.

#graphify/document #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
