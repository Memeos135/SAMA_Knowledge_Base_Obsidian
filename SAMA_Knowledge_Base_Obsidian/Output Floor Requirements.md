---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Counterparty Credit Risk Approaches"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Counterparty_Credit_Risk_Approaches
  - graphify/enriched
---

# Output Floor Requirements

## Connections

### [[Basel III Framework]] — `cites` [EXTRACTED]
- **What this link tells you:** When identifying the legal basis and scope of the output-floor rules, treat them as SAMA's domestic adoption of the Basel III December 2017 post-crisis reforms rather than a free-standing SAMA invention — this anchors interpretation to the Basel output-floor concept (limiting internal-model RWA to a percentage of standardised RWA). The output floor is issued by SAMA under the Central Bank Law (Royal Decree M/36) and Banking Control Law, applies to all domestic banks on consolidated and standalone bases, and excludes foreign bank branches. Conclude that the Basel III text informs technical meaning while SAMA's issuance sets the binding scope, timeline (effective 1 January 2023) and the specific approaches prohibited from the floor base (IRB, SEC-IRBA, IMA, VaR, IMM).
- **Grounding — this node (Page 729, s.1.1):** "The Basel Committee on Banking Supervision issued the Basel III: Finalizing post-crisis reforms in December 2017, which includes among others, the requirements for output floor."
- **Grounding — related node (Page 3 / Glossary p.737):** "issued by SAMA as part of its adoption of Basel III post-crisis final reforms."

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's use of the IRB approach delivers actual capital relief, the Output Floor Requirements are decisive: they cap modelled RWA at a percentage of standardised-approach RWA, and paragraph 5.8 expressly bars the IRB credit-risk approach from being used, directly or by cross-reference, in the floor base calculation. A compliance reviewer should conclude that IRB outputs cannot be relied on in isolation — the floored figure (effective 1 January 2023, subject to phase-in) governs the minimum. Check the floor calibration and reporting obligation alongside any IRB RWA number.
- **Grounding — this node (Page 734 / Art 5.8):** "the following approaches are not permitted to be used, directly or by cross reference ... IRB approach to credit risk"
- **Grounding — related node (Page 755):** "RWA for modelled approaches that banks have SAMA approval to use ... subject to the credit risk IRB approaches"

### [[Pillar 3 Disclosure Requirements Framework]] — `references` [INFERRED]
- **What this link tells you:** If you are determining what a bank must publicly disclose about its floored capital position, note that the output floor and the Pillar 3 framework appear to interlock: Pillar 3 requires disclosure of RWAs 'as calculated by the bank's internal models and according to the standardised approaches', which is exactly the modelled-versus-standardised comparison the output floor drives. Both documents are issued under the same SAMA authority (Central Bank Law M/36 and Banking Control Law) and derive from the December 2017 Basel III finalisation. Because this link is inferred from thematic overlap rather than an explicit cross-citation, verify in the primary Pillar 3 templates (e.g. the modelled-vs-standardised RWA template) whether output-floor outputs are a mandated disclosure line before relying on it.
- **Grounding — this node (Page 729 / para 1.1):** "the requirements for output floor, which aims to reduce excessive variability of Risk-Weighted Assets “RWA” and to enhance the comparability of risk-weighted capital ratios"
- **Grounding — related node (Page 738 / Introduction (b)):** "Risk-weighted assets (RWAs) as calculated by the bank's internal models and according to the standardised approaches"
- **Caveat:** Link is INFERRED from shared Basel origin and thematic overlap; no explicit cross-reference between the two frameworks is quoted, so confirm in primary text.

### [[Risk-Weighted Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a domestic bank's capital adequacy, treat the output floor not as a standalone rule but as a constraint applied on top of the RWA calculation, because the floor is expressly defined as a limit on RWAs derived from internal models relative to standardised-approach outputs. The Output Floor Requirements reference RWA as the object being floored, and prohibit certain modelled approaches (IRB, SEC-IRBA, IMA, VaR, IMM) from the floor base. You should conclude that any RWA figure reported to SAMA must be reconciled against the floored calculation, and that internal-model RWAs cannot fall below the calibrated percentage of standardised RWAs.
- **Grounding — this node (Page 729 / para 1.1):** "banks using internal models to derive RWAs will be subject to a floor requirement that is applied to RWAs"
- **Grounding — related node (Page 490 / 14.1):** "The risk-weighted assets for market risk under the simplified standardised approach are determined by multiplying the capital requirements ... by 12.5"

### [[Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital adequacy for banks using internal models, the Output Floor Requirements bind directly to the Standardized Approach because the floor is calibrated as a percentage of RWA computed under standardized approaches — the standardized approach for credit risk is expressly the base for the floor. The link is decision-critical: paragraph 5.8 prohibits using the IRB approach and other modelled methods 'directly or by cross reference' in the floor base, so a bank cannot avoid the standardized calculation. You would conclude that any internal-model bank must maintain a parallel standardized computation, and that capital cannot fall below the floored figure.
- **Grounding — this node (Page 733):** "The standardized approaches to be used to calculate the base of the output floor ... (1) The standardized approach for credit risk"
- **Grounding — related node (Page 755):** "Definition of standardised approach: The standardised approach for credit risk"

### [[Template CMS1 - Modelled vs Standardised RWA at Risk Level]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying how a bank must evidence its output-floor position, treat Template CMS1 as the disclosure vehicle that operationalises the floor's core comparison, because CMS1 sets out RWA under modelled approaches (cell a) against RWA under standardised approaches (cell b) at risk level — the same modelled-vs-standardised split that defines the output floor. The floor's prohibition on modelled approaches (IRB, SEC-IRBA, IMA, VaR, IMM) in the floor base is exactly what CMS1 makes transparent. You should conclude that the floored RWA logic and the CMS1 template must be read together to determine both the calculation and the reporting of the floor.
- **Grounding — this node (Page 734 / 5.8):** "the following approaches are not permitted to be used ... in the calculation of the base of the output floor: (1) IRB approach to credit risk; (2) SEC-IRBA; (3) IMA for market risk"
- **Grounding — related node (Page 755):** "RWA for modelled approaches that banks have SAMA approval to use (cell 1/a) ... RWA for portfolios where standardised approaches are used (cell 1/b)"

#graphify/document #graphify/EXTRACTED #community/Counterparty_Credit_Risk_Approaches #graphify/enriched
