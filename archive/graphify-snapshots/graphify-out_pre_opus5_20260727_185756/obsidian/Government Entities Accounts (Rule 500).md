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

# Government Entities Accounts (Rule 500)

## Connections

### [[Dual Control  Joint Signature|Dual Control / Joint Signature]] — `references` [EXTRACTED]
- **Why:** Rule 500 for government entity accounts explicitly requires that authorised signatories be Saudis only and prescribes joint-signature/dual-control disbursement controls as an integrity safeguard for public funds, directly cross-referencing the dual-control concept applied across high-sensitivity account categories throughout the document.
- **This node (Page 102 / Rule 500.1.1):** "Signatories of the accounts of Saudi government entities and agencies shall be Saudis only. No authorization shall be granted to non-Saudis in this regard."
- **Related node (Page 76 / Rule 300.1.5.14):** "Withdrawal from these accounts shall be as per dual control, and in case of withdrawal by checks, check shall be payable to the first beneficiary."
- **Implication:** Account management systems for government entity accounts must enforce a dual-signatory rule at transaction authorisation and must validate signatory nationality at onboarding and on each re-authorisation event, with an audit trail confirming both controls.

### [[SAMA (Saudi Central Bank)]] — `references` [EXTRACTED]
- **Why:** Rule 500 on government entity accounts creates direct, named obligations requiring SAMA's intermediation for account opening notifications, foreign currency approvals, and account transfers, making SAMA an operational actor—not merely a rule-issuer—within the government accounts regime.
- **This node (Page 101-102 / Rule 500.1.1):** "the Ministry of Finance shall inform SAMA about opening the account... Government accounts shall not be transferred from one bank to another unless the approval of the Ministry of Finance is obtained therefor and communicated to the bank through SAMA."
- **Related node (Page 1):** "Rules for Bank Accounts Updated March 2022... Please refer to SAMA's website (www.sama.gov.sa) for the last updated and amended version of the Rules."
- **Implication:** Banks' onboarding workflows for government entity accounts must include a SAMA-notification trigger at account opening and a SAMA-communication gate for any subsequent account transfer, with both steps documented as mandatory approval checkpoints in the account management system.

#graphify/document #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
