---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# Credit Card & Fraud Rules

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

Credit card issuance/operation, individual-customer collections, and counter-fraud controls form an interlocking consumer-facing conduct and fraud-prevention regime for card products.

## How members connect

- Rules for Issuing and Operating Credit Cards references the updated Collection Regulations, so card issuers must apply the individual-customer collection conduct limits to card debt recovery.
- The two Collection Regulations entries are duplicate/near-identical versions; treat as the same obligation set to avoid conflicting readings.
- Counter-Fraud Fundamental Requirements is conceptually tied to card rules, extending fraud-prevention obligations to the card lifecycle.
- The Counter-Fraud Guide Circular is the subordinate issuing instrument carrying the Fundamental Requirements into force — read the Requirements as the substantive obligation, the circular as its promulgation.

## Members
- [[Counter-Fraud Fundamental Requirements]] - document - markdown/SAMA_EN_10530_VER1.md
- [[Counter-Fraud Fundamental Requirements Guide Circular]] - document - markdown/SAMA_EN_10529_VER1.md
- [[Rules for Issuing and Operating Credit Cards]] - document - markdown/SAMA_EN_10465_VER1.md
- [[Update of Collection Regulations and Procedures for Individual Customers]] - document - markdown/SAMA_EN_10400_VER1.md
- [[Update of Collection Regulations and Procedures for Individual Customers (dup)]] - document - markdown/SAMA_EN_10417_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credit_Card__Fraud_Rules
SORT file.name ASC
```
