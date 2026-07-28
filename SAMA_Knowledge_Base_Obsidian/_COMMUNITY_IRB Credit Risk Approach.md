---
type: community
cohesion: 0.06
members: 37
enriched: true
---

# IRB Credit Risk Approach

**Cohesion:** 0.06 - loosely connected
**Members:** 37 nodes

## Why this community

Basel-based Internal Ratings-Based (IRB) credit risk capital regime as adopted by SAMA: how banks using internal models compute RWA, plus the credit risk mitigation (CRM) rules that reduce exposure, and the minimum requirements/validation gating IRB use.

## How members connect

- IRB risk components (PD, LGD, EAD, M) feed the risk-weight functions; asset-class taxonomy (corporate, specialized lending sub-types PF/OF/CF/IPRE/HVCRE, retail/QRRE, equity, purchased receivables) determines which function and whether F-IRB or A-IRB applies.
- Specialized Lending links to the Supervisory Slotting Approach as the fallback where banks cannot estimate own parameters — a scope/exception relationship within IRB.
- CRM sub-cluster (Comprehensive vs Simple collateral approach, supervisory haircuts Table 14, holding periods Table 15, Hfx currency mismatch, netting, guarantees/derivatives, sovereign guarantees) modifies LGD/EAD inputs — CRM effects are cross-referenced into the IRB risk components.
- Minimum-requirement nodes (rating system design, PD estimation, Definition of Default, re-ageing, validation, disclosure) are conditions precedent to IRB eligibility, binding the modelling nodes to supervisory approval standards.

## Members
- [[Commodities Finance (CF)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Comprehensive Approach (Collateral)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Corporate Exposures]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Credit Risk Mitigation (CRM)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Currency Mismatch Haircut (Hfx)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Definition of Default]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Effect of Guarantees and Credit Derivatives]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Effective Maturity (M)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Equity Exposures]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Expected Loss and Provisions]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Foundation and Advanced IRB Approaches]] - document - markdown/SAMA_EN_3487_VER1.md
- [[High-Volatility Commercial Real Estate (HVCRE)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[IRB Asset Classes]] - document - markdown/SAMA_EN_3487_VER1.md
- [[IRB Disclosure Requirements]] - document - markdown/SAMA_EN_3487_VER1.md
- [[IRB Minimum Requirements]] - document - markdown/SAMA_EN_3487_VER1.md
- [[IRB Risk Components (PD, LGD, EAD, M)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[IRB Risk-Weight Functions]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Income-Producing Real Estate (IPRE)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Loss Given Default (LGD)_1]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Minimum Holding Periods (Table 15)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Object Finance (OF)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[On-Balance Sheet Netting]] - document - markdown/SAMA_EN_3487_VER1.md
- [[PD Estimation Requirements]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Probability of Default (PD)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Project Finance (PF)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Qualifying Purchased Receivables]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Qualifying Revolving Retail Exposures (QRRE)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[RWA for Purchased Receivables]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Rating System Design]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Re-ageing and Overdrafts Treatment]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Retail Exposures]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Simple Approach (Collateral)]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Sovereign Guarantees and Counter-Guarantees]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Specialized Lending (SL)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Supervisory Haircuts (Table 14)]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Supervisory Slotting Approach]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Validation of Internal Estimates]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IRB_Credit_Risk_Approach
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Counterparty Credit Risk Approaches]]
- 2 edges to [[_COMMUNITY_Standardized Credit Risk Approach]]
- 2 edges to [[_COMMUNITY_SA-CCR & CVA Framework]]
- 2 edges to [[_COMMUNITY_Securitization Exposures]]
- 1 edge to [[_COMMUNITY_Credit Conversion & EAD]]

## Top bridge nodes
- [[IRB Risk Components (PD, LGD, EAD, M)]] - degree 7, connects to 2 communities
- [[Specialized Lending (SL)]] - degree 8, connects to 1 community
- [[Comprehensive Approach (Collateral)]] - degree 6, connects to 1 community
- [[IRB Asset Classes]] - degree 5, connects to 1 community
- [[Credit Risk Mitigation (CRM)]] - degree 3, connects to 1 community