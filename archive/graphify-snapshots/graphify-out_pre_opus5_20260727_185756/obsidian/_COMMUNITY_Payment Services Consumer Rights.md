---
type: community
cohesion: 0.33
members: 6
enriched: true
---

# Payment Services Consumer Rights

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Why this community

This community covers the consumer-facing obligations imposed on payment service licensees under SAMA's Payment Services regulatory regime: execution integrity, liability allocation for unauthorized transactions, refund entitlements, and dispute resolution. It maps the obligation chain from correct payment order execution through to consumer redress, forming the core of payment consumer-protection compliance.

## How members connect

- Payment Order Execution Rules set the baseline for what constitutes correct execution, which directly triggers liability analysis under Unauthorized Payment Liability when execution fails or fraud occurs
- Unauthorized Payment Liability and Refund Rights for Payment Transactions are causally linked — a finding of unauthorized payment activates the refund entitlement and defines who bears the loss (licensee vs. payer)
- Complaints and Disputes references Unauthorized Payment Liability, establishing the procedural channel through which consumers assert execution failures and liability claims
- Account Information and Payment Initiation Services references Payment Order Execution Rules, extending execution-quality and liability obligations to AISP/PISP actors operating on behalf of payers
- Licensee Change Notification Obligations references Payment Order Execution Rules, indicating that material changes to service terms or infrastructure must be disclosed in a way that preserves execution continuity and consumer awareness
- Collectively these nodes define the auditable evidence trail an examiner expects: timestamped execution records, unauthorized-transaction dispute logs, refund processing timelines, and consumer notification records
## Members
- [[Account Information and Payment Initiation Services]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Complaints and Disputes]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Licensee Change Notification Obligations]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Payment Order Execution Rules]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Refund Rights for Payment Transactions]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Unauthorized Payment Liability]] - document - markdown/SAMA_EN_1430_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Payment_Services_Consumer_Rights
SORT file.name ASC
```
