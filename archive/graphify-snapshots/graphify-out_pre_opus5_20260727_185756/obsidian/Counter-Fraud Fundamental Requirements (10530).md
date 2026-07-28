---
source_file: "markdown/SAMA_EN_10530_VER1.md"
type: "document"
community: "Counter-Fraud Requirements"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Counter-Fraud_Requirements
  - graphify/enriched
---

# Counter-Fraud Fundamental Requirements (10530)

## Connections

### [[Anti-Fraud Rules for Finance Companies (circular 381000103246)]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Fundamental Requirements document defines 'Financial Institution' as the regulated entity subject to its controls, which encompasses finance companies governed by SAMA's Anti-Fraud Rules for Finance Companies, establishing the prior regulatory basis that these requirements build upon.
- **This node (Page 10, SAMA_EN_10530_VER1.md):** "Member Organizations should develop a risk-based Counter-Fraud Programme proportional to the size and nature of its business to address people, process, and technology, including adequate systems and controls to prevent, detect and respond to fraud."
- **Related node (Page 18, SAMA_EN_10530_VER1.md):** "External Fraud: A fraudulent event conducted by any persons on the 'outside' of the organization i.e., not employed by the organization."
- **Implication:** Finance companies must map their existing Anti-Fraud Rules obligations against the five domains of the Fundamental Requirements (Governance, Prevention, Detection, Response, Technology) to identify gaps and produce the Board-approved roadmap required by circular 10529.
- **Caveat:** The node 'Anti-Fraud Rules for Finance Companies (circular 381000103246)' is referenced as a concept within 10530's source file but the verbatim citation of that circular number does not appear in the extracted page context; the link is inferred from the document's regulatory scope covering finance companies and from the circular 10529 cover letter.

### [[Counter-Fraud Framework (CFF)]] — `references` [EXTRACTED]
- **Why:** The Counter-Fraud Fundamental Requirements document operationalises the Counter-Fraud Framework (CFF) concept by defining its constituent elements — Programme, Policy, Governance Committee, and Technology — and assigning specific control requirements to each, making the document the primary reference text for the CFF construct.
- **This node (Page 8, SAMA_EN_10530_VER1.md):** "The Fundamental Requirements span the prevention, detection, and response to fraud, as well as the governance of a Member Organization's Counter-Fraud Programme. Chapter 3 … is structured around five domains."
- **Related node (Page 17, SAMA_EN_10530_VER1.md):** "Counter-Fraud Programme: A collection of strategy, policies, processes, guidelines, risk management approaches, actions, training, best practices, assurance, and technologies that are used to protect the Member Organization and its customers against internal and external fraud t…"
- **Implication:** A RegTech architect mapping the CFF must instantiate all five domains as distinct control modules (Governance, Prevention, Detection, Response, Technology), each with KPI/KRI monitoring capability, to satisfy the document's numbered control requirements and demonstrate programme completeness to a SAMA examiner.

### [[Counter-Fraud Fundamental Requirements Circular (10529)]] — `semantically_similar_to` [INFERRED]
- **Why:** Document 10529 is the SAMA circular mandating compliance with the Counter-Fraud Fundamental Requirements, while document 10530 is the substantive requirements document itself; the circular explicitly approves and promulgates the guide, making the two inseparable in the compliance chain.
- **This node (Page 8, SAMA_EN_10530_VER1.md):** "The Fundamental Requirements span the prevention, detection, and response to fraud, as well as the governance of a Member Organization's Counter-Fraud Programme."
- **Related node (Page 1, SAMA_EN_10529_VER1.md):** "نفيدكم باعتماد دليل المتطلبات الأساسية لمكافحة الاحتيال (Counter-Fraud Fundamental Requirements) والذي يهدف إلى تعزيز ممارسات مكافحة الاحتيال"
- **Implication:** Any SAMA examination of counter-fraud compliance will treat the circular (10529) as the enforceable mandate and the requirements document (10530) as the control benchmark; both must be mapped together in a compliance gap-assessment workflow with Board-approved roadmap evidence.
- **Caveat:** Confidence is INFERRED because the two documents are separate files and the circular's direct citation of the guide's reference number is rendered in OCR-degraded Arabic; however the substantive link is unambiguous from context.

#graphify/document #graphify/EXTRACTED #community/Counter-Fraud_Requirements #graphify/enriched
