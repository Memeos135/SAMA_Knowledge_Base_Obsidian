---
source_file: "markdown/SAMA_EN_3726_VER1.md"
type: "concept"
community: "Aggregation Business Continuity"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Cyber Security Operations and Technology

## Connections

### [[Cyber Security Event Management]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping operational cyber controls, read event management as part of the operations-and-technology domain of the SAMA Cyber Security Framework, not a separate obligation set: both are subdomains addressed to Member Organizations and share the same governance chain (board responsibility, CISO-maintained standards, defined/approved/implemented controls). The policy expressly requires that cyber security breaches and suspected weaknesses are reported and reflected in ongoing management, which is where event management sits within the technology domain. For a compliance decision, conclude that event-management controls must be aligned with the general operations/technology standards; verify the specific control considerations in the primary text since the framework uses maturity-based 'should' language.
- **Grounding — this node (Page 16):** "ensuring that standards, processes and procedures reflect security requirements (if applicable)"
- **Grounding — related node (Page 15 / 3.1.3(f)(7)):** "cyber security breaches and suspected cyber security weaknesses are reported"
- **Caveat:** Node contexts share the same framing pages; the discrete event-management clauses are not shown here, so confirm against the relevant subdomain section.

### [[Cyber Security Incident Management]] — `references` [EXTRACTED]
- **What this link tells you:** For incident-response obligations, treat incident management as nested within the operations-and-technology control domain of the same SAMA Cyber Security Framework rather than as a freestanding regime: both bind Member Organizations and flow from the same governance structure (board ultimate responsibility, senior management ensuring standards/procedures reflect security requirements). The policy's requirement that breaches be reported and that cyber security feature in business continuity underpins the incident-management function within that domain. In a compliance review, conclude incident-management controls should conform to the general operations/technology standards and be defined, approved and implemented; verify the precise incident-management clauses in the primary text because the framework is maturity-graded rather than absolute.
- **Grounding — this node (Page 16):** "ensuring that standards, processes and procedures reflect security requirements"
- **Grounding — related node (Page 15 / 3.1.3(f)(7)-(8)):** "cyber security breaches and suspected cyber security weaknesses are reported ... reflected in business continuity management"
- **Caveat:** Shared framing pages only; the specific incident-management section text is not provided, so confirm directly before relying on scope.

### [[Electronic Banking Services Security]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping obligations under the SAMA Cyber Security Framework, treat electronic banking security as a subset of the broader operations-and-technology control domain rather than a standalone regime: both are subdomains of the same Framework applicable to Member Organizations, and controls defined for the technology environment (policy, standards, procedures, roles) cascade into the electronic-banking channel. For a compliance decision, this means you should not assess e-banking controls in isolation but confirm they inherit and satisfy the general operations/technology control considerations. Note the framework is expressed in 'should' control considerations against a maturity model, so verify the specific control clauses in the primary text before treating any single item as a discrete requirement.
- **Grounding — this node (Page 16):** "ensuring that standards, processes and procedures reflect security requirements ... cyber security architecture"
- **Grounding — related node (Page 15 / 3.1.4):** "the reference to supporting cyber security standards and procedures ... cyber security requirements that ensure ... information is protected"
- **Caveat:** Both nodes derive from the same document's shared framing pages; the specific electronic-banking vs operations-technology control text is not fully shown, so confirm the sub-domain clauses directly.

### [[Payment Systems Security]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing payment-systems security, read it as an application of the operations-and-technology control domain within the same SAMA Cyber Security Framework, so payment infrastructure inherits the general technology controls (architecture, standards, procedures, information protection) plus any payment-specific controls. Both subdomains apply to Member Organizations and share the same governance chain, meaning payment-system controls should not be evaluated against a lighter standard than the wider technology environment. For a compliance decision, confirm payment-systems controls satisfy both the general operations/technology considerations and the dedicated payment provisions; check the primary text for the payment-specific clauses since only the shared framing pages are shown here.
- **Grounding — this node (Page 16):** "developing and maintaining ... cyber security architecture ... standards, processes and procedures reflect security requirements"
- **Grounding — related node (Page 15 / 3.1.3(f)(2)):** "information is protected in terms of cyber security requirements, in line with the risk appetite"
- **Caveat:** The distinct payment-systems security clauses are not present in the provided context; verify the dedicated subdomain section before relying on scope.

### [[SAMA Cyber Security Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which cyber security controls apply to a Member Organization's systems and delivery channels, treat 'Operations and Technology' as one of the Framework's substantive control domains that sits under the same governance and risk-treatment structure, so operational/technical controls must still trace back to defined ownership, documented risk treatment, and board-level accountability. The Framework binds risk acceptance to business-owner sign-off and prohibits accepting risks that contradict SAMA regulations, meaning technology controls cannot be waived on operational convenience alone. Conclude that operational/technology control deficiencies should be evaluated as Framework non-compliance with a required risk-treatment and approval trail.
- **Grounding — this node (Page 21 (risk response/treatment control considerations)):** "accepting, avoiding, transferring or mitigating risks by applying cyber security controls"
- **Grounding — related node (Page 21):** "the accepted cyber security risk does not contradict SAMA regulations"
- **Caveat:** The provided context does not include the full text of the Operations and Technology subdomain; its scope is inferred from the Framework's shared governance/risk-treatment structure — confirm specific controls against the relevant Framework section.

### [[Threat Management]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping technical defence obligations, treat threat management (threat intelligence and vulnerability management) as part of the operations-and-technology domain of the SAMA Cyber Security Framework, feeding the technology function with intelligence to inform controls and risk response. The threat-intelligence process expressly draws on internal technology sources (logs, IDS/IPS, SIEM) and external sources including SAMA, and channels output to SOC and risk management — linking it directly to operational technology controls. For a compliance decision, conclude that threat-management processes must be defined, approved and implemented and integrated with the wider operations/technology and risk-management controls, and that intelligence-sharing with SAMA is an expected element; verify the specific control considerations (sections 3.3.16-3.3.17) in the primary text.
- **Grounding — this node (Page 16):** "cyber security risk management process ... standards, processes and procedures reflect security requirements"
- **Grounding — related node (Page 35 / 3.3 Threat Management):** "the use of internal sources, such as ... IDS, IPS ... SIEM ... external sources, such as SAMA ... sharing the relevant intelligence"

### [[Vulnerability Management]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping a Member Organization's obligations under the SAMA Cyber Security Framework, treat vulnerability management as a required sub-control within the broader Operations and Technology domain (3.3), not an optional add-on. The Framework mandates a defined, approved and implemented vulnerability management process whose effectiveness must be measured and periodically evaluated — the same 'define, approve, implement, measure' obligation pattern that runs through the operations domain. A reviewer assessing maturity against domain 3.3 should therefore check that application and infrastructure vulnerability identification and mitigation are documented and evidenced, since a gap here counts as a deficiency in the parent operations-and-technology domain.
- **Grounding — this node (Page 4 / section 3.3):** "3.3 Cyber Security Operations and Technology ... 3.3.4 Cyber Security Architecture"
- **Grounding — related node (Page 35 / 3.3.17):** "should define, approve and implement a vulnerability management process for the identification and mitigation of application and infrastructural vulnerabilities"

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
