---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "IRB Credit Risk Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_Credit_Risk_Approach
  - graphify/enriched
---

# Comprehensive Approach (Collateral)

## Connections

### [[Credit Risk Mitigation (CRM)]] — `references` [EXTRACTED]
- **What this link tells you:** When recognising collateral to reduce credit risk capital, treat the Comprehensive Approach as one of the permitted techniques within the broader CRM framework rather than a standalone rule, because CRM is the umbrella regime and the comprehensive approach (with standard supervisory haircuts) is the specific method for adjusting exposure and collateral values. The reference tells you that under the standardised approach a bank must use either the simple approach or the comprehensive approach with standard supervisory haircuts to measure the degree of mitigation. Conclude that CRM disclosure and eligibility conditions (Table CRC, Template CR3) apply, and that electing the comprehensive approach commits you to the haircut methodology — verify collateral eligibility and haircut rules before claiming the RWA reduction.
- **Grounding — this node (Page 755 / Row 1):** "When calculating the degree of credit risk mitigation, banks must use the simple approach or the comprehensive approach with standard supervisory haircuts."
- **Grounding — related node (Page 794 / 19.2.2):** "Credit risk mitigation: Table CRC - Qualitative disclosure related to credit risk mitigation techniques; Template CR3 - Credit risk mitigation techniques – overview."

### [[Currency Mismatch Haircut (Hfx)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying collateral-based credit risk mitigation under the comprehensive approach, the currency mismatch haircut (Hfx) is one of the adjustments you must apply: where the credit protection or collateral is denominated in a currency different from the exposure, an additional haircut is layered onto the standard supervisory haircuts. This link tells you that recognising collateral value is not the end point — currency mismatch reduces the recognised protection. When claiming CRM relief, confirm whether a currency mismatch exists and apply Hfx before concluding the net protected amount.
- **Grounding — this node (Page 755 (SAMA_EN_3487)):** "banks must use the simple approach or the comprehensive approach with standard supervisory haircuts."
- **Grounding — related node (Page 96 / 9.81 (SAMA_EN_3487)):** "Currency mismatches 9.81 Where the credit protection is denominated in a currency different from"

### [[Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether collateral reduces loss estimates, note the two regimes differ: the comprehensive approach with supervisory haircuts governs collateral recognition under the standardised/foundation route, while own-LGD estimates under the advanced IRB approach must reflect economic downturn and cannot fall below the long-run default-weighted average loss rate. This link tells you collateral recognised under the comprehensive approach and internally estimated LGD are alternative, not additive, ways of reflecting collateral value. When deciding which basis applies, confirm the bank's approval status (F-IRB fixed LGDs vs own-LGD) and that any currency mismatch between obligation and collateral is addressed in either route.
- **Grounding — this node (Page 123 / 12.6 (SAMA_EN_3487)):** "senior claims on sovereigns, banks... that are not secured by recognized collateral will be assigned a 45% LGD."
- **Grounding — related node (Page 211 / 16.82-16.83 (SAMA_EN_3487)):** "This LGD cannot be less than the long-run default-weighted average loss rate given default... Any currency mismatch between the underlying obligation and the collateral must also be consid[ered]."

### [[Master Netting Agreements for SFTs]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital relief a bank may claim on securities financing transactions covered by a master netting agreement, treat the comprehensive approach as the collateral-recognition engine and the master netting rules as the gateway. The comprehensive approach with standard supervisory haircuts is the method the standardised framework mandates for measuring credit-risk mitigation, and paragraph 12.38-12.39 show that recognising an SFT master netting agreement's netted effect (using E* as EAD) still depends on applying those haircuts or an approved VaR alternative. Conclude that the netting agreement alone does not reduce exposure — the bank must also correctly apply comprehensive-approach haircuts and, for the VaR alternative, satisfy the criteria in paragraphs 9.61-9.62 and hold supervisory recognition.
- **Grounding — this node (Page 755):** "banks must use the simple approach or the comprehensive approach with standard supervisory haircuts"
- **Grounding — related node (Page 135 / 12.38–12.39):** "the counterparty credit risk arising from the set of transactions covered by the master netting agreement, E* must be used as the EAD"

### [[On-Balance Sheet Netting]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how netting reduces credit exposure under the standardised framework, recognise that on-balance-sheet netting and the comprehensive collateral approach are complementary steps, not alternatives. On-balance-sheet netting first offsets loans and deposits under enforceable netting, while the comprehensive approach then applies supervisory haircuts to any collateral supporting the residual exposure; the LI2 disclosure note confirms Basel netting rules differ from accounting netting and may add or reverse netting relative to the balance sheet. Conclude that a bank claiming netted exposure must verify both that the arrangement meets Basel netting eligibility and that residual collateral is haircut under the comprehensive approach — accounting netting figures cannot be relied on as the regulatory measure.
- **Grounding — this node (Page 755):** "banks must use the simple approach or the comprehensive approach with standard supervisory haircuts"
- **Grounding — related node (Page 893):** "The netting rules under the Basel framework are different from the rules under the applicable accounting frameworks"

### [[Supervisory Haircuts (Table 14)]] — `references` [EXTRACTED]
- **What this link tells you:** When using the comprehensive approach to recognise collateral, the supervisory haircut table is the mandatory input: the rule text itself states the comprehensive approach is applied 'with standard supervisory haircuts,' so the haircut schedule directly governs how much collateral value can be recognised. This link tells you the comprehensive approach cannot be operated independently of the prescribed haircuts. When calculating adjusted collateral value, apply the standard supervisory haircuts (subject to any currency-mismatch and holding-period adjustments) rather than unadjusted market values.
- **Grounding — this node (Page 755 (SAMA_EN_3487)):** "the comprehensive approach with standard supervisory haircuts."
- **Grounding — related node (Page 879 (SAMA_EN_3487)):** "The averages are calculated after the application of any haircuts, inflow and outflow rates and caps, where applicable."
- **Caveat:** Node B is labelled 'Supervisory Haircuts (Table 14)' but the provided context pages (LCR haircuts, slotting, commodities) do not clearly contain the CRM supervisory-haircut table; verify the actual Table 14 haircut values in the primary text before relying on specific figures.

#graphify/concept #graphify/EXTRACTED #community/IRB_Credit_Risk_Approach #graphify/enriched
