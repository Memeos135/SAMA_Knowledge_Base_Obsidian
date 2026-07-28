---
type: community
cohesion: 0.17
members: 13
enriched: true
---

# Bank Account Rules

**Cohesion:** 0.17 - loosely connected
**Members:** 13 nodes

## Why this community

SAMA's account-opening and operation regime for banks, centered on the umbrella 'Rules for Bank Accounts' and its account-type-specific annexes, integrating KYC/AML obligations and cross-referencing corporate-insolvency law.

## How members connect

- The 'Rules for Bank Accounts' is the parent instrument; each specialized regime (Government Entity, Non-resident Juristic Persons, WAMY, Liquidation/Restructuring, Correspondent) is subordinate and references it for baseline definitions and General Rules for Operation.
- Chapter I: Definitions and the General Rules supply the shared defined terms and operational obligations applied across all account types.
- AML/CFT obligations enter via the KYC Principle and AML/CFT Form, imposed on higher-risk openings (non-resident juristic persons, correspondent relationships) — note KYB-style due diligence on juristic customers.
- Liquidation/Restructuring account rules cross-reference the Bankruptcy Law and Companies Law, tying account operation to insolvency and corporate-status triggers.

## Members
- [[AMLCFT Form]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Bank Accounts for Liquidation and Financial Restructuring]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Bankruptcy Law]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Chapter I Definitions]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Companies Law]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Correspondence Relationship]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[General Rules for Operation of Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Government Entity Account Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[KYC Principle]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Non-resident Commercial Bank Correspondent Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Non-resident Juristic Persons Account Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Rules for Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[WAMY Bank Account Rules]] - document - markdown/SAMA_EN_1644_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bank_Account_Rules
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Natural Persons Accounts]]
- 1 edge to [[_COMMUNITY_Bank Account Supervision]]
- 1 edge to [[_COMMUNITY_Customer Due Diligence Levels]]

## Top bridge nodes
- [[Rules for Bank Accounts]] - degree 9, connects to 2 communities
- [[KYC Principle]] - degree 2, connects to 1 community