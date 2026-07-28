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

# Retail Exposures

## Connections

### [[IRB Asset Classes]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the correct capital treatment for a bank's lending book, read the retail exposure rules as a sub-set nested inside the broader IRB asset-class taxonomy — the general categorisation provision names retail as one of the five broad asset classes and states three retail sub-classes exist, while the retail exposures provision supplies the actual scope tests and risk weights. This matters because the phased-rollout and 'all exposures within that asset class in that unit' constraint (para 10.45) attaches at the asset-class level, so classifying an exposure as retail pulls it under both the retail criteria and the asset-class adoption discipline. Conclude that you cannot apply retail risk weights (75%/45%/100%) without first confirming the exposure satisfies the asset-class definition and the granularity/threshold tests, and that adopting IRB for retail commits the whole retail class.
- **Grounding — this node (Page 39 / para 7.55):** "The retail exposure class excludes exposures within the real estate exposure class. The retail exposure class includes... Exposures to an individual person or persons"
- **Grounding — related node (Page 99 / para 10.4):** "The classes of assets are (a) corporate, (b) sovereign, (c) bank, (d) retail, and (e) equity... Within the retail asset class, three sub-classes are separately identified."

### [[Qualifying Revolving Retail Exposures (QRRE)]] — `references` [EXTRACTED]
- **What this link tells you:** When segmenting a retail portfolio for IRB capital, treat QRRE as one of the three mandatory retail sub-classes rather than a free-standing category — the retail asset-class provision requires banks to identify residential mortgages, QRRE and 'all other retail' separately, and the QRRE node supplies the cumulative eligibility criteria (revolving, unsecured, uncommitted) that a sub-portfolio must satisfy. This means an exposure only earns QRRE treatment if it first sits within the retail exposure class and then meets every QRRE criterion at sub-portfolio level. Conclude that failing any QRRE test does not eject the exposure from retail — it defaults to 'other retail', so verify both the retail scope and the QRRE conditions before applying the corresponding treatment.
- **Grounding — this node (Page 39 / para 7.56):** "the retail exposure class consists of the follow three sets of exposures: 'Regulatory retail' exposures that do not arise from exposures to 'transactors'"
- **Grounding — related node (Page 105 / para 10.21-10.22):** "three sub-classes of exposures: (1) Residential mortgage loans... (2) Qualifying revolving retail exposures... All of the following criteria must be satisfied for a sub-portfolio to be treated as a QRRE."

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
