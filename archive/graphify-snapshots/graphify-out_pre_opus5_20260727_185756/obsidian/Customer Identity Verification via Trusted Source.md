---
source_file: "markdown/SAMA_EN_4833_VER1.md"
type: "document"
community: "Counter-Fraud Framework"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Customer Identity Verification via Trusted Source

## Connections

### [[Due Diligence Standards]] — `conceptually_related_to` [INFERRED]
- **Why:** SAMA_EN_2217 requires Customer Due Diligence to capture and validate customer identity to reduce external fraud losses, while SAMA_EN_4833 operationalises identity verification by mandating mobile-number matching via the national 'Absher/Taqqa' trusted source — directly implementing the verification step that fraud-focused CDD requires.
- **This node (Page 1 / SAMA_EN_4833_VER1):** "يتعيّن على المؤسسات المالية... التحقق من أن رقم الجوال المرتبط بالحساب... عائد لنفس الشخص وذلك من خلال مطابقة رقم الهوية لصاحب الحساب ورقم الهوية لصاحب الجوال في 'خدمة تحقق'"
- **Related node (Page 32 / Section 4.2.2):** "Member Organisations should establish controls to capture and validate the identity of customers to reduce the exposure to external fraud losses."
- **Implication:** CDD onboarding and periodic review workflows must integrate a real-time API call to the national 'Taqqa/Absher' verification service to match account-holder national ID against registered mobile number, with results retained as evidence of identity validation under both the fraud framework and the circular's 45-day remediation mandate.
- **Caveat:** Node B clause is in Arabic; excerpt is transliterated/paraphrased in structure but drawn verbatim from source. Confirm OCR fidelity of Arabic text before use in formal documentation.

### [[Tahaqaq Verification Service]] — `references` [EXTRACTED]
- **Why:** The Customer Identity Verification circular explicitly mandates that financial institutions use 'Tahaqaq' (خدمة تحقق) as the trusted national source for validating that a mobile number registered against an account belongs to the same identity holder, making Tahaqaq the operative technical mechanism underpinning the CDD obligation.
- **This node (Page 1):** "ربط رقم جوال صاحب الحساب المسجل لدى المؤسسة المالية وفقاً للرقم المعتمد لدى "خدمة تحقق""
- **Related node (Page 1):** "اعتماد تسجيل رقم جوال العميل المعتمد لدى "خدمة تحقق" ضمن إجراءات فتح الحسابات البنكية أو العضويات الجديدة"
- **Implication:** Financial institutions must integrate an API or automated lookup against the national Tahaqaq service into both new account-opening workflows and remediation of existing accounts, with evidence of match/mismatch outcomes retained to demonstrate CDD compliance within the 45-day deadline.

#graphify/document #graphify/INFERRED #community/Counter-Fraud_Framework #graphify/enriched
