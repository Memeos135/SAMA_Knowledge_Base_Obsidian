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

# Multi-Factor Authentication

## Connections

### [[Electronic Banking Services Security]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping controls for electronic banking services, MFA is not optional or generic — the framework makes it a mandatory component of the Electronic Banking Services Security requirement. Section 3.3 requires MFA at customer registration, for all electronic banking services, and for specified high-risk processes (sign-on, adding beneficiaries, high-risk transactions, password reset), with additional channel-separation and lockout rules. In assessing a Member Organization you would verify MFA is applied across each enumerated process, not merely offered as a feature, since partial coverage would fail these control considerations.
- **Grounding — this node (Page 32 / 3.3):** "multi-factor authentication should be implemented for the following processes: sign-on; adding or modifying beneficiaries ... high-risk transactions ... password reset"
- **Grounding — related node (Page 32 / 3.3):** "multi-factor authentication should be implemented for all electronic banking services available to customers"

### [[Hard Token]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing whether an entity's electronic-banking authentication satisfies the SAMA Cyber Security Framework, treat a hard token as one of the authentication factors that may compose the required multi-factor mechanism, not as a standalone control. The glossary itself defines a hard token as a hardware device that, when combined with other measures, produces 'multi-factor authentication', and the Framework mandates MFA for registration, all e-banking services, and high-risk transactions. You would conclude that deploying a hard token alone does not discharge the MFA obligation unless it is combined with an additional factor and password-protected as the control considerations require.
- **Grounding — this node (Page 32 / 3.3.x Electronic Banking):** "multi-factor authentication should be implemented for all electronic banking services available to customers; ... the use of hard and soft tokens should be password protected"
- **Grounding — related node (Page 51 / Appendix F Glossary):** "Some hard tokens are used in combination with other security measures to further enhance security (known as multi-factor authentication)."

### [[SAMA Cyber Security Glossary]] — `references` [EXTRACTED]
- **What this link tells you:** When using this document to identify authentication obligations, note that MFA is a substantive control requirement carried within the framework, not merely a glossary term. The document mandates MFA for customer registration and all electronic banking services, with specified lockout, channel-separation and high-risk-transaction triggers. For compliance scoping, treat these as enforceable control considerations for Member Organizations and check each enumerated MFA process rather than assuming a single blanket MFA implementation suffices.
- **Grounding — this node (Page 32 / 3.3):** "multi-factor authentication should be used during the registration process for the customer in order to use of electronic banking services"
- **Grounding — related node (Page 15 / 3.1.4):** "the reference to supporting cyber security standards and procedures"

### [[Soft Token]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When evaluating MFA implementations, recognise that the Framework expressly contemplates soft tokens (alongside hard tokens) as an acceptable authentication factor, but subjects them to the same protection requirements. The e-banking control considerations state that 'the use of hard and soft tokens should be password protected', linking the soft-token concept directly to the MFA obligation. You would conclude that a soft-token-based MFA is permissible, but must be password-protected and combined with a second factor to meet the mandate — a bare soft token does not by itself satisfy the requirement.
- **Grounding — this node (Page 32 / Electronic Banking controls):** "the use of hard and soft tokens should be password protected"
- **Grounding — related node (Page 51 / Glossary (cross-ref)):** "multi-factor authentication ... See also 'Soft token'."

#graphify/concept #graphify/EXTRACTED #community/Cyber_Security_Governance #graphify/enriched
