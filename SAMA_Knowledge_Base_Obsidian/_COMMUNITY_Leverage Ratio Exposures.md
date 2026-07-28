---
type: community
cohesion: 0.22
members: 11
enriched: true
---

# Leverage Ratio Exposures

**Cohesion:** 0.22 - loosely connected
**Members:** 11 nodes

## Why this community

The Basel leverage-ratio framework's exposure-measure rules, focused on how derivatives, SFTs, written credit derivatives and CCR-related items are captured in the non-risk-based denominator.

## How members connect

- Hierarchy: the Leverage Ratio Framework governs the Leverage Ratio Exposure Measure, which decomposes into Derivative Exposures, SFT Exposures and their calculation methods.
- Derivative-exposure treatment references the specific measurement components — Cash Variation Margin Treatment, Written Credit Derivatives Treatment, and Qualifying CCP status — that determine what may reduce or must inflate the exposure figure.
- SFT exposure calculation depends on recognition of a Qualifying Master Netting Agreement and QCCP status, setting the conditions under which netting is permitted.
- Risk-integrity conditions (Wrong-way Risk, CCR Stress Testing Program) constrain the exposure and internal-model treatment, so they act as qualifying limits rather than standalone capital rules.

## Members
- [[CCR Stress Testing Program]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Cash Variation Margin Treatment]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Derivative Exposures (Leverage Ratio)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Leverage Ratio Exposure Measure]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Leverage Ratio Framework]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Qualifying CCP (QCCP)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Qualifying Master Netting Agreement]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[SFT Exposures (Leverage Ratio)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Securities Financing Transaction Exposures Calculation]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Written Credit Derivatives Treatment]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Wrong-way Risk]] - concept - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Leverage_Ratio_Exposures
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_SA-CCR & CVA Framework]]
- 2 edges to [[_COMMUNITY_Credit Risk & CCP Capital]]
- 2 edges to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 1 edge to [[_COMMUNITY_SA-CCR Derivative Add-ons]]
- 1 edge to [[_COMMUNITY_Credit Conversion & EAD]]

## Top bridge nodes
- [[Leverage Ratio Framework]] - degree 5, connects to 3 communities
- [[Qualifying CCP (QCCP)]] - degree 4, connects to 2 communities
- [[Derivative Exposures (Leverage Ratio)]] - degree 7, connects to 1 community
- [[Wrong-way Risk]] - degree 3, connects to 1 community