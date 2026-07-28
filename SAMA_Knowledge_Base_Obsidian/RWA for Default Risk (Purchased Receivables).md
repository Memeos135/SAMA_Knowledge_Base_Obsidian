---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB CRM & Receivables"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_CRM__Receivables
  - graphify/enriched
---

# RWA for Default Risk (Purchased Receivables)

## Connections

### [[Eligible Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising purchased receivables, treat the default-risk RWA method and the eligibility definition as a chained test: the receivables must first qualify as 'eligible purchased receivables' (retail vs corporate, with the corporate top-down route limited to cases of undue burden), and only then is the chapter 14 default-risk risk-weight function applied. Chapter 14 expressly presupposes eligibility — it 'presents the method of calculating the unexpected loss capital requirements for purchased receivables' with 'IRB capital charges for both default risk and dilution risk' — while chapter 10 defines which receivables and which approach (F-IRB vs A-IRB) are available. Conclude that a reviewer must confirm the eligibility classification and permitted approach before accepting the default-risk RWA calculation.
- **Grounding — this node (Page 168 / Para 14.1–14.2):** "there are internal ratings-based (IRB) capital charges for both default risk and dilution risk ... the IRB risk weight for default risk is based on the risk-weight function applicable to that particular exposure type"
- **Grounding — related node (Page 105 / Para 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available ... For eligible retail receivables ... only the A-IRB approach is available."

### [[Top-Down Approach for Purchased Corporate Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating default-risk RWA for purchased corporate receivables, first resolve whether the top-down approach is even available, because it is a supervisory-permission exception, not a default choice. Chapter 14 says banks are expected to apply bottom-up IRB quantification but 'may employ' top-down for eligible corporate receivables subject to supervisory permission, and chapter 10 (paras 10.27–10.28) limits top-down to undue-burden situations, subjects it to eligibility conditions, and lets SAMA deny it. Conclude that RWA-for-default-risk calculation cannot be finalized until you confirm the receivables meet the chapter 10 eligibility conditions and that SAMA has not withheld or restricted top-down use.
- **Grounding — this node (Page 168 / para 14.4):** "for eligible purchased corporate receivables, and subject to supervisory permission, a bank may employ [the top-down approach]"
- **Grounding — related node (Page 101 / para 10.28):** "SAMA may deny the use of the top-down approach for purchased corporate receivables depending on the bank's compliance with minimum requirements."

#graphify/concept #graphify/EXTRACTED #community/IRB_CRM__Receivables #graphify/enriched
