---
source_file: "markdown/SAMA_EN_996_VER1.md"
type: "document"
community: "Bank Fraud Combating Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Fraud_Combating_Rules
  - graphify/enriched
---

# Banking Control Law

## Connections

### [[Bank (definition)]] — `references` [EXTRACTED]
- **Why:** The Banking Control Law's Article 1 supplies the foundational definition of 'Bank' that scopes every subsequent obligation in the Law; the defined term is the primary subject of supervision, licensing, and prudential requirements throughout the document.
- **This node (Page 3 / Article 1):** "Bank: any natural or juristic person practicing basically any of the banking business in the Kingdom."
- **Related node (Page 13 / Article 16 (context excerpt)):** "SAMA may, from time to time, issue decisions concerning the following… Fixing the assets to be maintained by each bank within the Kingdom."
- **Implication:** A RegTech licensing or entity-classification system must apply the Article 1 'Bank' definition as the threshold test to determine which entities fall within scope of all Banking Control Law prudential and supervisory obligations.

### [[Banking Licensing Provisions]] — `references` [EXTRACTED]
- **Why:** Articles 2 and 3 of the Banking Control Law establish the prohibition on unlicensed banking business and set out the complete licensing process—conditions, applicant, recommending authority, and minimum capital—making licensing provisions a direct, enforceable sub-regime of the Law.
- **This node (Page 4 / Article 2):** "No person, natural or juristic, unlicensed in accordance with the provisions of this Law, shall carry on basically any of the banking business."
- **Related node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA… The license for a National Bank shall stipulate the following: 1) It shall be a Saudi Joint Stock Company. 2) The paid-up capital shall not be less than SAR 2.5 […"
- **Implication:** An onboarding or entity-verification workflow must confirm SAMA licensing status before allowing any counterparty to conduct banking business; the licensing record must capture entity type (national vs. foreign), paid-up capital, and SAMA approval date as auditable evidence.

### [[POS KYC Verification Circular]] — `references` [EXTRACTED]
- **Why:** The POS KYC circular explicitly cites the Banking Control Law (issued by Royal Decree) as one of its foundational authorities, establishing SAMA's supervisory mandate over payment systems as a precondition for issuing the KYC directive to payment service companies.
- **This node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information."
- **Related node (Page 1):** "استناداً إلى نظام مراقبة البنوك الصادر بالمرسوم الملكي... بالتأكيد على أنه الجهة المختصة نظاماً بتشغيل نظم المدفوعات والتسوية المالية وخدماتها في المملكة ومراقبتها والإشراف عليها وله إصدار القواعد والتعليمات والتراخيص"
- **Implication:** SAMA's authority to mandate KYC standards on PSPs for POS deployment derives from its Banking Control Law supervisory powers; an examiner will expect PSPs to maintain evidence that their KYC procedures are formally approved and auditable as a licensing condition, not merely a best-practice aspiration.
- **Caveat:** The Banking Control Law node context does not contain an explicit article granting SAMA jurisdiction over payment systems specifically; the connection is inferred from the circular's own citation of the law and the general supervisory mandate in Articles 2–3 of the Banking Control Law.

### [[SAMA (Monetary Authority)]] — `references` [EXTRACTED]
- **Why:** The Banking Control Law constitutes SAMA as the central regulatory authority with express supervisory, licensing, information-collection, and inspection powers over all banks, making SAMA both the enforcing subject and the institutional reference throughout the Law.
- **This node (Page 13 / Article 17):** "SAMA may, at any time, request any bank to supply it, within a time limit it will specify and in the manner it will prescribe, with any information that it deems necessary for ensuring the realization of the purposes of this Law."
- **Related node (Page 3 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information and submit its recommendations to the Minister of Finance and National Economy."
- **Implication:** Banks must maintain a real-time data-provision capability—structured reporting pipelines and document repositories—capable of responding to ad hoc SAMA information requests within any deadline SAMA specifies, with a full audit trail of submissions.

#graphify/document #graphify/EXTRACTED #community/Bank_Fraud_Combating_Rules #graphify/enriched
