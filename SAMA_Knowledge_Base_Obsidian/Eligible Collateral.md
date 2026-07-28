---
source_file: "markdown/SAMA_EN_2757_VER1.md"
type: "concept"
community: "Non-Cleared Derivatives Margin"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Non-Cleared_Derivatives_Margin
  - graphify/enriched
---

# Eligible Collateral

## Connections

### [[Initial Margin]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two concepts appear operationally linked: eligible-collateral rules define *what* may be posted, while initial-margin rules define *how much* must be posted, and both are grounded in the same document (Elements 3 and 4). The connection is inferred rather than a stated cross-reference, but the text supports it — collateral must satisfy the eligibility and haircut standards to count toward the required initial margin amount. Treat this as a lead: when verifying an initial-margin position, confirm the posted collateral independently meets Element 4 eligibility, but check the primary text for the precise linkage rather than assuming the two rules substitute for one another.
- **Grounding — this node (Page 11 / para 32):** "eligible collateral should not be exposed to excessive credit, market and FX risk ... subject to appropriate haircuts"
- **Grounding — related node (Page 9 / para 26):** "Initial margin should be collected at the outset of a transaction, and collected thereafter on a routine and consistent basis"
- **Caveat:** Relationship is INFERRED — the two concepts are functionally related within the same document but no explicit cross-reference is quoted; confirm the operative linkage in the primary text.

### [[Margin Requirements for Non-centrally Cleared Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing what a covered entity may lawfully collect to satisfy SAMA margin obligations, treat 'Eligible Collateral' as a scoping constraint on the framework, not a free choice. Element 4 of this document limits acceptable collateral to assets permitted under the standardised approach for credit risk in SAMA's Risk-based Capital Framework, subject to prescribed haircuts and 'wrong way risk' exclusions (e.g. securities issued by the counterparty or its related parties). Conclude that collateral eligibility is governed by an external SAMA framework and cannot be self-defined; verify each posted asset against the standardised credit-risk list and Appendix B haircuts before relying on it to meet a margin call.
- **Grounding — this node (Page 11 / para 32):** "SAMA only considers eligible collaterals, which are allowed under the standardised approach for credit risk under the Risk-based Capital Framework adopted by SAMA"
- **Grounding — related node (Page 4 / Element 1):** "these margin requirements apply to all non-centrally cleared derivatives"

#graphify/concept #graphify/EXTRACTED #community/Non-Cleared_Derivatives_Margin #graphify/enriched
