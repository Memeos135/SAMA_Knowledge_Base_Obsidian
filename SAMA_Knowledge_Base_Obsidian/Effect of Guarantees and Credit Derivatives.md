---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "IRB Credit Risk Approach"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Effect of Guarantees and Credit Derivatives

## Connections

### [[Currency Mismatch Haircut (Hfx)]] — `references` [EXTRACTED]
- **What this link tells you:** When claiming capital relief from a guarantee or credit derivative denominated in a currency different from the underlying exposure, you cannot recognise full protection value — the currency-mismatch haircut (Hfx) reduces the eligible amount. The guarantees/credit-derivatives CRM provisions expressly address 'Currency mismatches ... where the credit protection is denominated in a currency different from' the exposure, which triggers the Hfx adjustment. Conclude that protected-portion treatment must be applied to the haircut-adjusted (not nominal) amount whenever the protection and exposure currencies differ.
- **Grounding — this node (Page 96 / 9.81):** "Currency mismatches ... Where the credit protection is denominated in a currency different from"
- **Grounding — related node (Page 399 / 7.14):** "the FX delta risk factors are all the exchange rates between the currency in which an instrument is denominated and the reporting currency"
- **Caveat:** Node A context centres on market-risk FX delta risk factors; the Hfx-to-guarantees link rests on the CRM currency-mismatch provision at 9.81. Verify the specific Hfx formula in the CRM chapter before relying on it.

### [[Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **What this link tells you:** When a guarantee or eligible collateral backs an exposure under IRB, the protection is commonly reflected through the facility's LGD estimate, and any currency mismatch between the obligation and the collateral must be factored in conservatively. The LGD requirements expressly direct that 'any currency mismatch between the underlying obligation and the collateral must also be considered' and that dependence between borrower and collateral-provider risk be treated conservatively. Conclude that recognising credit derivatives/guarantees via LGD requires downward adjustment for currency mismatch and provider-borrower correlation, not a simple full offset.
- **Grounding — this node (Page 96 / 9.79):** "the protected portion of the exposure receives the treatment applicable to eligible guarantees /credit derivatives, with the remainder treated as unsecured"
- **Grounding — related node (Page 211 / 16.82–16.83):** "the bank must consider the extent of any dependence between the risk of the borrower and that of the collateral or collateral provider ... Any currency mismatch ... must also be considered"

### [[PD Estimation Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When recognising a guarantee or credit derivative under the IRB approach, decide whether you are adjusting PD (substituting the protection provider's default risk) rather than LGD — the two routes are mutually exclusive per exposure. The CRM guarantee/credit-derivative rules feed the IRB parameter framework, where PD estimation governs the borrower/guarantor default probability. Check which recognition method your bank has SAMA approval for, because double-counting protection across both PD and LGD is not permitted.
- **Grounding — this node (Page 887 / Template CR3):** "Exposures to be secured: carrying amount of exposures which have at least one credit risk mitigation mechanism (collateral, financial guarantees, credit derivatives)"
- **Grounding — related node (Page 210 / 16.79):** "banks must regard internal data as the primary source of information for estimating loss characteristics"
- **Caveat:** INFERRED as to the PD-substitution mechanism: the provided contexts confirm both topics exist in the framework but do not quote the specific rule tying guarantee recognition to PD adjustment. Verify the IRB guarantee-recognition article before relying on the PD-substitution treatment.

### [[Sovereign Guarantees and Counter-Guarantees]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital relief from credit protection, treat sovereign/counter-guarantee treatment as a special case sitting on top of the general guarantee and credit-derivative recognition rules, not as an independent regime. Both provisions live in SAMA's Minimum Capital Requirements for Credit Risk: the general provisions define eligible guarantees and credit derivatives as credit risk mitigation techniques, while the sovereign section extends 0% risk-weight and guarantee cover to sovereign/central-bank guarantees and indirect counter-guarantees. Conclude that a sovereign counter-guarantee only reduces the exposure's risk weight if it covers all credit-risk elements and both the original guarantee and counter-guarantee meet the operational requirements for guarantees set out in the general rules — so you must check compliance with the underlying eligibility conditions before applying the preferential treatment.
- **Grounding — this node (Page 887):** "Exposures to be secured: carrying amount of exposures which have at least one credit risk mitigation mechanism (collateral, financial guarantees, credit derivatives)"
- **Grounding — related node (Page 97 / para 9.83):** "both the original guarantee and the counter-guarantee meet all operational requirements for guarantees, except that the counter-guarantee need not be direct and explicit"

#graphify/document #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
