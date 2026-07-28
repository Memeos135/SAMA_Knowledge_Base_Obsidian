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

# IRB Asset Classes

## Connections

### [[Corporate Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When categorising banking-book exposures for IRB, treat 'corporate' as one of the five defined asset classes, each with distinct risk characteristics and treatment rules. The corpus mandates that banks categorize exposures into corporate, sovereign, bank, retail and equity classes, and separately defines the scope of corporate exposures (incorporated entities, associations, funds etc., excluding individuals and other financial-institution classes). A reader assigning an exposure should first confirm it does not fall into another class before applying corporate treatment, since misclassification changes the applicable risk weights and available approaches.
- **Grounding — this node (Page 99 / 10.4):** "The classes of assets are (a) corporate, (b) sovereign, (c) bank, (d) retail, and (e) equity"
- **Grounding — related node (Page 30 / 7.37):** "The corporate exposure class does not include exposures to individuals. The corporate exposure class differentiates between the following subcategories"

### [[Equity Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding which IRB approach applies, note that equity is one of the five defined asset classes but is treated differently: the corpus expressly states the IRB approach is not permitted for the equity asset class. So a reader classifying an exposure as equity should not apply IRB modelling to it and must instead follow the separate treatment prescribed for equity holdings. This is a scope-limiting link — belonging to an asset class does not automatically entitle the bank to the IRB modelling framework.
- **Grounding — this node (Page 99 / 10.4):** "For the equity asset class, the IRB approach is not permitted, as outlined further below"
- **Grounding — related node (Page 10 (Contents)):** "Equity exposures 104"
- **Caveat:** Node B's provided context (CRB-A / CR3 pages) does not directly cover equity-exposure IRB treatment; the exclusion is grounded in node A's text. Verify the dedicated equity-exposure provisions before relying.

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how a bank must apply the IRB approach, treat asset-class categorization as the mandatory entry gate, not an afterthought: the IRB rules operate by requiring banks to sort banking-book exposures into corporate, sovereign, bank, retail and equity classes, and rollout obligations attach at the asset-class level. Because 10.4 fixes the taxonomy and 10.44–10.46 require that adoption of IRB for an asset class in a business unit be applied to ALL exposures in that class in that unit under a SAMA-agreed plan, the two provisions are read together to scope the obligation. A compliance reviewer should conclude that IRB commitments cannot be cherry-picked within an asset class, and that the equity class is excluded from IRB entirely.
- **Grounding — this node (Page 99 / 10.4):** "banks must categorize banking-book exposures into broad classes of assets... (a) corporate, (b) sovereign, (c) bank, (d) retail, and (e) equity."
- **Grounding — related node (Page 113 / 10.45):** "when a bank adopts an IRB approach for an asset class within a particular business unit, it must apply the IRB approach to all exposures within that asset class in that unit."

### [[Qualifying Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying purchased receivables, recognise this is a cross-cutting treatment that 'straddles two asset classes' — it applies within both the corporate and retail asset classes rather than being a standalone class, subject to eligibility and operational conditions. The corpus lists corporate and retail purchased receivables as distinct roll-out categories and permits a top-down approach only where the receivables meet arm's-length, third-party and other conditions. A reader should therefore confirm both the underlying asset class (corporate vs retail, which dictates F-IRB vs A-IRB availability) and the specific eligibility criteria before applying purchased-receivables treatment.
- **Grounding — this node (Page 99 / 10.4):** "Within the corporate and retail asset classes, a distinct treatment for purchased receivables may also apply provided that certain conditions are met"
- **Grounding — related node (Page 112 / 10.42):** "The treatment potentially straddles two asset classes. For eligible corporate receivables, both a foundation and advanced approach are available"

### [[Retail Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the correct capital treatment for a bank's lending book, read the retail exposure rules as a sub-set nested inside the broader IRB asset-class taxonomy — the general categorisation provision names retail as one of the five broad asset classes and states three retail sub-classes exist, while the retail exposures provision supplies the actual scope tests and risk weights. This matters because the phased-rollout and 'all exposures within that asset class in that unit' constraint (para 10.45) attaches at the asset-class level, so classifying an exposure as retail pulls it under both the retail criteria and the asset-class adoption discipline. Conclude that you cannot apply retail risk weights (75%/45%/100%) without first confirming the exposure satisfies the asset-class definition and the granularity/threshold tests, and that adopting IRB for retail commits the whole retail class.
- **Grounding — this node (Page 99 / para 10.4):** "The classes of assets are (a) corporate, (b) sovereign, (c) bank, (d) retail, and (e) equity... Within the retail asset class, three sub-classes are separately identified."
- **Grounding — related node (Page 39 / para 7.55):** "The retail exposure class excludes exposures within the real estate exposure class. The retail exposure class includes... Exposures to an individual person or persons"

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
