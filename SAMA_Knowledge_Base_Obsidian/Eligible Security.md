---
source_file: "markdown/SAMA_EN_6073_VER1.md"
type: "concept"
community: "Repurchase Agreements"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Repurchase_Agreements
  - graphify/enriched
---

# Eligible Security

## Connections

### [[Custodian]] — `references` [EXTRACTED]
- **What this link tells you:** When structuring a repo with a custodial arrangement, do not assume custody affects legal ownership: the guideline defines the Custodian as a third party providing custody/segregation of the collateral, but separately requires that ownership of the Eligible Security be fully transferred from seller to buyer even where a custodian holds it. The two defined terms interlock — the Custodian services the same Eligible Security that the repo seller provides to secure funding — but the custody service is operational, not proprietary. You would conclude that appointing a custodian does not preserve the seller's title, and would verify that the transfer of ownership is documented despite the custodial holding (section 8.9).
- **Grounding — this node (Page 8 / 8.9):** "The ownership of the eligible securities must be fully transferred from the seller to the buyer, even if a custodial arrangement is used"
- **Grounding — related node (Page 5 / 6.1.1):** "Custodian: It is a third party that provides services in relation to collateral... custody of the collateral, collateral management, collateral account segregation"

### [[Repurchase Agreement (Repo)]] — `references` [EXTRACTED]
- **What this link tells you:** When testing whether a proposed repo qualifies under these Guidelines, note that 'Eligible Security' is a gating defined term for the transaction itself: a repo is only in scope where it involves eligible securities meeting the requirements in Section 10, and Section 10.3 further excludes securities issued or guaranteed by the repo seller. The Guidelines apply to SAR-denominated sale/purchase of eligible securities with a repurchase agreement, and the collateral eligibility rules (listed sukuk/bonds, maturity at least matching the repo tenor) directly limit which repos are compliant. Conclude that you must verify each security against the Section 10 eligibility criteria before relying on the standard MRA framework, since ineligible collateral takes the transaction outside the intended regime.
- **Grounding — this node (Page 5 / 6.1.2):** "Eligible Security: an eligible security (or referred to as collateral) that the repo seller provides to the repo buyer to secure funding and meet the requirements in Section 10"
- **Grounding — related node (Page 5 / 5.2):** "applicable to any Saudi Riyal (SAR) denominated, outright sale or purchase of eligible securities with an agreement to repurchase or resell"

#graphify/concept #graphify/EXTRACTED #community/Repurchase_Agreements #graphify/enriched
