---
type: community
cohesion: 0.29
members: 8
enriched: true
---

# Real Estate Finance Rules

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Why this community

Real estate and finance-lease regulatory regime, spanning the primary laws, their implementing regulations, secondary-market/securitization mechanics, and the specific banking-account rules for real estate financing (including non-resident owners).

## How members connect

- Clear legal hierarchy: the Implementing Regulation of Finance Lease Law implements the Finance Lease Law, and both cite/interact with the Real Estate Finance Law — establishing law→implementing-regulation subordination.
- The regime enables secondary-market activity — Real Estate Finance Law references the Secondary Market, and the Implementing Regulation references Securitization and the Contracts Register — linking origination rules to funding/registration mechanics.
- Account-side compliance is scoped in: Bank Accounts for Non-Resident Real Estate Owners is governed by the Banking Account Rules and conceptually tied to the Real Estate Finance Law, connecting the finance regime to deposit-account controls.

## Members
- [[Bank Accounts for Non-Resident Real Estate Owners]] - document - markdown/SAMA_EN_11101_VER1.md
- [[Banking Account Rules]] - document - markdown/SAMA_EN_11101_VER1.md
- [[Contracts Register]] - concept - markdown/SAMA_EN_123_VER1.md
- [[Finance Lease Law_2]] - document - markdown/SAMA_EN_123_VER1.md
- [[Implementing Regulation of Finance Lease Law]] - document - markdown/SAMA_EN_123_VER1.md
- [[Real Estate Finance Law_1]] - document - markdown/SAMA_EN_1272_VER1.md
- [[Secondary Market of Real Estate Finance]] - concept - markdown/SAMA_EN_1272_VER1.md
- [[Securitization]] - concept - markdown/SAMA_EN_123_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Real_Estate_Finance_Rules
SORT file.name ASC
```
