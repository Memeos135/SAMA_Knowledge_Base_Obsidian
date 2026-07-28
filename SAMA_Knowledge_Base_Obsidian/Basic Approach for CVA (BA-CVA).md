---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Basic Approach for CVA (BA-CVA)

## Connections

### [[CVA Supervisory Risk Weights]] — `references` [EXTRACTED]
- **What this link tells you:** The linked node here is the SA-CVA supervisory risk-weight/sensitivity machinery (delta and vega sensitivities), which belongs to the SA-CVA calculation, not BA-CVA. For a compliance reviewer, the practical point is that the two approaches use different inputs: BA-CVA works from counterparty-level supervisory weights and hedge recognition, while the sensitivity-based supervisory risk weights (11.46–11.53) apply to banks approved for SA-CVA. Confirm which approach a bank is actually approved for before deciding which risk-weight provisions govern its capital number.
- **Grounding — this node (Page 87 / Art 11.7):** "the standardized approach (SA-CVA) and the basic approach (BA-CVA). Banks must use the BA-CVA unless they receive approval..."
- **Grounding — related node (Page 104 / Art 11.47):** "A bank may use AAD and similar computational techniques to calculate CVA sensitivities under the SA-CVA if doing so is consistent..."
- **Caveat:** The 'CVA Supervisory Risk Weights' node content shown (11.46-11.53 sensitivities) is SA-CVA machinery; the link to BA-CVA is via the shared Chapter 11 regime rather than a direct BA-CVA computation. Verify the primary text before treating these risk weights as applicable to a BA-CVA bank.

### [[Credit Valuation Adjustment (CVA) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which CVA capital method applies, start from the default rule: BA-CVA is the mandatory approach under the CVA framework unless SAMA has granted approval to use SA-CVA. Chapter 11 (11.7) establishes the two available approaches and expressly makes BA-CVA the fallback, so the BA-CVA node is a subordinate method within the overarching CVA framework. Conclude that a bank may only rely on SA-CVA where it holds documented SAMA approval; otherwise it must apply BA-CVA (or, below the 446 billion SAR non-centrally-cleared notional threshold, the permitted alternative treatment).
- **Grounding — this node (Page 87 / 11.7):** "Banks must use the BA-CVA unless they receive approval from Saudi Central Bank (SAMA) to use the SA-CVA."
- **Grounding — related node (Page 86 / 11.1):** "11. Credit Valuation Adjustment (CVA) Framework ... The risk-weighted assets for Credit Value Adjustment risk are determined by multiplying the capital requirements..."

### [[Eligible CVA Hedges]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's BA-CVA capital number, check whether it recognizes hedges, because hedge recognition is only permitted for hedges meeting the Framework's eligibility criteria and only under the full version of BA-CVA. Art 11.10 ties eligibility of CVA hedges specifically to paragraphs 11.17–11.19 for BA-CVA, and the reduced version eliminates hedging recognition entirely. A reviewer should conclude that a bank claiming hedge offsets under BA-CVA must be using the full version and must demonstrate each hedge meets the stated eligibility conditions; unrecognized or ineligible hedges cannot reduce the BA-CVA charge.
- **Grounding — this node (Page 90 / Art 11.14):** "The reduced version eliminates the element of hedging recognition from the full version."
- **Grounding — related node (Page 89 / Art 11.10):** "Eligibility criteria for CVA hedges are specified in 11.17 to 11.19 for the BA-CVA and in 11.37 to 11.39 for the SA-CVA."

### [[Stand-alone CVA Capital (SCVAc)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a BA-CVA capital figure, understand that Stand-alone CVA capital (SCVAc) is the per-counterparty building block from which the BA-CVA total is aggregated. The reduced version of BA-CVA computes the charge by summing each counterparty's SCVAc contribution and applying the 0.65 discount scalar, so SCVAc is definitionally part of the BA-CVA calculation. A reviewer checking a BA-CVA number should trace it back to correctly determined counterparty-level SCVAc inputs before accepting the aggregate.
- **Grounding — this node (Page 90 / Art 11.14):** "The capital requirement for CVA risk under the reduced version of the BA-CVA ... where the discount scalar ... = 0.65 ... summations are taken over all counterparties"
- **Grounding — related node (Page 90):** "SCVAc is the CVA capital requirement that counterparty c would [contribute]"
- **Caveat:** Node B's defining formula text is partly OCR-garbled; the SCVAc definition is inferred from the reduced BA-CVA summation. Confirm the exact SCVAc formula in the primary text.

### [[Template CVA1 Reduced Basic Approach BA-CVA|Template CVA1: Reduced Basic Approach BA-CVA]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When determining whether Template CVA1 disclosure applies to your bank, treat it as the reporting counterpart of the substantive BA-CVA capital rule: the template only captures RWA from netting sets measured under the reduced BA-CVA, and the calculation mandate itself sits in SAMA's CCR framework (para 11.7), which requires banks to use the BA-CVA unless approved for SA-CVA. The link appears strong because CVA1 explicitly references SCCR11.14 as the source of its component figures, but the disclosure document does not itself set the capital methodology. Conclude that scoping CVA1 requires first confirming BA-CVA (reduced variant) is the approach applied, and that the authoritative calculation rules — including the 446 billion SAR materiality carve-out — live in SAMA_EN_4283, not in the template.
- **Grounding — this node (Page 87 / para 11.7):** "Banks must use the BA-CVA unless they receive approval from Saudi Central Bank (SAMA) to use the SA-CVA."
- **Grounding — related node (Page 115 / Template CVA1):** "The template is mandatory for banks having part or all of their RWA for CVA risk measured according to the reduced BA-CVA."
- **Caveat:** Relation is INFERRED: CVA1 cites SCCR11.14 for its inputs, but the direct textual bridge to SAMA_EN_4283 is by cross-reference rather than an explicit named link; verify the SCCR11 paragraphs before relying on the mapping.

#graphify/document #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
