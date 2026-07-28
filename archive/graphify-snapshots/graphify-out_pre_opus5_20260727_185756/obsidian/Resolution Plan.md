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

# Resolution Plan

## Connections

### [[Competent Authority]] — `references` [EXTRACTED]
- **Why:** The competent authority is the sole author, owner, and updater of the resolution plan for each SIFI, and must submit it through a defined approval chain, making the resolution plan the primary supervisory instrument through which the competent authority exercises its SIFI-specific resolution mandate.
- **This node (Page 7 / Article 9):** "The competent authority shall submit the resolution plan and any update thereto along with the SIFI's opinion, following its review in light of the SIFI's feedback, to the Council of Economic and Development Affairs for approval."
- **Related node (Page 6 / Article 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Implication:** A RegTech workflow must track the full plan lifecycle—drafting, 60-day SIFI feedback window, competent authority review, and CEDA submission—with timestamped evidence at each stage to satisfy examiner expectations on governance of the plan approval process.

### [[Council of Economic and Development Affairs]] — `references` [EXTRACTED]
- **Why:** Article 9 mandates that the competent authority submit the completed resolution plan—together with the SIFI's feedback—to the Council of Economic and Development Affairs for approval within a 60-day window, making the Council the ultimate approval authority for resolution plans and for resolution fund rules under Article 31.
- **This node (Page 7 / Article 8 para 6):** "The competent authority shall share with the SIFI its vision of the main components of the resolution plan or its update in order to receive feedback from the SIFI within a specified period, provided that it is not less than 60 days."
- **Related node (Page 7 / Article 9):** "The competent authority shall submit the resolution plan and any update thereto along with the SIFI's opinion, following its review in light of the SIFI's feedback, to the Council of Economic and Development Affairs for approval."
- **Implication:** Compliance workflow must sequence three timed stages before Council submission: (1) competent authority drafts plan, (2) SIFI feedback period ≥60 days, (3) authority review and submission to Council—evidence of each stage must be retained to demonstrate procedural compliance to a SAMA examiner.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
