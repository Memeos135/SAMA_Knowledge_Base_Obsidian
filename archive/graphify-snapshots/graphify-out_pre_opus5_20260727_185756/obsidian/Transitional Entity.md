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

# Transitional Entity

## Connections

### [[Asset Management Entity]] — `references` [EXTRACTED]
- **Why:** Article 18 explicitly designates the asset management entity as a receiving vehicle for assets or liabilities originating from either a SIFI under resolution or a transitional entity, making the transitional entity a direct source counterparty in the separation-of-assets procedure. The two concepts are also co-defined in the Law's definitions section as distinct competent-authority-established vehicles with complementary roles in the resolution framework.
- **This node (Page 12 / Article 17):** "the competent authority may take the necessary actions to establish a transitional entity to which all or part of the shares, stocks, assets, or liabilities of the SIFl under resolution are transferred, whether in one or multiple stages, provided that the total value of transfer…"
- **Related node (Page 13 / Article 18):** "The competent authority may take necessary actions to establish an asset management entity to which assets or liabilities of a SIFl under resolution or a transitional entity are transferred, provided that this procedure is only carried out in conjunction with another resolution…"
- **Implication:** Resolution-planning systems must model a two-hop transfer chain (SIFI → Transitional Entity → Asset Management Entity) and maintain auditable asset/liability ledgers at each stage, with valuation records aligned to Article 12(3) to evidence compliance with the conjunctive-procedure requirement and the liability-cap constraint.

### [[Resolution Procedures]] — `references` [EXTRACTED]
- **Why:** The Transitional Entity procedure (Article 17) is a named resolution tool deployed by the competent authority within the resolution procedures regime, with Article 17 expressly cross-referencing the sale procedure conditions in Article 16(2) and (3), making both subject to the overarching principles of Article 15.
- **This node (Page 12 / Article 17):** "the competent authority may take the necessary actions to establish a transitional entity to which all or part of the shares, stocks, assets, or liabilities of the SIFI under resolution are transferred … provided that the total value of transferred liabilities do not exceed the…"
- **Related node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: … Mitigate the potential negative impact arising from resolution procedures on other financial institutions within the financial group or sector."
- **Implication:** Systems supporting resolution execution must enforce the Article 17 balance-sheet constraint (transferred liabilities ≤ transferred assets) as a real-time calculation gate, and must log compliance with Article 15 principles — particularly systemic impact mitigation — as an auditable record at the point of transitional entity establishment.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
