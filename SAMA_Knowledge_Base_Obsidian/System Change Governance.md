---
source_file: "markdown/SAMA_EN_11051_VER1.md"
type: "document"
community: "IT & Shariah Governance"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IT__Shariah_Governance
  - graphify/enriched
---

# System Change Governance

## Connections

### [[Patch Management]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the full System Change Management domain, note that Patch Management (3.4.9) is another distinct sub-domain governed by the same overarching change-governance principle, not a substitute for it. Change governance requires all changes be classified, tested and approved before production, while patch management adds a specific obligation to install applicable patches in a timely manner to close known vulnerabilities. Conclude that patch deployment must still flow through the change-governance controls (approval, CAB, cyber-security review) — a compliance reviewer should not treat patching as exempt from the change-approval chain.
- **Grounding — this node (Page 27 / 3.4.1):** "changes to the Member Organization's information assets are classified, tested and approved before their deployment into production environments"
- **Grounding — related node (Page 31 / 3.4.9):** "Patch management process should be defined and implemented to ensure up-to-date with latest applicable and relevant patches ... are installed in a timely manner"

### [[SAMA Cyber Security Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a Member Organization's change management controls are sufficient under this IT Governance Framework, do not treat the change-governance requirements as self-contained: the framework's System Change subdomain expressly defers change security to a separate, named SAMA instrument. Control Requirement 3.4.2(6) requires that changes be reviewed and approved by the cyber security function before submission to the CAB, and states this is 'required as per the SAMA Cyber Security Framework, 3.3.7 Change Management, Control Requirements, 4 — d.' For a compliance decision this means you must satisfy both instruments concurrently; approval under the IT Governance change process does not evidence cyber-security sign-off, which is sourced in the cross-referenced Cyber Security Framework provision.
- **Grounding — this node (Page 28 / 3.4.2):** "Any changes in the information assets should be reviewed and approved by the cyber security function before submitting to 'CAB' (required as per the SAMA Cyber Security Framework, 3.3.7 Change Management)."
- **Grounding — related node (Page 6-7 / 1.1-1.5):** "The framework is mandated by SAMA... The Member Organizations are responsible for implementing and complying with the framework."

### [[System Change Management]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When scoping a Member Organization's change-control obligations under this IT Governance Framework, treat System Change Governance as the mandatory sub-domain (3.4.1) sitting within the broader System Change Management process (3.4). The governance node states the enforceable principle — changes must be classified, tested and approved before deployment — and requires the process itself to be defined, approved, communicated and periodically evaluated. Conclude that satisfying System Change Management means implementing the governance controls as the top-level obligation, then the child controls (definition/approval, testing, release) that hang beneath it.
- **Grounding — this node (Page 27 / 3.4.1):** "A Change Management process should be established to ensure that changes to the Member Organization's information assets are classified, tested and approved before their deployment into production environments"
- **Grounding — related node (Page 27 / 3.4):** "System change management is a process of defining, designing, testing and implementing changes related to information assets"

#graphify/document #graphify/EXTRACTED #community/IT__Shariah_Governance #graphify/enriched
