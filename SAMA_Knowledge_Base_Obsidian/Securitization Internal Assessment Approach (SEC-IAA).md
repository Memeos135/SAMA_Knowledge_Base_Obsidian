---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Securitization Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Securitization Internal Assessment Approach (SEC-IAA)

## Connections

### [[ABCP Conduit  Programme|ABCP Conduit / Programme]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank holds securitization exposures to an ABCP programme (e.g. liquidity facilities or credit enhancements), the SEC-IAA is the specific capital route available for those conduit exposures — but only with prior SAMA approval and only if the bank has at least one approved IRB model and meets the operational requirements. This link tells you the two concepts are directly coupled: the IAA is essentially the internal-assessment mechanism designed for exposures extended to ABCP programmes, with internal assessments mapped to equivalent ECAI external ratings. Conclude that if you are evaluating ABCP-conduit exposures for capital, you must check SEC-IAA eligibility (SAMA notification and approval, IRB-model prerequisite, and the mapping-to-external-ratings requirement) before applying it.
- **Grounding — this node (Page 313 / 21.1):** "a bank may use its internal assessments of the credit quality of its securitization exposures extended to ABCP programmes (e.g. liquidity facilities and credit enhancements)"
- **Grounding — related node (Page 276 / 18.96):** "ABCP programme – the programme of commercial paper issued by an ABCP conduit"

### [[External Credit Assessment Institution (ECAI)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses the SEC-IAA for ABCP-programme securitisation exposures, ECAI standards remain the benchmark even though the assessment is internal, because internal assessments must be mapped to equivalent ECAI external ratings and be at least as conservative as major ECAIs' publicly available criteria. The reference tells you SEC-IAA is not a way to bypass external ratings — it borrows ECAI methodology and eligibility criteria and requires SAMA approval plus a validated IRB model. Conclude that you must demonstrate the internal-to-ECAI rating correspondence and conservatism to SAMA; the ECAI framework governs how the internal grades translate into risk weights.
- **Grounding — this node (Page 313 / 21.1):** "Internal assessments of exposures provided to ABCP programmes must be mapped to equivalent external ratings of an ECAI."
- **Grounding — related node (Page 314 / 21.x(5)-(6)):** "Internal assessments must correspond to the external ratings of ECAIs... must be at least as conservative as the publicly available rating criteria of the major ECAIs."

### [[Hierarchy of Securitization Approaches]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank holds securitization exposures to ABCP programmes (e.g. liquidity facilities or credit enhancements), note that SEC-IAA sits within the hierarchy of approaches but is not self-selecting: 21.1 requires the bank to notify SAMA and obtain approval, hold at least one approved IRB model, and map internal assessments to ECAI-equivalent ratings before using IAA. The hierarchy provisions (18.59-18.62) determine where IAA applies relative to other approaches. Conclude that IAA cannot be relied on absent SAMA approval and the stated operational preconditions, and its use must still be consistent with the hierarchy's ordering.
- **Grounding — this node (Page 313 / 21.1):** "banks shall notify SAMA of the transactions and seek approval to apply the IAA treatment ... provided that the bank has at least one approved IRB model"
- **Grounding — related node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62."

### [[SEC-ERBA (External Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When selecting a securitization capital approach, SEC-ERBA and SEC-IAA are alternative methods within the same securitization hierarchy, not interchangeable at will — the framework orders and conditions their use. SEC-IAA is restricted to ABCP-programme exposures and requires prior SAMA notification and approval plus at least one approved IRB model, whereas SEC-ERBA is the external-ratings method; both feed into the same risk-weight determination. Conclude that eligibility conditions govern which approach applies, and check the SEC-IAA approval prerequisites before assuming internal assessments can substitute for external ratings.
- **Grounding — this node (Page 313 / 21.1):** "banks shall notify SAMA of the transactions and seek approval to apply the IAA treatment ... provided that the bank has at least one approved IRB model"
- **Grounding — related node (Page 13 / Ch 20):** "External-ratings-based approach (SEC-ERBA) ... Operational requirements for use of external credit assessments"

### [[SEC-SA (Standardized Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge for ABCP-programme securitization exposures, understand that SEC-IAA maps internal assessments to external-rating equivalents which then feed the risk-weight calculation, while SEC-SA is the standardized fallback in the same securitization framework hierarchy. The two connect because IAA-derived rating equivalents and the SA formula sit within the same ordered method stack (SCRE18–SCRE22), so the approach used depends on eligibility rather than preference. Conclude that where IAA prerequisites are not met, you should verify whether SEC-SA (or another approach in the hierarchy) is the mandated fallback for that exposure.
- **Grounding — this node (Page 313 / 21.1):** "Internal assessments of exposures provided to ABCP programmes must be mapped to equivalent external ratings of an ECAI. Those rating equivalents are used to determine the [risk weight]"
- **Grounding — related node (Page 755):** "RWA for portfolios where standardised approaches are used (cell 1/b): RWA which result from applying the above-described standardised approach"
- **Caveat:** The direct textual cross-reference between SEC-IAA and SEC-SA is inferred from their shared position in the securitization framework hierarchy rather than an explicit citation; verify the ordering rules in the primary text before relying on SA as the fallback.

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
