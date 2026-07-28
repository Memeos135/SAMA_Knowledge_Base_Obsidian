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

# Controller

## Connections

### [[Data Subject]] — `conceptually_related_to` [EXTRACTED]
- **Why:** The PDPL structurally defines the Controller as the party that determines the purpose and manner of processing and imposes direct obligations toward the Data Subject, including the duty to maintain a privacy policy, respond to access/rectification rights, apply data-minimisation, and destroy data once the purpose is fulfilled.
- **This node (Page 3 / Article 1(18)):** "Controller: Any public entity or any private natural or legal person that determines the purpose and manner of personal data processing, whether it conducts such processing…"
- **Related node (Page 14 / Appendix / amended Article 1(16)):** "Data Subject: An individual to whom personal data relate."
- **Implication:** A SAMA-regulated entity acting as Controller must implement a subject-rights workflow (access, rectification, erasure, portability) with auditable response timelines and a published privacy policy, evidenced per Articles 4, 12, and 31 of the PDPL.

### [[Personal Data Protection Law]] — `references` [EXTRACTED]
- **Why:** The PDPL defines 'Controller' in Article 1 and then imposes a cascade of substantive obligations—processor selection and oversight, processing records, privacy policy, registration, consent management—directly on that defined role, making the Controller concept the primary duty-bearer node within the Law.
- **This node (Page 11 / Article 31):** "The controller shall, according to the nature of the activity carried out thereby, keep records of the activities of personal data processing for a period determined by the Regulations to be available when requested by the Competent Authority."
- **Related node (Page 3 / Article 1(4–5)):** "Personal Data: All data… that would identify an individual or make it possible to identify him directly or indirectly… Processing: Any operation performed on personal data by manual or automated means, such as the collection, recording, preservation… or destruction of personal d…"
- **Implication:** A data-governance system must map every organisational entity that determines the purpose and means of processing to the PDPL 'Controller' role, then assign that entity ownership of Article 31 processing records, processor contracts, privacy policy publication, and national-register registration—each with retention periods set by the Regulations and producible on Competent Authority request.

### [[Processor]] — `conceptually_related_to` [EXTRACTED]
- **Why:** The PDPL mandates that the Controller select a Processor providing 'necessary guarantees' for PDPL compliance, verify ongoing compliance, and retain full accountability toward the Data Subject and Competent Authority notwithstanding delegation — creating a principal-agent compliance chain with contractual and audit requirements.
- **This node (Page 15 / Appendix / amended Article 8):** "the controller shall select a processor that provides the necessary guarantees for implementing the provisions of this Law and the Regulations, and shall verify the processor's compliance with the provisions of this Law and the Regulations."
- **Related node (Page 4 / Article 1(19)):** "Processor: Any public entity or any private natural or legal person that processes personal data for the benefit or on behalf of the controller."
- **Implication:** SAMA-regulated entities outsourcing data processing (e.g., to cloud providers, fintechs, or bureaus) must maintain a vendor-due-diligence and ongoing-monitoring programme with documented contractual clauses covering sub-processor chains, directly evidenceable to an examiner under Article 8 and Article 31 record-keeping requirements.

#graphify/concept #graphify/EXTRACTED #community/Personal_Data_Protection #graphify/enriched
