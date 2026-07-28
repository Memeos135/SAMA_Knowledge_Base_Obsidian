---
type: community
cohesion: 1.00
members: 1
enriched: true
---

# Account Data Disclosure Blocking

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Why this community

Governs the circumstances under which a financial institution may or must disclose customer account data and block/freeze account balances — sitting at the intersection of bank-secrecy/data-protection duties and sanctions/TFS or law-enforcement freezing obligations.

## How members connect

- Single-member node: links disclosure permissions to balance-blocking as paired enforcement actions.
- Compliance reading: disclosure and blocking are exceptions to ordinary confidentiality/customer-access rights, triggered by competent-authority order or TFS obligation.
- No internal edges present; treat as a standalone provision pending cross-reference to AML/TFS and account-operation rules.

## Members
- [[Disclosing Account Data and Blocking Balances]] - document - markdown/SAMA_EN_8383_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Account_Data_Disclosure_Blocking
SORT file.name ASC
```
