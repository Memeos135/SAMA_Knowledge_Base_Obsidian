---
source_file: "markdown/SAMA_EN_11055_VER1.md"
type: "concept"
community: "Collateral & LGD"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Collateral__LGD
  - graphify/enriched
---

# Loss Given Default (LGD)

## Connections

### [[DRC Requirement Internal Model]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank uses an internal model (IMA) for default risk capital, LGD is not a free parameter — [13.38] requires use of the bank's SAMA-approved IRB LGD estimates where they exist. This links the DRC internal model to the LGD input via the same default-risk modelling regime ([13.18]–[13.20]), which itself is contingent on desk-level SAMA approval for credit spread and default risk. A reviewer should confirm the model draws on approved IRB LGD estimates (and IRB-consistent PDs), since desks without SAMA approval fall out of the IMA and revert to the standardised DRC framework where LGD is fixed by rule (e.g. 100% / 75%).
- **Grounding — this node (Page 75 / 8.12):** "For calculating the gross JTD, LGD is set as follows: Equity instruments and non-senior debt instruments are assigned an LGD of 100%... Senior debt instruments are assigned an LGD of 75%."
- **Grounding — related node (Page 131 / 13.38; Page 127 / 13.18):** "Banks must have a separate internal model to measure the default risk of trading book positions... Where a bank has approved loss-given-default (LGD) estimates as part of th[e IRB approach]"
- **Caveat:** Node B's LGD context is the standardised (fixed-percentage) treatment, while the DRC internal-model LGD linkage sits at [13.38] where the IRB LGD sentence is truncated in the provided text; verify the full IMA LGD conditions in the primary source.

### [[Gross JTD Risk Position]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the default risk capital (DRC) requirement under the standardised approach, note that Gross JTD is not a free-standing figure — it is defined as a function of LGD, notional and realised P&L, so the prescribed LGD values directly drive the JTD amount. Section 8.11–8.12 fixes LGD at 100% for equity and non-senior debt and 75% for senior debt, meaning the instrument's seniority determines the loss assumption feeding each gross JTD calculation. Conclude that any gross JTD figure must apply the mandated LGD for that instrument type before offsetting against same-obligor positions; you cannot substitute internal LGD estimates in the standardised DRC computation (internal LGD is a separate internal-models path under 13.38).
- **Grounding — this node (Page 75 / 8.12):** "For calculating the gross JTD, LGD is set as follows: Equity instruments and non-senior debt instruments... 100%... Senior debt instruments... 75%"
- **Grounding — related node (Page 75 / 8.11):** "The gross JTD is a function of the loss given default (LGD), notional amount (or face value) and the cumulative profit and loss (P&L) already realised"

#graphify/concept #graphify/EXTRACTED #community/Collateral__LGD #graphify/enriched
