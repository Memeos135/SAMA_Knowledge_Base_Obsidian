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

# Ongoing Capital Requirements

## Connections

### [[E-Money Company Classification]] — `references` [EXTRACTED]
- **Why:** E-money company classification is a defined PSP sub-category under the Implementing Regulation; ongoing capital requirements are calibrated per licensee category, so the e-money company classification is the prerequisite that determines which ongoing capital obligation applies to that entity.
- **This node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات"
- **Related node (Page 3 / Table of Contents):** "الفصل الثاني - إصدار النقود الإلكترونية واستردادها"
- **Implication:** An e-money company must maintain a real-time capital adequacy monitor that references its licence classification to apply the correct ongoing capital floor, and must report to SAMA immediately if the floor is breached.
- **Caveat:** Specific article numbers and capital figures for e-money companies are not present in the provided page excerpts; both nodes draw from the same OCR-heavy Arabic source with bidi noise, so the structural inference is based on the table of contents only.

### [[Initial Capital Requirements]] — `references` [EXTRACTED]
- **Why:** The Implementing Regulation treats initial (entry) capital and ongoing capital as a two-stage sequential requirement within the same licensing chapter: initial capital must be demonstrated at licence application, while ongoing capital must be maintained throughout the licence term, with the latter typically defined by reference to the former or to a risk-based formula.
- **This node (Page 3 / Table of Contents):** "الباب الرابع: التزامات المرخص لهم — الفصل الأول: قواعد الإسناد والمراجعة وإدارة المخاطر"
- **Related node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات"
- **Implication:** A PSP must implement a capital monitoring control that distinguishes the one-time initial capital verification (pre-licence) from the continuous ongoing capital obligation (post-licence), with automated alerts to the board and SAMA when ongoing capital approaches or breaches the prescribed minimum.
- **Caveat:** Both nodes reference the same context pages (1–4) where specific initial and ongoing capital figures and article numbers are not visible; the relationship is inferred from the regulatory design pattern of the Implementing Regulation's licensing chapter structure.

### [[Small Payment Company Classification]] — `references` [EXTRACTED]
- **Why:** The Implementing Regulation's licensing chapter differentiates PSP categories including 'small payment company'; ongoing capital requirements are set by reference to the company's classification, so the small-payment-company threshold definition directly determines which ongoing capital floor applies.
- **This node (Page 3 / Table of Contents):** "الفصل الثالث - متطلبات الترخيص لمقدمي خدمات المدفوعات ... الفصل الرابع - نطاق التطبيق على المرخص لهم"
- **Related node (Page 3 / Table of Contents):** "الباب الرابع: التزامات المرخص لهم"
- **Implication:** A licensee's compliance monitoring system must continuously map actual paid-up capital against the ongoing minimum applicable to its specific classification (small vs standard), triggering an alert and SAMA notification if capital falls below the class-specific floor.
- **Caveat:** Specific article numbers and SAR thresholds for small payment company classification and ongoing capital are not visible in the provided context excerpts; the link is inferred from the document's structural chapter references and standard regulatory design.

#graphify/document #graphify/EXTRACTED #community/Payment_Company_Accounts__Capital #graphify/enriched
