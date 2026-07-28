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

# Net JTD Risk Position

## Connections

### [[Gross JTD Risk Position]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's default risk capital (DRC) under the standardised approach, gross JTD and net JTD are sequential steps in the same mandated computation, not interchangeable inputs. Per [8.3], gross JTD is computed exposure-by-exposure first, then long and short JTD amounts against the same obligor are offset (where permissible) to produce net JTD, which is then allocated to buckets. A compliance reviewer should confirm that offsetting was only applied to the same obligor and only where permitted, since improperly netting distinct-obligor exposures would understate the net JTD and hence the DRC requirement.
- **Grounding — this node (Page 73 / 8.3(2)-(3)):** "the JTD amounts of long and short exposures are offset (where permissible) to produce net long and/or net short exposure amounts per distinct obligor... Net JTD risk positions are then allocated to buckets."
- **Grounding — related node (Page 73 / 8.3(1)):** "The gross JTD risk of each exposure is computed separately."

#graphify/concept #graphify/EXTRACTED #community/Default_Risk_Internal_Model #graphify/enriched
