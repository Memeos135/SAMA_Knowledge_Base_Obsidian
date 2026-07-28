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

# Competent Authority

## Connections

### [[Accredited Valuer]] — `references` [EXTRACTED]
- **Why:** The Law requires the Competent Authority to commission an Accredited Valuer for both the pre-resolution preliminary assessment and the rights-protection valuation, and jointly with the Saudi Authority for Accredited Valuers to issue the governing rules, creating a mandatory procedural dependency between the two concepts.
- **This node (Page 10 / Art 12 para 5):** "The competent authority shall, in cooperation with the Saudi Authority for Accredited Valuers, issue rules for the assessments referred to in paragraphs (1) and (3) of this Article and Article 22(3) of this Law."
- **Related node (Page 9 / Art 12):** "the competent authority shall conduct a preliminary assessment, either by itself or through an accredited valuer… shall first assess the value of its assets and liabilities through an accredited valuer."
- **Implication:** The Competent Authority's resolution workflow must include a documented valuer-appointment step with an escalation path (i.e., authority performs valuation itself) when time does not permit external appointment; both paths require an auditable evidence trail of the assessment outcome before resolution procedures are triggered.

### [[Capital Market Authority]] — `references` [EXTRACTED]
- **Why:** The SIFI Law defines 'Competent Authority' as either SAMA or the CMA depending on which body supervises the financial institution, meaning the CMA is one of the two instantiations of the defined term 'Competent Authority' and exercises identical statutory powers within its supervisory perimeter.
- **This node (Page 1 / Art 1):** "Competent Authority: The Saudi Central Bank or the Capital Market Authority, each with respect to financial institutions falling under its supervision."
- **Related node (Page 14 / Art 14):** "an action plan to be approved by the Governor of the Saudi Central Bank or the Board of the Capital Market Authority, as the case may be, prior to implementing the resolution plan."
- **Implication:** For any SIFI supervised by the CMA, resolution action plans and amendments require CMA Board approval as a hard gate; RegTech workflow controls must route approval chains to the correct authority based on the institution's supervisory classification, and cross-authority coordination (Art 5) must be evidenced where a financial group spans both perimeters.

### [[Resolution Funds]] — `references` [EXTRACTED]
- **Why:** The resolution plan mandated by the competent authority must include a description of how resolution procedures are funded, directly linking the competent authority's planning obligation to the existence and adequacy of resolution funds as a required plan component.
- **This node (Page 6 / Article 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Related node (Page 7 / Article 8(g)):** "Description of how the resolution procedures are funded."
- **Implication:** Resolution plan documentation submitted for CEDA approval must contain an explicit, auditable section on funding sources; examiners will verify this as a mandatory plan element, not a discretionary narrative.

### [[Resolution Plan]] — `references` [EXTRACTED]
- **Why:** The competent authority is the sole author, owner, and updater of the resolution plan for each SIFI, and must submit it through a defined approval chain, making the resolution plan the primary supervisory instrument through which the competent authority exercises its SIFI-specific resolution mandate.
- **This node (Page 6 / Article 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Related node (Page 7 / Article 9):** "The competent authority shall submit the resolution plan and any update thereto along with the SIFI's opinion, following its review in light of the SIFI's feedback, to the Council of Economic and Development Affairs for approval."
- **Implication:** A RegTech workflow must track the full plan lifecycle—drafting, 60-day SIFI feedback window, competent authority review, and CEDA submission—with timestamped evidence at each stage to satisfy examiner expectations on governance of the plan approval process.

### [[Resolution Procedures]] — `references` [EXTRACTED]
- **Why:** The competent authority is the exclusive decision-maker and executor of resolution procedures, with authority spanning domestic SIFIs, foreign branches, and cross-border asset actions, making resolution procedures the direct operational expression of the competent authority's statutory powers.
- **This node (Page 10 / Article 13):** "The competent authority may take one or more of the following procedures on any SIFI and its holding company or a subsidiary financial institution upon the existence of all conditions referred to in Article 10 of this Law."
- **Related node (Page 11 / Article 15):** "In carrying out resolution procedures, the competent authority shall observe the following principles: The losses incurred by the SIFI under resolution shall be borne by its owners and then by its creditors, taking into account the order of priority of their legal and contractua…"
- **Implication:** Compliance controls must capture the competent authority's trigger-condition assessment (Article 10 conditions), the chosen resolution tool(s), and adherence to creditor-hierarchy principles as auditable decision records for each resolution action taken.

### [[Saudi Central Bank]] — `references` [EXTRACTED]
- **Why:** The Law defines 'Competent Authority' as either the Saudi Central Bank or the Capital Market Authority, each exercising supervisory jurisdiction over its respective supervised institutions; SAMA is therefore the operationalising institution of the Competent Authority concept for banking-sector SIFIs.
- **This node (Page 1 / Art 1):** "Competent Authority: The Saudi Central Bank or the Capital Market Authority, each with respect to financial institutions falling under its supervision."
- **Related node (Page 2 / Art 1):** "Competent Judicial Authority: The commercial court with respect to financial institutions supervised by the Saudi Central Bank, and the committees for resolution of securities disputes with respect to financial institutions supervised by the Capital Market Authority."
- **Implication:** Any resolution-related workflow (plan approval, valuation rules, cross-border orders) must be routed through SAMA as Competent Authority when the subject institution is a SAMA-supervised financial institution; system access controls and escalation paths must reflect this dual-authority split.

### [[Systemically Important Financial Institution (SIFI)]] — `references` [EXTRACTED]
- **Why:** The Competent Authority is the exclusive body empowered to designate, plan for, and execute resolution procedures against a SIFI; every substantive obligation in the Law runs between the Competent Authority and the SIFI, making the two nodes the primary regulatory dyad of the Law.
- **This node (Page 6 / Art 8):** "The competent authority shall devise a resolution plan for each SIFI, which includes the resolution procedures to be taken upon the existence of the conditions referred to in Article 10 of this Law."
- **Related node (Page 1 / Art 1):** "Systemically Important Financial Institution (SIFI): A financial institution designated by the competent authority as SIFI in accordance with Article 2 of this Law."
- **Implication:** A SAMA-supervised institution's internal resolution-readiness system must track its SIFI designation status, the 90-day plan approval clock, and all Competent Authority instructions as auditable workflow events with timestamps and version control.

#graphify/concept #graphify/EXTRACTED #community/SIFI_Resolution__Recovery #graphify/enriched
