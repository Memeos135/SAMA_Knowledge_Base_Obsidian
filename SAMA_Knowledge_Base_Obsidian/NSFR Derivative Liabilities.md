---
source_file: "markdown/SAMA_EN_3467_VER1.md"
type: "concept"
community: "LCR & NSFR Metrics"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/LCR__NSFR_Metrics
  - graphify/enriched
---

# NSFR Derivative Liabilities

## Connections

### [[Available Stable Funding (ASF)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating Available Stable Funding, note that NSFR derivative liabilities are integrated into the ASF side on a net basis: the ASF prudential-return table includes 'NSFR derivative liabilities net of NSFR derivative assets' as a category (with a 0% ASF factor), and the netting is computed against derivative assets per the Required Stable Funding section. Because the standard also assigns a 20% RSF factor to derivative liabilities — a discretion SAMA expressly declined to lower below the 5% floor — the same derivative positions appear on both ASF and RSF sides. Conclude that you must apply the netting rule and the fixed 20% factor as specified, and cannot lower it by invoking national discretion.
- **Grounding — this node (Page 15):** "The NSFR assigns a 20% "required stable funding" factor to derivative liabilities... SAMA has decided not to exercise this discretion."
- **Grounding — related node (Page 18 / Prudential Returns 1):** "NSFR derivative liabilities net of NSFR derivative assets if NSFR derivative li[abilities]... 0%"

### [[Circular 351000133367 (Leverage Ratio)]] — `cites` [EXTRACTED]
- **What this link tells you:** When computing NSFR derivative liabilities, you cannot treat the NSFR guidance as self-contained: it borrows the netting and margin conditions from the Leverage Ratio circular. The NSFR text expressly references paragraphs 20 and 24 of Circular No. 351000133367 (Basel III Leverage Ratio Framework) to determine when netting and cash variation margin may be applied to derivative replacement cost. Conclude that the eligibility of any bilateral netting or margin offset for the derivative-liability figure must be tested against that circular's conditions, not decided within the NSFR document alone.
- **Grounding — this node (Page 15 / item (d)):** "20% of derivative liabilities (i.e. negative replacement cost amounts) as calculated according to General Guidance Section A ... (before deducting variation margin posted)"
- **Grounding — related node (Page 10):** "conditions as specified in paragraphs 20 of the Circular No. 351000133367, titled ... Basel Ill Leverage Ratio Framework and Disclosure Requirements"

### [[NSFR Derivative Assets]] — `shares_data_with` [INFERRED]
- **What this link tells you:** These two items appear operationally linked because each is defined by reference to the other: NSFR derivative assets are measured net of NSFR derivative liabilities where assets exceed liabilities, and derivative liabilities are measured net of derivative assets in the opposite case. This mutual netting means the same replacement-cost inputs and margin treatment feed both figures, so they should be computed together, not independently. Because this 'shares data with' link is inferred, verify against Item #5 Sections A and B that the netting direction and the exclusion of collateral/variation margin have been applied consistently before relying on either figure.
- **Grounding — this node (Page 12 / item (c)):** "Net of NSFR derivative assets ... if NSFR derivative liabilities are greater than NSFR derivative assets"
- **Grounding — related node (Page 15 / item (b)):** "Net of NSFR derivative liabilities ... if NSFR derivative assets are greater than NSFR derivative liabilities"
- **Caveat:** Relationship is INFERRED from the reciprocal netting language; the source frames these as calculation inputs rather than a shared data store — confirm the netting mechanics in Item #5 before relying on the characterisation.

#graphify/concept #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
