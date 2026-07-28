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

# Payment Order Execution Rules

## Connections

### [[Account Information and Payment Initiation Services]] — `references` [EXTRACTED]
- **Why:** Chapter 8 of the Implementing Regulation (Account Information and Payment Initiation Services — open banking) sets access and consent requirements that directly govern how payment initiation service providers (PISPs) must submit and execute payment orders; payment order execution rules therefore apply as the downstream operational layer once open-banking access is granted.
- **This node (Page 3 / Table of Contents):** "الباب السادس: خدمات المدفوعات ذات الصلة ... الفصل الثالث - تقديم خدمات المدفوعات ذات الصلة"
- **Related node (Page 3 / Table of Contents):** "الباب الثامن: متطلبات تقديم خدمة معلومات حساب المدفوعات وإنشاء المدفوعات"
- **Implication:** A RegTech workflow for PISPs must enforce a sequenced control: consent verification (Chapter 8) must be logged and confirmed before a payment order execution rule (Chapter 6, Section 3) is triggered, creating a mandatory audit trail linking authorisation to execution.
- **Caveat:** Both nodes share only the table-of-contents and cover-page context in the provided excerpts; operative article numbers for Chapter 8 and the relevant Chapter 6 sections are not visible, so the linkage is inferred from the regulatory structure rather than verbatim operative text.

### [[Licensee Change Notification Obligations]] — `references` [EXTRACTED]
- **Why:** Both nodes derive from the same Implementing Regulation (اللائحة التنفيذية لنظام المدفوعات وخدماتها) issued under Royal Decree م/26; licensee change-notification obligations form part of the broader licensee obligations framework (الباب الرابع) within which payment-order execution rules also sit, meaning changes to a licensee's structure or status directly affect the authorisation basis under which payment orders are executed.
- **This node (Page 3 / Table of Contents):** "الباب الرابع: التزامات المرخص لهم — الفصل الأول: قواعد الإسناد والمراجعة وإدارة المخاطر"
- **Related node (Page 1 / cover letter):** "يؤكد البنك المركزي على مقدمي خدمات المدفوعات ومشغلي نظم المدفوعات الخاضعين للنظام واللائحة الالتزام بكافة الأحكام الواردة في اللائحة التنفيذية"
- **Implication:** A RegTech workflow must link any notified change to the licensee's profile (ownership, controllers, key persons) to a real-time review of whether outstanding payment-order execution authorities remain valid under the unchanged licence scope.
- **Caveat:** Both nodes share identical context excerpts (pages 1–4 only); specific article numbers for change-notification and payment-order execution provisions are not visible in the provided context — locators are table-of-contents level only.

### [[Unauthorized Payment Liability]] — `references` [EXTRACTED]
- **Why:** The payment order execution rules determine whether an order has been validly authenticated and authorised; an order found to fall outside those rules triggers the unauthorized-payment liability regime, making execution standards the factual predicate for liability determination.
- **This node (Page 3 / Table of Contents):** "الباب السادس: خدمات المدفوعات ذات الصلة ... الفصل الثالث - تقديم خدمات المدفوعات ذات الصلة"
- **Related node (Page 3 / Table of Contents):** "الباب الخامس: حماية العملاء والشمول المالي ... الفصل الأول - حماية العملاء"
- **Implication:** PSPs must maintain timestamped authentication and execution logs for every payment order so that, when an unauthorized-payment claim is raised, the evidence trail is sufficient to establish or rebut liability within the regulatory timeframes.
- **Caveat:** Substantive article text for either the execution rules or the liability provisions is not present in the provided excerpts; enrichment is based on the structural ToC relationship and standard regulatory logic for payments regimes. Article locators cannot be confirmed.

#graphify/document #graphify/EXTRACTED #community/Payment_Services_Consumer_Rights #graphify/enriched
