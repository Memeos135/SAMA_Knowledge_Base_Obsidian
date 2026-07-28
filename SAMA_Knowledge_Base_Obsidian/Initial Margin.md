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

# Initial Margin

## Connections

### [[Eligible Collateral]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two concepts appear operationally linked: eligible-collateral rules define *what* may be posted, while initial-margin rules define *how much* must be posted, and both are grounded in the same document (Elements 3 and 4). The connection is inferred rather than a stated cross-reference, but the text supports it — collateral must satisfy the eligibility and haircut standards to count toward the required initial margin amount. Treat this as a lead: when verifying an initial-margin position, confirm the posted collateral independently meets Element 4 eligibility, but check the primary text for the precise linkage rather than assuming the two rules substitute for one another.
- **Grounding — this node (Page 9 / para 26):** "Initial margin should be collected at the outset of a transaction, and collected thereafter on a routine and consistent basis"
- **Grounding — related node (Page 11 / para 32):** "eligible collateral should not be exposed to excessive credit, market and FX risk ... subject to appropriate haircuts"
- **Caveat:** Relationship is INFERRED — the two concepts are functionally related within the same document but no explicit cross-reference is quoted; confirm the operative linkage in the primary text.

### [[Margin Requirements for Non-centrally Cleared Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** To determine a covered entity's obligations under this framework, read 'Initial Margin' as one of the two mandatory exchanges the document imposes on covered entities engaging in non-centrally cleared derivatives. Element 2 requires exchange of initial and variation margin, and Element 3 sets baseline amounts and permits either a SAMA-approved quantitative model or the standardised schedule (with no 'cherry picking' between methods). Conclude that initial-margin methodology choice is not discretionary in the ordinary sense — model use requires explicit SAMA approval and must be applied consistently per asset class; check approval status before treating a model-based figure as compliant.
- **Grounding — this node (Page 9 / para 25):** "it will not be allowed to switch between model- and schedule-based margin calculations in an effort to “cherry pick” the most favourable initial margin terms"
- **Grounding — related node (Page 5 / Element 2 para 11):** "All covered entities that engage in non-centrally cleared derivatives must calculate, balance and exchange, on a bilateral basis"

### [[Re-hypothecation Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether initial-margin collateral can be reused, apply the re-hypothecation rules as a strict limitation on the treatment of provided initial margin (Element 5). The default is that cash and non-cash collateral collected as initial margin must NOT be re-hypothecated, re-pledged or re-used; the narrow exception in para 43 permits it only for hedging the collector's derivatives position, only with SAMA case-by-case approval, only with the customer's express written consent after risk disclosure, and requires the collateral to be segregated and treated as a customer asset. Conclude that any reuse of initial-margin collateral is presumptively prohibited unless every one of these conditions is satisfied — do not treat re-hypothecation as generally available.
- **Grounding — this node (Page 13 / para 42):** "cash and non-cash collateral collected as initial margin should not be re-hypothecated, re-pledged or re-used"
- **Grounding — related node (Page 13 / para 43):** "the customer’s collateral may be re-hypothecated only if the conditions described below are met ... gives express consent in writing"

#graphify/concept #graphify/EXTRACTED #community/Non-Cleared_Derivatives_Margin #graphify/enriched
