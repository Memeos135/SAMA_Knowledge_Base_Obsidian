---
source_file: "markdown/SAMA_EN_1611_VER1.md"
type: "document"
community: "Banking Supervision & Payments"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Banking_Supervision__Payments
  - graphify/enriched
---

# Model Consumer Finance Contract (SAMA 1611)

## Connections

### [[Annual Percentage Rate (APR)]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a consumer finance contract for compliance with SAMA 1611, treat APR not as a free-form figure but as a defined term the model contract requires be disclosed and computed to SAMA's method: the contract defines the Annual Percentage Rate as the discount rate equating the present value of all instalments/payments to the present value of the financing amount, 'calculated per the formula stated in SAMA's instructions.' The contract summary mandates APR disclosure alongside term cost (profit), fees and total amount payable. Conclude that any contract omitting or independently deriving APR, rather than using SAMA's prescribed formula, is non-conforming to the mandatory model.
- **Grounding — this node (Page 4 (contract summary)):** "معدل النسبة السنوي (APR) | %"
- **Grounding — related node (Page 7 (definitions)):** "معدل النسبة السنوي (APR) معدل الخصم الذي تكون فيه القيمة الحالية لجميع الأقساط ... محسوبًا وفق المعادلة المنصوص عليها في تعليمات البنك المركزي السعودي"

### [[Banking Control Law]] — `references` [EXTRACTED]
- **What this link tells you:** Treat this as a weak, unverified lead rather than a live cross-reference: the graph asserts that the Banking Control Law node references the Model Consumer Finance Contract (SAMA 1611), but node B carries no extractable text beyond a filename, so nothing in the supplied context substantiates a genuine legal linkage. The Banking Control Law and its Implementation Rules govern bank licensing, board appointments, inspections and penalties, which is a different regime from a model consumer finance contract. Before relying on any dependency, verify against the primary text of SAMA 1611 whether it actually invokes the Banking Control Law; do not assume the model contract is subordinate to or scoped by that Law on the strength of this edge alone.
- **Grounding — this node:** "sama_en_1611_ver1.pdf (no substantive text available in context)"
- **Grounding — related node (Page 1):** "Implementation Rules for Banking Control Law ... Article (12) regarding appointment to boards of directors and senior positions in banks"
- **Caveat:** Node B has no extractable body text; the 'references' relation is unsupported by the provided context and should be confirmed against SAMA 1611's primary text.

### [[Consumer Protection Principles]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a finance company's consumer contracts are compliant, treat the Model Consumer Finance Contract as a mandatory drafting standard grounded in SAMA's consumer-protection mandate, not merely a template. The covering circular expressly ties the model form to SAMA's ongoing efforts to protect finance-company customers and promote fairness in dealings, and requires all financiers to adopt it from the stated effective date and to enter no contracts that deviate from it. You should conclude that departures from the model form or its embedded consumer-protection features are a compliance exposure, and verify each executed contract against the prescribed structure and disclosures.
- **Grounding — this node (Page 1):** "which all financiers must comply with ... and not enter into any contracts contradicting it (paraphrase of Arabic covering letter)"
- **Grounding — related node (Page 1):** "من جهود البنك المركزي المستمرة لحماية عملاء المؤسسات المالية وتعزيز عدالة التعاملات في القطاع المالي (financier's protection of customers / fairness)"
- **Caveat:** Source is a bilingual circular whose body is Arabic; the consumer-protection basis is paraphrased from the covering letter rather than a discrete titled article.

### [[Credit Information Law]] — `references` [EXTRACTED]
- **What this link tells you:** Treat this as a weak cross-regime lead rather than an established cross-reference: the credit information circular (SAMA 1608) concerns bureaus admitting fintechs that enter a 'credit relationship with the consumer,' while the Model Consumer Finance Contract (SAMA 1611) governs the financing agreement itself between a financier and beneficiary. The plausible connection is that a consumer-finance relationship formed under 1611 is the kind of 'credit relationship' whose data feeds the credit-information regime, but the provided context contains no explicit reference from the Credit Information Law to this model contract. Verify the primary texts before relying on any direct linkage; the substantive overlap is the shared consumer/credit subject, not a citation.
- **Grounding — this node (Page 1):** "الصيغة النموذجية لعقد التمويل الاستهلاكي للأفراد ... تلتزم جهات التمويل كافة الالتزام بها"
- **Grounding — related node (Page 1):** "أن يتضمن نشاط شركة التقنية المالية الذي تسعى لمزاولته دخولها في علاقة ائتمانية مع المستهلك"
- **Caveat:** No explicit citation between the two instruments appears in the provided context; the link rests on a shared consumer-credit subject. Confirm against primary texts before relying on it.

### [[Early Repayment Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** If you are reviewing prepayment terms in a consumer finance agreement, note that early-repayment treatment is a required, standardized clause within the model contract rather than a freely negotiable term. The contract's index lists Article (10) 'Early Repayment Provisions' (أحكام السداد المبكر) and the finance summary cross-references it, meaning every conforming contract must address early settlement on the prescribed basis. You should conclude that omitting or varying an early-repayment clause deviates from the mandated form; confirm the exact substantive terms against Article (10) in the primary text before relying on any particular settlement calculation.
- **Grounding — this node (Page 4):** "أحكام السداد المبكر المادة (10) (Early repayment provisions — Article 10, in the finance summary)"
- **Grounding — related node (Page 3):** "المادة (10): أحكام السداد المبكر (Article 10: Early Repayment Provisions, table of contents)"
- **Caveat:** Substance of the early-repayment terms is not in the provided extract (index/summary only); source Arabic is partly OCR-noisy. Verify Article 10 wording in the full contract.

### [[Finance Companies Control Law]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the legal authority behind the model contract, treat it as a subordinate instrument issued under SAMA's supervisory powers over the finance sector, so its terms bind licensed financiers as a regulatory requirement. The circular states the model form is issued pursuant to SAMA's powers under its own law and the banking-control regime, and it is distributed to banks and finance companies operating in the Kingdom. You should conclude that the model contract carries enforceable weight for SAMA-licensed lenders and that non-compliance is actionable under the parent licensing/supervisory framework; verify the precise enabling instruments cited in the Arabic preamble before asserting a specific statutory basis.
- **Grounding — this node (Page 1):** "licensed under ... and subject to the control and supervision of the Saudi Central Bank (اسم الممول ... مرخص ... وخاضع لرقابة وإشراف البنك المركزي السعودي)"
- **Grounding — related node (Page 1):** "شركات التمويل العاملة في المملكة (finance companies operating in the Kingdom — distribution scope)"
- **Caveat:** The 'Finance Companies Control Law' node is a concept; the preamble's Arabic citing the enabling laws is OCR-garbled, so the exact statute/decree numbers cannot be confirmed from this extract.

#graphify/document #graphify/EXTRACTED #community/Banking_Supervision__Payments #graphify/enriched
