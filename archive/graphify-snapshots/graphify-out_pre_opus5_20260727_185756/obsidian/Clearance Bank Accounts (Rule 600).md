---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "document"
community: "Bank Account Operation Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# Clearance Bank Accounts (Rule 600)

## Connections

### [[Bank Compliance Department]] — `references` [EXTRACTED]
- **Why:** The Bank Accounts Rules require the bank's compliance department to act as the mandatory internal gateway for submitting account-opening applications to SAMA for sensitive account categories (e.g. Hajj/pilgrim affairs offices), and the same rules place clearance and other high-sensitivity accounts under compliance oversight, linking the compliance function structurally to account-opening approval processes.
- **This node (Page 5 / Table of Contents):** "600 Clearance Bank Accounts 75"
- **Related node (Page 56 / Rule 300.1.6.1 (Hajj pilgrim affairs)):** "Upon meeting the above requirements by the bank, the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Implication:** For any account category requiring SAMA pre-approval, banks must configure workflow controls that route the complete documentation package through the compliance department to SAMA on the same day (or next working day at latest), with a timestamped audit trail evidencing the submission.
- **Caveat:** The source context for node_a (clearance accounts, Rule 600) does not contain a direct verbatim excerpt specifically about compliance department involvement in clearance accounts; clause_a uses the table-of-contents locator only. The compliance department link is drawn from adjacent high-sensitivity account rules within the same document.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** Rule 600 on Clearance Bank Accounts is promulgated within the SAMA Rules for Bank Accounts framework, and the Rules expressly require SAMA approval and communication channels for account transfers and closures, establishing SAMA as the supervisory authority over the clearance account regime.
- **This node (Page 102 / Rule 500.1.1 (para 11)):** "Government accounts shall not be transferred from one bank to another unless the approval of the Ministry of Finance is obtained therefor and communicated to the bank through SAMA."
- **Related node (Page 1):** "Rules for Bank Accounts Updated March 2022... Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** Any system workflow for clearance or government account transfers must include a SAMA-communication checkpoint as a hard gate before execution, with documentary evidence of SAMA notification retained in the account file.
- **Caveat:** The source context for Rule 600 itself is limited to a table-of-contents entry (page 5); the referenced operational detail is drawn from the adjacent Rule 500 provisions, which share the same supervisory communication mechanism. Confidence is slightly inferred for the clearance-specific content.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
