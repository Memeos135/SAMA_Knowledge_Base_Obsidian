---
type: community
cohesion: 0.50
members: 5
enriched: true
---

# Basic Approach CVA

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Why this community

Capital-charge methodology for credit valuation adjustment (CVA) risk under the Basic Approach — the SAMA-adopted Basel framework for capitalising counterparty-credit CVA on derivatives/SFTs.

## How members connect

- BA-CVA is the governing method; it references its components — stand-alone CVA capital (SCVAc), supervisory risk weights, and eligible CVA hedges — which define how the charge is computed and reduced.
- Template CVA1 is the disclosure vehicle for the reduced BA-CVA result, conceptually downstream of the BA-CVA computation.
- Compliance consequence: only hedges meeting the 'Eligible CVA Hedges' definition reduce SCVAc, and risk weights are supervisory-set (not model-derived), so the calculation is prescriptive with limited firm discretion.

## Members
- [[Basic Approach for CVA (BA-CVA)_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[CVA Supervisory Risk Weights]] - document - markdown/SAMA_EN_4283_VER1.md
- [[Eligible CVA Hedges_1]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Stand-alone CVA Capital (SCVAc)]] - concept - markdown/SAMA_EN_4283_VER1.md
- [[Template CVA1 Reduced Basic Approach BA-CVA]] - document - markdown/SAMA_EN_4234_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Basic_Approach_CVA
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_CCR & CVA Capital Requirements]]
- 1 edge to [[_COMMUNITY_Regulatory Capital Disclosure Templates]]
- 1 edge to [[_COMMUNITY_CCP Exposure Calculation]]

## Top bridge nodes
- [[Basic Approach for CVA (BA-CVA)_1]] - degree 5, connects to 1 community
- [[Stand-alone CVA Capital (SCVAc)]] - degree 3, connects to 1 community
- [[Template CVA1 Reduced Basic Approach BA-CVA]] - degree 2, connects to 1 community
- [[Eligible CVA Hedges_1]] - degree 2, connects to 1 community