---
source_file: "markdown/SAMA_EN_3689_VER1.md"
type: "concept"
community: "Aggregation Business Continuity"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Aggregation_Business_Continuity
  - graphify/enriched
---

# Aggregation Entity

## Connections

### [[Aggregation Platform]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping where the entity's data-security, confidentiality, and disclosure duties bite, note the Platform is the defined electronic channel through which the regulated activity and all consumer data flow. Article 1.2.7 defines Platform as 'any electronic means used to carry out the activity, including websites and applications,' and the entity must maintain/operate it (Art 3), safeguard confidentiality, security, integrity and availability of platform data (5.1–5.2), retain records for 10 years (5.3), and post terms and cybersecurity instructions on it (7.1, 8.1, 8.4). Conclude that platform-level failures — data disclosure without SAMA approval, missing pop-up acknowledgments, inadequate complaint feature — are directly attributable to the entity as breaches of these Instructions.
- **Grounding — this node (Page 5 / Art 5.2):** "Ensure the security, integrity and availability of the information provided through the platform, including... the consumer’s personal information from loss and unauthorized access."
- **Grounding — related node (Page 3 / Art 1.2.7):** "Platform: Any electronic means used to carry out the activity, including websites and applications."

### [[Consumer]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping consumer-protection duties, treat the Consumer as the protected beneficiary of the Entity's obligations rather than a party with symmetrical duties. Article 1.2.5 defines Consumer as 'a person to whom services are offered by the entity,' and Section II obligations (e.g. 8.5–8.7, 8.13, 8.14) require the entity to inform, educate, and deal fairly with that consumer, plus retain consumer files for at least 10 years and sign a contract clarifying rights and obligations. Conclude that consumer-facing failures — misleading information, non-disclosure of rejection reasons, inadequate contract terms — are enforceable breaches by the entity; note this 'Consumer' definition is finance-support specific and should not be conflated with the AML 'Customer' concept.
- **Grounding — this node (Page 6 / Art 8.6):** "The entity shall consider the needs and desires of consumers and provide them with information in a clear, transparent and not misleading manner."
- **Grounding — related node (Page 3 / Art 1.2.5):** "Consumer: A person to whom services are offered by the entity."

### [[Financier]] — `references` [EXTRACTED]
- **What this link tells you:** When defining the aggregation entity's permissible dealings with lenders, recognise that the Entity–Financier relationship is tightly scoped and contractually mandated, not open commercial discretion. Article 1.2.4 defines Financier as banks, finance companies, and licensed finance entities, and the Instructions restrict the electronic linkage to aggregation purposes only (8.2), bar receiving/delivering funds on the financier's behalf without SAMA approval (8.8), prohibit favouring or marketing any financier (8.10), and require a written contract stating the financier's licensing number and service levels (Art 10). Conclude that the entity must remain a neutral conduit; check that any financier it lists is itself licensed and that the inter-party contract meets the Article 10 minimum content before relying on the arrangement.
- **Grounding — this node (Page 6 / Art 8.2):** "The entity shall ensure that the electronic linkage between the entity and the financier serves the provision of aggregation activity only and is not used for any other purposes, unless approved by SAMA."
- **Grounding — related node (Page 3 / Art 1.2.4):** "Financier: Banks, finance companies, and entities licensed to engage in finance activities under the laws applicable in Saudi Arabia."

### [[Instructions for Practicing Aggregation Activity]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying who bears the compliance burden under these Instructions, note that the 'Entity' is the defined, licensed actor on whom nearly every operative obligation falls. Article 1.2.6 defines Entity as 'an entity licensed by SAMA to practice aggregation activity,' and Article 2.2 confirms the Instructions apply to such licensed entities, so the duties in Sections II–III (accuracy verification, retention, cybersecurity, disclosure, contracting) all attach to this single defined role. Conclude that any obligation phrased 'the entity shall' is enforceable against the license holder, and that carrying out the activity without the SAMA license (Art 2.3) is itself prohibited.
- **Grounding — this node (Page 3 / Art 1.2.6):** "Entity: An entity licensed by SAMA to practice aggregation activity."
- **Grounding — related node (Page 3 / Art 2.2):** "These Instructions shall apply to entities licensed by SAMA to engage in the activity."

### [[Saudi Central Bank (SAMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining who is legally bound by the Aggregation Activity Instructions and to whom they answer, read the 'Entity' as the sole licensed obligor and SAMA as the issuing/supervising authority whose approval gates key acts. The Instructions define 'Entity' as a body licensed by SAMA and 'SAMA' as the Saudi Central Bank issuing under the Finance Companies Control Law (Royal Decree M/51); numerous obligations (breach notification, funds handling, data disclosure) are triggered only 'unless SAMA's approval is obtained' or require immediate notification to SAMA. You should conclude that the entity cannot self-authorise the carve-out activities and must treat SAMA approval/notification as a precondition, not a formality.
- **Grounding — this node (Page 6 / clause 8.1, 8.8):** "In case of a breach, the entity shall immediately notify SAMA... The entity shall not receive or deliver funds on behalf of the financier unless SAMA's approval is obtained."
- **Grounding — related node (Page 3 / clause 1.2.6, 1.2.1):** "SAMA: The Saudi Central Bank... Entity: An entity licensed by SAMA to practice aggregation activity."

#graphify/concept #graphify/EXTRACTED #community/Aggregation_Business_Continuity #graphify/enriched
