---
source_file: "markdown/SAMA_EN_2217_VER1.md"
type: "concept"
community: "Counter-Fraud Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Due Diligence Standards

## Connections

### [[Customer Identity Verification via Trusted Source]] — `conceptually_related_to` [INFERRED]
- **Why:** SAMA_EN_2217 requires Customer Due Diligence to capture and validate customer identity to reduce external fraud losses, while SAMA_EN_4833 operationalises identity verification by mandating mobile-number matching via the national 'Absher/Taqqa' trusted source — directly implementing the verification step that fraud-focused CDD requires.
- **This node (Page 32 / Section 4.2.2):** "Member Organisations should establish controls to capture and validate the identity of customers to reduce the exposure to external fraud losses."
- **Related node (Page 1 / SAMA_EN_4833_VER1):** "يتعيّن على المؤسسات المالية... التحقق من أن رقم الجوال المرتبط بالحساب... عائد لنفس الشخص وذلك من خلال مطابقة رقم الهوية لصاحب الحساب ورقم الهوية لصاحب الجوال في 'خدمة تحقق'"
- **Implication:** CDD onboarding and periodic review workflows must integrate a real-time API call to the national 'Taqqa/Absher' verification service to match account-holder national ID against registered mobile number, with results retained as evidence of identity validation under both the fraud framework and the circular's 45-day remediation mandate.
- **Caveat:** Node B clause is in Arabic; excerpt is transliterated/paraphrased in structure but drawn verbatim from source. Confirm OCR fidelity of Arabic text before use in formal documentation.

### [[Prevent Domain]] — `references` [EXTRACTED]
- **Why:** Due Diligence Standards are explicitly listed as a mandated control category within the Prevent Domain's fraud prevention standards, serving as the primary mechanism for preventing establishment of fraudulent relationships with employees, customers and third parties before harm occurs.
- **This node (Page 31 / Section 4.2):** "Member Organisations should define, approve and implement standards for assessing the fraud risk associated with employees, customers and third parties to prevent the establishment of relationships outside risk appetite and manage fraud risks throughout the duration of the relat…"
- **Related node (Page 40 / Section 4.6 (Prevent Domain controls)):** "The controls implemented to prevent fraud (e.g., segregation of duties, approval and escalations, employee training, access restrictions, due diligence and integrity checks, notification of account changes, transaction limits, underwriting checks)."
- **Implication:** Due Diligence Standards must be versioned artefacts that are explicitly cross-referenced in the fraud prevention standards document, with evidence of periodic review, risk-based tiering for employees/customers/third parties, and outcomes fed back into the Fraud Risk Assessment cycle.

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
