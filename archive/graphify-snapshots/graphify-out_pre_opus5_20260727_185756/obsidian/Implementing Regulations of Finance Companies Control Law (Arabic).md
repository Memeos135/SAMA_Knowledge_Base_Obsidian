---
source_file: "markdown/SAMA_AR_10698_VER1_0.md"
type: "document"
community: "Finance Companies Control Law"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Finance_Companies_Control_Law
  - graphify/enriched
---

# Implementing Regulations of Finance Companies Control Law (Arabic)

## Connections

### [[BNPL Financing Cap Increase Circular]] — `conceptually_related_to` [INFERRED]
- **Why:** The BNPL Financing Cap Increase Circular amends Article 22(1) of the BNPL Company Rules, which govern 'شركة الدفع الآجل' — a licence category defined and regulated within the Implementing Regulations of the Finance Companies Control Law — linking the two instruments through the shared regulatory object of BNPL/deferred-payment activity.
- **This node (Page 3 / Article 1 (Definitions)):** "شركة الدفع الآجل: الشركة الحاصلة على ترخيص لممارسة نشاط الدفع الآجل دون غيره من الأنشطة التمويلية"
- **Related node (Page 1):** "رفع الحد الأعلى لمجموع التمويل القائم لكل عميل فرد في نشاط الدفع الآجل. ليصبح بما لا يتجاوز مبلغ (١٠٠٠٠) عشرة آلاف ريال"
- **Implication:** BNPL companies' credit-limit monitoring systems must be updated to enforce the revised SAR 10,000 per-customer aggregate cap, and the change must be reconciled with the Responsible Finance principles referenced in the same circular to avoid conflicting rule parameters in the origination engine.
- **Caveat:** The Implementing Regulations context provided does not itself set the BNPL cap figure; the cap originates in a separate BNPL-specific ruleset. The conceptual link is confirmed but the Regulations serve as the definitional parent, not the direct source of the amended limit.

### [[Capital Market Law]] — `references` [EXTRACTED]
- **Why:** The Finance Companies Control Law (and hence its Implementing Regulations) expressly reference the Capital Market Law as a parallel conduct standard: founding members and board nominees must not be in breach of the Capital Market Law, and lending restrictions carve out listed joint-stock companies on the Saudi Capital Market, creating a cross-regulatory compliance dependency.
- **This node (Page 3 / Article 1 (Definitions)):** "أنظمة التمويل: نظام التمويل العقاري ونظام الإيجار التمويلي ونظام مراقبة شركات التمويل"
- **Related node (Page 3 / Article 5 (1)(3)(b)):** "not be in breach of the provisions of the Capital Market Law and its Regulations, the Banking Control Law, the Cooperative Insurance Companies Control Law or finance laws"
- **Implication:** Licensing and ongoing fit-and-proper workflows for finance company founders and board nominees must include a screening check against Capital Market Law breach/conviction records, requiring integration with CMA enforcement data or equivalent external source.
- **Caveat:** The Arabic Regulations context provided does not itself cite the Capital Market Law by name; the reference is sourced from the English Law (node_b context). The cross-reference is genuine but arises in the parent Law, not in the Implementing Regulations text shown.

### [[Finance Companies Control Law (English Translation)]] — `references` [EXTRACTED]
- **Why:** The Implementing Regulations (Arabic) were issued expressly pursuant to the Finance Companies Control Law; the Law itself defines 'Regulations' as its own implementing instrument, creating a direct hierarchical dependency whereby the Regulations derive their authority from and must be read alongside the Law.
- **This node (Page 2):** "أصدر البنك المركزي السعودي هذه اللائحة وفقاً للصلاحيات المخولة له بموجب نظام مراقبة شركات التمويل"
- **Related node (Page 2 / Article 1):** "Regulations: Implementing Regulations of this Law. [...] Finance company: A joint stock company licensed to engage in finance activities."
- **Implication:** Any compliance gap analysis for a finance company must be run against both instruments simultaneously; the Arabic Regulations supply operative detail (e.g. activity-specific caps, APR calculation) that the Law delegates but does not itself specify, so a RegTech rule engine must ingest both layers.

#graphify/document #graphify/EXTRACTED #community/Finance_Companies_Control_Law #graphify/enriched
