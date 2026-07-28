---
source_file: "markdown/SAMA_EN_1644_VER1.md"
type: "concept"
community: "Bank Account Operation Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bank_Account_Operation_Rules
  - graphify/enriched
---

# SAMA (Saudi Central Bank)

## Connections

### [[Credit Information Company]] — `references` [EXTRACTED]
- **Why:** Credit information companies are defined as entities that must obtain a SAMA licence to operate, and SAMA retains ongoing supervisory powers over their conduct including complaint procedures, data accuracy, and wind-down measures, creating a direct regulatory relationship between the two nodes.
- **This node (Page 5 / Article 8(2)):** "Companies shall set specific procedures for handling consumers' complaints and shall publish such procedures upon SAMA's approval."
- **Related node (Page 2 / Article 1):** "Companies: Credit information companies licensed to collect and maintain credit information on consumers and provide the same to members upon request."
- **Implication:** A credit information company's operational controls—including complaint-handling workflows, data-update cadences, and wind-down plans—require documented SAMA approval or notification, and must be maintained as auditable artefacts demonstrating ongoing licence compliance.

### [[Credit Information Law]] — `references` [EXTRACTED]
- **Why:** The Credit Information Law explicitly defines SAMA as the Saudi Arabian Monetary Authority and grants it licensing, supervisory, and regulatory authority over credit information companies, making SAMA the primary referenced regulator throughout the Law's operative provisions.
- **This node (Page 2 / Article 1):** "SAMA: Saudi Arabian Monetary Authority."
- **Related node (Page 7 / Article 12):** "engaging in activities of credit information companies without obtaining a license from SAMA; companies' violation of license conditions and controls"
- **Implication:** Credit information companies must evidence a valid SAMA licence and ongoing compliance with licence conditions; an examiner will expect a licence register, condition-tracking log, and breach-escalation procedure mapped to Article 12 violations.

### [[SAMA (Monetary Authority)]] — `semantically_similar_to` [INFERRED]
- **Why:** Both nodes represent SAMA (Saudi Arabian Monetary Authority) as defined within their respective regulatory instruments—the Credit Information Law and the Banking Control Law—confirming it is the same supervisory institution referred to across both regimes, though each instrument grants SAMA distinct powers in its domain.
- **This node (Page 2 / Article 1):** "SAMA: Saudi Arabian Monetary Authority."
- **Related node (Page 3 / Article 1):** "SAMA may, from time to time, issue decisions concerning the following: Definition of the term 'deposit liabilities'…"
- **Implication:** When mapping cross-regime obligations (e.g. a bank that is also a Member under the Credit Information Law), compliance teams must track SAMA's authority under both instruments separately, as powers and enforcement mechanisms differ; a unified SAMA-entity node in a knowledge graph should carry instrument-specific edge attributes to avoid conflating licensing, supervisory, and prudential powers.
- **Caveat:** The semantic equivalence is logically sound given the same institutional name and KSA context, but the two source documents confer distinct legal powers on SAMA; the 'semantically_similar_to' relation should not be interpreted as identity of powers or obligations across the two regimes.

#graphify/concept #graphify/EXTRACTED #community/Bank_Account_Operation_Rules #graphify/enriched
