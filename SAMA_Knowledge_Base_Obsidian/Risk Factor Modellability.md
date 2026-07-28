---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Risk Factor Modellability"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Risk_Factor_Modellability
  - graphify/enriched
---

# Risk Factor Modellability

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **What this link tells you:** When adjudicating whether a backtesting exception can be legitimately disregarded, check the modellability status of the risk factor driving it: the standard permits an exception to be set aside only where it is driven by a non-modellable risk factor (NMRF) that receives an SES capital requirement exceeding the day's loss, and only with SAMA notification and supporting documentation. Risk factor modellability (RFET and the [11.25]–[11.26] principles) is what determines whether a factor is an NMRF in the first place, so the two concepts are directly linked in the exception-treatment test. Conclude that a bank cannot claim the disregard relief without first establishing, to SAMA's satisfaction, that the factor is genuinely non-modellable and separately capitalised at the required desk level.
- **Grounding — this node (Page 105 / 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 110 / 12.6):** "If the backtesting exception at a desk-level test is being driven by a non-modellable risk factor that receives an SES capital requirement... it is permitted to be disregarded"

### [[Internal Models Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can use the internal models approach (IMA) for a given position, treat risk factor modellability as a gating precondition rather than a technical detail — under the same instrument (SAMA_EN_3553), a risk factor that fails the modellability principles must be excluded from the ES model and capitalised as a non-modellable risk factor (NMRF). SAMA may deem data unsuitable for a particular risk factor and force NMRF treatment, and modellability is judged against defined principles, not merely the count of real-price observations. Conclude that IMA capital recognition cannot be assumed for the full portfolio; you must check which risk factors pass the RFET/modellability principles and confirm that non-modellable ones carry the separate NMRF charge.
- **Grounding — this node (Page 105 / 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"
- **Grounding — related node (Page 92 / 10.8):** "a distinct unit ... must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements"

#graphify/document #graphify/EXTRACTED #community/Risk_Factor_Modellability #graphify/enriched
