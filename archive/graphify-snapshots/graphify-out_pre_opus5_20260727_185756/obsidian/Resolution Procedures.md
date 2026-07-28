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

# Resolution Procedures

## Connections

### [[Amendment of Rights]] — `references` [EXTRACTED]
- **Why:** Amendment of Rights is defined as one of the four enumerated resolution procedures under Article 13 and is governed by its own procedural rules (Articles 19–21); it is simultaneously constrained by the creditor-protection principles in Article 15 and Article 22, which set a 'no worse than liquidation' floor that applies across all resolution procedures including this one.
- **This node (Page 11 / Article 15):** "Accord the creditors of the SIFI subject to resolution a fair treatment to ensure that they will not receive a value less than the value they would receive if the SIFI is dissolved at the start of resolution procedures."
- **Related node (Page 14 / Article 19):** "The competent authority may conduct the amendment of rights procedure on the SIFI under resolution by amending the rights of its creditors and capital instrument holders to the extent that enables the institution to recover its status and fulfill statutory requirements."
- **Implication:** Any system implementing the Amendment of Rights procedure must enforce the Article 20 exclusion list (deposits, insurance policies, guaranteed liabilities, client assets, etc.) as hard controls, and must trigger an independent accredited-valuer assessment under Article 22(3) to evidence the 'no worse than liquidation' threshold before rights are amended.

### [[Asset Management Entity]] — `references` [EXTRACTED]
- **Why:** The Asset Management Entity (Article 18) is a discrete resolution procedure tool that is legally required to be used only in conjunction with another resolution procedure, directly embedding it within the resolution procedures framework of Articles 15–18.
- **This node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: The losses incurred by the SIFI under resolution shall be borne by its owners and then by its creditors, taking into account the order of priority of their legal and contractua…"
- **Related node (Page 13 / Article 18):** "the competent authority may take necessary actions to establish an asset management entity to which assets or liabilities of a SIFI under resolution or a transitional entity are transferred, provided that this procedure is only carried out in conjunction with another resolution…"
- **Implication:** A resolution playbook or system workflow must enforce a hard dependency check: activation of the asset management entity procedure cannot be logged or executed as a standalone action — the system must require and record a co-active primary resolution procedure (e.g. sale, transitional entity) as a prerequisite.

### [[Competent Authority]] — `references` [EXTRACTED]
- **Why:** The competent authority is the exclusive decision-maker and executor of resolution procedures, with authority spanning domestic SIFIs, foreign branches, and cross-border asset actions, making resolution procedures the direct operational expression of the competent authority's statutory powers.
- **This node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: The losses incurred by the SIFI under resolution shall be borne by its owners and then by its creditors, taking into account the order of priority of their legal and contractua…"
- **Related node (Page 10 / Article 13):** "The competent authority may take one or more of the following procedures on any SIFI and its holding company or a subsidiary financial institution upon the existence of all conditions referred to in Article 10 of this Law."
- **Implication:** Compliance controls must capture the competent authority's trigger-condition assessment (Article 10 conditions), the chosen resolution tool(s), and adherence to creditor-hierarchy principles as auditable decision records for each resolution action taken.

### [[Sale of the SIFI]] — `references` [EXTRACTED]
- **Why:** Article 16 (Sale of the SIFI) is enumerated as the first and primary named resolution procedure under the resolution procedures framework introduced by Article 15, with the principles in Article 15 governing the conduct of the Article 16 sale and all subsequent procedures.
- **This node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: … Avoid unnecessary depreciation of assets and reduce the cost of resolution procedures, as possible."
- **Related node (Page 11 / Article 16):** "The competent authority may sell all or part of the shares, stocks, assets, or liabilities of the SIFI under resolution, whether the sale occurs in one or multiple stages. The Implementing Regulations shall set the rules governing the sale procedures."
- **Implication:** Resolution management systems must apply the Article 15 creditor-protection and loss-absorption principles as binding constraints on any Article 16 sale transaction record, including evidencing that the 'no creditor worse off' standard was assessed prior to execution.

### [[Transitional Entity]] — `references` [EXTRACTED]
- **Why:** The Transitional Entity procedure (Article 17) is a named resolution tool deployed by the competent authority within the resolution procedures regime, with Article 17 expressly cross-referencing the sale procedure conditions in Article 16(2) and (3), making both subject to the overarching principles of Article 15.
- **This node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: … Mitigate the potential negative impact arising from resolution procedures on other financial institutions within the financial group or sector."
- **Related node (Page 12 / Article 17):** "the competent authority may take the necessary actions to establish a transitional entity to which all or part of the shares, stocks, assets, or liabilities of the SIFI under resolution are transferred … provided that the total value of transferred liabilities do not exceed the…"
- **Implication:** Systems supporting resolution execution must enforce the Article 17 balance-sheet constraint (transferred liabilities ≤ transferred assets) as a real-time calculation gate, and must log compliance with Article 15 principles — particularly systemic impact mitigation — as an auditable record at the point of transitional entity establishment.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
