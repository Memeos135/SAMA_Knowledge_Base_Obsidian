---
source_file: "markdown/SAMA_EN_2340_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Definition of Exposure Value

## Connections

### [[Large Exposure (LEX) Rules for Banks]] — `references` [EXTRACTED]
- **What this link tells you:** When quantifying exposures to test against the LEX limits, use the exposure-value definitions in the Appendices rather than assuming capital-framework measures carry over unchanged — the Rules flag that some LEX measures differ from those used for risk-based capital. The document specifies distinct treatments per instrument type (trading-book positions, options, credit derivatives, CCP clearing exposures with segregated initial margin valued at 0), so the numerator of each limit test depends on these definitions. Conclude that exposure value must be derived per the relevant Appendix for each instrument, and note explicitly where the LEX measure diverges from the capital measure (e.g. options).
- **Grounding — this node (Page 30 / Appendix VII):** "The measures of exposure values of options under this framework differ from the exposure value used for risk-based capital requirements."
- **Grounding — related node (Page 18 / Section 4.1):** "The sum of all exposures values a bank has to a single non-bank counterparty... must not be higher than 15% of the banks available eligible capital base"

### [[Standardised Approach for Counterparty Credit Risk (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the exposure value of OTC derivatives and other counterparty-credit-risk instruments for the large-exposure limits, do not derive your own measure — Appendix VI mandates the exposure-at-default computed under the Standardised Approach for Counterparty Credit Risk (SA-CCR), as adopted by SAMA via Circulars 351000095021 (21 May 2014) and 371000101120 (20 June 2016). This links the LEX exposure-value definition to the risk-based capital methodology, ensuring one measurement basis across regimes. Conclude that SA-CCR is the required input for derivative exposure values here; verify you are applying the SAMA-implemented version and note that options exposure values under LEX differ from the capital measure.
- **Grounding — this node (Page 27 / Appendix VI):** "The exposure value ... must be the exposure at default according to the standardised approach for counterparty credit risk (SA-CCR ...)"
- **Grounding — related node (Page 27 / Appendix VI):** "SA-CCR — (See SAMA Circular No 351000095021, 21 May 2014 and circular no. 371000101120 dated 20 June 2016 ...)"

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
