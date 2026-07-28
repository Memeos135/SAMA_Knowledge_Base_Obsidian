---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB Default & Provisions"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_Default__Provisions
  - graphify/enriched
---

# Risk Quantification

## Connections

### [[Assessing Effect of Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital treatment for credit derivatives, you must read the eligibility/recognition rules together with the quantification rules, because the framework explicitly routes ineligible nth-to-default derivatives to the risk-weight aggregation treatment in paragraph 7.94 (and 7.95). Paragraph 9.77 states that first-to-default and other nth-to-default derivatives are not eligible credit risk mitigation and therefore give no capital relief, cross-referencing the aggregation-of-risk-weights quantification method. For a compliance decision, conclude that a credit derivative failing the CRM eligibility test cannot reduce RWA and must instead be capitalized under the aggregation rules — check paragraphs 7.94–7.95 and 9.76–9.78 together, not in isolation.
- **Grounding — this node (Page 88 / Para 9.77):** "are not eligible as a credit risk mitigation technique and therefore cannot provide any regulatory capital relief... it shall apply the treatment described in paragraph 7.94"
- **Grounding — related node (Page 48 / Para 7.95):** "the risk weights of the assets included in the basket must be aggregated up to a maximum of 1250% and multiplied by the nominal amount of the protection provided"

### [[Assessing Effect of Guarantees]] — `references` [EXTRACTED]
- **What this link tells you:** When reflecting the risk-mitigating effect of guarantees under A-IRB, you must apply the guarantee-specific quantification standards as part of the overall risk-quantification regime, because the option to adjust PD or LGD for guarantees is available only where the bank is approved to use its own LGD estimates and must be applied consistently. Paragraphs 16.99–16.100 require both borrower and guarantor to be assigned ratings and monitored, and require retaining information on the exposure absent the guarantee — an integral part of the quantification minimum requirements. For a compliance decision, conclude that guarantee recognition through PD/LGD adjustment is conditional on own-LGD approval and consistent rating of guarantors, and verify these standalone conditions before assuming guarantee relief is available in your parameter estimates.
- **Grounding — this node (Page 178 / Para 16.4):** "reasonably accurate and consistent quantitative estimates of risk"
- **Grounding — related node (Page 211 / Para 16.99):** "When a bank uses its own estimates of LGD, it may reflect the risk-mitigating effect of guarantees through an adjustment to PD or LGD estimates. The option... is available only to those banks that have been approved to use their own internal estimates of LGD"

### [[Definition of Default]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying IRB risk parameters you cannot use an internal or ad hoc default trigger, because the framework mandates that PD, and where relevant LGD and EAD, be estimated using the same reference definition of default set out in the definition-of-default provisions. Paragraph 16.71 expressly ties actual default recording and parameter estimation to that reference definition, permitting external data only subject to the mapping conditions. For a compliance decision, conclude that your quantification inputs must be reconciled to the reference default definition (including the unlikeliness-to-pay indicators and the retail facility-level option in 16.70) and verify that any external data has been mapped consistently before relying on the estimates.
- **Grounding — this node (Page 173 / Para 14.12):** "Credit risk mitigants will be recognized generally using the same type of framework as set forth in paragraphs 12.21 to 12.28"
- **Grounding — related node (Page 199 / Para 16.71):** "A bank must also use the reference definition for its estimation of PDs, and (where relevant) LGDs and EADs"
- **Caveat:** Node B's tagged context spans several quantification/CRM pages; the definition-of-default linkage is grounded in 16.71, but confirm the exact quantification paragraphs (16.x PD/LGD/EAD standards) that consume the default definition.

### [[Minimum Requirements to Use IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When evaluating a bank's own estimates of PD, LGD and EAD, read risk quantification (Section 7) as an integral part of the IRB minimum requirements, not a standalone modelling exercise — the framework's structure places Section 7 within Chapter 16 and paragraph 16.61 states it 'addresses the broad standards for own-estimates of PD, LGD, and EAD.' The practical consequence is that a bank on the advanced approach that fails the quantification standards cannot use its own LGD/EAD and is pushed back to supervisory estimates. Conclude that IRB eligibility for a given parameter is contingent on meeting Section 7's estimation standards, and check quantification compliance parameter-by-parameter before accepting own-estimate use.
- **Grounding — this node (Page 197 / 16.61-16.62):** "This section addresses the broad standards for own-estimates of PD, LGD, and EAD ... banks that do not meet the requirements ... must use the supervisory estimates"
- **Grounding — related node (Page 3 / Ch.16):** "Section 7: risk quantification 197"

### [[Own-EAD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may use A-IRB own-EAD estimates, treat the EAD estimation standards as a subset of the broader risk-quantification minimum requirements rather than a standalone rule, because both sit within the same IRB minimum-requirement chapter governing quantification of PD/LGD/EAD. Paragraphs 16.88–16.95 impose specific EAD constraints (floor at current drawn amount, reflecting additional drawings up to and after default, no capping of reference data), which operationalize the general quantification objective that estimates be reasonably accurate and conservative. For a compliance decision, conclude that own-EAD use requires meeting these detailed standards on top of the general quantification requirements — check the EAD-specific paragraphs (including the ULF instability and no-capping rules) before assuming an EAD model qualifies.
- **Grounding — this node (Page 178 / Para 16.4):** "reasonably accurate and consistent quantitative estimates of risk... consistent with internal use of these estimates"
- **Grounding — related node (Page 206 / Para 16.88):** "banks must estimate EAD at no less than the current drawn amount... estimates of EAD should reflect the possibility of additional drawings by the borrower up to and after the time a default event is triggered"

### [[Own-LGD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's advanced-IRB LGD model meets SAMA requirements, treat the own-LGD estimation standards as a sub-component of the broader Risk Quantification section rather than a standalone rule set. Section 7 (Risk Quantification) sets the overarching estimation standards for PD, LGD and EAD, and expressly cross-refers own-LGD estimation to paragraphs 16.82–16.87, so the specific guarantee/collateral treatment for own-LGD inherits the general requirements (representativeness, conservatism, use test). You would therefore verify the LGD estimates against both the specific own-LGD paragraphs and the general Section 7 estimation principles before concluding compliance.
- **Grounding — this node (Page 197 / 16.61-16.62):** "This section addresses the broad standards for own-estimates of PD, LGD, and EAD... Banks on the advanced approach must estimate an appropriate LGD (as defined in paragraphs 16.82 to 16.87)"
- **Grounding — related node (Page 211 / 16.99):** "When a bank uses its own estimates of LGD, it may reflect the risk-mitigating effect of guarantees through an adjustment to PD or LGD estimates."

### [[PD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping IRB eligibility, read the PD estimation requirements as one mandatory element within the Risk Quantification section, not a discrete obligation. Section 7 requires all IRB banks to estimate a PD for each borrower grade or retail pool and points to the specific PD paragraphs (16.76–16.81), meaning the PD-specific rules are subordinate to and read together with the general estimation standards (long-run averages, data representativeness, conservatism). You should therefore check PD estimates against both the dedicated PD paragraphs and the umbrella Section 7 principles when confirming a bank's IRB compliance.
- **Grounding — this node (Page 197 / 16.61-16.62):** "Generally, all banks using the IRB approaches must estimate a PD for each internal borrower grade... PD estimates must be a long-run average of one-year default rates"
- **Grounding — related node (Page 178 / 16.6):** "all IRB banks must produce their own estimates of probability of default (PD) and must adhere to the overall requirements for... estimation and validation of PD measures"

#graphify/concept #graphify/EXTRACTED #community/IRB_Default__Provisions #graphify/enriched
