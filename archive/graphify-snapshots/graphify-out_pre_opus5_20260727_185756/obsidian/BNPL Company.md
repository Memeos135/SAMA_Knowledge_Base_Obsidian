---
source_file: "markdown/SAMA_EN_6523_VER1.md"
type: "concept"
community: "AML/CTF BNPL Finance Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML/CTF_BNPL_Finance_Rules
  - graphify/enriched
---

# BNPL Company

## Connections

### [[AMLCTF Compliance Requirements|AML/CTF Compliance Requirements]] — `references` [EXTRACTED]
- **Why:** The Rules directly impose AML/CTF obligations on the BNPL Company as part of its mandatory internal policies and information-security/financial-crimes compliance framework, making AML/CTF requirements a subset of the BNPL Company's enforceable regulatory burden.
- **This node (Page 8 / Article 14):** "the company shall comply with the requirements and instructions issued by SAMA on financial crimes."
- **Related node (Page 7 / Article 13):** "Develop appropriate written organizational policies that address, at least… anti-money laundering and counter-terrorist financing (AML/CTF)."
- **Implication:** A BNPL Company must maintain documented AML/CTF policies and evidence of compliance with SAMA's financial-crimes instructions as a licensing condition, examinable via supervisory visits under Article 29; the RegTech architecture must include transaction monitoring and STR workflows calibrated to BNPL transaction patterns.

### [[Consumer Due Diligence Program]] — `references` [EXTRACTED]
- **Why:** Article 21 of the BNPL Rules directly imposes on the BNPL Company a mandatory obligation to develop and operate a Consumer Due Diligence (CDD) program, making the BNPL Company the regulated entity that owns and must operationalise the CDD program as a licensing condition.
- **This node (Page 3 / Article 1):** "BNPL Company: A joint stock company licensed by SAMA to engage in BNPL activity."
- **Related node (Page 10 / Article 21):** "The BNPL company shall develop a CDD program and comply with the AML/CTF regulations and instructions. The CDD program must include policies and procedures for the following, as a minimum: a. Know Your Customer (KYC). b. Information security. c. Data privacy and confidentiality."
- **Implication:** A SAMA examiner will expect the BNPL company to produce a documented CDD program covering KYC, information security, and data privacy, with evidence of consumer identity verification (including phone and national address checks per Art. 21.2) maintained for at least 10 years per Art. 13.4.

### [[Credit Information Registration]] — `references` [EXTRACTED]
- **Why:** Article 19(3) imposes a standing obligation on the BNPL Company to register each consumer's credit information with licensed credit information companies and keep it current, creating a direct regulatory link between the BNPL Company's operational activity and the credit information registration regime.
- **This node (Page 3 / Article 1):** "BNPL Company: A joint stock company licensed by SAMA to engage in BNPL activity."
- **Related node (Page 9 / Article 19(3)):** "Register the consumer's credit information, with their consent, at one or more of the companies licensed to collect credit information according to the relevant laws, regulations and instructions. Such information must be updated throughout the period of dealing with the consume…"
- **Implication:** The BNPL company's origination workflow must capture consumer consent at onboarding, trigger real-time or periodic data feeds to licensed credit bureaus, and maintain an audit trail showing registration and ongoing update events per the finance contract lifecycle; this is independently verifiable by SAMA during supervisory visits under Art. 28.

### [[Rules for Regulating BNPL Companies]] — `references` [EXTRACTED]
- **Why:** The BNPL Company is the defined regulated entity whose entire existence, licensing, obligations, and conduct are governed by the Rules; the Rules are the primary instrument constituting the BNPL Company as a legal/regulatory subject and imposing enforceable requirements on it.
- **This node (Page 3 / Article 1):** "BNPL Company: A joint stock company licensed by SAMA to engage in BNPL activity."
- **Related node (Page 3 / Article 2):** "These Rules apply to companies licensed by SAMA to engage in BNPL activity."
- **Implication:** Any compliance programme, licensing workflow, or examiner-readiness checklist for a BNPL Company must map every obligation to a specific article in these Rules as the controlling instrument.

#graphify/concept #graphify/EXTRACTED #community/AML/CTF_BNPL_Finance_Rules #graphify/enriched
