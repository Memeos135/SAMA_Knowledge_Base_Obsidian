---
type: community
cohesion: 0.22
members: 10
enriched: true
---

# Credit & Securitization Templates

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Why this community

Regulatory disclosure/reporting templates for credit and securitisation risk under SAMA's credit risk capital framework — standardised (CR4/CR5), IRB (CR6/CR9/CR10), and securitisation (SEC1/SEC3/SEC4) reporting. Defines the format in which banks evidence credit-risk capital calculations.

## How members connect

- The SCRE Credit Risk Framework is the governing rule set; the CR and SEC templates reference it as the authority prescribing their content and calculation basis.
- Templates split by approach: CR4/CR5 for the standardised approach, CR6/CR9/CR10 for IRB (including PD backtesting and slotting), and SEC1/3/4 by securitisation role (originator/sponsor vs investor).
- Minimum Capital Requirements for Credit Risk is conceptually the substantive obligation these templates operationalise as disclosure — the templates report against the framework's required capital, not independent rules.

## Members
- [[Minimum Capital Requirements for Credit Risk_1]] - document - markdown/SAMA_EN_3502_VER1.md
- [[SCRE Credit Risk Framework]] - concept - markdown/SAMA_EN_3487_VER1.md
- [[Template CR10 IRB specialised lending slotting approach]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR4 Standardised approach credit risk exposure and CRM effects]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR5 Standardised approach exposures by asset classes and risk weights]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR6 IRB credit risk exposures by portfolio and PD range]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template CR9 IRB backtesting of PD per portfolio]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template SEC1 Securitisation exposures in the banking book]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template SEC3 Securitisation banking book originatorsponsor]] - document - markdown/SAMA_EN_3487_VER1.md
- [[Template SEC4 Securitisation banking book investor]] - document - markdown/SAMA_EN_3487_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit__Securitization_Templates
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Credit Conversion & EAD]]
- 1 edge to [[_COMMUNITY_CCR Collateral & Mitigation]]

## Top bridge nodes
- [[SCRE Credit Risk Framework]] - degree 8, connects to 1 community
- [[Minimum Capital Requirements for Credit Risk_1]] - degree 3, connects to 1 community