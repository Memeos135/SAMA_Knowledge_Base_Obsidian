---
type: community
cohesion: 1.00
members: 2
enriched: true
---

# SMS Notification Governance

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Why this community

Governance of bank/PSP-originated SMS notifications to customers, covering both permitted sender-name identification and the mandatory content elements of customer messages. Sits within consumer-protection and operational-conduct rules.

## How members connect

- Two SAMA circulars addressing the same conduct area: one governs approved SMS sender names/identifiers, the other mandates the unified data elements a customer notification must contain.
- Linked as conceptually related — together they set enforceable minimum requirements for how supervised entities notify customers by SMS.
- Neither is a subordinate of the other; read them as parallel obligations that a compliant messaging practice must satisfy simultaneously.

## Members
- [[SMS Sender Names Governance Circular]] - document - markdown/SAMA_EN_9663_VER1.md
- [[Unified SMS Notification Elements Circular]] - document - markdown/SAMA_EN_9665_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SMS_Notification_Governance
SORT file.name ASC
```
