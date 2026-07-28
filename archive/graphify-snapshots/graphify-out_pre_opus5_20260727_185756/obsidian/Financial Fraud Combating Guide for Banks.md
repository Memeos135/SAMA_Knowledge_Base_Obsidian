---
source_file: "markdown/SAMA_EN_5696_VER1.md"
type: "document"
community: "Bank Fraud Combating Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bank_Fraud_Combating_Rules
  - graphify/enriched
---

# Financial Fraud Combating Guide for Banks

## Connections

### [[Anti-Money Laundering Law (referenced)]] — `references` [EXTRACTED]
- **Why:** The Financial Fraud Combating Guide is issued explicitly on the authority of, and with direct reference to, the Anti-Money Laundering Law (Royal Decree م/١٠), positioning AML obligations as the legal basis that makes the fraud guide's controls mandatory and linking financial fraud as a predicate offence to money laundering.
- **This node (Page 1):** "دليل مكافحة الاحتيال المالي في البنوك والمصارف العاملة في المملكة العربية السعودية الذي يهدف إلى مساعدة البنوك في وضع الحد الأدنى من الإجراءات والسياسات لمكافحة حالات الاحتيال المالي"
- **Related node (Page 4):** "نظام مكافحة غسل الأموال الصادر بالمرسوم الملكي رقم (م/١٠) ... جريمة الاحتيال المالي أحد الجرائم الأصلية لجريمة غسل الأموال"
- **Implication:** Banks' fraud-control frameworks must be designed to satisfy both the fraud guide's minimum standards and AML obligations simultaneously, meaning transaction monitoring rules must flag fraud typologies as potential predicate-offence indicators triggering STR evaluation under the AML Law.

### [[Banking Control Law (referenced)]] — `references` [EXTRACTED]
- **Why:** The Financial Fraud Combating Guide explicitly derives its authority from the Banking Control Law (Royal Decree م/5), citing it alongside the SAMA Establishment Law and AML Law as the legal bases empowering SAMA to issue binding fraud-control requirements on licensed banks. The Banking Control Law thus constitutes the primary supervisory mandate under which the Guide's minimum standards are enforceable.
- **This node (Page 4):** "دليل لمساعدة البنوك والمصارف العاملة في المملكة العربية السعودية في توفير الحد الأدنى من إجراءات ومعايير مكافحة حالات الاحتيال المالي"
- **Related node (Page 4):** "نظام مراقبة البنوك الصادر بالمرسوم الملكي رقم (0/a) بتاريخ 773/.7/77١ه"
- **Implication:** Banks must document that their fraud-control policies and procedures satisfy the Guide's minimum standards as an enforceable obligation grounded in the Banking Control Law, not merely advisory guidance, and SAMA examiners will assess compliance against that legal hierarchy.
- **Caveat:** OCR/bidi rendering of the Royal Decree number is unclear; the locator and excerpt are taken from the Arabic preamble (Page 4) where the decree reference appears; confirm exact decree number against an authenticated Arabic original.

### [[Financial Fraud Combating Unit]] — `references` [EXTRACTED]
- **Why:** The Guide's Table of Contents and definitions chapter explicitly establish the Financial Fraud Combating Unit (وحدة مكافحة الاحتيال) as a defined, mandatory administrative structure within each bank, and Chapter Three of the Guide is dedicated entirely to specifying that unit's tasks, making the unit a direct structural output of the Guide's requirements.
- **This node (Page 3):** "الفصل الثالث: مهام وحدة مكافحة الاحتيال المالي"
- **Related node (Page 5):** "وحدة مكافحة الاحتيال: الوحدة الإدارية في البنك المعنية بمكافحة الاحتيال المالي والتعامل مع الحالات والقضايا ذات العلاقة به"
- **Implication:** Each licensed bank must maintain a formally designated Fraud Combating Unit with a defined administrative mandate; an examiner will expect an organisational chart, terms of reference, and case-management records evidencing the unit's operation as a distinct function.

### [[Governance and Responsibilities]] — `references` [EXTRACTED]
- **Why:** Chapter Two of the Guide (الفصل الثاني) is explicitly titled 'Governance and Responsibilities', embedding governance and accountability structures as a mandatory component of the fraud-control framework, thereby linking the Guide as the normative source that defines governance obligations for fraud risk management.
- **This node (Page 3):** "الفصل الثاني: الحوكمة — الحوكمة والمسئوليات"
- **Related node (Page 4):** "ونظراً للقدرة العالية والمتوقعة من البنوك والمصارف العاملة في المملكة للقيام بمسؤوليتها الرقابية الكاملة والتزامها"
- **Implication:** Banks must establish and document board- or senior-management-level accountability for fraud risk, with a governance framework (roles, responsibilities, escalation paths) that can be evidenced to SAMA examiners under Chapter Two of the Guide.

### [[POS KYC Verification Circular]] — `conceptually_related_to` [INFERRED]
- **Why:** Both instruments address fraud detection and KYC obligations in the payments/banking sector: the Fraud Guide sets the minimum anti-fraud policies and procedures for banks, while the POS KYC Circular mandates that payment service companies verify merchant customers (KYB) before deploying POS devices and maintain fraud detection procedures under the PSP Regulatory Rules. The POS Circular explicitly cites Article 8 of the PSP Rules on fraud detection policies, mirroring the Fraud Guide's minimum-standards framework.
- **This node (Page 4, Preamble / Page 5, Art 1-1):** "دليل لمساعدة البنوك والمصارف العاملة في المملكة العربية السعودية في توفير الحد الأدنى من إجراءات ومعايير مكافحة حالات الاحتيال المالي والتعامل معها"
- **Related node (Page 1):** "إلزامية وضع سياسات وإجراءات للكشف عن حالات الاحتيال والتعامل معها بالإضافة إلى إبلاغ الجهات المختصة في الدولة وإشعار البنك المركزي وفق الصيغة التي يحددها"
- **Implication:** A PSP operating POS channels must map its fraud-detection policies to the minimum standards in the Fraud Guide (governance, unit responsibilities, reporting) and evidence merchant KYC/KYB completion before device activation, creating an auditable pre-onboarding control gate.
- **Caveat:** Confidence INFERRED: the two documents address overlapping regulatory objectives but are directed at different regulated populations (licensed banks vs. payment service companies); direct cross-reference between the two texts is not present in the provided context.

#graphify/document #graphify/EXTRACTED #community/Bank_Fraud_Combating_Rules #graphify/enriched
