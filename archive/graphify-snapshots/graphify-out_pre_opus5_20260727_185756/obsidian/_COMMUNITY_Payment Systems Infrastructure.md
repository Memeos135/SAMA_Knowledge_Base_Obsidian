---
type: community
cohesion: 0.50
members: 4
enriched: true
---

# Payment Systems Infrastructure

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Why this community

This community addresses the classification, oversight principles, and disclosure standards for systemically important payment and settlement infrastructures in Saudi Arabia, sitting at the intersection of SAMA's domestic Important Payment Systems regime and international CPMI-IOSCO standards. It defines the regulatory expectations for financial market infrastructure (FMI) operators regarding resilience, settlement finality, and public accountability.

## How members connect

- Important Payment Systems Classification is the gateway node: designation as an important payment system triggers application of the Principles for Financial Market Infrastructures (PFMIs) as the governing prudential standard
- Principles for Financial Market Infrastructures cites the CPMI-IOSCO Disclosure Framework, linking substantive FMI requirements to the structured self-assessment and public disclosure obligations that demonstrate PFMI compliance
- Settlement Finality and Insolvency references Important Payment Systems Classification, indicating that finality protections — shielding settled transactions from insolvency reversal — apply specifically within classified systems, a critical legal-certainty control
- CPMI-IOSCO Disclosure Framework functions as an accountability and transparency mechanism, requiring classified FMIs to publish standardized assessments against the PFMIs — auditable by SAMA and market participants
- An examiner would expect: documented classification analysis, PFMI self-assessments mapped to each applicable principle, legal opinions confirming settlement finality under KSA insolvency law, and published CPMI-IOSCO disclosure reports
## Members
- [[CPMI-IOSCO Disclosure Framework]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Important Payment Systems Classification]] - document - markdown/SAMA_EN_1430_VER1.md
- [[Principles for Financial Market Infrastructures]] - concept - markdown/SAMA_EN_1430_VER1.md
- [[Settlement Finality and Insolvency]] - document - markdown/SAMA_EN_1430_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Payment_Systems_Infrastructure
SORT file.name ASC
```
