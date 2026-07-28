---
type: community
cohesion: 0.67
members: 3
enriched: true
---

# Bank Interactions & Exposure

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Why this community

Prudential risk-management expectations for banks engaging with highly leveraged institutions (HLIs) and measuring counterparty credit exposure. Covers governance-of-exposure and exposure-quantification concepts within the banking/risk regime.

## How members connect

- 'Sound Practices for Banks' Interactions with HLIs' references the 'Internal Control Guidelines for Commercial Banks', tying HLI counterparty risk into the bank's overarching internal-control obligations.
- It also references 'Potential Future Exposure (PFE)' as the measurement concept used to size counterparty exposure to leveraged counterparties.
- Read together: the sound-practices guidance sets the supervisory expectation, PFE supplies the quantification metric, and internal controls provide the enforcement/governance backbone.

## Members
- [[Internal Control Guidelines for Commercial Banks]] - document - markdown/SAMA_EN_9068_VER1.md
- [[Potential Future Exposure (PFE)_1]] - concept - markdown/SAMA_EN_9068_VER1.md
- [[Sound Practices for Banks' Interactions with HLIs]] - paper - markdown/SAMA_EN_9068_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bank_Interactions__Exposure
SORT file.name ASC
```
