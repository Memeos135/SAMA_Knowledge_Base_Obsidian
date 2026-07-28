---
source_file: "markdown/SAMA_EN_5888_VER1.md"
type: "concept"
community: "Cyber Security Governance"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Cyber_Security_Governance
  - graphify/enriched
---

# Electronic Banking Services Security

## Connections

### [[Cyber Security Operations and Technology]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping obligations under the SAMA Cyber Security Framework, treat electronic banking security as a subset of the broader operations-and-technology control domain rather than a standalone regime: both are subdomains of the same Framework applicable to Member Organizations, and controls defined for the technology environment (policy, standards, procedures, roles) cascade into the electronic-banking channel. For a compliance decision, this means you should not assess e-banking controls in isolation but confirm they inherit and satisfy the general operations/technology control considerations. Note the framework is expressed in 'should' control considerations against a maturity model, so verify the specific control clauses in the primary text before treating any single item as a discrete requirement.
- **Grounding — this node (Page 15 / 3.1.4):** "the reference to supporting cyber security standards and procedures ... cyber security requirements that ensure ... information is protected"
- **Grounding — related node (Page 16):** "ensuring that standards, processes and procedures reflect security requirements ... cyber security architecture"
- **Caveat:** Both nodes derive from the same document's shared framing pages; the specific electronic-banking vs operations-technology control text is not fully shown, so confirm the sub-domain clauses directly.

### [[Multi-Factor Authentication]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping controls for electronic banking services, MFA is not optional or generic — the framework makes it a mandatory component of the Electronic Banking Services Security requirement. Section 3.3 requires MFA at customer registration, for all electronic banking services, and for specified high-risk processes (sign-on, adding beneficiaries, high-risk transactions, password reset), with additional channel-separation and lockout rules. In assessing a Member Organization you would verify MFA is applied across each enumerated process, not merely offered as a feature, since partial coverage would fail these control considerations.
- **Grounding — this node (Page 32 / 3.3):** "multi-factor authentication should be implemented for all electronic banking services available to customers"
- **Grounding — related node (Page 32 / 3.3):** "multi-factor authentication should be implemented for the following processes: sign-on; adding or modifying beneficiaries ... high-risk transactions ... password reset"

#graphify/concept #graphify/EXTRACTED #community/Cyber_Security_Governance #graphify/enriched
