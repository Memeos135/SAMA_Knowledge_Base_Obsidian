---
source_file: "markdown/SAMA_EN_2340_VER1.md"
type: "document"
community: "Large Exposure Limits"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Large Exposure (LEX) Rules for Banks

## Connections

### [[BCBS Supervisory framework for measuring and controlling large exposures 2014]] — `cites` [EXTRACTED]
- **What this link tells you:** When interpreting gaps or technical calculation methods in the LEX Rules, treat the BCBS 2014 large exposures framework as the authoritative source the Rules are built on and expressly cite. The Rules footnote specific BCBS paragraphs (e.g. paragraphs 84-89 for CCP clearing exposures) and note where SAMA has deliberately narrowed scope — such as focusing only on single-counterparty/connected-counterparty default risk and excluding other concentration risks. Conclude that where the SAMA text is silent or ambiguous on measurement, the cited BCBS provisions inform the intended treatment, but SAMA's explicit carve-outs and modifications (which override the BCBS default) govern in KSA.
- **Grounding — this node (Page 40 (footnote 19)):** "Paragraphs 84-89 of BCBS "Supervisory framework for measuring and controlling large exposures" April 2014"
- **Grounding — related node (Page 29 (Note)):** "SAMA has decided to focus this framework on losses incurred due to default of a single counterparty or a group of connected counterparties and not to take into account any other type of concentration risk."

### [[Banking Control Law]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing the legal enforceability of the LEX Rules, treat them as subordinate SAMA prudential rules issued under the Banking Control Law rather than as free-standing guidance, since SAMA's rule-making authority over banks and its power to impose exposure limits, exemptions and reporting derives from that primary statute. This tells you the LEX limits (e.g. 15% single-counterparty, 25% for non-banking financial subsidiaries) carry the force of the underlying banking supervision regime and apply to all licensed banks. Conclude that compliance is mandatory and that any dispute over SAMA's authority to set or waive these limits should be traced back to the Banking Control Law, not to the Rules alone.
- **Grounding — this node (Page 18 / sec 6):** "While ensuring compliance with the exposure limits under these Rules, the banks shall also meet the following additional requirements"
- **Grounding — related node (Page 5 / sec 1.3):** "Rules: Large Exposure (LEX) Rules for Banks."
- **Caveat:** The provided context does not contain the Banking Control Law text itself; the citation relationship is inferred from the LEX Rules' standing as SAMA banking prudential rules. Verify the specific enabling article in the primary law.

### [[Basel III Risk-Based Capital Framework]] — `cites` [EXTRACTED]
- **What this link tells you:** When computing exposure values and capital base for LEX compliance, you cannot read the Rules in isolation — key defined terms are expressly imported from the Basel risk-based capital framework, so the Basel definitions govern their meaning. Specifically, 'Exposure' covers on/off-balance-sheet and counterparty-credit-risk items 'under the Basel risk-based capital framework,' and 'Eligible Capital Base' is Tier 1 capital 'fulfilling the criteria defined in the Basel III framework.' Conclude that measurement disputes must be resolved by reference to SAMA's adopted Basel III framework (including the referenced SAMA circulars and guidance documents), and do not apply LEX limits using a bespoke internal definition of exposure or capital.
- **Grounding — this node (Page 5 / sec 1.3):** "instruments with counterparty credit risk under the Basel risk-based capital framework. Banking and trading books have the same meaning as under the Basel risk-based capital framework."
- **Grounding — related node (Page 5 / sec 1.3):** "Eligible Capital Base: is the effective amount of Tier 1 capital fulfilling the criteria defined in the Basel III framework."

### [[Covered Bonds]] — `references` [EXTRACTED]
- **What this link tells you:** When assigning an exposure value to covered bond holdings for LEX purposes, do not default to the 100% nominal value — Appendix VIII permits a reduced value of no less than 20% only if strict conditions are met. The Rules define covered bonds and set the eligibility tests (qualifying underlying asset pool, at least 10% over-collateralisation, LTV thresholds for RRE/CRE), and identify the issuing bank as the counterparty to which the value is assigned. Conclude that the preferential 20% treatment is conditional and must be justified against every listed criterion; failing any condition, the full 100% nominal value applies against the LEX limit.
- **Grounding — this node (Page 18 / Section 6):** "the banks shall also meet the following additional requirements... report all exposures net of amounts reduced by eligible CRM techniques."
- **Grounding — related node (Page 33 / Appendix VIII):** "A covered bond satisfying the conditions set out in the next paragraph may be assigned an exposure value of no less than 20% of the nominal value... Other covered bonds must be assigned an exposure value equal to 100%"

### [[Credit Risk Mitigation Techniques]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a bank breaches the LEX limits, you cannot use gross exposure figures — the Rules require exposures to be measured net of eligible CRM. This link is enforceable: Section 6(ii) mandates measuring, monitoring and reporting exposures net of amounts reduced by eligible CRM, while Section 5.2-5.3 defines which CRM techniques qualify (only those recognised under the standardised approach for risk-based capital; equities, convertible bonds and UCITS are excluded). Conclude that any CRM claimed for LEX purposes must first be recognised for risk-based capital purposes and satisfy the LEX framework conditions; do not assume a mitigant that reduces capital charges automatically reduces the LEX exposure value unless it meets these criteria.
- **Grounding — this node (Page 18 / Section 6(ii)):** "banks shall measure, monitor, and report all exposures net of amounts reduced by eligible CRM techniques."
- **Grounding — related node (Page 13 / Section 5.2):** "Eligible credit risk mitigation techniques for large exposures purposes are those that meet the minimum requirements and eligibility criteria... SAMA does not consider equities... as eligible CRM mitigants"

