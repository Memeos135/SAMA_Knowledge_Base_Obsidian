---
source_file: "markdown/SAMA_EN_4041_VER1.md"
type: "concept"
community: "Operational Risk Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Operational_Risk_Capital
  - graphify/enriched
---

# The Standardized Approach

## Connections

### [[Business Indicator Component (BIC)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating minimum operational risk capital, the BIC is not a standalone metric — it is a required multiplicand in the Standardized Approach formula (ORC = BIC x ILM), so any dispute over the BIC calculation is a dispute over the capital charge itself. The framework defines the BIC via marginal coefficients on the Business Indicator and makes it the floor even where loss data is deficient (minimum 100% of BIC). A reader should conclude the BIC and the Standardized Approach cannot be assessed independently, and that BIC inputs directly drive regulatory capital adequacy.
- **Grounding — this node (Page 5 / sec 7.1):** "The Banks must calculate minimum ORC requirements based on the Standardized Approach by multiplying the BIC and the ILM: ORC = BIC x ILM"
- **Grounding — related node (Page 5 / sec 7.1):** "Business Indicator Component (BIC) is calculated as the sum of: (i) 12% of the Bank's BI..."

### [[Internal Loss Multiplier (ILM)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating operational risk capital, the ILM is the second required factor of the Standardized Approach (ORC = BIC x ILM) and is where a bank's own loss history feeds into the charge — so loss-data quality directly raises or lowers required capital. The framework ties the ILM to a 10-year (exceptionally 5-year) loss window and empowers SAMA to force an ILM greater than 1 where loss-data standards are unmet. A compliance reader should conclude that data-standard failures are not neutral: they can be penalised through a higher supervisory ILM and mandatory Pillar 3 disclosure.
- **Grounding — this node (Page 8 / sec 7.4.1):** "In such cases, SAMA may require the bank to apply an ILM which is greater than 1."
- **Grounding — related node (Page 7 / sec 7.3.1):** "A bank's internal operational risk loss experience affects the calculation of operational risk capital through the Internal Loss Multiplier (ILM)."

### [[Minimum Capital Requirements for Operational Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's operational risk capital charge, treat the Standardized Approach as the mandatory (and sole) methodology under this framework — the parent document builds all of its loss-data, threshold and exclusion rules around it. The document specifies operational loss data feeds directly into the standardized calculation (e.g. the SAR 44,600 inclusion threshold, treatment of credit/market-risk-related losses), meaning the collection rules are not optional housekeeping but capital-determining inputs. A compliance reader should conclude that any lapse in loss-data identification or scoping is a capital-adequacy issue, not merely a data-governance one.
- **Grounding — this node (Page 8 / sec 7.4):** "The proper identification, collection and treatment of internal loss data are essential prerequisites to capital calculation under the standardized approach."
- **Grounding — related node (Page 9 / sec 9):** "Operational risk losses related to market risk ... will therefore be subject to the standardized approach for operational risk."

### [[Operational Risk (Stress Testing)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** If you are reconciling a bank's operational-risk obligations, note these two provisions address different regimes: the Standardized Approach (4041) sets the Pillar 1 minimum capital calculation, whereas the operational-risk stress-testing rules (4226) sit within the ICAAP/supervisory-review process and feed additional capital planning. They appear related because both draw on the bank's past operational loss events, but the link is conceptual, not a cross-reference. A reader should treat them as complementary but distinct obligations — stress-test outcomes may drive capital add-ons beyond the standardized minimum — and check each document's primary text rather than assuming one satisfies the other.
- **Grounding — this node (Page 8 / sec 8):** "Internally generated loss data calculations used for regulatory capital purposes must be based on a 10-year observation period."
- **Grounding — related node (Page 30 / sec 7.5):** "Any additional capital requirements emanating from the outcome of operational risk stress tests should be taken into account in the capital planning process."
- **Caveat:** INFERRED / conceptually related — the shared subject is operational loss data, but the documents serve different capital regimes (Pillar 1 vs ICAAP stress testing) and do not cross-reference; verify scope in each primary text.

#graphify/concept #graphify/EXTRACTED #community/Operational_Risk_Capital #graphify/enriched
