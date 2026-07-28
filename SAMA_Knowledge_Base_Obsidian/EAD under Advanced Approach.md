---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB CRM & Receivables"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_CRM__Receivables
  - graphify/enriched
---

# EAD under Advanced Approach

## Connections

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When validating a bank's own EAD estimates, treat the advanced-approach requirements as a specialization of the general EAD definition, not a substitute for it. Paragraph 16.88 defines EAD as the expected gross exposure upon default and sets a floor at current drawn amount, then focuses the advanced-approach requirements on off-balance-sheet items and requires estimates reflecting possible drawings up to and after default. Conclude that any A-IRB own-EAD estimate must still satisfy the base definition and the on-balance-sheet floor, and check that estimates are long-run default-weighted with an appropriate conservatism margin and are not capped to facility limits (16.95).
- **Grounding — this node (Page 206 / Para 16.89):** "Under the advanced approach, banks must assign an estimate of EAD for each eligible facility. It must be an estimate of the long-run default-weighted average EAD"
- **Grounding — related node (Page 206 / Para 16.88):** "EAD for an on-balance sheet or off-balance sheet item is defined as the expected gross exposure of the facility upon default of the obligor."

### [[Top-Down Approach for Purchased Corporate Receivables]] — `shares_data_with` [INFERRED]
- **What this link tells you:** If you are assessing capital treatment for purchased corporate receivables under the IRB framework, note that these two provisions belong to the same advanced-approach estimation regime but govern different asset situations — own-EAD estimation for facilities generally versus the top-down treatment for purchased receivable pools. The link appears to reflect that both operate within the advanced IRB approach and both address EAD estimation, but the 'shares_data_with' label is a weak, inferred connection rather than a stated cross-reference in the text. Before relying on this, verify in the primary text whether the top-down purchased-receivables chapter actually imports the own-EAD standards of paragraphs 16.88–16.95, since the two cover distinct eligibility and operational requirements.
- **Grounding — this node (Page 206 / Para 16.88):** "The additional minimum requirements for internal estimation of EAD under the advanced approach... focus on the estimation of EAD for off-balance sheet items"
- **Grounding — related node (Page 105 / Para 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available subject to certain operational requirements being met."
- **Caveat:** Relation is INFERRED and the 'shares_data_with' label is not textually supported; the two provisions merely sit within the same advanced IRB regime. Verify any actual cross-reference in the primary text.

#graphify/concept #graphify/EXTRACTED #community/IRB_CRM__Receivables #graphify/enriched