### [[Definition of Exposure Value]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying exposures to test against the LEX limits, use the exposure-value definitions in the Appendices rather than assuming capital-framework measures carry over unchanged — the Rules flag that some LEX measures differ from those used for risk-based capital. The document specifies distinct treatments per instrument type (trading-book positions, options, credit derivatives, CCP clearing exposures with segregated initial margin valued at 0), so the numerator of each limit test depends on these definitions. Conclude that exposure value must be derived per the relevant Appendix for each instrument, and note explicitly where the LEX measure diverges from the capital measure (e.g. options).
- **Grounding — this node (Page 18 / Section 4.1):** "The sum of all exposures values a bank has to a single non-bank counterparty... must not be higher than 15% of the banks available eligible capital base"
- **Grounding — related node (Page 30 / Appendix VII):** "The measures of exposure values of options under this framework differ from the exposure value used for risk-based capital requirements."

### [[G-SIB Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which banks face heightened LEX treatment, note that the Rules reference the G-SIB/D-SIB classification framework, which is set by separate SAMA circulars (e.g. circular no. 107018 dated 10 July 2013 for G-SIB methodology; annual D-SIB lists). A bank's systemic-importance status is determined outside these Rules and can change annually. Conclude that to apply any G-SIB/D-SIB-linked LEX consequence you must check the current SAMA/FSB classification lists and the referenced circulars, since status — and thus applicability — is not fixed within this document.
- **Grounding — this node (Page 25 / Appendix V):** "the Basel Committee on Banking Supervision has developed a methodology for identifying G-SIB's... (issued via SAMA circular no. 107018 dated 10 July 2013)"
- **Grounding — related node (Page 25 / Appendix V):** "The list of G-SIB's is reviewed annually, and banks can move in or out of G-SIB classification or be re-classified at a different level of systemic importance."
- **Caveat:** The LEX Rules reference the G-SIB/D-SIB framework contextually in an appendix; the precise LEX consequence tied to that status is not fully stated in the provided excerpts, so verify the operative limit differences in the primary text.

### [[Maximum Exposure Limits]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's binding concentration ceilings, this link points you to the operative numeric limits: 15% of eligible capital for a single non-bank counterparty, 25% for non-banking financial-sector subsidiaries, with defined exemptions (sovereign/SAMA/GCC, intra-day and qualifying intra-group exposures). Note the residual rule — anything 'not specifically listed above as exempted, must be fully subject to the large exposure limits' — so exemptions are read narrowly. Conclude that you must classify each exposure against these limits and the exemption list, and that SAMA's discretionary ex-post tolerance for interbank breaches is a supervisory concession, not an entitlement.
- **Grounding — this node (Page 18 / sec 6):** "The exposure limits under these Rules shall be calculated based on the eligible capital base as disclosed in the latest published quarterly financial statements"
- **Grounding — related node (Page 10 / sec 4.1):** "The sum of all exposures values a bank has to a single non-bank counterparty ... must not be higher than 15% of the banks available eligible capital base at all"

### [[Qualifying Central Counterparties (QCCPs)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank's exposures to a central counterparty must count toward the 25% large-exposure limit, do not treat all CCP exposures alike — the LEX Rules exempt clearing-related exposures only where the CCP is a Qualifying CCP (QCCP), with QCCP defined per Appendix X by the same test used for risk-based capital. For non-QCCPs, clearing and other exposures must be summed and remain subject to the general 25% limit, and the connected-counterparties concept does not apply to clearing-related CCP exposures. Conclude that QCCP status is the pivotal classification: verify the CCP's licensing and CPSS-IOSCO-consistent supervision before applying any exemption, and note the exemption still carries regulatory reporting obligations.
- **Grounding — this node (Page 17):** "v. Exposures to central counterparties. 5.6. Exposures Exempted from Exposure Limits"
- **Grounding — related node (Page 40 / Appendix X):** "Banks' exposures to qualifying central counterparties (QCCPs ...) related to clearing activities are exempted from the large exposures limits."

### [[Trading Book Exposure Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring a bank's total exposure to a single counterparty for large-exposure purposes, you cannot silo the trading book — Appendix VII requires trading-book exposures to a counterparty to be added to that counterparty's banking-book exposures. This aggregation flows directly from the LEX Rules' core requirement that both on- and off-balance-sheet exposures in either book count toward the single-counterparty and connected-group limits. Conclude that bond and equity positions in the trading book are constrained by the limit (while pure commodity/currency concentrations are not), and check that trading and banking book exposures to the same name are combined before testing the 15%/25% thresholds.
- **Grounding — this node (Page 13):** "banks must consider both on and off-balance sheet exposures included in either the banking or trading books, and instruments with counterparty credit risk"
- **Grounding — related node (Page 29 / Appendix VII):** "A bank must add any exposures to a single counterparty arising in the trading book to any other exposures to that counterparty that lie in the banking book"

#graphify/document #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
