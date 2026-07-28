---
type: community
cohesion: 0.27
members: 10
enriched: true
---

# CCP Exposure Calculation

**Cohesion:** 0.27 - loosely connected
**Members:** 10 nodes

## Why this community

Counterparty credit risk capital regime: computing exposure to derivatives counterparties and to central counterparties (CCPs) under the Standardized Approach (SA-CCR).

## How members connect

- SA-CCR is the governing method; EAD is its output, built from Replacement Cost (RC) plus Potential Future Exposure (PFE), scaled by the Alpha Multiplier.
- RC references the Margin Agreement / NICA and Net Independent Collateral Amount as collateral inputs reducing exposure.
- Exposures to CCPs applies SA-CCR and distinguishes Qualifying CCPs (QCCP), which attract preferential treatment, from non-qualifying ones.
- Default Fund Contribution Capital (KCMi/KCCP) references SA-CCR for the separate capital charge on a bank's clearing-fund contributions.

## Members
- [[Alpha Multiplier]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Default Fund Contribution Capital (KCMiKCCP)]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Exposure at Default (EAD)_2]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Exposures to Central Counterparties (CCPs)]] - document - markdown/SAMA_EN_4283_VER1.md
- [[Margin Agreement  NICA]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Net Independent Collateral Amount (NICA)_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Potential Future Exposure (PFE)]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Qualifying CCP (QCCP)_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Replacement Cost (RC)_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Standardized Approach for CCR (SA-CCR)_1]] - concept - markdown/SAMA_EN_4283_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CCP_Exposure_Calculation
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SA-CCR Supervisory Parameters]]
- 2 edges to [[_COMMUNITY_CCR & CVA Capital Requirements]]
- 1 edge to [[_COMMUNITY_SA-CCR Derivative Add-ons]]
- 1 edge to [[_COMMUNITY_Leverage & SA-CCR Requirements]]
- 1 edge to [[_COMMUNITY_Basic Approach CVA]]

## Top bridge nodes
- [[Exposure at Default (EAD)_2]] - degree 8, connects to 4 communities
- [[Standardized Approach for CCR (SA-CCR)_1]] - degree 8, connects to 2 communities
- [[Alpha Multiplier]] - degree 2, connects to 1 community