---
source_file: "markdown/document.md"
type: "concept"
community: "Personal Data Protection"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Personal_Data_Protection
  - graphify/enriched
---

# Credit Data Processing

## Connections

### [[Credit Information Law]] — `references` [EXTRACTED]
- **Why:** The Personal Data Protection Law's definition of 'Personal Data' explicitly includes 'bank accounts, and credit card numbers', overlapping directly with the Credit Information Law's scope of 'credit transactions' data; entities processing credit information must comply with both regimes simultaneously, as credit data constitutes personal data subject to PDPL controls.
- **This node (Page 3 / Article 1):** "Personal Data: All data... that would identify an individual... including his name... bank accounts, and credit card numbers... and any other data of a personal nature."
- **Related node (Page 2 / Article 1):** "Credit Information: Information and data on consumers with respect to credit transactions, such as: loans, installment purchase, lease, credit sale and credit cards and their commitment to payment."
- **Implication:** A RegTech system processing credit bureau data must enforce dual-regime controls: PDPL consent/minimisation requirements (Art. 11) and Credit Information Law written-consent requirements (Art. 9(1)), with audit trails evidencing lawful basis under each law separately.

### [[Personal Data Protection Law]] — `references` [EXTRACTED]
- **Why:** Credit data—including bank accounts and credit card numbers—falls within the PDPL's definition of 'Personal Data', meaning any credit data processing operation (collection, storage, sharing with bureaus, etc.) is directly governed by the obligations and lawful-basis requirements of the PDPL.
- **This node (Page 3 / Article 1(4)):** "Personal Data: All data…that would identify an individual or make it possible to identify him directly or indirectly, including…bank accounts, and credit card numbers…and any other data of a personal nature."
- **Related node (Page 6 / Article 11(1)):** "The purpose of the collection of personal data shall be directly related to the original purpose of the controller and shall not be inconsistent with any statutory provision."
- **Implication:** A credit bureau or lender's data-processing system must enforce purpose-limitation controls ensuring that credit data collected for underwriting is not subsequently used for incompatible purposes, with audit-trail evidence of the declared collection purpose for each data element.

#graphify/concept #graphify/EXTRACTED #community/Personal_Data_Protection #graphify/enriched
