---
source_file: "markdown/SAMA_EN_4833_VER1.md"
type: "concept"
community: "Counter-Fraud Framework"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Counter-Fraud_Framework
  - graphify/enriched
---

# Tahaqaq Verification Service

## Connections

### [[Customer Identity Verification via Trusted Source]] — `references` [EXTRACTED]
- **Why:** The Customer Identity Verification circular explicitly mandates that financial institutions use 'Tahaqaq' (خدمة تحقق) as the trusted national source for validating that a mobile number registered against an account belongs to the same identity holder, making Tahaqaq the operative technical mechanism underpinning the CDD obligation.
- **This node (Page 1):** "اعتماد تسجيل رقم جوال العميل المعتمد لدى "خدمة تحقق" ضمن إجراءات فتح الحسابات البنكية أو العضويات الجديدة"
- **Related node (Page 1):** "ربط رقم جوال صاحب الحساب المسجل لدى المؤسسة المالية وفقاً للرقم المعتمد لدى "خدمة تحقق""
- **Implication:** Financial institutions must integrate an API or automated lookup against the national Tahaqaq service into both new account-opening workflows and remediation of existing accounts, with evidence of match/mismatch outcomes retained to demonstrate CDD compliance within the 45-day deadline.

#graphify/concept #graphify/EXTRACTED #community/Counter-Fraud_Framework #graphify/enriched
