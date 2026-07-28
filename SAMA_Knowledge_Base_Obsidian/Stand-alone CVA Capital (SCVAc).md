---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "Basic Approach CVA"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Basic_Approach_CVA
  - graphify/enriched
---

# Stand-alone CVA Capital (SCVAc)

## Connections

### [[Basic Approach for CVA (BA-CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a BA-CVA capital figure, understand that Stand-alone CVA capital (SCVAc) is the per-counterparty building block from which the BA-CVA total is aggregated. The reduced version of BA-CVA computes the charge by summing each counterparty's SCVAc contribution and applying the 0.65 discount scalar, so SCVAc is definitionally part of the BA-CVA calculation. A reviewer checking a BA-CVA number should trace it back to correctly determined counterparty-level SCVAc inputs before accepting the aggregate.
- **Grounding — this node (Page 90):** "SCVAc is the CVA capital requirement that counterparty c would [contribute]"
- **Grounding — related node (Page 90 / Art 11.14):** "The capital requirement for CVA risk under the reduced version of the BA-CVA ... where the discount scalar ... = 0.65 ... summations are taken over all counterparties"
- **Caveat:** Node B's defining formula text is partly OCR-garbled; the SCVAc definition is inferred from the reduced BA-CVA summation. Confirm the exact SCVAc formula in the primary text.

### [[CVA Supervisory Risk Weights]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's CVA capital charge under the SA-CVA, treat the supervisory risk weights and the stand-alone CVA capital (SCVAc) as parts of a single calculation chain rather than separate items: the delta/vega sensitivities against each risk-class risk factor feed the capital requirement that SCVAc aggregates for the CVA portfolio. Both derive from the same Chapter 11 framework, which sets the CVA portfolio on a standalone basis (para 11.6) and prescribes the sensitivity-based procedures (11.47-11.53). For a compliance review, conclude that you cannot validate the SCVAc figure without confirming the risk-weight inputs and sensitivity computations were applied per the framework's specified shifts.
- **Grounding — this node (Page 87 / 11.6):** "The CVA risk capital requirement is calculated for a bank's "CVA portfolio" on a standalone basis."
- **Grounding — related node (Page 104 / 11.47):** "For each risk class, (i) the sensitivity of the aggregate CVA ... and (ii) the sensitivity of the market value of all eligible hedging instruments ... to each risk factor k in the risk class are calculated."

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's total counterparty-credit-risk capital under this framework, treat EAD and the CVA charge as two distinct but connected outputs rather than one figure. EAD (Chapter 5–8) quantifies exposure to default, while the CVA capital requirement—of which SCVAc is the stand-alone per-counterparty component under the reduced BA-CVA—captures losses from changing CVA values driven by counterparty spread and market moves; both apply to the same covered derivative and SFT populations. For a compliance decision, conclude that a bank in scope must compute and hold capital for both, and that recognizing collateral or hedges in one calculation constrains what can be recognized in the other (e.g. LGD limits when collateral is in EAD).
- **Grounding — this node (Page 87 / 11.5–11.6):** "The capital requirement for CVA risk must be calculated by all banks involved in covered transactions... The CVA risk capital requirement is calculated for a bank's 'CVA portfolio' on a standalone basis."
- **Grounding — related node (Page 50 / 7.8):** "To the extent that a bank recognizes collateral in EAD via current exposure, a bank would not be permitted to recognize the benefits in its estimates of loss given-default (LGD)."

#graphify/concept #graphify/EXTRACTED #community/Basic_Approach_CVA #graphify/enriched
