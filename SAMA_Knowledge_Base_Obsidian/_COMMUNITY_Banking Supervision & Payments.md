---
type: community
cohesion: 0.14
members: 17
enriched: true
---

# Banking Supervision & Payments

**Cohesion:** 0.14 - loosely connected
**Members:** 17 nodes

## Why this community

Core banking, payments, and consumer-finance supervision: the law-to-regulation hierarchy governing licensing, prudential/reporting duties, consumer protection, and credit information across banks, PSPs, and finance companies.

## How members connect

- Primary statutes (Banking Control Law, Finance Companies Control Law, Credit Information Law) sit at the top; implementation rules and implementing regulations (SAMA 1429, Payments Law reg SAMA 1430) operationalise them into supervisory, reporting, and licensing obligations.
- The Payments Law implementing regulation is the hub for PSP duties — it references licensing, payment services, risk/compliance, complaints, and customer protection, defining who may operate and under what conduct obligations.
- Model Consumer Finance Contract (SAMA 1611) draws multiple regimes together — Finance Companies Control Law, Credit Information Law, APR, early repayment, and consumer protection — making it a composite compliance reference for finance contracts.
- Consumer Protection Principles and the payments regime's Customer Protection provisions are semantically aligned; note both terms coexist across regimes and should be scoped to the relevant instrument.

## Members
- [[Annual Percentage Rate (APR)]] - concept - markdown/SAMA_EN_1611_VER1.md
- [[Bank Periodic Data Reporting]] - concept - markdown/SAMA_EN_1429_VER1.md
- [[Banking Control Law]] - concept - markdown/SAMA_EN_1429_VER1.md
- [[Complaints and Disputes]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Consumer Protection Principles]] - concept - markdown/SAMA_EN_1611_VER1.md
- [[Credit Bureaus Fintech Membership Circular (SAMA 1608)]] - document - markdown/SAMA_EN_1608_VER1.md
- [[Credit Information Law]] - concept - markdown/SAMA_EN_1608_VER1.md
- [[Customer Protection and Financial Inclusion]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Early Repayment Provisions]] - concept - markdown/SAMA_EN_1611_VER1.md
- [[Finance Companies Control Law_3]] - concept - markdown/SAMA_EN_1611_VER1.md
- [[Implementation Rules for Banking Control Law (SAMA 1429)]] - document - markdown/SAMA_EN_1429_VER1.md
- [[Implementing Regulation for Payments Law (SAMA 1430)]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Licensing of Payment Service Providers]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Model Consumer Finance Contract (SAMA 1611)]] - document - markdown/SAMA_EN_1611_VER1.md
- [[Payment Services]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Risk Management and Compliance]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[SAMA Supervision and Inspection]] - concept - markdown/SAMA_EN_1429_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Banking_Supervision__Payments
SORT file.name ASC
```
