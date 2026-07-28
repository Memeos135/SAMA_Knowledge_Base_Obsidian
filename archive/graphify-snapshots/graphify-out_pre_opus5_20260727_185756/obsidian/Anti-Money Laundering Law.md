---
source_file: "markdown/SAMA_EN_10667_VER1.md"
type: "concept"
community: "Targeted Financial Sanctions"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Targeted_Financial_Sanctions
  - graphify/enriched
---

# Anti-Money Laundering Law

## Connections

### [[AMLCTF Compliance Requirements|AML/CTF Compliance Requirements]] — `references` [INFERRED]
- **Why:** Article 13 and Article 14 of the BNPL Rules require the BNPL company to develop AML/CTF internal policies and comply with SAMA's financial crimes instructions, which are grounded in and must be consistent with the substantive obligations (risk assessment, transaction monitoring, record-keeping, internal controls) established by the Anti-Money Laundering Law applied to Financial Institutions.
- **This node (Page 5 / Article 14(1)(A)):** "Have in place and effectively implement internal policies, procedures and controls against money laundering aimed at managing and mitigating any risks identified … proportionate to the nature and size of the FI."
- **Related node (Page 7 / Article 13(1)):** "Develop appropriate written organizational policies that address, at least, the internal organization guides, governance … and anti-money laundering and counter-terrorist financing (AML/CTF)."
- **Implication:** The BNPL company's AML/CTF policy framework must satisfy both the BNPL Rules' internal-policy obligation and the AML Law's risk-proportionate controls standard, meaning an examiner will cross-reference both instruments; gaps between the two (e.g., absence of a documented ML risk assessment per AML Law Art. 5) constitute dual regulatory findings.
- **Caveat:** Confidence is INFERRED for the direct cross-citation: the BNPL Rules reference 'requirements and instructions issued by SAMA on financial crimes' rather than citing the AML Law by name; the linkage is operationally clear but the primary text does not explicitly name the AML Law as the source instrument.

### [[Anti-Money Laundering Law (referenced)]] — `references` [INFERRED]
- **Why:** The Fraud Guide expressly cites the Anti-Money Laundering Law (Royal Decree م/١٠) as a foundational legal basis, and explicitly states that financial fraud is a predicate offence to money laundering with overlapping countermeasures — making the AML Law a direct legislative source for the Fraud Guide's obligations on banks.
- **This node (Page 3, Art 4(1)):** "A money laundering offence shall be deemed a separate offence from the predicate offense, and a conviction for the predicate offense shall not be necessary for a conviction for money laundering"
- **Related node (Page 4, Preamble):** "نظام مكافحة غسل الأموال الصادر بالمرسوم الملكي رقم (م/١٠) … جريمة الاحتيال المالي أحد الجرائم الأصلية لجريمة غسل الأموال … هناك تداخل في التدابير المتخذة لمكافحة الاحتيال من جهة وتدابير مكافحة غسل الأموال من جهة أخرى"
- **Implication:** Banks must configure their fraud-monitoring systems to generate Suspicious Transaction Reports (STRs) independently of any predicate-offence prosecution, and ensure that fraud case records satisfy the AML Law's ten-year retention and transaction-reconstruction requirements under Article 12.
- **Caveat:** The Fraud Guide references the AML Law by royal decree number but does not quote specific AML articles; the link between the two nodes is confirmed by explicit citation in the preamble and conceptual overlap, but exact article cross-mapping requires reading both instruments together rather than from a single in-text cross-reference.

### [[Confiscation]] — `references` [EXTRACTED]
- **Why:** The AML Law establishes the predicate-offence and proceeds-of-crime framework (Art. 2–4) that defines what constitutes 'laundered funds' and 'proceeds of crime,' which are precisely the categories subject to mandatory confiscation under Arts. 33–35; the confiscation provisions are therefore the enforcement consequence of the offence definitions earlier in the same statute.
- **This node (Page 3 / Art. 2):** "Conceals or disguises the true nature, source, movement, ownership, place, disposition, or manner of disposition, or rights with respect to funds that the person knows are proceeds of crime."
- **Related node (Page 11 / Art. 33):** "in the event of a conviction for a money laundering or predicate offence, the competent Court shall issue an order to confiscate the following: a. Laundered funds; b. Proceeds of the crime, including proceeds intermingled with funds acquired from legitimate sources up to the val…"
- **Implication:** FIs must design transaction-monitoring and record-keeping systems capable of reconstructing the full fund-flow trail (source, movement, disposition) so that, in the event of a confiscation order, records are sufficient for the competent court to identify and value laundered funds, intermingled proceeds, and instrumentalities as required by Art. 33.

