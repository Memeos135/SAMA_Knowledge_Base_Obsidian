---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# OTC Derivative Trade Reporting

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

Technical reporting rules for OTC derivative life-cycle events under SAMA's trade-reporting regime — how trades and subsequent events must be reported, identified, and attributed to a reporting counterparty.

## How members connect

- Life Cycle Event Reporting Scenarios is the operative provision, cross-referencing OTC Derivative Life Cycle Events (the reportable events), the Action Type Field (Item 53), and the Internal Unique Trade ID (Item 14) as mandated data fields.
- Reporting Counterparty Determination Rules (Appendix C) fixes who bears the reporting obligation and links to the trade ID used to tie events to a single transaction.
- These are field-level and scenario-level specifications subordinate to SAMA's derivative reporting requirement; the linkage defines mandatory content and attribution, not discretionary practice.

## Members
- [[Action Type Field (Item 53)]] - document - markdown/SAMA_EN_10593_VER1_0.md
- [[Internal Unique Trade ID (Item 14)]] - document - markdown/SAMA_EN_10593_VER1_0.md
- [[Life Cycle Event Reporting Scenarios]] - document - markdown/SAMA_EN_10593_VER1_0.md
- [[OTC Derivative Life Cycle Events]] - document - markdown/SAMA_EN_10593_VER1_0.md
- [[Reporting Counterparty Determination Rules (Appendix C)]] - document - markdown/SAMA_EN_10593_VER1_0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OTC_Derivative_Trade_Reporting
SORT file.name ASC
```
