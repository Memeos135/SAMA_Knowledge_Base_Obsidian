---
source_file: "markdown/SAMA_EN_8725_VER1.md"
type: "document"
community: "Bank Fraud Combating Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Fraud_Combating_Rules
  - graphify/enriched
---

# POS KYC Verification Circular

## Connections

### [[Banking Control Law]] — `references` [EXTRACTED]
- **Why:** The POS KYC circular explicitly cites the Banking Control Law (issued by Royal Decree) as one of its foundational authorities, establishing SAMA's supervisory mandate over payment systems as a precondition for issuing the KYC directive to payment service companies.
- **This node (Page 1):** "استناداً إلى نظام مراقبة البنوك الصادر بالمرسوم الملكي... بالتأكيد على أنه الجهة المختصة نظاماً بتشغيل نظم المدفوعات والتسوية المالية وخدماتها في المملكة ومراقبتها والإشراف عليها وله إصدار القواعد والتعليمات والتراخيص"
- **Related node (Page 4 / Article 3):** "All applications, for the grant of licenses to carry on banking business in the Kingdom, shall be addressed to SAMA which will study the applications after obtaining all the necessary information."
- **Implication:** SAMA's authority to mandate KYC standards on PSPs for POS deployment derives from its Banking Control Law supervisory powers; an examiner will expect PSPs to maintain evidence that their KYC procedures are formally approved and auditable as a licensing condition, not merely a best-practice aspiration.
- **Caveat:** The Banking Control Law node context does not contain an explicit article granting SAMA jurisdiction over payment systems specifically; the connection is inferred from the circular's own citation of the law and the general supervisory mandate in Articles 2–3 of the Banking Control Law.

### [[Financial Fraud Combating Guide for Banks]] — `conceptually_related_to` [INFERRED]
- **Why:** Both instruments address fraud detection and KYC obligations in the payments/banking sector: the Fraud Guide sets the minimum anti-fraud policies and procedures for banks, while the POS KYC Circular mandates that payment service companies verify merchant customers (KYB) before deploying POS devices and maintain fraud detection procedures under the PSP Regulatory Rules. The POS Circular explicitly cites Article 8 of the PSP Rules on fraud detection policies, mirroring the Fraud Guide's minimum-standards framework.
- **This node (Page 1):** "إلزامية وضع سياسات وإجراءات للكشف عن حالات الاحتيال والتعامل معها بالإضافة إلى إبلاغ الجهات المختصة في الدولة وإشعار البنك المركزي وفق الصيغة التي يحددها"
- **Related node (Page 4, Preamble / Page 5, Art 1-1):** "دليل لمساعدة البنوك والمصارف العاملة في المملكة العربية السعودية في توفير الحد الأدنى من إجراءات ومعايير مكافحة حالات الاحتيال المالي والتعامل معها"
- **Implication:** A PSP operating POS channels must map its fraud-detection policies to the minimum standards in the Fraud Guide (governance, unit responsibilities, reporting) and evidence merchant KYC/KYB completion before device activation, creating an auditable pre-onboarding control gate.
- **Caveat:** Confidence INFERRED: the two documents address overlapping regulatory objectives but are directed at different regulated populations (licensed banks vs. payment service companies); direct cross-reference between the two texts is not present in the provided context.

### [[Payment Service Providers Regulatory Rules]] — `references` [EXTRACTED]
- **Why:** The POS KYC Verification Circular explicitly grounds its KYC and fraud-control obligations in Article 3 and Article 8 of the Payment Service Providers Regulatory Rules, making the Rules the direct legislative authority that the Circular operationalises for POS device sale and deployment.
- **This node (Page 1):** "التأكيد على إلزامية التحقق من العميل وفاعلية الإجراءات المتبعة للالتزام بمبدأ اعرف عميلك قبل الشروع في عملية بيع أو تشغيل أجهزة نقاط البيع"
- **Related node (Page 1 / Art 3 (as cited in circular)):** "استناداً إلى المادة الثالثة من القواعد التنظيمية لمقدمي خدمات المدفوعات والتي نصت على أن دعوة أو حث أي شخص... يعد ممارسة لخدمات المدفوعات في المملكة ويستلزم الحصول على ترخيص البنك المركزي"
- **Implication:** PSP KYB/KYC onboarding workflows for POS merchant customers must be evidenced as operative before device activation, with internal policies covering risk identification, monitoring, and reporting covering all customer categories, as this is a named SAMA supervisory expectation.
- **Caveat:** Both nodes derive from the same single-page Arabic circular; the 'Payment Service Providers Regulatory Rules' node represents the underlying ruleset cited within that circular rather than a separately provided document, so the locator for node_a is inferred from the circular's own citation rather than a standalone Rules document in the corpus.

#graphify/document #graphify/EXTRACTED #community/Bank_Fraud_Combating_Rules #graphify/enriched
