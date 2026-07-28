---
type: community
cohesion: 0.10
members: 23
enriched: true
---

# Operational Risk Capital

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Why this community

Basel III-derived prudential capital and stress-testing regime for banks: computing operational-risk capital under the Standardized Approach and testing capital resilience through SAMA's stress-testing and ICAAP requirements, with Pillar 3 disclosure of the inputs.

## How members connect

- Minimum Capital Requirements for Operational Risk cites Basel III Post-Crisis Reforms and mandates the Standardized Approach; SOPE is the SAMA-implemented instrument referencing that requirement.
- A defined calculation chain: Business Indicator -> Business Indicator Component -> combined with the Internal Loss Multiplier (built from the Loss Component and Standardized Approach Loss Data Set / Loss Event Type Classification) -> Operational Risk Capital.
- Rules on Stress Testing cite BCBS principles and require Stress Testing feeding ICAAP, using scenario/sensitivity/reverse and top-down analysis, with operational risk as one tested dimension.
- Pillar 3 Disclosure requirements consume the loss data set outputs, linking the capital-computation and public-disclosure obligations.

## Members
- [[BCBS Principles for Sound Stress Testing]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Basel III Post-Crisis Reforms]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Basel III Post-Crisis Reforms_1]] - concept - markdown/SAMA_EN_4234_VER1.md
- [[Business Indicator (BI)_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Business Indicator Component (BIC)_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Detailed Loss Event Type Classification_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Internal Capital Adequacy Assessment Plan (ICAAP)_1]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Internal Loss Multiplier (ILM)_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Loss Component (LC)_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Minimum Capital Requirements for Operational Risk_1]] - document - markdown/SAMA_EN_4041_VER1.md
- [[Operational Risk (Stress Testing)]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Operational Risk Capital (ORC)_1]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Pillar 3 Disclosure]] - concept - markdown/SAMA_EN_4234_VER1.md
- [[Pillar 3 Disclosure Requirements Framework_1]] - document - markdown/SAMA_EN_4234_VER1.md
- [[Reverse Stress Testing]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Rules on Stress Testing for Banks]] - document - markdown/SAMA_EN_4226_VER1.md
- [[SOPE - Minimum Capital Requirements for Operational Risk_1]] - concept - markdown/SAMA_EN_4234_VER1.md
- [[Scenario Analysis]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Sensitivity Analysis]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[Standardized Approach Loss Data Set]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Stress Testing_1]] - concept - markdown/SAMA_EN_4226_VER1.md
- [[The Standardized Approach]] - concept - markdown/SAMA_EN_4041_VER1.md
- [[Top-Down  Macro Stress Testing]] - concept - markdown/SAMA_EN_4226_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Operational_Risk_Capital
SORT file.name ASC
```
