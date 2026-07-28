---
source_file: "markdown/document.md"
type: "document"
community: "Personal Data Protection"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Personal_Data_Protection
  - graphify/enriched
---

# Personal Data Protection Law

## Connections

### [[Competent Authority (PDPL)]] — `references` [EXTRACTED]
- **Why:** The PDPL defines 'Competent Authority' as a core term and simultaneously assigns it binding supervisory, registration, enforcement, and licensing powers throughout the Law; the Competent Authority concept is therefore constitutively defined by and operative only within the PDPL framework.
- **This node (Page 3 / Article 1(3)):** "Competent Authority: The authority to be determined pursuant to a resolution by the Council of Ministers."
- **Related node (Page 11 / Article 32):** "The Competent Authority shall establish an electronic portal for the purpose of creating a national register for controllers. Said portal shall aim to monitor the controllers' compliance with this Law and the Regulations."
- **Implication:** A compliance system must treat the Competent Authority as the single supervisory counterparty for PDPL obligations—controller registration, processing records availability, accreditation licensing, and penalty proceedings must all be routed to or evidenced for that authority, with the specific entity confirmed by reference to the relevant Council of Ministers resolution.

### [[Controller]] — `references` [EXTRACTED]
- **Why:** The PDPL defines 'Controller' in Article 1 and then imposes a cascade of substantive obligations—processor selection and oversight, processing records, privacy policy, registration, consent management—directly on that defined role, making the Controller concept the primary duty-bearer node within the Law.
- **This node (Page 3 / Article 1(4–5)):** "Personal Data: All data… that would identify an individual or make it possible to identify him directly or indirectly… Processing: Any operation performed on personal data by manual or automated means, such as the collection, recording, preservation… or destruction of personal d…"
- **Related node (Page 11 / Article 31):** "The controller shall, according to the nature of the activity carried out thereby, keep records of the activities of personal data processing for a period determined by the Regulations to be available when requested by the Competent Authority."
- **Implication:** A data-governance system must map every organisational entity that determines the purpose and means of processing to the PDPL 'Controller' role, then assign that entity ownership of Article 31 processing records, processor contracts, privacy policy publication, and national-register registration—each with retention periods set by the Regulations and producible on Competent Authority request.

### [[Credit Data Processing]] — `references` [EXTRACTED]
- **Why:** Credit data—including bank accounts and credit card numbers—falls within the PDPL's definition of 'Personal Data', meaning any credit data processing operation (collection, storage, sharing with bureaus, etc.) is directly governed by the obligations and lawful-basis requirements of the PDPL.
- **This node (Page 6 / Article 11(1)):** "The purpose of the collection of personal data shall be directly related to the original purpose of the controller and shall not be inconsistent with any statutory provision."
- **Related node (Page 3 / Article 1(4)):** "Personal Data: All data…that would identify an individual or make it possible to identify him directly or indirectly, including…bank accounts, and credit card numbers…and any other data of a personal nature."
- **Implication:** A credit bureau or lender's data-processing system must enforce purpose-limitation controls ensuring that credit data collected for underwriting is not subsequently used for incompatible purposes, with audit-trail evidence of the declared collection purpose for each data element.

### [[Data Subject]] — `references` [EXTRACTED]
- **Why:** The PDPL defines 'Data Subject' as the individual to whom personal data relate and constructs an enumerated set of enforceable rights (access, rectification, erasure, etc.) held by that individual against the controller, making the concept legally operative only within and through the PDPL framework.
- **This node (Page 14 / Appendix):** "'The data subject shall, pursuant to this Law and the Regulations, have the following rights: 1. Right to be informed…2. Right of access…3. Right to request personal data…4. Right to rectifica[tion]…'"
- **Related node (Page 14 / Appendix (Royal Decree M/148, 5/9/1444H)):** "'16. Data Subject: An individual to whom personal data relate.'"
- **Implication:** Controllers must implement a subject-rights management workflow—covering intake, identity verification, response-timing, and audit logging—mapped directly to each enumerated right in the PDPL and its Implementing Regulations.

### [[Processor]] — `references` [EXTRACTED]
- **Why:** The PDPL explicitly defines 'Processor' as a distinct legal role and imposes on the controller a duty to select processors offering adequate compliance guarantees and to verify ongoing adherence, establishing a controller-processor accountability chain within the statute itself.
- **This node (Page 4 / Article 1(19)):** "Processor: Any public entity or any private natural or legal person that processes personal data for the benefit or on behalf of the controller."
- **Related node (Page 15 / Appendix (amended Article 8)):** "'…the controller shall select a processor that provides the necessary guarantees for implementing the provisions of this Law and the Regulations, and shall verify the processor's compliance with the provisions of this Law and the Regulations.'"
- **Implication:** Controllers must maintain a processor register with documented due-diligence assessments, contractual clauses covering sub-processor chains, and periodic compliance verification records auditable by the Competent Authority.

### [[Saudi Central Bank (PDPL)]] — `references` [EXTRACTED]
- **Why:** The PDPL explicitly defines 'Credit Data' as personal data relating to an individual's financing applications or creditworthiness, directly intersecting with SAMA-regulated entities (banks, finance companies, credit bureaus) that collect and process such data; SAMA-licensed institutions are therefore Controllers or Processors under the PDPL when handling customer credit and financial information.
- **This node (Page 3 / Article 1(15)):** "Credit Data: Any personal data relating to an individual's application for financing or receipt thereof from a funding entity for personal or family purposes, including any data relating to his creditworthiness or credit history."
- **Related node (Page 3 / Article 1(11)):** "Sensitive Data: Any personal data that indicate or include a reference to a person's… credit data; health data; location data; and data that indicate that one, or both, of an individual's parents are unknown."
- **Implication:** SAMA-regulated entities processing credit data must treat it as Sensitive Data under the PDPL, requiring elevated collection justification, consent controls, and data-minimisation safeguards — all of which an examiner would expect to see documented in the entity's privacy policy and data-processing records.
- **Caveat:** The provided context identifies the PDPL document but the node_b label 'Saudi Central Bank (PDPL)' does not correspond to a distinct SAMA regulatory text in the corpus; the link is inferred from the PDPL's definition of Credit Data and its inherent applicability to SAMA-licensed entities as Controllers/Processors.

#graphify/document #graphify/EXTRACTED #community/Personal_Data_Protection #graphify/enriched
