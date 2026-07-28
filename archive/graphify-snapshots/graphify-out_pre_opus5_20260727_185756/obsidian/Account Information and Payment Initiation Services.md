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

# Account Information and Payment Initiation Services

## Connections

### [[Payment Order Execution Rules]] — `references` [EXTRACTED]
- **Why:** Chapter 8 of the Implementing Regulation (Account Information and Payment Initiation Services — open banking) sets access and consent requirements that directly govern how payment initiation service providers (PISPs) must submit and execute payment orders; payment order execution rules therefore apply as the downstream operational layer once open-banking access is granted.
- **This node (Page 3 / Table of Contents):** "الباب الثامن: متطلبات تقديم خدمة معلومات حساب المدفوعات وإنشاء المدفوعات"
- **Related node (Page 3 / Table of Contents):** "الباب السادس: خدمات المدفوعات ذات الصلة ... الفصل الثالث - تقديم خدمات المدفوعات ذات الصلة"
- **Implication:** A RegTech workflow for PISPs must enforce a sequenced control: consent verification (Chapter 8) must be logged and confirmed before a payment order execution rule (Chapter 6, Section 3) is triggered, creating a mandatory audit trail linking authorisation to execution.
- **Caveat:** Both nodes share only the table-of-contents and cover-page context in the provided excerpts; operative article numbers for Chapter 8 and the relevant Chapter 6 sections are not visible, so the linkage is inferred from the regulatory structure rather than verbatim operative text.

#graphify/document #graphify/EXTRACTED #community/Payment_Services_Consumer_Rights #graphify/enriched
