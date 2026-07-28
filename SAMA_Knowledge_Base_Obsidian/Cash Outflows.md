---
source_file: "markdown/SAMA_EN_3417_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Cash Outflows

## Connections

### [[Retail Deposit Run-off]] — `references` [EXTRACTED]
- **What this link tells you:** When building the outflow side of the LCR, retail deposit run-off is one of the specific categories whose balances are multiplied by prescribed run-off rates to produce total expected cash outflows. The standard sets differentiated rates — 3%/5% for stable insured deposits, minimum 10% and higher for less stable buckets — and lets supervisors add jurisdiction-specific buckets. You should therefore verify how SAMA has set the national retail run-off parameters (transparent and publicly available per para 70) and default deposits to 'less stable' buckets where stability criteria cannot be evidenced.
- **Grounding — this node (Page 26 / para 69):** "Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off"
- **Grounding — related node (Page 28 / para 79-80):** "Supervisory authorities are expected to develop additional buckets with higher run-off rates... with a minimum run-off rate of 10%"

### [[Secured Funding Run-off]] — `references` [EXTRACTED]
- **What this link tells you:** Secured funding run-off is another prescribed outflow category feeding the total expected cash outflows in the LCR. For secured funding transactions maturing within 30 days, the outflow is calculated on the amount of funds raised (not collateral value), with factors driven by the quality of the underlying collateral — notably 0% against Level 1 assets. You should conclude that repo, reverse-repo, collateral swaps and customer short positions must be mapped to the relevant collateral-based factor, and not double-counted with other outflow categories.
- **Grounding — this node (Page 26 / para 69):** "Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off"
- **Grounding — related node (Page 34 / para 113-114):** "The amount of outflow is calculated based on the amount of funds raised through the transaction, and not the value of the underlying collateral"

### [[Total Net Cash Outflows]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the LCR denominator for a SAMA-supervised bank, treat 'Cash Outflows' as a component of, not a synonym for, 'Total Net Cash Outflows': the net figure is total expected outflows minus capped inflows over the 30-day stress horizon. Paragraph 69 defines the net measure and its inflow cap at 75% of total expected outflows, so gross outflow categories feed directly into it. You should conclude that any outflow category (retail, wholesale, secured, derivatives) must be aggregated and then netted against eligible inflows, subject to the 75% floor on inflow offset, before assessing LCR compliance.
- **Grounding — this node (Page 26 / para 69):** "Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off"
- **Grounding — related node (Page 26 / para 69):** "total net cash outflows... is defined as the total expected cash outflows minus total expected cash inflows in the specified stress scenario for the subsequent 30 calendar days"

### [[Unsecured Wholesale Funding Run-off]] — `references` [EXTRACTED]
- **What this link tells you:** Unsecured wholesale funding run-off is a defined outflow category contributing to total expected cash outflows, with run-off factors that turn on the counterparty type and operational relationship (e.g. 40%, reduced to 20% if fully insured, and 100% for other legal-entity customers). Note the definition captures liabilities from non-natural persons callable within 30 days, expressly excluding derivative obligations. You should classify each funding source by counterparty and operational status to apply the correct factor, and check that debt securities are only re-categorised as retail where the stated distribution limitations are met.
- **Grounding — this node (Page 26 / para 69):** "Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off"
- **Grounding — related node (Page 29 / para 85):** "'unsecured wholesale funding' is defined as those liabilities and general obligations that are raised from non-natural persons... Obligations related to derivative contracts are explicitly excluded"

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
