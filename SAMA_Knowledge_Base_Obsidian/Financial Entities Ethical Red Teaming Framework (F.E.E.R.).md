---
source_file: "markdown/SAMA_EN_2898_VER1.md"
type: "document"
community: "Ethical Red Teaming"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Ethical_Red_Teaming
  - graphify/enriched
---

# Financial Entities Ethical Red Teaming Framework (F.E.E.R.)

## Connections

### [[Blue Team]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a Member Organization's obligations under the F.E.E.R. red teaming regime, treat the Blue Team as a defined role whose detection/response performance is the actual object being tested, not a peripheral participant. The Framework defines the Blue Team as the cyber security monitoring team (e.g. SOC) tasked with detecting the Red Team's malicious activities and following incident response procedures, and its detection events directly govern whether a test continues or is adjusted. For compliance scoping you should conclude that the Framework's resilience assessment turns on Blue Team capability, and that the Blue Team is intentionally kept unaware of the test to preserve realism — so obligations around test control fall on the White/Green Teams, not the Blue Team.
- **Grounding — this node (Page 4):** "The Financial Entities Ethical Red Teaming Framework (F.E.E.R.) is intended as a guide for Member Organizations within Saudi Arabia in preparing and executing controlled attacks"
- **Grounding — related node (Page 7):** "The cyber security monitoring team of the Member Organization (e.g. SOC)... It is the task of the Blue Team to detect the malicious activities (of the Red Team)"

### [[Cyber Kill Chain Methodology]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing what a red teaming exercise under F.E.E.R. must actually cover, use the Cyber Kill Chain as the conceptual model the Framework adopts to structure and report the simulated attack. The Framework describes the seven-stage kill chain as the end-to-end attacker process and requires the Red Team Evaluation Report to explain the exploited kill chains and the associated TTPs. For compliance you would conclude that a deliverable lacking a Cyber Kill Chain / TTP explanation is incomplete against the Framework's reporting expectations, and that the methodology defines the analytical scope of the test rather than being optional.
- **Grounding — this node (Page 22):** "Explanation of the Cyber Kill Chain methodology and Tactics, Techniques and Procedures that were planned and eventually executed"
- **Grounding — related node (Page 8):** "The Cyber Kill Chain provides a conceptual model to describe an attack... seven (7) stages characterize an advanced cyber-attack in the cyber kill chain"

### [[Green Team]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping who holds authority in a F.E.E.R. exercise, note that the Green Team is SAMA's own supervisory arm and sits at the top of the control chain — not a Member Organization function. The Framework provides that SAMA's IT Risk of Financial Sector Supervision department supplies the Green Team, appoints the Test Manager, and must approve the selection of the Red Teaming Provider before procurement can begin. For compliance you should conclude that key gating steps (provider approval, threat-intelligence provision, test initiation) are SAMA-controlled, so a Member Organization cannot unilaterally procure or scope a test without Green Team involvement.
- **Grounding — this node (Page 7):** "SAMA IT Risk of Financial Sector Supervision department provides the Green Team. The Green Team appoints the Test Manager... approves the selection of Red Teaming Provider"
- **Grounding — related node (Page 11):** "Upon approval of the Red Teaming Provider by the Green Team, the Member Organization should initiate their procurement process"

### [[Penetration Testing]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a Member Organization's existing testing satisfies F.E.E.R., do not treat a penetration test as equivalent to red teaming — the Framework expressly distinguishes them by goal, scope, techniques and recurrence. F.E.E.R. defines penetration testing as targeting a predefined subset of assets with a focus on preventive controls, whereas red teaming replicates a realistic attack against the entire organization with a focus on detection and response. For compliance you should conclude that prior penetration-test evidence does not discharge red teaming obligations, and that the two produce different assurance about resilience.
- **Grounding — this node (Page 4 / 2.6):** "Red Teaming is not a penetration test... it focuses on replicating a targeted and realistic attack against the entire Member Organization"
- **Grounding — related node (Page 26 / Appendix C):** "Penetration testing often involves issuing real attacks on real systems and data... looking for combinations of vulnerabilities on a single system or multiple systems"

### [[Red Team]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying who conducts the simulated attack under F.E.E.R., recognise the Red Team (the certified external Red Teaming Provider's staff) as the actor executing the controlled cyber-attack, subject to Green Team approval and contractual controls (NDA, liability, Letter of Authorization). The Framework has the Red Teaming Provider use the latest TTPs to compromise the organization, with its team introduced to the White and Green Teams during procurement. For compliance you should conclude that Red Team engagement requires the LOA/NDA and provider-vetting steps in Appendix A, and that liability for test consequences must be contractually allocated before execution.
- **Grounding — this node (Page 4):** "The Red Teaming Provider will use the latest attack tactics, techniques and procedures (i.e. TTPs) in an attempt to compromise the Member Organization"
- **Grounding — related node (Page 11 / 3.5):** "Agreeing on contractual considerations, e.g. Non-Disclosure Agreement (NDA) clauses, the liability for any consequence flowing from the test, and a Letter of Authorization (LOA)"

### [[White Team]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing who bears responsibility for a controlled red teaming exercise under F.E.E.R., treat the White Team as the Member Organization's mandated internal owner, not the framework's SAMA-side actors. The Framework requires each Member Organization to establish and formalize a White Team (including a White Team Leader) to facilitate, oversee and control the exercise across all phases, and it is the White Team that procures the Red Teaming Provider under the Appendix A requirements. For a compliance decision, this means accountability for controlled execution, contracting (NDA, LOA, liability) and scope stays with the tested institution — the White Team is where you look to confirm the exercise was run in a controlled manner.
- **Grounding — this node (Page 4 / Section 1.1):** "F.E.E.R. is intended as a guide for Member Organizations ... in preparing and executing controlled attacks ... with the help of certified and experienced Red Teaming Providers"
- **Grounding — related node (Page 11 / Section 3.4):** "The Member Organization should carefully establish a White Team and nominate a White Team Leader in order to facilitate, oversee and lead the red teaming exercises during all phases"

#graphify/document #graphify/EXTRACTED #community/Ethical_Red_Teaming #graphify/enriched
