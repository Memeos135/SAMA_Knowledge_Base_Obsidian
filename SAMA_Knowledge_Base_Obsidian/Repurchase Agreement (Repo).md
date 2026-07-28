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

# Repurchase Agreement (Repo)

## Connections

### [[Eligible Security]] — `references` [EXTRACTED]
- **What this link tells you:** When testing whether a proposed repo qualifies under these Guidelines, note that 'Eligible Security' is a gating defined term for the transaction itself: a repo is only in scope where it involves eligible securities meeting the requirements in Section 10, and Section 10.3 further excludes securities issued or guaranteed by the repo seller. The Guidelines apply to SAR-denominated sale/purchase of eligible securities with a repurchase agreement, and the collateral eligibility rules (listed sukuk/bonds, maturity at least matching the repo tenor) directly limit which repos are compliant. Conclude that you must verify each security against the Section 10 eligibility criteria before relying on the standard MRA framework, since ineligible collateral takes the transaction outside the intended regime.
- **Grounding — this node (Page 5 / 5.2):** "applicable to any Saudi Riyal (SAR) denominated, outright sale or purchase of eligible securities with an agreement to repurchase or resell"
- **Grounding — related node (Page 5 / 6.1.2):** "Eligible Security: an eligible security (or referred to as collateral) that the repo seller provides to the repo buyer to secure funding and meet the requirements in Section 10"

### [[Master Repo Agreement (MRA)]] — `references` [EXTRACTED]
- **What this link tells you:** When documenting a repo in Saudi Arabia, treat the SAMA-approved standard Master Repurchase Agreement (MRA, 2020 version) as mandatory documentation, not a template: Section 7.1 requires all repo market participants to ensure their repo transactions are governed by the MRA, and any variations must be captured in Annexures and mutually agreed. The MRA is also subject to and governed by Saudi law. Conclude that a repo not documented under the approved MRA (or without properly incorporated annexures for any deviation) would be non-compliant, and that deviations require documented mutual agreement rather than informal adjustment.
- **Grounding — this node (Page 6 / 7.1):** "All repo market participants shall ensure that their repo transactions in Saudi Arabia must be governed by the standard Master Repurchase Agreement (MRA)"
- **Grounding — related node (Page 6 / 7.1):** "repo transactions in Saudi Arabia must be governed by the standard Master Repurchase Agreement (MRA)... (2020 version) as attached in Appendix A, approved by SAMA"

### [[Reverse Repurchase Agreement]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When applying obligations in these Guidelines, note that 'repo' and 'reverse repo' are treated as two sides of the same transaction and the Guidelines expressly use 'repo' to refer to both equivalently unless otherwise specified. A reverse repo is defined as the buyer's purchase of securities with a simultaneous promise for resale, i.e. the mirror position of the repo seller. Conclude that policy requirements framed around 'repo' generally apply to the reverse-repo side too, so a market participant acting as cash provider/buyer cannot assume the rules bind only the securities seller; check for any provision that expressly distinguishes the two before assuming a requirement applies to only one leg.
- **Grounding — this node (Page 6):** "repo term will be used commonly in this guideline referring to repo and reverse repo equivalently unless otherwise is specified"
- **Grounding — related node (Page 6 / 6.1.9):** "Reverse Repurchase Agreement (Reverse Repo): It is an agreement where a buyer buys financial securities from a seller with a simultaneous promise arrangement for the seller to repurchase"

### [[SAMA Guidelines on Repurchase Agreements]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which transactions these Guidelines capture, rely on the defined term 'Repurchase Agreement (Repo)' as the trigger: Section 5.2 applies the Guidelines to any SAR-denominated outright sale/purchase of eligible securities with an agreement to repurchase or resell at an agreed future date or on demand, and Section 6 confirms 'repo' is used to cover repo and reverse repo equivalently. Note the carve-out in 5.3 — existing foreign-currency-leg transactions governed by the GMRA are not prohibited, subject to applicable KSA rules. You would conclude that a transaction's currency and structure determine whether the mandatory MRA and risk-management requirements bite, so classify each trade against this definition before applying the binding policy requirements.
- **Grounding — this node (Page 6 / Section 6.1.9-6.1.11):** "repo term will be used commonly in this guideline referring to repo and reverse repo equivalently unless otherwise is specified."
- **Grounding — related node (Page 5 / Section 5.2):** "applicable to any Saudi Riyal (SAR) denominated, outright sale or purchase of eligible securities with an agreement to repurchase or resell"

#graphify/concept #graphify/EXTRACTED #community/Repurchase_Agreements #graphify/enriched
