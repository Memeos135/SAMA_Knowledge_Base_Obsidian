---
source_file: "markdown/SAMA_EN_11005_VER1.md"
type: "document"
community: "Finance Consumer Protection Laws"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Finance_Consumer_Protection_Laws
  - graphify/enriched
---

# Beneficial Owner Inquiry Service for Nonprofits

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **What this link tells you:** When justifying why financial institutions must use the nonprofit beneficial-owner inquiry service, rely on this circular's citation chain: it is issued under the Central Bank Law and, materially, the Anti-Money Laundering Law and its Implementing Regulation, which impose the CDD obligation to identify and verify beneficial owners. The service is thus a means of satisfying an existing statutory AML duty toward association/nonprofit customers, not a new standalone obligation. Conclude that where a beneficial owner is undisclosed or the data conflicts, the institution must still apply its own CDD measures and the suspicious-transaction reporting requirements of the AML regime — the service does not discharge those duties by itself.
- **Grounding — this node (Page 1):** "لاستيفاء متطلبات العناية الواجبة تجاه عملاء المؤسسات المالية من الجمعيات والمؤسسات الأهلية"
- **Grounding — related node (Page 1):** "نظام مكافحة غسل الأموال ... وما تضمنته من التزامات على المؤسسات المالية بتطبيق تدابير العناية الواجبة"

### [[Beneficial Owner Verification]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping beneficial-owner verification duties across customer types, read these two instruments as parallel applications of one CDD obligation: SAMA_EN_10959 mandates linking to the Ministry of Commerce 'Wathiq' service to verify BOs of companies, while 11005 directs use of the NCNP service for BOs of associations and nonprofit entities. Both rest on the same AML Law/Implementing Regulation duty to identify and verify the beneficial owner and both impose the same fallback — apply internal CDD and report discrepancies. Conclude that verifying a BO via one registry source does not exhaust the obligation; the correct source depends on the customer's legal form, and unresolved or conflicting BO data triggers the same CDD and STR escalation in either case.
- **Grounding — this node (Page 1):** "وفي حال وجود مستفيد حقيقي غير مفصح عنه ... على المؤسسة المالية اتخاذ تدابير العناية الواجبة المطبقة لديها"
- **Grounding — related node (Page 1):** "الربط التقني مع خدمة 'وثاق' للتحقق من هوية المستفيد الحقيقي (source Arabic is OCR-garbled; paraphrased)"
- **Caveat:** Node A source Arabic is OCR-garbled (presentation-form glyphs); clause_a excerpt is an English paraphrase of the subject line about linking to the 'Wathiq' verification service.

### [[SAMA Central Bank Law (Royal Decree M36)|SAMA Central Bank Law (Royal Decree M/36)]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing what legally compels financial institutions to use the National Center's beneficial-owner inquiry service for nonprofit customers, note that the circular grounds SAMA's authority to instruct in the Central Bank Law (Royal Decree), read together with the AML Law and CTF Law and the AML Implementing Regulation. The service is a means to discharge the CDD duty to identify and verify the beneficial owner already imposed by the AML regime, not a free-standing new obligation. You would treat the circular as an enforcement instrument of that existing CDD chain: where a nonprofit's disclosed beneficial-owner data is missing or inconsistent, the institution must still apply its own CDD and SAR-reporting obligations, subject to the Personal Data Protection Law.
- **Grounding — this node (Page 1):** "استناداً لأحكام نظام البنك المركزي ... ونظام مكافحة غسل الأموال ... ونظام مكافحة جرائم الإرهاب وتمويله ... وما تضمنته من التزامات على المؤسسات المالية بتطبيق تدابير العناية الواجبة"
- **Grounding — related node (Page 1):** "استناداً إلى الصلاحيات المنوطة به بموجب [النظام] الصادر بالمرسوم الملكي (governing authority under the Central Bank Law Royal Decree)"
- **Caveat:** Central Bank Law decree number appears inconsistently in the OCR (M/36 vs M/37); verify the exact decree reference in the primary text.

### [[Technical Integration with Waathiq Beneficial Owner Verification Service]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Treat these two circulars as parallel instruments implementing the same beneficial-owner CDD obligation through two different registries: SAMA_EN_10959 directs integration with the Ministry of Commerce 'Waathiq' service for beneficial owners of *companies*, while SAMA_EN_11005 directs use of the NCNP inquiry service for beneficial owners of *nonprofits and charitable associations*. Both rest on the same AML/CTF Law and AML Implementing Regulation and impose the same fallback: apply your own due diligence and notify where an owner is undisclosed or data conflicts. For a compliance decision, do not assume one covers the other's customer class — confirm which service applies to the customer type, since the obligation is common but the data source is segmented by legal-person category.
- **Grounding — this node (SAMA_EN_11005 / Page 1):** "خدمة الاستعلام عن معلومات المستفيد الحقيقي من الجمعيات والمؤسسات الأهلية ... اتخاذ تدابير العناية الواجبة المطبقة لديها"
- **Grounding — related node (SAMA_EN_10959 / Page 1):** "integration with the 'Waathiq' service for beneficial-owner verification of companies; notify the Ministry of Commerce where undisclosed/conflicting"
- **Caveat:** Relation is INFERRED; node A Arabic is OCR-garbled (clause_a paraphrased). The two circulars are functionally parallel but target different customer classes — verify applicability per customer type in the primary texts.

#graphify/document #graphify/EXTRACTED #community/Finance_Consumer_Protection_Laws #graphify/enriched
