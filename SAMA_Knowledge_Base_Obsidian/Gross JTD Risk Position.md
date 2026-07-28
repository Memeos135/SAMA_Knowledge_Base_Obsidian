---
source_file: "markdown/SAMA_EN_3553_VER1.md"
type: "concept"
community: "Default Risk Internal Model"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Default_Risk_Internal_Model
  - graphify/enriched
---

# Gross JTD Risk Position

## Connections

### [[Jump-to-Default (JTD) Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the DRC requirement, treat 'gross JTD risk position' as the first computational step that operationalises the broader JTD (jump-to-default) risk concept. In the same SAMA framework, [8.1] defines DRC as capturing JTD risk, and [8.3] prescribes that the gross JTD of each exposure is computed first, before offsetting into net JTD and bucketing. Conclude that gross JTD is a defined input within the JTD-risk regime, so the general JTD definition ([Page 6]) governs its meaning while [8.9]+ governs its measurement — apply both when determining the capital charge.
- **Grounding — this node (Page 73 / 8.3(1)):** "The gross JTD risk of each exposure is computed separately."
- **Grounding — related node (Page 73 / 8.1):** "The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks"

### [[Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the default risk capital (DRC) requirement under the standardised approach, note that Gross JTD is not a free-standing figure — it is defined as a function of LGD, notional and realised P&L, so the prescribed LGD values directly drive the JTD amount. Section 8.11–8.12 fixes LGD at 100% for equity and non-senior debt and 75% for senior debt, meaning the instrument's seniority determines the loss assumption feeding each gross JTD calculation. Conclude that any gross JTD figure must apply the mandated LGD for that instrument type before offsetting against same-obligor positions; you cannot substitute internal LGD estimates in the standardised DRC computation (internal LGD is a separate internal-models path under 13.38).
- **Grounding — this node (Page 75 / 8.11):** "The gross JTD is a function of the loss given default (LGD), notional amount (or face value) and the cumulative profit and loss (P&L) already realised"
- **Grounding — related node (Page 75 / 8.12):** "For calculating the gross JTD, LGD is set as follows: Equity instruments and non-senior debt instruments... 100%... Senior debt instruments... 75%"

### [[Net JTD Risk Position]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's default risk capital (DRC) under the standardised approach, gross JTD and net JTD are sequential steps in the same mandated computation, not interchangeable inputs. Per [8.3], gross JTD is computed exposure-by-exposure first, then long and short JTD amounts against the same obligor are offset (where permissible) to produce net JTD, which is then allocated to buckets. A compliance reviewer should confirm that offsetting was only applied to the same obligor and only where permitted, since improperly netting distinct-obligor exposures would understate the net JTD and hence the DRC requirement.
- **Grounding — this node (Page 73 / 8.3(1)):** "The gross JTD risk of each exposure is computed separately."
- **Grounding — related node (Page 73 / 8.3(2)-(3)):** "the JTD amounts of long and short exposures are offset (where permissible) to produce net long and/or net short exposure amounts per distinct obligor... Net JTD risk positions are then allocated to buckets."

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Internal_Model #graphify/enriched
