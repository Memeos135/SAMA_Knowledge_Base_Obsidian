---
source_file: "markdown/SAMA_EN_2898_VER1.md"
type: "concept"
community: "Ethical Red Teaming"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Ethical_Red_Teaming
  - graphify/enriched
---

# Blue Team

## Connections

### [[Blue Team Report (BTR)]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating the evidence outputs of a red teaming exercise, the Blue Team Report is the deliverable capturing the detection/response side and feeds directly into remediation. The Blue Team is the institution's monitoring function (e.g. SOC) tasked with detecting the Red Team's activity, and its report becomes one of the two inputs (with the Red Team Evaluation Report) on which the White Team bases the Remediation Plan. For a decision, this means you should look to the BTR to assess how well internal detection and incident response actually performed, and confirm its findings were carried into the remediation roadmap.
- **Grounding — this node (Page 7 / Section 2.2):** "It is the task of the Blue Team to detect the malicious activities (of the Red Team) and to follow the agreed incident response procedures the moment an incident is detected"
- **Grounding — related node (Page 24 / Remediation Plan (RP)):** "The White Team should draft a Remediation Plan, which should be based on the Red Teaming Evaluation Report and the Blue Team Report"
- **Caveat:** The BTR node's supplied context is largely OCR image-caption noise; its content and role are grounded from the surrounding RP and Blue Team text rather than a clean BTR definition. Verify the BTR reporting requirements in Appendix B of the primary document.

### [[Financial Entities Ethical Red Teaming Framework (F.E.E.R.)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a Member Organization's obligations under the F.E.E.R. red teaming regime, treat the Blue Team as a defined role whose detection/response performance is the actual object being tested, not a peripheral participant. The Framework defines the Blue Team as the cyber security monitoring team (e.g. SOC) tasked with detecting the Red Team's malicious activities and following incident response procedures, and its detection events directly govern whether a test continues or is adjusted. For compliance scoping you should conclude that the Framework's resilience assessment turns on Blue Team capability, and that the Blue Team is intentionally kept unaware of the test to preserve realism — so obligations around test control fall on the White/Green Teams, not the Blue Team.
- **Grounding — this node (Page 7):** "The cyber security monitoring team of the Member Organization (e.g. SOC)... It is the task of the Blue Team to detect the malicious activities (of the Red Team)"
- **Grounding — related node (Page 4):** "The Financial Entities Ethical Red Teaming Framework (F.E.E.R.) is intended as a guide for Member Organizations within Saudi Arabia in preparing and executing controlled attacks"

#graphify/concept #graphify/EXTRACTED #community/Ethical_Red_Teaming #graphify/enriched
