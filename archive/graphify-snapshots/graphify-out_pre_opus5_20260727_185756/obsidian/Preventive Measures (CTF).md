---
source_file: "markdown/SAMA_EN_853_VER1.md"
type: "concept"
community: "AML/CTF BNPL Finance Rules"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/AML/CTF_BNPL_Finance_Rules
  - graphify/enriched
---

# Preventive Measures (CTF)

## Connections

### [[Due Diligence Measures]] — `shares_data_with` [INFERRED]
- **Why:** AML Due Diligence Measures (Art 7–8, SAMA_EN_791) and CTF Preventive Measures (Art 63–66, SAMA_EN_853) impose materially identical CDD/EDD data-collection obligations on FIs and DNFBPs — customer identity, risk profile, source of funds, beneficial ownership — meaning the same customer data set must simultaneously satisfy both regimes' requirements.
- **This node (Page 14 / Art 64):** "FIs and DNFBPs shall apply due diligence measures, and determine the extent of due diligence measures, on the basis of TF risks, to its customers and the business relationship, and shall apply enhanced due diligence measures when the TF risks are high."
- **Related node (Page 4 / Art 7):** "Apply due diligence measures to their customers… Determine the extent of due diligence measures based on the risks relation to a customer or business relationship. Where a higher risk of money laundering was identified, they shall apply enhanced due diligence measures."
- **Implication:** A unified KYC/CDD workflow and customer risk-scoring engine must capture and tag data attributes sufficient to satisfy both ML-risk and TF-risk assessments; separate ML and TF risk scores should be maintained per customer record so that EDD triggers under either regime are independently auditable.
- **Caveat:** The 'shares_data_with' relation is inferred from the structural and substantive overlap of the two regimes' CDD requirements rather than an explicit cross-reference between the two source documents; no article in either law directly cites the other for data-sharing purposes.

### [[Law on Combating the Financing of Terrorism]] — `references` [EXTRACTED]
- **Why:** Chapter Six of the CTF Law establishes the Preventive Measures regime (Articles 63–70), imposing binding CDD, record-keeping, EDD, and STR obligations on FIs, DNFBPs, and NPOs—these are the primary prophylactic controls through which the Law operationalises its TF-risk framework at the entity level.
- **This node (Page 14 / Article 63):** "FIs, DNFBPs, and NPOs shall identify, assess, understand and document its financing of terrorism risks, taking into account a wide range of risk factors, including those relating to its customers, countries or geographic areas, products, services, transactions and delivery chann…"
- **Related node (Page 1 / Chapter 1 (Definitions)):** "Terrorism Financing Crime: The financing of terrorist act or terrorist entity or a terrorist in any forms as set forth under this Law, including financing the travel and training of a terrorist individual."
- **Implication:** FIs must maintain a documented TF risk assessment (distinct from ML risk assessment) covering all customer, product, channel, and geographic dimensions, and must be able to produce it to supervisory authorities on request—a gap here would constitute a direct breach of Article 63 and expose the entity to monetary sanctions of up to SAR 5 million per violation.

#graphify/concept #graphify/INFERRED #community/AML/CTF_BNPL_Finance_Rules #graphify/enriched
