---
source_file: "markdown/SAMA_EN_853_VER1.md"
type: "document"
community: "AML/CTF BNPL Finance Rules"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/AML/CTF_BNPL_Finance_Rules
  - graphify/enriched
---

# Law on Combating the Financing of Terrorism

## Connections

### [[AMLCTF Compliance Requirements|AML/CTF Compliance Requirements]] — `references` [INFERRED]
- **Why:** The BNPL Rules require BNPL companies to maintain written AML/CTF policies and comply with financial-crime requirements (Art. 13 and Art. 14), which derive their substantive obligations from the Law on Combating the Financing of Terrorism as the primary statutory instrument establishing CTF offences, STR obligations, and supervisory enforcement powers.
- **This node (Page 18):** "the supervisory authority may impose one or more of the following measures … Impose a monetary fine of up to 5.000.000 riyals per violation … Ban individuals from employment within the sectors for which the supervisory authority has competences."
- **Related node (Page 7 / Art. 13(1)):** "Develop appropriate written organizational policies that address, at least, the internal organization guides, governance … and anti-money laundering and counter-terrorist financing (AML/CTF)."
- **Implication:** A BNPL company's AML/CTF policy document must map its controls to CTF Law obligations; SAMA examiners will test whether the policy covers CTF-specific triggers (terrorist-financing typologies, STR escalation paths, UNSC-resolution screening) and not merely generic AML language.
- **Caveat:** Confidence is INFERRED: the BNPL Rules cite AML/CTF requirements generically without an explicit cross-reference article to SAMA_EN_853; the link is established by regulatory logic and SAMA's supervisory authority under both instruments rather than a verbatim citation.

### [[Anti-Money Laundering Law]] — `references` [EXTRACTED]
- **Why:** The AML Law and the CTF Law constitute parallel primary legislation covering ML and TF respectively, sharing near-identical enforcement architecture (supervisory powers, monetary fines up to SAR 5 million per violation, record-keeping periods of ten years, and mutual legal assistance frameworks) that FIs and DNFBPs must satisfy simultaneously under both regimes.
- **This node (Page 18 / Art 83 (sanctions)):** "Impose a monetary fine of up to 5.000.000 riyals per violation; Ban individuals from employment within the sectors for which the supervisory authority has competences for a period to be determined by the supervisory authority."
- **Related node (Page 5 / Art 13):** "FIs and DNFBPs shall: Monitor and scrutinize transactions, document and data on an ongoing basis to ensure that they are consistent with the reporting entity's knowledge of the customer, the customer's commercial activities and risk profile."
- **Implication:** Compliance programmes and transaction-monitoring systems must be designed to satisfy both AML and CTF obligations concurrently; a single control gap (e.g., inadequate EDD documentation) can attract parallel sanctions under each law, doubling maximum financial exposure.

### [[General Directorate of Financial Intelligence (CTF)]] — `references` [EXTRACTED]
- **Why:** The CTF Law establishes the General Directorate of Financial Intelligence as the mandated national central agency under Chapter 8, defining its powers to receive STRs, demand additional information from FIs, and disseminate analytical results to competent authorities—making the Directorate a primary operational node created and governed by this Law.
- **This node (Page 15 / Article 70):** "FIs, DNFBPs, and NPOs…shall…Promptly and directly, Report such transaction to the General Directorate of Financial Intelligence; and provide a detailed report including all available data and information on such transaction and relevant parties."
- **Related node (Page 16 / Article 76):** "The Directorate – as a national central agency, shall enjoy adequate operational independence, shall undertake receiving suspicious transaction reports or other reports or information relating to financing of terrorism…to analyze such reports and information, and to disseminate…"
- **Implication:** FIs must configure their STR workflow to route terrorism-financing reports directly to the Directorate (not through the supervisory authority), and must be able to evidence prompt, direct transmission with timestamped submission records auditable by SAMA examiners.

### [[Permanent Committee for Combating Terrorism and its Financing]] — `references` [EXTRACTED]
- **Why:** The CTF Law expressly creates and mandates the Permanent Committee for Combating Terrorism and its Financing under Article 75, assigning it the specific function of receiving and implementing UN Security Council Resolutions on terrorism suppression—a TFS/sanctions function that the Law directly governs and activates.
- **This node (Page 16 / Article 75):** "The Permanente Committee for Combating Terrorism and its financing receive requests from countries and organizations for the implementation of UN Security Council Resolutions relating to the prevention and suppression of terrorism and financing of terrorism."
- **Related node (Page 16 / Article 75):** "The Committee shall put in place, and update, mechanisms, and take the necessary measures…to implement the said resolutions…The mechanisms shall be issued pursuant to a decision by the President of State Security."
- **Implication:** FIs must maintain a live feed to UNSC designation lists operationalised through the Permanent Committee's mechanisms; sanctions-screening systems should be capable of consuming updates issued under Presidential decisions and evidencing timely list refresh with audit trails.

### [[Preventive Measures (CTF)]] — `references` [EXTRACTED]
- **Why:** Chapter Six of the CTF Law establishes the Preventive Measures regime (Articles 63–70), imposing binding CDD, record-keeping, EDD, and STR obligations on FIs, DNFBPs, and NPOs—these are the primary prophylactic controls through which the Law operationalises its TF-risk framework at the entity level.
- **This node (Page 1 / Chapter 1 (Definitions)):** "Terrorism Financing Crime: The financing of terrorist act or terrorist entity or a terrorist in any forms as set forth under this Law, including financing the travel and training of a terrorist individual."
- **Related node (Page 14 / Article 63):** "FIs, DNFBPs, and NPOs shall identify, assess, understand and document its financing of terrorism risks, taking into account a wide range of risk factors, including those relating to its customers, countries or geographic areas, products, services, transactions and delivery chann…"
- **Implication:** FIs must maintain a documented TF risk assessment (distinct from ML risk assessment) covering all customer, product, channel, and geographic dimensions, and must be able to produce it to supervisory authorities on request—a gap here would constitute a direct breach of Article 63 and expose the entity to monetary sanctions of up to SAR 5 million per violation.

### [[Terrorism Financing Crime]] — `references` [EXTRACTED]
- **Why:** The Law on Combating the Financing of Terrorism is the primary source document that establishes and defines the concept of 'Terrorism Financing Crime' as a distinct criminal offence; the document node contains the authoritative definition that gives the concept node its legal content and scope.
- **This node (Page 1 / Chapter 1 / Definition 4):** "Terrorism Financing Crime: The financing of terrorist act or terrorist entity or a terrorist in any forms as set forth under this Law, including financing the travel and training of a terrorist individual."
- **Related node (Page 1 / Chapter 1 / Definition 4):** "Terrorism Financing Crime: The financing of terrorist act or terrorist entity or a terrorist in any forms as set forth under this Law, including financing the travel and training of a terrorist individual."
- **Implication:** Transaction monitoring rules and STR workflows must be calibrated to detect not only direct financing of terrorist acts but also financing of travel and training, requiring granular typology coverage beyond simple funds-transfer screening.

#graphify/document #graphify/EXTRACTED #community/AML/CTF_BNPL_Finance_Rules #graphify/enriched
