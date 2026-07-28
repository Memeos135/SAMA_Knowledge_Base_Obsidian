---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "concept"
community: "Bank Account Operation Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# Bank Compliance Department

## Connections

### [[Clearance Bank Accounts (Rule 600)]] — `references` [EXTRACTED]
- **Why:** The Bank Accounts Rules require the bank's compliance department to act as the mandatory internal gateway for submitting account-opening applications to SAMA for sensitive account categories (e.g. Hajj/pilgrim affairs offices), and the same rules place clearance and other high-sensitivity accounts under compliance oversight, linking the compliance function structurally to account-opening approval processes.
- **This node (Page 56 / Rule 300.1.6.1 (Hajj pilgrim affairs)):** "Upon meeting the above requirements by the bank, the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Related node (Page 5 / Table of Contents):** "600 Clearance Bank Accounts 75"
- **Implication:** For any account category requiring SAMA pre-approval, banks must configure workflow controls that route the complete documentation package through the compliance department to SAMA on the same day (or next working day at latest), with a timestamped audit trail evidencing the submission.
- **Caveat:** The source context for node_a (clearance accounts, Rule 600) does not contain a direct verbatim excerpt specifically about compliance department involvement in clearance accounts; clause_a uses the table-of-contents locator only. The compliance department link is drawn from adjacent high-sensitivity account rules within the same document.

### [[International Multilateral Organizations Accounts]] — `references` [EXTRACTED]
- **Why:** The bank's compliance department is the mandatory internal escalation and submission channel for accounts requiring SAMA pre-approval, and the rules for multilateral international organisations expressly require SAMA to be informed upon account opening, creating a direct procedural dependency between the compliance function and the multilateral-org onboarding process.
- **This node (Page 56 / Rule 300.1.5 (Hajj context, same procedural template)):** "Upon meeting the above requirements by the bank, the bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Related node (Page 87 / Rule 300.1.6.5):** "SAMA must be informed when the account is opened. OIC may transfer money related to its programs or projects to accounts outside Saudi Arabia."
- **Implication:** The compliance department's workflow must include a same-day or next-business-day SAMA notification/approval submission step for multilateral organisation accounts, with a documented evidence trail (application, supporting documents, SAMA acknowledgement) that an examiner can trace from branch receipt to SAMA filing.

### [[Private Associations Accounts]] — `references` [EXTRACTED]
- **Why:** The bank's compliance department acts as a mandatory gateway for private association (and Hajj/pilgrim-office) account opening: it must review documents, approve the account, and submit the SAMA application, creating a direct procedural dependency between the compliance function and this customer-type's onboarding rules.
- **This node (Page 59):** "The bank's compliance department shall submit an application to SAMA along with all necessary documents to obtain SAMA approval for opening the bank account."
- **Related node (Page 61):** "This section covers private associations licensed by the Ministry of Human Resources and Social Development (MHRSD) to carry out different activities… Bank accounts for these associations and offices shall be opened in Saudi riyal only."
- **Implication:** Compliance department workflows must include a formal sign-off step and same-day document escalation trigger for private association account applications, with the compliance manager's approval documented and the SAMA submission timestamped to evidence adherence to the same-day or next-working-day deadline.
- **Caveat:** The node_b context pages (16, 17, 22) relate to dormant/abandoned accounts generally; the direct private-association compliance-department link is drawn from Page 61 (node_a context) and Page 65, not from the dormant-account pages shown in node_b's context field.

#graphify/concept #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
