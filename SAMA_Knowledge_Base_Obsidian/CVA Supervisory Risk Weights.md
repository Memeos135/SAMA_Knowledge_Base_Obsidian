---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "document"
community: "Basic Approach CVA"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Basic_Approach_CVA
  - graphify/enriched
---

# CVA Supervisory Risk Weights

## Connections

### [[Basic Approach for CVA (BA-CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** The linked node here is the SA-CVA supervisory risk-weight/sensitivity machinery (delta and vega sensitivities), which belongs to the SA-CVA calculation, not BA-CVA. For a compliance reviewer, the practical point is that the two approaches use different inputs: BA-CVA works from counterparty-level supervisory weights and hedge recognition, while the sensitivity-based supervisory risk weights (11.46–11.53) apply to banks approved for SA-CVA. Confirm which approach a bank is actually approved for before deciding which risk-weight provisions govern its capital number.
- **Grounding — this node (Page 104 / Art 11.47):** "A bank may use AAD and similar computational techniques to calculate CVA sensitivities under the SA-CVA if doing so is consistent..."
- **Grounding — related node (Page 87 / Art 11.7):** "the standardized approach (SA-CVA) and the basic approach (BA-CVA). Banks must use the BA-CVA unless they receive approval..."
- **Caveat:** The 'CVA Supervisory Risk Weights' node content shown (11.46-11.53 sensitivities) is SA-CVA machinery; the link to BA-CVA is via the shared Chapter 11 regime rather than a direct BA-CVA computation. Verify the primary text before treating these risk weights as applicable to a BA-CVA bank.

### [[Stand-alone CVA Capital (SCVAc)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's CVA capital charge under the SA-CVA, treat the supervisory risk weights and the stand-alone CVA capital (SCVAc) as parts of a single calculation chain rather than separate items: the delta/vega sensitivities against each risk-class risk factor feed the capital requirement that SCVAc aggregates for the CVA portfolio. Both derive from the same Chapter 11 framework, which sets the CVA portfolio on a standalone basis (para 11.6) and prescribes the sensitivity-based procedures (11.47-11.53). For a compliance review, conclude that you cannot validate the SCVAc figure without confirming the risk-weight inputs and sensitivity computations were applied per the framework's specified shifts.
- **Grounding — this node (Page 104 / 11.47):** "For each risk class, (i) the sensitivity of the aggregate CVA ... and (ii) the sensitivity of the market value of all eligible hedging instruments ... to each risk factor k in the risk class are calculated."
- **Grounding — related node (Page 87 / 11.6):** "The CVA risk capital requirement is calculated for a bank's "CVA portfolio" on a standalone basis."

#graphify/document #graphify/EXTRACTED #community/Basic_Approach_CVA #graphify/enriched
