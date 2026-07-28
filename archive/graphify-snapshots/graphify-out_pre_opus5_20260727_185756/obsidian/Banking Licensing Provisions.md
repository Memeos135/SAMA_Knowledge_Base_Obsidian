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

# Banking Licensing Provisions

## Connections

### [[Banking Control Law]] — `references` [EXTRACTED]
- **Why:** Articles 2 and 3 of the Banking Control Law establish the prohibition on unlicensed banking business and set out the complete licensing process—conditions, applicant, recommending authority, and minimum capital—making licensing provisions a direct, enforceable sub-regime of the Law.
- **This node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA… The license for a National Bank shall stipulate the following: 1) It shall be a Saudi Joint Stock Company. 2) The paid-up capital shall not be less than SAR 2.5 […"
- **Related node (Page 4 / Article 2):** "No person, natural or juristic, unlicensed in accordance with the provisions of this Law, shall carry on basically any of the banking business."
- **Implication:** An onboarding or entity-verification workflow must confirm SAMA licensing status before allowing any counterparty to conduct banking business; the licensing record must capture entity type (national vs. foreign), paid-up capital, and SAMA approval date as auditable evidence.

### [[SAMA (Monetary Authority)]] — `references` [EXTRACTED]
- **Why:** The Banking Control Law assigns SAMA the exclusive gatekeeping role for all banking licenses: applications must be addressed to SAMA, which studies them and submits recommendations, and SAMA must also approve branch openings, cessation of business, and ongoing prudential conditions. Licensing provisions are therefore operationally inseparable from SAMA's institutional mandate.
- **This node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information and submit its recommendations to the Minister of Finance and National Economy."
- **Related node (Page 13 / Article 17):** "SAMA may, at any time, request any bank to supply it, within a time limit it will specify and in the manner it will prescribe, with any information that it deems necessary for ensuring the realization of the purposes of this Law."
- **Implication:** A RegTech licensing-workflow system must route all new bank license applications, branch-opening requests, and cessation notices through a SAMA-addressed submission process with documented information packages, creating an auditable evidence trail that SAMA can inspect or supplement via Article 17 information requests at any subsequent point.

#graphify/concept #graphify/EXTRACTED #community/Bank_Fraud_Combating_Rules #graphify/enriched
