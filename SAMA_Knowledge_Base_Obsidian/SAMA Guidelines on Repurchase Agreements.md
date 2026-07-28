---
source_file: "markdown/SAMA_EN_6073_VER1.md"
type: "document"
community: "Repurchase Agreements"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Repurchase_Agreements
  - graphify/enriched
---

# SAMA Guidelines on Repurchase Agreements

## Connections

### [[Master Repo Agreement (MRA)]] — `references` [EXTRACTED]
- **What this link tells you:** When advising a repo market participant on documentation, note that the Guidelines make use of the SAMA-approved standard Master Repurchase Agreement mandatory, not optional: Section 7.1 requires all SAR repo transactions in Saudi Arabia to be governed by the standard MRA (2020 version, Appendix A), any variations must sit in Annexures and be mutually agreed, and the MRA is governed by Saudi law. Because Section 3.2 states all policy requirements are binding on participants, you would conclude that deviating from the standard MRA form (outside agreed annexures/confirmations) is a compliance breach — check that live templates are the approved 2020 version and that amendments are properly documented.
- **Grounding — this node (Page 6-7 / Section 7.1):** "All repo market participants shall ensure that their repo transactions in Saudi Arabia must be governed by the standard Master Repurchase Agreement (MRA)"
- **Grounding — related node (Page 7 / Section 7.4):** "The MRA shall be subject to and governed by Saudi law."

### [[Repurchase Agreement (Repo)]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which transactions these Guidelines capture, rely on the defined term 'Repurchase Agreement (Repo)' as the trigger: Section 5.2 applies the Guidelines to any SAR-denominated outright sale/purchase of eligible securities with an agreement to repurchase or resell at an agreed future date or on demand, and Section 6 confirms 'repo' is used to cover repo and reverse repo equivalently. Note the carve-out in 5.3 — existing foreign-currency-leg transactions governed by the GMRA are not prohibited, subject to applicable KSA rules. You would conclude that a transaction's currency and structure determine whether the mandatory MRA and risk-management requirements bite, so classify each trade against this definition before applying the binding policy requirements.
- **Grounding — this node (Page 5 / Section 5.2):** "applicable to any Saudi Riyal (SAR) denominated, outright sale or purchase of eligible securities with an agreement to repurchase or resell"
- **Grounding — related node (Page 6 / Section 6.1.9-6.1.11):** "repo term will be used commonly in this guideline referring to repo and reverse repo equivalently unless otherwise is specified."

### [[SARIE Interbank Express]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how a repo settlement must be executed, treat SARIE as the mandated payment rail rather than an optional channel: the Guidelines define SARIE (Saudi Arabian Riyal Interbank Express or any future instant payments system) in Section 6 and then require in Section 13 that fund transfers for both non-SAMA and SAMA-issued eligible securities be done through SARIE where both counterparties are licensed agents and the currency is SAR. This means for SAR-denominated repos between licensed agents, settlement of the cash leg outside SARIE is non-compliant; the alternative 'any agreed systems' route in 13.7 applies only where a counterparty is non-licensed or the currency is not SAR. Conclude that the settlement channel is dictated by counterparty licensing and currency, not party choice.
- **Grounding — this node (Page 6 / 6.1.14):** "SARIE: The Saudi Arabian Riyal Interbank Express or any other future instant payments system"
- **Grounding — related node (Page 10 / 13.5–13.6):** "delivery and fund transfer... must be done through Tadawul and SARIE, respectively... where both the counterparties being licensed agents and currency of transaction is SAR"

### [[Tadawul (Saudi Exchange)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing how eligible securities must be delivered in a repo, treat Tadawul (the Saudi Exchange) as the mandated delivery venue for non-SAMA-issued securities: the Guidelines define Tadawul in 6.1.16 and require in 13.5 that delivery of non-SAMA issued eligible securities be done through Tadawul where both counterparties are licensed agents and the currency is SAR. Note the split — SAMA-issued securities settle through SAMA (13.6), not Tadawul — so the correct delivery channel depends on the issuer of the security and the counterparties' licensing status. Conclude that you must classify each security by issuer before selecting the delivery mechanism, and cannot default all securities to Tadawul.
- **Grounding — this node (Page 6 / 6.1.16):** "Tadawul: Saudi Exchange"
- **Grounding — related node (Page 10 / 13.5–13.6):** "delivery and fund transfer of non-SAMA issued eligible securities with cash must be done through Tadawul and SARIE"

#graphify/document #graphify/EXTRACTED #community/Repurchase_Agreements #graphify/enriched
