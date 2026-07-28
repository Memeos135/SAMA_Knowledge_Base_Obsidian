---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "SA-CCR & CVA Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR__CVA_Framework
  - graphify/enriched
---

# Regulatory CVA Calculation

## Connections

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping capital obligations, keep CCR/IMM exposure measurement distinct from the CVA capital requirement: they are separate charges applying to the same covered transactions, and the CVA framework uses 'regulatory CVA' (excluding the bank's own default) computed per counterparty. Chapter 11 requires the CVA capital requirement to be calculated by all banks in covered transactions in both banking and trading books, independent of the exposure method used for CCR. Conclude that IMM approval for CCR does not discharge CVA obligations; you must separately calculate regulatory CVA (via BA-CVA by default, or SA-CVA with SAMA approval) for each counterparty with a covered position.
- **Grounding — this node (Page 97 / 11.31):** "A bank must calculate regulatory CVA for each counterparty with which it has at least one covered position for the purpose of the CVA risk capital requirements."
- **Grounding — related node (Page 48 / 7.1):** "A bank that wishes to adopt an internal models method to measure exposure or exposure at default (EAD) for regulatory capital purposes must seek SAMA approval."

### [[Standardized Approach for CVA (SA-CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which CVA capital methodology a bank must apply, treat 'regulatory CVA' as the required input measure that feeds the SA-CVA, not as an interchangeable concept. The framework defines regulatory CVA (excluding the bank's own default, with best-practice accounting constraints) and then states the SA-CVA uses as inputs the sensitivities of that regulatory CVA to credit spreads and market risk factors; SA-CVA use is conditional on SAMA approval, otherwise BA-CVA applies. A reader should conclude that eligibility for SA-CVA depends on being able to compute regulatory CVA and its sensitivities per Chapter 11, and should not assume SA-CVA can be used without both SAMA approval and a compliant regulatory CVA calculation.
- **Grounding — this node (Page 87 / 11.31-11.32):** "A bank must calculate regulatory CVA for each counterparty with which it has at least one covered position for the purpose of the CVA risk capital requirements."
- **Grounding — related node (Page 97 / 11.29):** "The SA-CVA uses as inputs the sensitivities of regulatory CVA to counterparty credit spreads and market risk factors driving the values of covered transactions."

#graphify/concept #graphify/EXTRACTED #community/SA-CCR__CVA_Framework #graphify/enriched
