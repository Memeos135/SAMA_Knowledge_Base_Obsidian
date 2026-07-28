---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "IRB Credit Risk Approach"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Supervisory Slotting Approach

## Connections

### [[Expected Loss and Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** If you are mapping which capital regime governs a given exposure, treat operational-risk loss provisioning and the supervisory slotting approach as distinct components of the same Basel/SCRE-derived capital framework rather than interchangeable methods. The linked material sits within one SAMA capital rulebook: operational-risk loss data feeds the operational-risk capital calculation, while supervisory slotting (SCRE13) produces credit-risk RWA reported separately in the OV1 template. Conclude that provisioning inputs for operational losses do not migrate into the slotting credit-risk numbers; verify the SCRE13 cross-reference before attributing any exposure's RWA to the slotting approach.
- **Grounding — this node (Page 751):** "Of which: supervisory slotting approach: RWA and capital requirements according to the supervisory slotting approach (as specified in SCRE13)."
- **Grounding — related node (Page 540):** "Operational loss events related to credit risk and that are accounted for in credit risk RWAs should not be included in the loss data set."
- **Caveat:** The 'references' link is thin — the two topics co-occur in the same capital rulebook but no direct textual cross-reference between them is shown; confirm against SCRE13 and the operational-risk sections.

### [[Project Finance (PF)]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding how a specialized-lending project finance exposure is capitalised, note that project finance is a defined SL sub-class whose RWA — where no eligible external rating exists — is derived through the supervisory slotting approach, which the disclosure templates locate in the IRB family under SCRE13. The project finance provisions set the risk weights (130% pre-operational, 100%/80% operational) and the 'high quality' conditions that feed the slotting categorisation, while the slotting node confirms slotting is reported separately from F-IRB/A-IRB. Conclude that PF capital treatment must be traced through the slotting criteria rather than assumed to follow ordinary corporate IRB, and that its RWA is disclosed in the dedicated supervisory-slotting row.
- **Grounding — this node (Page 751 / row 4):** "Of which: supervisory slotting approach: RWA and capital requirements according to the supervisory slotting approach (as specified in SCRE13)."
- **Grounding — related node (Page 34 / para 7.44-7.45):** "Project finance exposures will be risk-weighted at 130% during the pre-operational phase and 100% during the operational phase... deemed to be high quality... risk weighted at 80%."

### [[Specialized Lending (SL)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank cannot meet the PD-estimation requirements of the corporate IRB approach for its SL exposures, the Supervisory Slotting Approach is the mandatory fallback for calculating RWA and expected losses. Chapter 13 (para 13.1–13.2) requires banks not meeting PD-estimation requirements to map internal grades to five supervisory categories each carrying a specific risk weight, and the regulatory reporting template (OV1 row 4) recognizes 'supervisory slotting approach' as a distinct RWA basis under SCRE13. Conclude that SL exposures fall under slotting where own-PD estimates are not qualified — confirm which SL sub-classes (PF, OF, CF, IPRE, HVCRE) are being slotted and apply the corresponding supervisory category weights.
- **Grounding — this node (Page 751 / OV1 row 4):** "Of which: supervisory slotting approach: RWA and capital requirements according to the supervisory slotting approach (as specified in SCRE13)."
- **Grounding — related node (Page 145 / 13.2):** "banks that do not meet the requirements for the estimation of probability of default (PD) ... will be required to map their internal grades to five supervisory categories, each ... associated with a specific risk weight."

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
