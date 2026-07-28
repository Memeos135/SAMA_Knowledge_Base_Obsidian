---
source_file: "markdown/document3.md"
type: "concept"
community: "SIFI Resolution & Recovery"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/SIFI_Resolution__Recovery
  - graphify/enriched
---

# Saudi Central Bank

## Connections

### [[Competent Authority]] — `references` [EXTRACTED]
- **Why:** The Law defines 'Competent Authority' as either the Saudi Central Bank or the Capital Market Authority, each exercising supervisory jurisdiction over its respective supervised institutions; SAMA is therefore the operationalising institution of the Competent Authority concept for banking-sector SIFIs.
- **This node (Page 2 / Art 1):** "Competent Judicial Authority: The commercial court with respect to financial institutions supervised by the Saudi Central Bank, and the committees for resolution of securities disputes with respect to financial institutions supervised by the Capital Market Authority."
- **Related node (Page 1 / Art 1):** "Competent Authority: The Saudi Central Bank or the Capital Market Authority, each with respect to financial institutions falling under its supervision."
- **Implication:** Any resolution-related workflow (plan approval, valuation rules, cross-border orders) must be routed through SAMA as Competent Authority when the subject institution is a SAMA-supervised financial institution; system access controls and escalation paths must reflect this dual-authority split.

### [[Saudi Central Bank (SAMA)]] — `semantically_similar_to` [INFERRED]
- **Why:** Both nodes refer to the same regulatory authority—'Saudi Central Bank (SAMA)'—but appear in two distinct regulatory instruments: the Credit Information Law Implementing Regulations (document2) and the Systemically Important Financial Institutions Law (document3). The semantic similarity is the shared supervisory identity, not substantive overlap in regulatory obligations.
- **This node (Page 1 / Art 1 / document3.md):** "Competent Authority: The Saudi Central Bank or the Capital Market Authority, each with respect to financial institutions falling under its supervision."
- **Related node (Page 1 / Art 1 / document2.md):** "SAMA: Saudi Central Bank (SAMA)*. [...] 'Saudi Arabian Monetary Agency' was replaced by the 'Saudi Central Bank' in accordance with The Saudi Central Bank Law No. (M/36), dated 11/04/1442H."
- **Implication:** A RegTech system mapping supervisory authority must resolve 'SAMA' as 'Saudi Central Bank' uniformly across both regimes, but note that document3 splits competence between SAMA and CMA depending on institution type, while document2 assigns sole supervisory authority to SAMA for credit information companies.
- **Caveat:** Relation is INFERRED: the two nodes are linked by shared institutional identity across different regulatory instruments, not by a cross-reference or explicit legal link between the two documents.

#graphify/concept #graphify/INFERRED #community/SIFI_Resolution__Recovery #graphify/enriched
