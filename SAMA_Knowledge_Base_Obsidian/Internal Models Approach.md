---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "document"
community: "P&L Attribution Testing"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/PL_Attribution_Testing
  - graphify/enriched
---

# Internal Models Approach

## Connections

### [[Backtesting]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can keep using its internal model for market risk capital, treat backtesting not as a stand-alone diagnostic but as a gating condition on IMA eligibility. Under this SAMA market risk standard the IMA requires an independent risk control unit to conduct regular backtesting of both desk-level and bank-wide models, and backtesting outcomes drive SAMA's response — a higher multiplication factor, a backtesting add-on, or outright disallowance of the model. The practical conclusion: a compliance reviewer evaluating continued IMA approval should read backtesting results as directly determinative of the model's regulatory standing, not as a separate exercise.
- **Grounding — this node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level... backtesting of its bank-wide internal models"
- **Grounding — related node (Page 111 / 12.14–12.15):** "SAMA may consider whether to disallow the bank's use of the model for market risk capital requirement purposes altogether... will automatically increase the multiplication factor"

### [[P&L Attribution (PLA) Test]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When scoping the ongoing conditions for a bank to retain IMA capital treatment, treat the PLA test as an embedded IMA requirement rather than an independent measure: the IMA mandates that the independent risk control unit conduct regular PLA assessments at the trading desk level, and the standard requires the PLA test programme to begin when the internal models capital requirement becomes effective and to be reported for SAMA model approval. PLA results, alongside backtesting and the RFET, feed quarterly into which desks remain eligible for the IMA. Conclude that a compliance reviewer evaluating continued IMA approval should confirm PLA testing is running per the standard, since desk-level PLA failure affects whether that desk stays within the internal-models regime.
- **Grounding — this node (Page 92 / 10.7):** "The bank's risk control unit must conduct regular backtesting and PLA assessments at the trading desk level."
- **Grounding — related node (Page 109 / 12.3):** "The implementation of the backtesting programme and the PLA test must begin on the date that the internal models capital requirement becomes effective."

### [[Risk Factor Modellability]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can use the internal models approach (IMA) for a given position, treat risk factor modellability as a gating precondition rather than a technical detail — under the same instrument (SAMA_EN_3553), a risk factor that fails the modellability principles must be excluded from the ES model and capitalised as a non-modellable risk factor (NMRF). SAMA may deem data unsuitable for a particular risk factor and force NMRF treatment, and modellability is judged against defined principles, not merely the count of real-price observations. Conclude that IMA capital recognition cannot be assumed for the full portfolio; you must check which risk factors pass the RFET/modellability principles and confirm that non-modellable ones carry the separate NMRF charge.
- **Grounding — this node (Page 92 / 10.8):** "a distinct unit ... must conduct the initial and ongoing validation of all internal models used to determine market risk capital requirements"
- **Grounding — related node (Page 105 / 11.23):** "the risk factor must be excluded from the ES model and subject to capital requirements as an NMRF"

#graphify/document #graphify/EXTRACTED #community/PL_Attribution_Testing #graphify/enriched
