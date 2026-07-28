---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "IRB Credit Risk Approach"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Supervisory Haircuts (Table 14)

## Connections

### [[Comprehensive Approach (Collateral)]] — `references` [EXTRACTED]
- **What this link tells you:** When using the comprehensive approach to recognise collateral, the supervisory haircut table is the mandatory input: the rule text itself states the comprehensive approach is applied 'with standard supervisory haircuts,' so the haircut schedule directly governs how much collateral value can be recognised. This link tells you the comprehensive approach cannot be operated independently of the prescribed haircuts. When calculating adjusted collateral value, apply the standard supervisory haircuts (subject to any currency-mismatch and holding-period adjustments) rather than unadjusted market values.
- **Grounding — this node (Page 879 (SAMA_EN_3487)):** "The averages are calculated after the application of any haircuts, inflow and outflow rates and caps, where applicable."
- **Grounding — related node (Page 755 (SAMA_EN_3487)):** "the comprehensive approach with standard supervisory haircuts."
- **Caveat:** Node B is labelled 'Supervisory Haircuts (Table 14)' but the provided context pages (LCR haircuts, slotting, commodities) do not clearly contain the CRM supervisory-haircut table; verify the actual Table 14 haircut values in the primary text before relying on specific figures.

### [[Minimum Holding Periods (Table 15)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating collateral haircuts under the comprehensive approach, treat Table 15's minimum holding periods as an input that scales Table 14's supervisory haircuts — they are used together, not independently. Paragraph 9.55-9.56 states that different transaction types (repo-style five days, other capital-market ten days, secured lending twenty days) require different holding periods and thus different haircuts, so the haircut magnitude depends on the applicable holding period and remargining/revaluation frequency. Conclude that a bank cannot apply Table 14 haircuts without first classifying the transaction and selecting the correct holding period, and must adjust haircuts where remargining/revaluation is less frequent than the standard.
- **Grounding — this node (Page 83 (Table 14 context)):** "paraphrase: supervisory collateral haircuts applied under the comprehensive approach, scaled by the minimum holding period"
- **Grounding — related node (Page 83 / 9.55–9.56):** "different holding periods and thus different haircuts must be applied ... The minimum holding period for various products is summarized in table 15"
- **Caveat:** Node B's provided context (Pages 879/192/594) does not contain the Table 14 haircut text; the link to holding periods rests on the paragraph 9.55–9.56 framework — verify Table 14 in the primary source before relying on specific haircut values.

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
