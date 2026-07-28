---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Securitization Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# External Credit Assessment Institution (ECAI)

## Connections

### [[External Credit Risk Assessment Approach (ECRA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining risk weights for exposures under the standardised credit risk framework, you cannot treat the choice of ECAI as separate from the ECRA methodology, because ECRA is the approach that consumes ECAI ratings to assign risk weights, and only ratings from ECAIs meeting the chapter 8 eligibility criteria may be used. The reference tells you that an ECAI must satisfy SAMA's recognition conditions (resources, credibility, cooperation, public-availability of methodology) before its ratings feed the ECRA calculation. Conclude that you must verify the rating source is a SAMA-eligible ECAI first, then confirm the ECRA mapping applies — an ineligible or private rating disqualifies the exposure from ECRA treatment.
- **Grounding — this node (Page 61 / 8.3(7)):** "ECAIs should notify SAMA of significant changes to methodologies and provide access to external ratings... to support initial and continued determination of eligibility."
- **Grounding — related node (Page 755):** "The standardised approach for credit risk. When calculating the degree of credit risk mitigation, banks must use the simple approach or the comprehensive approach with standard supervisory haircuts."

### [[SEC-ERBA (External Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising securitisation exposures under SEC-ERBA, the eligibility and operational status of the ECAI is a gating condition, because SEC-ERBA is an external-ratings-based approach whose risk weights derive directly from eligible external credit assessments and inferred ratings. The reference points you to the operational requirements for use of external credit assessments, which incorporate the chapter 8 ECAI recognition criteria (including that securitisation ratings be publicly available, non-selective and free of charge). Conclude that a rating available only to transaction parties, or from a non-eligible ECAI, cannot support SEC-ERBA treatment; verify public availability and ECAI eligibility before applying it.
- **Grounding — this node (Page 309 / 8.3(3) exception):** "an eligible credit assessment... must be publicly available, on a non-selective basis and free of charge... ratings made available only to the parties to a transaction do not satisfy this requirement."
- **Grounding — related node (Page 13 / Ch.20):** "Securitization: External-ratings-based approach (SEC-ERBA)... Operational requirements for use of external credit assessments... Operational requirements for inferred ratings."

### [[Securitization Internal Assessment Approach (SEC-IAA)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses the SEC-IAA for ABCP-programme securitisation exposures, ECAI standards remain the benchmark even though the assessment is internal, because internal assessments must be mapped to equivalent ECAI external ratings and be at least as conservative as major ECAIs' publicly available criteria. The reference tells you SEC-IAA is not a way to bypass external ratings — it borrows ECAI methodology and eligibility criteria and requires SAMA approval plus a validated IRB model. Conclude that you must demonstrate the internal-to-ECAI rating correspondence and conservatism to SAMA; the ECAI framework governs how the internal grades translate into risk weights.
- **Grounding — this node (Page 314 / 21.x(5)-(6)):** "Internal assessments must correspond to the external ratings of ECAIs... must be at least as conservative as the publicly available rating criteria of the major ECAIs."
- **Grounding — related node (Page 313 / 21.1):** "Internal assessments of exposures provided to ABCP programmes must be mapped to equivalent external ratings of an ECAI."

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
