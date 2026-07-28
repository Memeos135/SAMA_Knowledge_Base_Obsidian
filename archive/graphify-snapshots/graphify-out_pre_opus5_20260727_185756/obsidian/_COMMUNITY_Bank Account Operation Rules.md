---
type: community
cohesion: 0.14
members: 20
enriched: true
---

# Bank Account Operation Rules

**Cohesion:** 0.14 - loosely connected
**Members:** 20 nodes

## Why this community

This community covers SAMA's prescriptive ruleset for the opening, operation, and closure of bank accounts across legally distinct customer categories — ranging from government entities and international organisations to civil society bodies and Hajj-related operators. The dominant regime is SAMA's Rules for Bank Accounts, which imposes category-specific documentation, authorisation, and operational controls enforced through bank compliance and supported by inter-ministerial coordination.

## How members connect

- Rules for Bank Accounts is the primary instrument; all account-category rules (Government, Clearance, International Organisations, Endowments, Associations, Foundations, Cooperative Funds, Hajj/Pilgrim) reference SAMA as the supervisory authority and must conform to General Rules for Operation of Bank Accounts
- Hajj Organizer and Pilgrim Affairs Office account rules are semantically paired and share identical structural controls — Dual Control/Joint Signature and Ministry of Hajj and Umrah authorisation — reflecting the elevated fiduciary and custody risk of pilgrim funds
- Private Associations, Private Foundations, and Cooperative Associations/Funds all reference the Ministry of Human Resources and Social Development for registration verification, creating a cross-ministerial documentary chain that Bank Compliance Departments must evidence
- Disclosure and Enforcement on Accounts and Account Closure Rules define the lifecycle endpoints — attachment, freezing, and termination — within which all category-specific accounts must operate, with SAMA as the enforcement anchor
- Cash and Deposit Controls (ATM/CAM) impose transaction-channel constraints applicable across account types, linking operational system capabilities to the same SAMA supervisory authority
- Definitions and the General Rules nodes act as shared interpretive infrastructure, ensuring that category-specific rules inherit consistent terms for account holder, authorised signatory, and permissible operations
## Members
- [[Account Closure Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Bank Compliance Department]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Cash and Deposit Controls (ATMCAM)]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Clearance Bank Accounts (Rule 600)]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Cooperative Associations and Funds]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Definitions]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Disclosure and Enforcement on Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Dual Control  Joint Signature]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Endowments and Bequests Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[General Rules for Operation of Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Government Entities Accounts (Rule 500)]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Hajj Organizer Bank Account Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[International Multilateral Organizations Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Ministry of Hajj and Umrah]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Ministry of Human Resources and Social Development]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Pilgrim Affairs Office Bank Account Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Private Associations Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Private Foundations Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Rules for Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[SAMA (Saudi Central Bank)]] - concept - markdown/SAMA_EN_1644_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bank_Account_Operation_Rules
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AML Due Diligence & Accounts]]

## Top bridge nodes
- [[SAMA (Saudi Central Bank)]] - degree 11, connects to 1 community