### [[Due Diligence Measures]] — `references` [EXTRACTED]
- **Why:** The AML Law directly mandates due diligence as a preventive measure obligation on FIs and DNFBPs, calibrating its intensity to customer risk profile; Articles 7–13 collectively establish due diligence as the primary operational control mechanism through which the Law's risk-based approach is operationalised.
- **This node (Page 5 / Article 13):** "Monitor and scrutinize transactions, document and data on an ongoing basis to ensure that they are consistent with the reporting entity's knowledge of the customer, the customer's commercial activities and risk profile, and where necessary the customer's source of funds."
- **Related node (Page 4 / Article 7):** "Determine the extent of due diligence measures based on the risks relation to a customer or business relationship. Where a higher risk of money laundering was identified, they shall apply enhanced due diligence measures."
- **Implication:** RegTech systems must implement a risk-tiered CDD/EDD workflow that dynamically links customer risk scoring to monitoring rule intensity, with a documented audit trail demonstrating that enhanced scrutiny was triggered and applied when elevated ML/TF risk was identified.

### [[General Directorate of Financial Intelligence]] — `references` [EXTRACTED]
- **Why:** The AML Law constitutes and defines the General Directorate of Financial Intelligence as the national central agency for receiving, analysing, and disseminating suspicious transaction reports; the Law's reporting obligations on FIs/DNFBPs (Articles 15–16) are structurally directed at and operationally processed by the Directorate, making it the institutional counterpart to every STR obligation in the Law.
- **This node (Page 6 / Article 16):** "FIs, DNFBPs, and NPOs as well as their Members of Board of Directors, directors… are prohibited from disclosing to a customer or any other person the fact that a report under this Law or related information will be, is being or has been submitted to the Directorate."
- **Related node (Page 6–7 / Article 17):** "The General Directorate of Financial intelligence shall… act as a national central agency to receive suspicious transaction reports… to analyze such reports and information, and to disseminate the results of its analysis to competent authorities, either spontaneously or upon req…"
- **Implication:** Compliance systems must maintain a secure, tipping-off-proof STR submission channel to the Directorate, with access controls ensuring that STR filing status is segregated from customer-facing staff and that response workflows for Directorate information requests (Article 15(2)) are documented and time-stamped.

### [[Law on Combating the Financing of Terrorism]] — `references` [EXTRACTED]
- **Why:** The AML Law and the CTF Law constitute parallel primary legislation covering ML and TF respectively, sharing near-identical enforcement architecture (supervisory powers, monetary fines up to SAR 5 million per violation, record-keeping periods of ten years, and mutual legal assistance frameworks) that FIs and DNFBPs must satisfy simultaneously under both regimes.
- **This node (Page 5 / Art 13):** "FIs and DNFBPs shall: Monitor and scrutinize transactions, document and data on an ongoing basis to ensure that they are consistent with the reporting entity's knowledge of the customer, the customer's commercial activities and risk profile."
- **Related node (Page 18 / Art 83 (sanctions)):** "Impose a monetary fine of up to 5.000.000 riyals per violation; Ban individuals from employment within the sectors for which the supervisory authority has competences for a period to be determined by the supervisory authority."
- **Implication:** Compliance programmes and transaction-monitoring systems must be designed to satisfy both AML and CTF obligations concurrently; a single control gap (e.g., inadequate EDD documentation) can attract parallel sanctions under each law, doubling maximum financial exposure.

### [[Predicate Offense]] — `references` [EXTRACTED]
- **Why:** The AML Law defines 'Predicate Offense' as an autonomous jurisdictional concept (Article 1(4)) and then explicitly decouples money laundering prosecution from any prior predicate offense conviction (Article 4(1)), which directly shapes how FIs must characterise suspicious activity without requiring confirmed criminal predicate evidence before filing an STR.
- **This node (Page 3 / Article 4):** "A money laundering offence shall be deemed a separate offence from the predicate offense, and a conviction for the predicate offense shall not be necessary for a conviction for money laundering or to establish that funds are proceeds of crime."
- **Related node (Page 1 / Article 1(4)):** "Predicate Offense: Any committed act within the KSA constituting an offense punishable by Sharia or statutory law, or any act committed outside the Kingdom if it constitutes a crime according to the laws of the State where it was committed and would have constituted an offense u…"
- **Implication:** Transaction monitoring alert-to-STR escalation procedures must not require internal confirmation of a specific predicate offense before reporting; the suspicion threshold is met by circumstantial indicators alone, and alert disposition documentation should reflect this autonomy to avoid creating a barrier to timely STR submission.

### [[Supervisory Authority]] — `references` [EXTRACTED]
- **Why:** The AML Law formally defines 'Supervisory Authority' and then operationalises that definition in Article 24 by conferring specific powers and duties on that authority to monitor FI/DNFBP/NPO compliance, creating the primary legal basis for SAMA's supervisory mandate over regulated entities.
- **This node (Page 9 / Art 25 (sanctions article)):** "The supervisory authority should inform the General Director of Financial Intelligence about the actions taken or imposed sanction."
- **Related node (Page 2 / Definition 12):** "Supervisory Authority: The authority with responsibility to monitor the compliance by FIs, DNFPBs, and NPOs with the requirements under this Law, its Regulation or any relevant decision or instructions."
- **Implication:** A RegTech system must maintain an audit trail of all supervisory actions (warnings, fines, licence restrictions) taken against the entity, with automated notification logic to the General Director of Financial Intelligence, evidencing timely reporting as required post-sanction.

#graphify/concept #graphify/EXTRACTED #community/Targeted_Financial_Sanctions #graphify/enriched
