---
source_file: "markdown/SAMA_EN_10959_VER1.md"
type: "document"
community: "Finance Consumer Protection Laws"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Finance_Consumer_Protection_Laws
  - graphify/enriched
---

# Technical Integration with Waathiq Beneficial Owner Verification Service

## Connections

### [[Anti-Money Laundering Law]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing the legal basis for the Waathiq beneficial-owner integration circular, note it is not a free-standing rule but is anchored in the Anti-Money Laundering Law (Royal Decree M/20) alongside the CTF Law and the AML Implementing Regulation. This means the circular's expectation that FIs use the verification service is enforceable as part of existing CDD/beneficial-owner obligations under the AML regime, not merely an operational suggestion. For a compliance decision, treat use of the service as one channel for meeting the statutory duty to identify and verify beneficial owners — and continue applying your own CDD and STR obligations where data is undisclosed or conflicting, since those flow from the AML Law/Regulation itself.
- **Grounding — this node (SAMA_EN_10959 / Page 1 (preamble)):** "reference to the AML Law issued by Royal Decree M/20 and its Implementing Regulation, as basis for verifying beneficial owner identity"
- **Grounding — related node (SAMA_EN_11005 / Page 1):** "نظام مكافحة غسل الأموال الصادر بالمرسوم الملكي رقم (م/٢٠) ... التزامات على المؤسسات المالية بتطبيق تدابير العناية الواجبة"
- **Caveat:** Node B Arabic source is OCR-garbled; clause_b is an English paraphrase of the circular's cited legal basis.

### [[Beneficial Owner Inquiry Service for Nonprofits]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Treat these two circulars as parallel instruments implementing the same beneficial-owner CDD obligation through two different registries: SAMA_EN_10959 directs integration with the Ministry of Commerce 'Waathiq' service for beneficial owners of *companies*, while SAMA_EN_11005 directs use of the NCNP inquiry service for beneficial owners of *nonprofits and charitable associations*. Both rest on the same AML/CTF Law and AML Implementing Regulation and impose the same fallback: apply your own due diligence and notify where an owner is undisclosed or data conflicts. For a compliance decision, do not assume one covers the other's customer class — confirm which service applies to the customer type, since the obligation is common but the data source is segmented by legal-person category.
- **Grounding — this node (SAMA_EN_10959 / Page 1):** "integration with the 'Waathiq' service for beneficial-owner verification of companies; notify the Ministry of Commerce where undisclosed/conflicting"
- **Grounding — related node (SAMA_EN_11005 / Page 1):** "خدمة الاستعلام عن معلومات المستفيد الحقيقي من الجمعيات والمؤسسات الأهلية ... اتخاذ تدابير العناية الواجبة المطبقة لديها"
- **Caveat:** Relation is INFERRED; node A Arabic is OCR-garbled (clause_a paraphrased). The two circulars are functionally parallel but target different customer classes — verify applicability per customer type in the primary texts.

### [[Beneficial Owner Verification]] — `references` [EXTRACTED]
- **What this link tells you:** This edge tells you the circular's operative subject is the defined AML/CTF duty of beneficial-owner identification and verification — the 'Waathiq' integration is the mechanism, but beneficial-owner verification is the substantive obligation it serves. For compliance purposes, using the service does not discharge the duty by itself: where a company has not disclosed a beneficial owner or where data conflicts, the circular directs the FI to apply its own due-diligence measures and notify the Ministry of Commerce, and to file STRs where warranted. Conclude that the verification duty remains owner of the outcome; the service is a data source feeding it, not a substitute.
- **Grounding — this node (SAMA_EN_10959 / Page 1):** "where a beneficial owner is undisclosed or information differs, the FI applies its own due-diligence measures and notifies via the platform"
- **Grounding — related node (SAMA_EN_10959 / Page 1 (subject line)):** "Technical integration with the 'Waathiq' service to verify the identity of the beneficial owner"
- **Caveat:** Source Arabic is OCR-garbled; excerpts are English paraphrases of the circular's subject and operative instruction.

### [[SAMA Central Bank Law (Royal Decree M36)|SAMA Central Bank Law (Royal Decree M/36)]] — `cites` [EXTRACTED]
- **What this link tells you:** When establishing why SAMA can direct FIs to integrate with the Waathiq service, note the circular grounds its authority in the SAMA Central Bank Law (Royal Decree M/36), which empowers SAMA to issue instructions to institutions under its supervision. This makes the directive binding on 'all financial institutions subject to SAMA's control and supervision' from its publication date, not advisory. For a compliance decision, treat the instruction as a supervisory requirement enforceable against SAMA-regulated FIs — the Central Bank Law supplies the jurisdictional hook, while the AML Law supplies the substantive CDD duty.
- **Grounding — this node (SAMA_EN_10959 / Page 1 (preamble)):** "reference to the SAMA Central Bank Law issued by Royal Decree M/36 and SAMA's competence to issue related instructions to financial institutions"
- **Grounding — related node (SAMA_EN_11021 / Page 1):** "استناداً إلى الصلاحيات المنوطة به بموجب نظامه الصادر بالمرسوم الملكي رقم (م/٣٦)"
- **Caveat:** Node B Arabic is OCR-garbled; clause_b paraphrases the cited legal basis. Locator/decree number for clause_a taken from a separate governance document quoting the same law.

#graphify/document #graphify/EXTRACTED #community/Finance_Consumer_Protection_Laws #graphify/enriched
