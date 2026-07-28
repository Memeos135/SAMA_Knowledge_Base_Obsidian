---
source_file: "markdown/SAMA_EN_1195_VER1.md"
type: "document"
community: "AML & Payment Regulations"
tags:
  - graphify/document
  - graphify/AMBIGUOUS
  - community/AML__Payment_Regulations
  - graphify/enriched
---

# Law of Payments and Payment Services

## Connections

### [[Business Risk Assessment Guide (AMLCFTPF)|Business Risk Assessment Guide (AML/CFT/PF)]] — `conceptually_related_to` [AMBIGUOUS]
- **Why:** The Business Risk Assessment Guide (10912) covers all SAMA-supervised financial institutions, a category that includes licensed payment service providers under the Law of Payments and Payment Services (1195); PSPs therefore must apply the BRA methodology to their specific product-delivery channels and customer risks, which the Payments Law separately defines and licenses.
- **This node (Page 6, Article 4):** "A person may not operate a payment system or provide payment services in the Kingdom unless licensed by SAMA."
- **Related node (Page 1, covering circular):** "كل مؤسسة مالية مشمولة بتنظيم ورقابة وإشراف البنك المركزي ومُكلفة بتطبيق متطلبات مكافحة غسل الأموال وتمويل الإرهاب وتمويل انتشار التسلح وفقًا لأحكام الأنظمة والتعليمات ذات الصلة"
- **Implication:** PSPs licensed under the Payments Law must conduct and document a BRA under the Guide, including scoring risks arising from their specific payment channels (e-wallets, payment orders, e-money) as a condition of maintaining SAMA supervisory good standing.
- **Caveat:** The link is conceptual/structural rather than an explicit cross-reference in either document's text; confidence is AMBIGUOUS as neither document directly cites the other.

### [[Implementing Regulation to the Law of Payments and Payment Services]] — `implements` [EXTRACTED]
- **Why:** The Law of Payments and Payment Services expressly grants SAMA authority to issue implementing regulations, and the Implementing Regulation to that Law (SAMA_EN_1430) was issued pursuant to and explicitly references that primary law, establishing the hierarchical implements relationship.
- **This node (Page 8 / Article 4):** "A person may not operate a payment system or provide payment services in the Kingdom unless licensed by SAMA... Determining the terms and conditions for issuing licenses, and the legal structure of Payment system operators and payment service providers"
- **Related node (Page 1):** "استنادًا إلى صلاحيات البنك المركزي السعودي بموجب نظام المدفوعات وخدماتها الصادر بالمرسوم الملكي رقم (م/17)... نحيطكم بصدور اللائحة التنفيذية لنظام المدفوعات وخدماتها"
- **Implication:** RegTech systems onboarding payment service providers must map licensing conditions, capital requirements, outsourcing rules, and customer protection obligations to specific Implementing Regulation articles, not merely to the parent Law — audit evidence must trace each control to its IR provision.

#graphify/document #graphify/AMBIGUOUS #community/AML__Payment_Regulations #graphify/enriched
