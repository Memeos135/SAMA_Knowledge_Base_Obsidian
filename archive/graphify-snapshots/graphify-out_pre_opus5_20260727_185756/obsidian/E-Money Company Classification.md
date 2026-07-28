---
source_file: "markdown/SAMA_EN_1430_VER1.md"
type: "document"
community: "Payment Company Accounts & Capital"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Payment_Company_Accounts__Capital
  - graphify/enriched
---

# E-Money Company Classification

## Connections

### [[Ongoing Capital Requirements]] — `references` [EXTRACTED]
- **Why:** E-money company classification is a defined PSP sub-category under the Implementing Regulation; ongoing capital requirements are calibrated per licensee category, so the e-money company classification is the prerequisite that determines which ongoing capital obligation applies to that entity.
- **This node (Page 3 / Table of Contents):** "الفصل الثاني - إصدار النقود الإلكترونية واستردادها"
- **Related node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات"
- **Implication:** An e-money company must maintain a real-time capital adequacy monitor that references its licence classification to apply the correct ongoing capital floor, and must report to SAMA immediately if the floor is breached.
- **Caveat:** Specific article numbers and capital figures for e-money companies are not present in the provided page excerpts; both nodes draw from the same OCR-heavy Arabic source with bidi noise, so the structural inference is based on the table of contents only.

### [[Protection and Safeguarding of Protected Funds]] — `references` [INFERRED]
- **Why:** E-money issuance inherently creates a float of client funds that must be segregated and protected; the Implementing Regulation dedicates a standalone chapter (الباب السابع) to protection and safeguarding of protected funds, which directly governs how an e-money company must handle the float arising from its issuance activity.
- **This node (Page 3 / Table of Contents):** "الفصل الثاني - إصدار النقود الإلكترونية واستردادها"
- **Related node (Page 3 / Table of Contents):** "الباب السابع: حماية وحفظ الأموال المحمية"
- **Implication:** An e-money company's systems must segregate issued e-money float into a designated safeguarding account on a real-time basis and produce a daily reconciliation evidencing that 100% of outstanding e-money liabilities are covered by protected funds held separately from own funds.
- **Caveat:** Specific safeguarding mechanics and percentage-coverage rules are not visible in the provided page excerpts; the link is structurally inferred from the table of contents; set caveat accordingly.

#graphify/document #graphify/EXTRACTED #community/Payment_Company_Accounts__Capital #graphify/enriched
