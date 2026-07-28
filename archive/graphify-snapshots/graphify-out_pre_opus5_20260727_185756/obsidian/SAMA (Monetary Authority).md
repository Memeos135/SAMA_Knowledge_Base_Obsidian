---
source_file: "markdown/SAMA_EN_996_VER1.md"
type: "concept"
community: "Bank Fraud Combating Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bank_Fraud_Combating_Rules
  - graphify/enriched
---

# SAMA (Monetary Authority)

## Connections

### [[Banking Control Law]] — `references` [EXTRACTED]
- **Why:** The Banking Control Law constitutes SAMA as the central regulatory authority with express supervisory, licensing, information-collection, and inspection powers over all banks, making SAMA both the enforcing subject and the institutional reference throughout the Law.
- **This node (Page 3 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information and submit its recommendations to the Minister of Finance and National Economy."
- **Related node (Page 13 / Article 17):** "SAMA may, at any time, request any bank to supply it, within a time limit it will specify and in the manner it will prescribe, with any information that it deems necessary for ensuring the realization of the purposes of this Law."
- **Implication:** Banks must maintain a real-time data-provision capability—structured reporting pipelines and document repositories—capable of responding to ad hoc SAMA information requests within any deadline SAMA specifies, with a full audit trail of submissions.

### [[Banking Licensing Provisions]] — `references` [EXTRACTED]
- **Why:** The Banking Control Law assigns SAMA the exclusive gatekeeping role for all banking licenses: applications must be addressed to SAMA, which studies them and submits recommendations, and SAMA must also approve branch openings, cessation of business, and ongoing prudential conditions. Licensing provisions are therefore operationally inseparable from SAMA's institutional mandate.
- **This node (Page 13 / Article 17):** "SAMA may, at any time, request any bank to supply it, within a time limit it will specify and in the manner it will prescribe, with any information that it deems necessary for ensuring the realization of the purposes of this Law."
- **Related node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information and submit its recommendations to the Minister of Finance and National Economy."
- **Implication:** A RegTech licensing-workflow system must route all new bank license applications, branch-opening requests, and cessation notices through a SAMA-addressed submission process with documented information packages, creating an auditable evidence trail that SAMA can inspect or supplement via Article 17 information requests at any subsequent point.

### [[SAMA (Saudi Central Bank)]] — `semantically_similar_to` [INFERRED]
- **Why:** Both nodes represent SAMA (Saudi Arabian Monetary Authority) as defined within their respective regulatory instruments—the Credit Information Law and the Banking Control Law—confirming it is the same supervisory institution referred to across both regimes, though each instrument grants SAMA distinct powers in its domain.
- **This node (Page 3 / Article 1):** "SAMA may, from time to time, issue decisions concerning the following: Definition of the term 'deposit liabilities'…"
- **Related node (Page 2 / Article 1):** "SAMA: Saudi Arabian Monetary Authority."
- **Implication:** When mapping cross-regime obligations (e.g. a bank that is also a Member under the Credit Information Law), compliance teams must track SAMA's authority under both instruments separately, as powers and enforcement mechanisms differ; a unified SAMA-entity node in a knowledge graph should carry instrument-specific edge attributes to avoid conflating licensing, supervisory, and prudential powers.
- **Caveat:** The semantic equivalence is logically sound given the same institutional name and KSA context, but the two source documents confer distinct legal powers on SAMA; the 'semantically_similar_to' relation should not be interpreted as identity of powers or obligations across the two regimes.

#graphify/concept #graphify/EXTRACTED #community/Bank_Fraud_Combating_Rules #graphify/enriched
