---
type: community
cohesion: 0.40
members: 6
enriched: true
---

# Finance Company Accounts

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Why this community

Account rules specific to Deposit-Taking Finance Companies (DTFCs) — SAMA's lifecycle framework for opening, operating, freezing, dormancy, and closing accounts held by these non-bank finance entities.

## How members connect

- 'DTFC General Account Opening Rules' is the anchor rule that all lifecycle rules reference — establishing the baseline conditions for the relationship.
- Term Deposit, Operating, Freezing/Updating, Inactive/Dormant, and Closing rules each govern a distinct phase of the account lifecycle and inherit the general opening requirements.
- Cross-reference between Operating Rules and Term Deposit Rules links day-to-day handling to product-specific conditions.
- Structure is parent rule -> lifecycle-stage sub-rules, defining ongoing obligations after on-boarding.

## Members
- [[Account Freezing and Updating Rules]] - document - markdown/SAMA_EN_8383_VER1.md
- [[Accounts Operating Rules_1]] - document - markdown/SAMA_EN_8383_VER1.md
- [[Closing of the Account]] - document - markdown/SAMA_EN_8383_VER1.md
- [[DTFC General Account Opening Rules]] - document - markdown/SAMA_EN_8383_VER1.md
- [[Inactive and Dormant Accounts_1]] - document - markdown/SAMA_EN_8383_VER1.md
- [[Term Deposit Account Rules]] - document - markdown/SAMA_EN_8383_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Finance_Company_Accounts
SORT file.name ASC
```
