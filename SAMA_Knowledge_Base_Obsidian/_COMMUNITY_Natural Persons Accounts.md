---
type: community
cohesion: 0.33
members: 6
enriched: true
---

# Natural Persons Accounts

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Why this community

Bank account-opening regime for natural persons under SAMA rules — the procedural and identity-verification requirements banks must meet before establishing a customer relationship, with segment-specific carve-outs. This is the on-boarding gateway where CDD/KYC obligations attach.

## How members connect

- Chapter III (Procedural Rules) sits above and references the substantive account-opening rules, giving the procedural spine for the regime.
- 'Rules for Opening Accounts for Natural Persons' is the parent rule set; 'Expatriates' and 'Minors' are scoped sub-rules that modify baseline identity/eligibility conditions for those categories.
- 'General Instructions for Opening Bank Accounts' cross-references 'Remote Opening', which relaxes or adapts in-person verification while preserving identity-confirmation obligations.
- Read as hierarchy: general instructions/procedural rules -> natural-person rules -> segment exceptions (minors, expatriates, remote channel).

## Members
- [[Bank Accounts for Minors]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Chapter III Procedural Rules]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Expatriates in Saudi Arabia Accounts]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[General Instructions for Opening Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Remote Opening of Bank Accounts]] - concept - markdown/SAMA_EN_1644_VER1.md
- [[Rules for Opening Accounts for Natural Persons]] - document - markdown/SAMA_EN_1644_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Natural_Persons_Accounts
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bank Account Rules]]
- 1 edge to [[_COMMUNITY_Juristic Persons Accounts]]
- 1 edge to [[_COMMUNITY_Bank Account Supervision]]

## Top bridge nodes
- [[Chapter III Procedural Rules]] - degree 4, connects to 2 communities
- [[Remote Opening of Bank Accounts]] - degree 2, connects to 1 community