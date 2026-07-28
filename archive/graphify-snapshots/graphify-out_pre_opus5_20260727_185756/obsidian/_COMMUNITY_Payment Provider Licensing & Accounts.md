---
type: community
cohesion: 0.40
members: 5
enriched: true
---

# Payment Provider Licensing & Accounts

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Why this community

This community governs the licensing, account-lifecycle management, and electronic record infrastructure for payment service providers and prepaid instrument issuers under SAMA's PSP and Prepaid Payment Services frameworks. It links market-entry authorization conditions to ongoing operational controls over account states and record integrity.

## How members connect

- Payment Service Provider Licensing Requirements and Regulatory Rules for Prepaid Payment Services are conceptually co-dependent: prepaid issuers must satisfy PSP licensing conditions as a prerequisite, making licensing the gateway control for prepaid operations
- Electronic Record Requirements supports both licensing and account-management obligations by defining the retention and integrity standards that evidence compliance across the account lifecycle
- Freezing of Bank Accounts references Electronic Record Requirements, indicating that account-freeze actions must be documented in the mandated electronic record format to be valid and auditable
- Inoperative Accounts references both Freezing of Bank Accounts and Regulatory Rules for Prepaid Payment Services, creating a state-transition chain: inactive status can trigger freeze procedures, with specific prepaid-service rules governing dormancy treatment
- An examiner would expect system controls demonstrating: license-status checks at onboarding, automated dormancy/freeze state transitions with audit logs, and retention of electronic records meeting SAMA-specified standards
## Members
- [[Electronic Record Requirements]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Freezing of Bank Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Inoperative Accounts]] - document - markdown/SAMA_EN_1644_VER1.md
- [[Payment Service Provider Licensing Requirements]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Regulatory Rules for Prepaid Payment Services]] - concept - markdown/SAMA_EN_1644_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Payment_Provider_Licensing__Accounts
SORT file.name ASC
```
