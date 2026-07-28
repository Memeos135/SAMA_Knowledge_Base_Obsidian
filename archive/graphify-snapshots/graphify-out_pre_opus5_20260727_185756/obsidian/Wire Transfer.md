---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "document"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Wire Transfer

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **Why:** Article 10 of the AML Law is the primary statutory basis for the Guide's Wire Transfer section, which translates the Law's obligations on originator/beneficiary information into granular operational requirements for cross-border and domestic transfers processed by Saudi-licensed financial institutions.
- **This node (Page 65 / Section 14):** "Article (10) of the Anti-Money Laundering Law and Article (68) of the Law on Combating Terrorism Crimes and Financing state the obligations of the financial institution when conducting cross-border and domestic wire transfers in any currency…received, sent or processed by a fina…"
- **Related node (Page 5 / Chapter IV Definitions):** "Anti-Money Laundering Law: The Anti-Money Laundering Law issued by Royal Decree No. (M/20) dated 05/02/1439H."
- **Implication:** Payment systems and SWIFT/messaging infrastructure must capture and validate the full originator and beneficiary data set (name, account/reference number, address or ID) before processing any wire transfer, with policies to reject, suspend, or escalate transfers lacking required fields—evidenced by system logs and policy documentation for SAMA examination.

### [[Record Keeping]] — `references` [EXTRACTED]
- **Why:** The Wire Transfer section explicitly cross-references the Record Keeping section as the governing retention standard for beneficiary identity verification data collected during wire transfers, and record keeping para 6.8 specifically addresses wire transfer record obligations, creating a direct normative cross-reference between the two regimes.
- **This node (Page 67 / Art 14.6 area):** "the financial institution receiving a wire transfer shall verify the beneficiary's identity and keep this information as stated under the Record Keeping Section."
- **Related node (Page 47 / Art 6.8):** "6.8 When conducting wire trans[fers] … [record keeping obligations apply]"
- **Implication:** Wire transfer processing systems must retain originator and beneficiary data fields (name, account/reference number, address/ID, purpose, relationship) for a minimum of ten years in a retrievable and auditable format, with records available to SAMA and competent authorities upon request — this data retention requirement must be built into the payment messaging and archiving infrastructure.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** SAMA's AML/CTF Guide incorporates Wire Transfer as a numbered section (Section 14) within the guide itself, establishing mandatory originator/beneficiary information requirements and processing obligations that financial institutions in Saudi Arabia must implement under SAMA's supervisory authority.
- **This node (Page 65 / Section 14 / Para 14.1):** "Article (10) of the Anti-Money Laundering Law and Article (68) of the Law on Combating Terrorism Crimes and Financing state the obligations of the financial institution when conducting cross-border and domestic wire transfers in any currency."
- **Related node (Page 2 / Table of Contents):** "14. Wire Transfer ... The Anti-Money Laundering and Counter-Terrorism Financing (AML/CTF) Guide ... AML/CTF Department, Saudi Central Bank"
- **Implication:** Financial institutions must configure wire transfer processing systems to capture and transmit, at minimum, originator full name, account/reference number, address/ID, beneficiary full name, beneficiary account/reference, and transfer purpose — with automated detection of missing fields and a documented risk-based decision workflow for executing, rejecting, or suspending incomplete transfers.

### [[Simplified Due Diligence Measures]] — `references` [EXTRACTED]
- **Why:** The wire transfer section establishes mandatory originator and beneficiary information requirements for all wire transfers regardless of risk level, meaning SDD cannot reduce or waive these data-collection obligations; the carve-outs in Para 14.8 are product-type exclusions, not risk-tier exemptions, reinforcing that SDD's scope reduction does not extend to wire transfer data fields.
- **This node (Page 65 / Para 14.1):** "Before processing a wire transfer, the financial institution should obtain information about the wire transfer originator and beneficiary, keep that information with each wire transfer, and verify that information."
- **Related node (Page 43 / Para 5.3):** "Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owner."
- **Implication:** Wire transfer processing workflows must enforce mandatory originator/beneficiary data fields as a hard pre-execution control that is independent of the customer's SDD risk classification; SDD does not create a permissible exemption from wire transfer information requirements.

#graphify/document #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
