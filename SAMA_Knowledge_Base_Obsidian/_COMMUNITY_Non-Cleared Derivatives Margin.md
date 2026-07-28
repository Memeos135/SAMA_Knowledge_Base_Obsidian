---
type: community
cohesion: 0.40
members: 6
enriched: true
---

# Non-Cleared Derivatives Margin

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Why this community

Margin regime for non-centrally cleared (bilateral OTC) derivatives — mandatory collateral posting to mitigate counterparty credit and systemic risk, transposing the BCBS-IOSCO international standard into SAMA requirements.

## How members connect

- 'Margin Requirements for Non-centrally Cleared Derivatives' is the governing SAMA rule and cites the BCBS-IOSCO standard as its source framework.
- Initial Margin and Variation Margin are the two mandated posting obligations defined within the rule; Eligible Collateral scopes what assets satisfy them.
- Re-hypothecation Treatment limits/conditions reuse of collected margin — a constraint on how posted collateral (esp. IM) may be handled.
- Hierarchy: international standard (BCBS-IOSCO) -> SAMA margin rule -> component definitions (IM/VM/collateral/re-hypothecation).

## Members
- [[BCBS-IOSCO Margin Requirements for Non-centrally Cleared Derivatives]] - paper - markdown/SAMA_EN_2757_VER1.md
- [[Eligible Collateral]] - concept - markdown/SAMA_EN_2757_VER1.md
- [[Initial Margin]] - concept - markdown/SAMA_EN_2757_VER1.md
- [[Margin Requirements for Non-centrally Cleared Derivatives]] - document - markdown/SAMA_EN_2757_VER1.md
- [[Re-hypothecation Treatment]] - concept - markdown/SAMA_EN_2757_VER1.md
- [[Variation Margin]] - concept - markdown/SAMA_EN_2757_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Non-Cleared_Derivatives_Margin
SORT file.name ASC
```
