---
source_file: "markdown/SAMA_EN_2082_VER1.md"
type: "concept"
community: "Debt Purchase & Fast Transfer"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Debt_Purchase__Fast_Transfer
  - graphify/enriched
---

# SARIE Fast Transfer System

## Connections

### [[Consumer Finance Debt Purchase Instructions]] — `references` [EXTRACTED]
- **Why:** The Consumer Finance Debt Purchase Instructions (Article 8) mandate that the purchasing finance company must use SARIE (the Saudi Fast Transfer System) as the exclusive settlement channel for repaying outstanding debts, and prescribe a minimum data set that each SARIE payment message must carry, directly linking the debt-purchase process to the SARIE system as a required operational control.
- **This node (Page 5 / Article 8 (المادة الثامنة)):** "استخدام النظام السعودي للتحويلات المالية السريعة "سريع" لسداد المديونيات القائمة"
- **Related node (Page 5 / Article 8 (المادة الثامنة)):** "على شركة التمويل الراغبة في شراء المديونية استخدام النظام السعودي للتحويلات المالية السريعة "سريع" لسداد المديونيات القائمة. ويجب أن تتضمن دفعة السداد الصادرة عبر نظام "سريع" بحد أدنى البيانات الآتية: اسم العميل، رقم الهوية الوطنية/ الإقامة، مبلغ المديونية، الغرض من التحويل، رقم…"
- **Implication:** The purchasing finance company's operational system must enforce SARIE as the sole settlement rail for debt-purchase payments and validate that each outgoing SARIE message includes all five mandatory data fields (customer name, national/residence ID, debt amount, transfer purpose, debt reference number) before submission — creating an auditable, structured payment record linking the transaction to the specific consumer debt being extinguished.
- **Caveat:** Both clause_a and clause_b are drawn from the same Article 8 source paragraph; the node_b context for SARIE does not contain a distinct standalone definition excerpt, so both excerpts reference the operative obligation text. OCR/bidi rendering of the Arabic source may affect exact field-name rendering.

#graphify/concept #graphify/EXTRACTED #community/Debt_Purchase__Fast_Transfer #graphify/enriched
