---
source_file: "markdown/SAMA_EN_1430_VER1.md"
type: "document"
community: "Payment Services Consumer Rights"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Payment_Services_Consumer_Rights
  - graphify/enriched
---

# Unauthorized Payment Liability

## Connections

### [[Complaints and Disputes]] — `references` [EXTRACTED]
- **Why:** Chapter 11 (Complaints and Disputes) provides the procedural channel through which a payer asserts an unauthorized-payment claim; the unauthorized-payment liability rules set the substantive standard that the complaints process must apply and resolve, creating a direct procedural-substantive linkage.
- **This node (Page 4 / Art. 1 definitions):** "الشكوى: التعبير المقدم إلى المرخص له من العميل أو المستهلك، المعبر عن عدم رضاه أو اعتراضه من خلال الوسائل المتاحة لذلك"
- **Related node (Page 3 / Table of Contents):** "الباب الحادي عشر: الشكاوى والمنازعات"
- **Implication:** The complaints-handling system must be configured to capture and route unauthorized-payment dispute categories specifically, with case-management fields that record the authentication evidence required to apply the liability determination standard under the Regulation.
- **Caveat:** The substantive articles on unauthorized-payment liability are not visible in the provided excerpts; the liability-side clause is inferred from the chapter structure. The complaints definition is verbatim from Art. 1 but does not itself reference unauthorized payments explicitly.

### [[Payment Order Execution Rules]] — `references` [EXTRACTED]
- **Why:** The payment order execution rules determine whether an order has been validly authenticated and authorised; an order found to fall outside those rules triggers the unauthorized-payment liability regime, making execution standards the factual predicate for liability determination.
- **This node (Page 3 / Table of Contents):** "الباب الخامس: حماية العملاء والشمول المالي ... الفصل الأول - حماية العملاء"
- **Related node (Page 3 / Table of Contents):** "الباب السادس: خدمات المدفوعات ذات الصلة ... الفصل الثالث - تقديم خدمات المدفوعات ذات الصلة"
- **Implication:** PSPs must maintain timestamped authentication and execution logs for every payment order so that, when an unauthorized-payment claim is raised, the evidence trail is sufficient to establish or rebut liability within the regulatory timeframes.
- **Caveat:** Substantive article text for either the execution rules or the liability provisions is not present in the provided excerpts; enrichment is based on the structural ToC relationship and standard regulatory logic for payments regimes. Article locators cannot be confirmed.

### [[Refund Rights for Payment Transactions]] — `references` [EXTRACTED]
- **Why:** Refund rights for payment transactions represent the remedy available to a payer once unauthorized-payment liability has been established against the PSP; the two regimes are causally linked in that the liability determination triggers and scopes the refund entitlement.
- **This node (Page 3 / Table of Contents):** "الباب السادس: خدمات المدفوعات ذات الصلة ... الفصل الثالث - تقديم خدمات المدفوعات ذات الصلة"
- **Related node (Page 3 / Table of Contents):** "الباب الخامس: حماية العملاء والشمول المالي ... الفصل الأول - حماية العملاء"
- **Implication:** PSPs must implement a refund workflow that is automatically triggered upon a positive unauthorized-payment liability finding, with defined value-dating and credit-restoration steps evidenced in the case file to satisfy examiner review of customer protection outcomes.
- **Caveat:** Neither the refund rights nor the unauthorized-payment liability operative articles are present in the provided excerpts; enrichment relies on the ToC structure and standard consumer-protection logic applicable to payments regulations. Article locators cannot be confirmed.

#graphify/document #graphify/EXTRACTED #community/Payment_Services_Consumer_Rights #graphify/enriched
