---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "concept"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Politically Exposed Persons (PEPs)

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **Why:** The AML Law (Article 8) and its Implementing Regulations directly mandate that financial institutions develop internal procedures and deploy appropriate tools to identify PEPs and apply enhanced due diligence to them, making the PEP concept an operative requirement derived from the Law itself.
- **This node (Page 39 / Section B):** "Article (8) of the Anti-Money Laundering Law and its Implementing Regulations require the financial institution to develop internal procedures and provide appropriate tools to identify PEPs and implement enhanced due diligence measures regarding them."
- **Related node (Page 5 / Chapter IV Definitions):** "Anti-Money Laundering Law: The Anti-Money Laundering Law issued by Royal Decree No. (M/20) dated 05/02/1439H."
- **Implication:** CDD/KYB workflows must include a PEP-screening module with documented procedures approved at board level, covering customers, beneficial owners, family members, and close associates, evidencing senior-management approval for any high-risk PEP relationship.

### [[Enhanced Due Diligence Measures]] — `references` [EXTRACTED]
- **Why:** The EDD section explicitly designates PEPs as a mandatory high-risk category requiring enhanced due diligence, making PEPs a primary trigger object within the EDD framework; Article (8) of the AML Law and its Implementing Regulations are cited as the legal basis for both identification and EDD application to PEPs.
- **This node (Page 39 / Section 4B):** "In cases of high-risk business relationships with PEPs, the financial institution shall apply enhanced due diligence measures and apply the same to all types of PEPs, their family members, and persons close to those PEPs."
- **Related node (Page 36 / Section 4A):** "The financial institution shall identify the risk factors to be taken into consideration when classifying a customer in the high-risk customer category from the AML/CTF perspective."
- **Implication:** The CDD/KYB workflow must include an automated PEP-screening gate that, upon a positive match for customer or beneficial owner, triggers an EDD subprocess covering family members and close associates before onboarding or relationship continuation is permitted.

### [[SAFIU]] — `references` [EXTRACTED]
- **Why:** PEP relationships are high-risk business relationships requiring EDD; where PEP activity raises ML/TF suspicion, the financial institution is obligated to file a suspicious transaction report (STR) with SAFIU, making SAFIU the mandatory reporting destination for PEP-triggered suspicions and creating a direct operational pathway from PEP monitoring to SAFIU notification.
- **This node (Page 39 / Section 4B):** "The financial institution shall take reasonable measures to identify whether a customer or beneficial owner is a PEP. In cases of high-risk business relationships with PEPs, the financial institution shall apply enhanced due diligence measures."
- **Related node (Page 52 / Para 8.3):** "The financial institution shall immediately and directly inform the SAFIU upon suspicion or the presence of information or reasonable grounds to suspect that a customer's behavior is related to ML/TF acts."
- **Implication:** The PEP monitoring workflow must include an escalation path that, upon detection of suspicious activity in a PEP relationship, automatically routes the case for STR preparation and direct submission to SAFIU, with the six-month account statement and CDD documents attached per Para 8.9 requirements.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
