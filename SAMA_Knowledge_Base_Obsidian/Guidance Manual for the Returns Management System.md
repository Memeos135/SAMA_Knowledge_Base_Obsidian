---
source_file: "markdown/الدليل الإرشادي لاستخدام نظام البيانات الإشرافية_0.md"
type: "document"
community: "Regulatory Data Returns"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Regulatory_Data_Returns
  - graphify/enriched
---

# Guidance Manual for the Returns Management System

## Connections

### [[Annual Regulatory Data Form]] — `shares_data_with` [INFERRED]
- **What this link tells you:** If you are scoping the reporting obligations of a supervised money-exchange/currency center, this link indicates the Annual Regulatory Data Form is one of the return templates likely submitted through SAMA's Returns Management System (RMS), the digital platform for entities under SAMA supervision to file supervisory returns. The connection is inferred from the shared SAMA supervisory-reporting context, not from an explicit reference in either document; the RMS manual describes generic return upload/validation steps and the form belongs to the currency-centers supervision division. Confirm from SAMA's return catalogue that this specific form is filed via RMS and on what periodicity before treating RMS as the mandated submission channel for it.
- **Grounding — this node (Page 2):** "a digital platform enabling companies under Central Bank supervision to submit supervisory returns per the defined templates (English paraphrase; source Arabic is OCR-garbled)"
- **Grounding — related node (Page 1):** "Money Exchange Centers Supervision Division / licensing, branches and leadership positions data (English paraphrase; source Arabic is OCR-garbled)"
- **Caveat:** INFERRED; neither document expressly names the other. Source Arabic is OCR-garbled. Verify the form is an RMS return via SAMA's return catalogue.

### [[Monthly Sales and Purchases Data Form]] — `shares_data_with` [INFERRED]
- **What this link tells you:** For a supervised money-exchange center's monthly reporting, this link indicates the Monthly Sales and Purchases Data Form is likely a return filed through SAMA's RMS platform, which the manual shows supports monthly returns (e.g. 'ME Monthly Return'). The connection is inferred from the shared currency-centers supervisory-return context and the manual's monthly-return upload example, not from an explicit reference in the form itself. Confirm via SAMA's return catalogue that this specific form is an RMS return and its filing deadline before treating RMS as the mandated submission route.
- **Grounding — this node (Page 6):** "ME Monthly Return... The file will be processed. If any validation errors are found the user will receive an email"
- **Grounding — related node (Page 1):** "Money Exchange Centers Supervision Division (English paraphrase; source Arabic is OCR-garbled; form body not provided)"
- **Caveat:** INFERRED; node A provides essentially only a division header. No express cross-reference. Verify the form is an RMS monthly return via SAMA's return catalogue.

### [[Quarterly Currency and Top Clients Form]] — `shares_data_with` [INFERRED]
- **What this link tells you:** If you are advising a money-exchange business on its reporting obligations, do not assume this quarterly currency form and the RMS manual describe the same filing channel without checking the primary text. The quarterly form is a currency/top-clients/counterfeit/staff return used by exchange centres under SAMA's exchange-supervision unit, while the RMS manual describes SAMA's general 'Return Management System' portal for entities submitting prudential returns; the two appear to share a data-collection purpose but the RMS documentation shown here centres on prudential (quarterly/annual) returns for supervised companies, not this exchange form specifically. Verify whether this particular quarterly form is in fact a defined return submitted through RMS before treating the manual's submission steps as governing it.
- **Grounding — this node (Page 2 / Definitions):** "منصة رقمية تمكن الشركات الخاضعة لإشراف البنك المركزي من تسليم النماذج الإشرافية حسب النماذج المعرفة"
- **Grounding — related node (Page 7):** "شعبة الرقابة على مراكز الصرافة ... النموذج الربعي للعملات وبيانات أكبر العملاء والعملات المزورة وبيانات الموظفين"
- **Caveat:** INFERRED link; the RMS manual describes prudential returns generally and does not name this exchange form. Confirm in the primary sources whether this form is submitted via RMS.

### [[Quarterly and Annual Financial Statements Comparison Form]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When mapping a currency center's periodic financial reporting duties, this link suggests the Quarterly and Annual Financial Statements Comparison Form is a supervisory return submitted through SAMA's RMS, which handles quarterly and annual return periods for supervised firms. The relationship is inferred from the common supervisory-return context — the form is a SAMA currency-centers template and the RMS manual expressly handles 'Quarterly - Annually' return periods — rather than from a cited cross-reference. Confirm from SAMA's return catalogue that this form is an RMS-filed return and its exact frequency before relying on RMS as the required channel.
- **Grounding — this node (Page 4):** "For each financial period (Quarterly - Annually) the RMS will send a notification to portal users via email when creating the return"
- **Grounding — related node (Page 1):** "Financial statements comparison form, version 2.0 / Money Exchange Centers Supervision Division (English paraphrase; source Arabic is OCR-garbled)"
- **Caveat:** INFERRED; no express cross-reference between the documents. Node A Arabic is OCR-garbled. Verify against SAMA's return catalogue.

### [[SAMA Circular on Amended LCR Prudential Returns]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When determining how a bank actually files its Amended LCR prudential returns, treat this as a lead rather than an established rule: the LCR circular sets the substantive obligation to submit prudential returns on defined deadlines, while the RMS manual describes the portal mechanism SAMA uses for submitting returns generally. Both concern 'prudential returns,' so the RMS process may be the current channel for the LCR filings, but the circular pre-dates the manual (2013 vs 2022) and does not itself reference RMS. Confirm from a current SAMA instruction whether LCR returns must now be filed through RMS before relying on the manual's steps for that obligation.
- **Grounding — this node (Page 4):** "Steps to submit the Prudential Return into Return Management System ... the RMS will send a notification to portal users via email when creating the return 'Prudential Returns'"
- **Grounding — related node (Page 2):** "the attached Prudential Returns should be completed on the basis of the above guidance documents ... provide their returns to SAMA on a monthly basis"
- **Caveat:** INFERRED; the circular does not mention RMS and predates the manual. The shared concept is 'prudential returns' only — verify the governing submission channel in current SAMA guidance.

#graphify/document #graphify/INFERRED #community/Regulatory_Data_Returns #graphify/enriched
