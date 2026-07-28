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

# Asset Management Entity

## Connections

### [[Resolution Procedures]] — `references` [EXTRACTED]
- **Why:** The Asset Management Entity (Article 18) is a discrete resolution procedure tool that is legally required to be used only in conjunction with another resolution procedure, directly embedding it within the resolution procedures framework of Articles 15–18.
- **This node (Page 13 / Article 18):** "the competent authority may take necessary actions to establish an asset management entity to which assets or liabilities of a SIFI under resolution or a transitional entity are transferred, provided that this procedure is only carried out in conjunction with another resolution…"
- **Related node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: The losses incurred by the SIFI under resolution shall be borne by its owners and then by its creditors, taking into account the order of priority of their legal and contractua…"
- **Implication:** A resolution playbook or system workflow must enforce a hard dependency check: activation of the asset management entity procedure cannot be logged or executed as a standalone action — the system must require and record a co-active primary resolution procedure (e.g. sale, transitional entity) as a prerequisite.

### [[Transitional Entity]] — `references` [EXTRACTED]
- **Why:** Article 18 explicitly designates the asset management entity as a receiving vehicle for assets or liabilities originating from either a SIFI under resolution or a transitional entity, making the transitional entity a direct source counterparty in the separation-of-assets procedure. The two concepts are also co-defined in the Law's definitions section as distinct competent-authority-established vehicles with complementary roles in the resolution framework.
- **This node (Page 13 / Article 18):** "The competent authority may take necessary actions to establish an asset management entity to which assets or liabilities of a SIFl under resolution or a transitional entity are transferred, provided that this procedure is only carried out in conjunction with another resolution…"
- **Related node (Page 12 / Article 17):** "the competent authority may take the necessary actions to establish a transitional entity to which all or part of the shares, stocks, assets, or liabilities of the SIFl under resolution are transferred, whether in one or multiple stages, provided that the total value of transfer…"
- **Implication:** Resolution-planning systems must model a two-hop transfer chain (SIFI → Transitional Entity → Asset Management Entity) and maintain auditable asset/liability ledgers at each stage, with valuation records aligned to Article 12(3) to evidence compliance with the conjunctive-procedure requirement and the liability-cap constraint.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
