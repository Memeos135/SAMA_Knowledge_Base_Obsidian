---
source_file: "markdown/SAMA_EN_1704_VER1.md"
type: "concept"
community: "AML Due Diligence & Accounts"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML_Due_Diligence__Accounts
  - graphify/enriched
---

# Enhanced Due Diligence Measures

## Connections

### [[Correspondence Relationship]] — `references` [EXTRACTED]
- **Why:** Correspondent banking relationships are treated as an inherently elevated-risk category requiring pre-relationship due diligence, senior management approval, and ongoing monitoring controls that align structurally with EDD obligations, as mandated by Article 9 of the AML Law and Article 68 of the CTF Law.
- **This node (Page 36 / Section 4 preamble):** "The financial institution shall identify the risk factors to be taken into consideration when classifying a customer in the high-risk customer category from the AML/CTF perspective. It shall also take additional steps to collect information about high-risk customers and business…"
- **Related node (Page 62 / Section 13 preamble):** "Before entering into a correspondence relationship, the financial institution should collect sufficient information about the correspondent institution to obtain a full understanding of the nature of its work and learn about its reputation, the level of supervision applied to it…"
- **Implication:** Correspondent relationship onboarding workflows must incorporate EDD controls — including senior management sign-off, AML/CTF compliance officer recommendation, shell-bank prohibition checks, and continuous account monitoring — all evidenced in a durable record available to SAMA.

### [[Due Diligence Measures]] — `conceptually_related_to` [EXTRACTED]
- **Why:** Standard due diligence is the baseline obligation; Enhanced Due Diligence (EDD) is the risk-triggered escalation layer applied when customer classification yields a high-risk determination, making EDD a mandatory extension of — not a substitute for — the core CDD framework.
- **This node (Page 36 / Section 4 preamble):** "Customer classification according to the level of risks is a key element in the financial institution's risk-based approach… It shall also take additional steps to collect information about high-risk customers and business relationships."
- **Related node (Page 35 / para 3.22 preamble):** "Article (7/10) of the Implementing Regulations of the Anti-Money Laundering Law allows the financial institution to rely on another financial institution… to carry out the due diligence measures."
- **Implication:** The CDD workflow must include a risk-scoring trigger that automatically escalates a customer record to the EDD queue when high-risk indicators are met, with an auditable decision log distinguishing standard from enhanced treatment.

### [[FATF]] — `references` [EXTRACTED]
- **Why:** FATF membership and its Recommendations underpin the EDD framework: the Guide was issued in response to FATF standards, Saudi Arabia's FATF membership (June 2019) created direct obligations to implement risk-proportionate enhanced measures consistent with FATF Recommendation 10 (and related recommendations on PEPs and high-risk countries).
- **This node (Page 36 / Section 4 preamble):** "Customer classification according to the level of risks is a key element in the financial institution's risk-based approach… It shall also take additional steps to collect information about high-risk customers and business relationships in order to understand and assess risks an…"
- **Related node (Page 3 / Introduction):** "Saudi Arabia joined the Financial Action Task Force (FATF) in June 2019 to be the 1st Arab country and the 37th country in the world to obtain the membership… SAMA has adopted various initiatives that include measures and other criteria in response to international developments…"
- **Implication:** EDD policy and control design must demonstrably reflect FATF Recommendations, as SAMA examiners will benchmark EDD procedures against FATF standards; the institution should maintain a mapping between its EDD controls and the specific FATF requirements they satisfy.
- **Caveat:** The source text does not cite specific FATF Recommendation numbers in the EDD section; the alignment is inferred from the Introduction's explicit reference to FATF membership and SAMA's adoption of international standards. Confidence is high but the specific Recommendation-to-clause mapping is inferred.

### [[Politically Exposed Persons (PEPs)]] — `references` [EXTRACTED]
- **Why:** The EDD section explicitly designates PEPs as a mandatory high-risk category requiring enhanced due diligence, making PEPs a primary trigger object within the EDD framework; Article (8) of the AML Law and its Implementing Regulations are cited as the legal basis for both identification and EDD application to PEPs.
- **This node (Page 36 / Section 4A):** "The financial institution shall identify the risk factors to be taken into consideration when classifying a customer in the high-risk customer category from the AML/CTF perspective."
- **Related node (Page 39 / Section 4B):** "In cases of high-risk business relationships with PEPs, the financial institution shall apply enhanced due diligence measures and apply the same to all types of PEPs, their family members, and persons close to those PEPs."
- **Implication:** The CDD/KYB workflow must include an automated PEP-screening gate that, upon a positive match for customer or beneficial owner, triggers an EDD subprocess covering family members and close associates before onboarding or relationship continuation is permitted.

### [[Record Keeping]] — `references` [EXTRACTED]
- **Why:** The EDD section cross-references the Record Keeping section directly, making documentation of enhanced measures a mandatory output of every EDD action; the record-keeping obligations (minimum 10-year retention, retrievable/auditable format) therefore apply with full force to all EDD evidence collected.
- **This node (Page 39 / Para 4.8):** "When taking enhanced customer due diligence measures, the financial institution shall properly document these measures in accordance with Paragraph (6.1) in the Record Keeping Section."
- **Related node (Page 45 / Para 6.1):** "The financial institution shall keep records for a period of no less than ten years from the date of the end of the business relationship or contract, conclusion of the transaction, or closure of the account."
- **Implication:** Every EDD action (senior management approval, source-of-wealth evidence, enhanced monitoring output) must be captured in the record-keeping system with a minimum 10-year retention tag and must be retrievable for SAMA examination on demand.

#graphify/concept #graphify/EXTRACTED #community/AML_Due_Diligence__Accounts #graphify/enriched
