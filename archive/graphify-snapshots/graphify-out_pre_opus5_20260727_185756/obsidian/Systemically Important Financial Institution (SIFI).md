---
source_file: "markdown/document3.md"
type: "concept"
community: "SIFI Resolution & Recovery"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SIFI_Resolution__Recovery
  - graphify/enriched
---

# Systemically Important Financial Institution (SIFI)

## Connections

### [[Competent Authority]] — `references` [EXTRACTED]
- **Why:** The Competent Authority is the exclusive body empowered to designate, plan for, and execute resolution procedures against a SIFI; every substantive obligation in the Law runs between the Competent Authority and the SIFI, making the two nodes the primary regulatory dyad of the Law.
- **This node (Page 1 / Art 1):** "Systemically Important Financial Institution (SIFI): A financial institution designated by the competent authority as SIFI in accordance with Article 2 of this Law."
- **Related node (Page 6 / Art 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Implication:** A SAMA-supervised institution's internal resolution-readiness system must track its SIFI designation status, the 90-day plan approval clock, and all Competent Authority instructions as auditable workflow events with timestamps and version control.

### [[Financial Group]] — `references` [EXTRACTED]
- **Why:** Where a SIFI is a holding company, the Law extends resolution and recovery planning obligations to the entire Financial Group, meaning the SIFI concept and the Financial Group concept are structurally linked through the holding-company trigger in Articles 6 and 8.
- **This node (Page 4 / Art 4):** "This Law shall apply to financial institutions, holding companies, subsidiaries, foreign branches, and financial groups."
- **Related node (Page 2 / Art 1):** "Financial Group: A holding company and its subsidiaries, of which any is a financial institution."
- **Implication:** A RegTech entity-mapping system must model the full legal-entity hierarchy of any SIFI holding company so that separate recovery and resolution plans can be generated, tracked, and submitted for each subsidiary financial institution within the group, not only at the consolidated level.

### [[Recovery Plan]] — `references` [EXTRACTED]
- **Why:** The Recovery Plan obligation under Article 6 applies to all financial institutions upon competent authority request, but the Resolution Plan under Article 8 is explicitly scoped to SIFIs; the competent authority must calibrate recovery plan requests by reference to SIFI-relevant criteria (size, interconnectedness, complexity), making SIFI designation the key trigger that escalates planning obligations.
- **This node (Page 1 / Article 1):** "Systemically Important Financial Institution (SIFI): A financial institution designated by the competent authority as SIFI in accordance with Article 2 of this Law."
- **Related node (Page 6 / Article 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Implication:** A RegTech workflow must gate resolution-plan preparation and the 90-day competent-authority review clock specifically against SIFI designation status; non-SIFI financial institutions face recovery plan obligations only, not the Article 8 resolution plan regime.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
