---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Customer Due Diligence Levels

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

Risk-based customer due diligence under the AML/CTF regime: the tiered CDD obligation set (standard, enhanced, simplified) and the higher-risk categories that trigger EDD. Defines who must be identified and verified and when intensified scrutiny is mandatory.

## How members connect

- 'Due Diligence Measures' is the baseline obligation; it references 'Beneficial Owner' because identifying and verifying the natural person behind the customer is a core CDD requirement.
- EDD and SDD are the up/down variants of the baseline — EDD is mandatory for higher-risk relationships, SDD permitted only where risk is demonstrably lower; both are conceptually subordinate to standard DD.
- EDD references PEPs: PEP status is a defined trigger that compels enhanced measures, linking the risk category to the intensified obligation.
- PEP and Beneficial Owner interact — beneficial-owner identification can surface PEP exposure, so both feed the risk assessment that sets the CDD tier.

## Members
- [[Beneficial Owner]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Due Diligence Measures]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Enhanced Due Diligence Measures]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Politically Exposed Persons (PEPs)]] - concept - markdown/SAMA_EN_1704_VER1.md
- [[Simplified Due Diligence Measures]] - concept - markdown/SAMA_EN_1704_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Customer_Due_Diligence_Levels
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bank Account Rules]]
- 1 edge to [[_COMMUNITY_AMLCTF Risk Assessment]]

## Top bridge nodes
- [[Due Diligence Measures]] - degree 5, connects to 2 communities