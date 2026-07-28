---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "CCR & CVA Disclosure Templates"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/CCR__CVA_Disclosure_Templates
  - graphify/enriched
---

# Template CC1 - Composition of Regulatory Capital

## Connections

### [[Regulatory Capital]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying where 'regulatory capital' is quantified for disclosure, Template CC1 is the template that itemizes its composition — CET1, Tier 1, Tier 2 and the deductions (goodwill, DTAs, cross-holdings, TLAC-related items) that determine the reported figures. The link is textually supported: CC1's rows are precisely the regulatory-capital elements and SACAP-based deductions. Conclude that the defined term 'regulatory capital' as used across the framework maps to CC1's build-up, so any assessment of a bank's stated capital position should be checked against the CC1 line items rather than a summary number.
- **Grounding — this node (Page 770 / Template CC1):** "Provisions included in Tier 2 capital, calculated in accordance with SACAP2.2.3... Investments in own Tier 2 instruments, amount to be deducted"
- **Grounding — related node (Page 779):** "CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capital, total capital and TLAC requirements"

### [[SACAP - Capital Reforms Guidance]] — `references` [EXTRACTED]
- **What this link tells you:** When populating or auditing Template CC1's regulatory-capital line items, treat SACAP as the governing rule set for each deduction and inclusion: CC1's rows are expressly cross-referenced to specific SACAP provisions (e.g. goodwill per SACAP4.1.1, DTA per SACAP4.1.2, Tier 2 provisions per SACAP2.2.3, cross-holdings per SACAP4.1.6/4.1.7), so the correct amount for any CC1 row is determined by applying the cited SACAP clause. Conclude that CC1 is a reporting surface for SACAP's substantive capital-composition requirements, and that any figure disclosed must be justified against the referenced SACAP article rather than the template alone.
- **Grounding — this node (Page 770):** "Investments in own Tier 2 instruments, amount to be deducted from Tier 2 capital in accordance with SACAP4.1.6."
- **Grounding — related node (Page 769):** "Goodwill net of related tax liability, as set out in SACAP4.1.1 ... DTA that rely on future profitability ... as set out in SACAP4.1.2."

### [[Template CC2 - Reconciliation of Regulatory Capital to Balance Sheet]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's Pillar 3 capital-composition disclosures, treat CC1 and CC2 as a linked pair rather than standalone tables: CC1 sets out the composition of regulatory capital, while CC2 reconciles that regulatory-capital view back to the published balance sheet under the regulatory scope of consolidation. The framework mandates a three-step approach requiring banks to show the link between the balance sheet and the numbers disclosed in CC1, with CC2 as the reconciliation step. For a reviewer, this means CC1 figures cannot be validated in isolation — you would trace them to CC2 to confirm that capital elements reconcile to accounting figures and that any differences between accounting and regulatory consolidation scopes are explained.
- **Grounding — this node (Page 760 / 14.3.2):** "Template CC1 details the composition of a bank's regulatory capital."
- **Grounding — related node (Page 760 / 14.3.3 & 14.6):** "Template CC2 provides users of Pillar 3 data with a reconciliation between the scope of a bank's accounting consolidation ... and the scope of its regulatory consolidation."

### [[Template KM1 Key metrics|Template KM1: Key metrics]] — `references` [EXTRACTED]
- **What this link tells you:** When reconciling a bank's Pillar 3 disclosures, treat Template KM1 (key metrics) and Template CC1 (composition of regulatory capital) as directly cross-tied: specific KM1 cells must equal specific CC1 cells, so a discrepancy is a reporting defect, not a permitted difference. The document explicitly states these linkages (e.g. KM1:1/a equals CC1:29/a for CET1). Conclude that KM1 headline capital figures cannot be validated independently — they must trace back to the CC1 capital-composition build-up, and both are mandatory for all banks.
- **Grounding — this node (Page 769-770 / Template CC1):** "Composition of Regulatory Capital... amount to be deducted from CET1 capital calculated in accordance with SACAP4.2"
- **Grounding — related node (Page 747 / KM1 Instructions):** "Linkages across templates: Amount in [KM1:1/a] is equal to [CC1:29/a]... Amount in [KM1:2/a] is equal to [CC1:45/a]"

### [[Template PV1 - Prudent Valuation Adjustments]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing regulatory-capital composition, note that prudent valuation adjustments feed the CET1 deduction line in CC1 and are broken down separately in PV1: CC1 records prudent valuation adjustments per the Basel 'prudent valuation guidance,' and PV1 provides the constituent-element breakdown of those same PVAs under the same guidance. Both cite SAMA's supervisory guidance on assessing banks' financial instrument fair value practices, so they draw on a common valuation standard. For a reviewer, PV1's line-item detail is the supporting basis for the aggregate PVA amount reflected in the CC1 capital calculation, so the two should be read together to test that deductions are complete and correctly derived.
- **Grounding — this node (Page 769):** "Prudent valuation adjustments according to the requirements of Basel Framework "prudent valuation guidance" ... taking into account the guidance set out in Supervisory guidance for assessing banks' financial instrument fair value practices"
- **Grounding — related node (Page 786 / Template PV1):** "Provide a breakdown of the constituent elements of a bank's PVAs according to the requirements of Basel Framework "prudent valuation guidance""

### [[Template TLAC1 - TLAC Composition]] — `references` [EXTRACTED]
- **What this link tells you:** For a G-SIB reviewer, CC1 and TLAC1 are directly coupled at the resolution-group level: for single-point-of-entry G-SIBs where the resolution group coincides with the regulatory scope of consolidation, TLAC1 rows referring to regulatory capital before adjustments coincide with information provided under CC1. TLAC1 applies only to G-SIB resolution groups, whereas CC1 is mandatory for all banks, so the overlap holds only for that G-SIB subset. This means a reviewer can cross-check TLAC1's capital-element rows against CC1 for SPE G-SIBs, but for MPE G-SIBs should not expect aggregation across resolution groups to equal CC1 values.
- **Grounding — this node (Page 760 / 14.3.2):** "Template CC1 details the composition of a bank's regulatory capital."
- **Grounding — related node (Page 774 / Instructions):** "those rows that refer to regulatory capital before adjustments coincide with information provided under Template CC1. For MPE G-SIBs ... will not necessarily equal ... values reported ... under Template CC1."

#graphify/concept #graphify/EXTRACTED #community/CCR__CVA_Disclosure_Templates #graphify/enriched
