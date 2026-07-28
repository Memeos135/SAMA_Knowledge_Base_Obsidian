---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "Real Estate Credit Mitigation"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Real_Estate_Credit_Mitigation
  - graphify/enriched
---

# Credit Risk Mitigation Framework

## Connections

### [[Collateralized Transactions]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital relief on collateralized dealings (repo-style, OTC derivatives, margin lending, secured lending), read these transaction rules as part of the wider Credit Risk Mitigation framework rather than as standalone treatment: haircut, holding-period and remargining conditions determine whether the collateral is recognised as an eligible mitigant at all. The CRM framework governs recognition of collateral, guarantees, netting and credit derivatives, and the collateralized-transactions provisions specify the operational conditions (daily revaluation, prompt liquidation/setoff, minimum holding periods) feeding into it. Conclude that collateral only reduces RWA where these transaction-level documentation and remargining requirements are met, and that the maturity/holding-period floors alter the haircut applied.
- **Grounding — this node (Page 61 / Art 9.1–9.3):** "No transaction in which credit risk mitigation (CRM) techniques are used shall receive a higher capital requirement than an otherwise identical transaction where such techniques are not used."
- **Grounding — related node (Page 76 / Art 9.55):** "the documentation contains remargining clauses; in secured lending transactions, it generally does not."

### [[Defaulted Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When applying credit risk mitigants to an exposure, be aware the CRM framework and the defaulted-exposures treatment are separate steps in the same standardized-approach chapter, listed sequentially in the contents (off-balance sheet, CCR, credit derivatives, then defaulted exposures). The CRM chapter governs how guarantees, collateral and credit derivatives substitute or reduce risk weights, while defaulted exposures carry their own risk-weight determination. Conclude that you should apply the defaulted-exposure classification first and then determine whether CRM recognition (and any residual uncovered portion) applies, rather than assuming mitigants automatically remove a defaulted-exposure treatment; verify the specific defaulted-exposures paragraphs since the provided context does not quote the direct cross-reference text.
- **Grounding — this node (Page 173 / 14.12):** "Credit risk mitigants will be recognized generally using the same type of framework... a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees."
- **Grounding — related node (Page 2 (Contents) / Section 7):** "Credit derivatives 48 / Defaulted exposures 49"
- **Caveat:** The direct textual cross-reference between the CRM framework and the defaulted-exposures provision is not quoted in the supplied context; relationship inferred from chapter structure. Verify the defaulted-exposures paragraphs (p.49) for the exact interaction.

### [[Guarantees and Credit Derivatives (CRM)]] — `references` [EXTRACTED]
- **What this link tells you:** When claiming capital relief from a guarantee or credit derivative, treat these as one recognised sub-category of the CRM framework with its own eligibility limits, not as automatically effective protection. The CRM chapter recognises third-party guarantees via the substitution approach (guarantor's risk weight replaces the exposure's), while the guarantees/credit-derivatives provisions restrict eligibility — only CDS and total return swaps giving guarantee-equivalent protection qualify, and first-/nth-to-default derivatives are ineligible for capital relief. Conclude that you must verify the instrument's eligibility and apply the correct split (protected portion → guarantor's weight; uncovered/below-threshold portion → underlying counterparty or 1250%) before recognising any reduction.
- **Grounding — this node (Page 173 / Art 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees... substitute the risk weight for an exposure to the guarantor."
- **Grounding — related node (Page 88 / Art 9.76–9.77):** "Only credit default swaps and total return swaps that provide credit protection equivalent to guarantees are eligible... nth-to-default credit derivatives... are not eligible."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing how a bank may capitalize purchased receivables covered by a seller or third-party guarantee, don't treat credit risk mitigation as a standalone adjustment: paragraphs 14.11-14.12 route mitigant recognition back through the IRB risk-component machinery (PD, LGD, EAD, M), substituting the guarantor's risk weight for the pool's default and/or dilution risk weight. The link tells you that whether a guarantee is recognized, and how, depends on which risk component it covers and on the underlying IRB estimates (e.g. exposure-weighted LGD under SEC-IRBA). Conclude that CRM eligibility cannot be evaluated without confirming the bank's IRB approval and the relevant risk-component treatment; partial-cover guarantees leave the uncovered component capitalized under ordinary CRM rules.
- **Grounding — this node (Page 173 / 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"
- **Grounding — related node (Page 91 / 10.1):** "The risk components include measures of the probability of default (PD), loss given default (LGD), the exposure at default (EAD), and effective maturity (M)"

### [[On-Balance Sheet Netting]] — `references` [EXTRACTED]
- **What this link tells you:** When netting loans against deposits from the same counterparty to reduce exposure, treat on-balance-sheet netting as a conditional CRM technique governed by the CRM chapter's requirements, not as automatic offset. The CRM framework lists netting among recognised techniques, and the netting provisions tie recognition to the standardized-approach conditions (paragraphs 9.67–9.68) and carry those same conditions into EAD estimation under IRB. Conclude that netting only reduces RWA/EAD where the specified legal and operational conditions are satisfied, and that its effect flows into EAD (not less than current drawn amount) rather than being applied ad hoc.
- **Grounding — this node (Page 61 / Art 9.1):** "banks may agree to net loans owed to them against deposits from the same counterparty."
- **Grounding — related node (Page 136 / Art 12.63):** "On-balance sheet netting of loans and deposits of a bank to or from a retail customer will be permitted subject to the same conditions outlined in paragraphs 9.67 and 9.68 of the standardized approach."

### [[Real Estate Exposure Class]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears to connect the Credit Risk Mitigation framework with the real estate exposure class, but the provided CRM context (paras 14.11–14.12) addresses recognition of guarantees and collateral for purchased receivables and securitization, not real estate collateral specifically. The real estate provisions here (LTV-based risk weights, 'materially dependent on cash flows') set exposure classification and risk weights rather than invoke CRM substitution. Treat this as a general framework relationship — real estate exposures are secured lending to which CRM concepts can be relevant — and verify in the primary text whether the CRM chapter actually modifies real estate risk weights before relying on any interaction.
- **Grounding — this node (Page 173 / Art 14.12):** "Credit risk mitigants will be recognized generally using the same type of framework as set forth in paragraphs 12.21 to 12.28"
- **Grounding — related node (Page 34 / Art 7.61):** "Exposures secured by real estate that are classified as “regulatory real estate” exposures."
- **Caveat:** The supplied CRM excerpts concern receivables/securitization, not real estate collateral; the direct cross-reference between these two nodes is not evidenced in context and should be verified against the CRM chapter.

#graphify/document #graphify/EXTRACTED #community/Real_Estate_Credit_Mitigation #graphify/enriched
