---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Securitization IRB Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_IRB_Approach
  - graphify/enriched
---

# Tranched Credit Protection Decomposition

## Connections

### [[Securitization Internal Ratings-Based Approach (SEC-IRBA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's capital treatment for tranched credit protection on a securitization exposure, do not treat protected and unprotected slices as one position: paragraph 18.59 requires the original tranche to be decomposed into protected and unprotected sub-tranches, with each sub-tranche's capital requirement then set 'as determined by the hierarchy of approaches for securitization exposures' — which includes SEC-IRBA at the top of that hierarchy. The link tells you that SEC-IRBA is the calculation engine applied to each resulting sub-tranche where the bank qualifies to use it. You would conclude that eligibility and the KIRB inputs of SEC-IRBA must be re-tested at the sub-tranche level, not assumed from the parent tranche.
- **Grounding — this node (Page 250 / 18.59):** "In the case of tranched credit protection, the original securitization tranche will be decomposed into protected and unprotected sub-tranches"
- **Grounding — related node (Page 311 / Ch.22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB ... Calculation of risk weight"

### [[Treatment of Credit Risk Mitigation for Securitization Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank buys or sells credit protection on only part of a securitization tranche, do not treat the position as a single exposure: paragraphs 18.59-18.62 require the original tranche to be decomposed into protected and unprotected sub-tranches, each risk-weighted separately under the securitization hierarchy of approaches. This decomposition sits within the broader CRM treatment for securitization exposures (18.56-18.58), and recognition is conditional on the guarantee/credit-derivative operational requirements in 9.69-9.74 being met and the protection provider not being an SPE. Conclude that partial/tranched hedges give no automatic blanket relief — you must confirm the 18.56 conditions and calculate each sub-tranche, treating any lower-priority sub-tranche as non-senior.
- **Grounding — this node (Page 250 / Art 18.59):** "In the case of tranched credit protection, the original securitization tranche will be decomposed into protected and unprotected sub-tranches"
- **Grounding — related node (Page 250 / Art 18.57-18.58):** "the bank buying full (or pro rata) credit protection may recognize the credit risk mitigation on the securitization exposure in accordance with the CRM framework"

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
