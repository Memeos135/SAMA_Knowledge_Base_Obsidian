---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Securitization Exposures"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# SEC-IRBA (Securitization Internal Ratings-Based Approach)

## Connections

### [[Attachment and Detachment Points (A, D)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing a securitization risk weight under SEC-IRBA, treat the attachment point (A) and detachment point (D) as required tranche inputs, not descriptive labels: the SEC-IRBA formula and worked examples derive each tranche's risk weight from its A/D boundaries together with KIRB and the supervisory parameter p. The chapter 22 contents list A, D and p under 'Definition' and the illustrative tables show distinct SEC-IRBA risk weights driven by each tranche's A/D. Conclude that any SEC-IRBA calculation must correctly fix A and D per tranche, since mis-stating the tranche boundaries directly changes the resulting RWA.
- **Grounding — this node (Page 13 / ch.22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p) 315; Calculation of risk weight 319"
- **Grounding — related node (Page 346 / Table 2):** "Attachment and detachment points for each tranche... Tranche A 30% 100%; Tranche B 5% 30%; Tranche C 0% 5%"

### [[Credit Risk Mitigation for Securitization Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank buys or provides credit protection on a securitization tranche, note that recognizing that mitigation feeds directly into the RWA computation performed under the chosen securitization method — which for internally-modelled pools is the SEC-IRBA. The CRM framework and the securitization approaches are not separate silos: protected/unprotected sub-tranches are each risk-weighted under the applicable securitization approach, and where the bank has SAMA approval for IRB, exposures excluded from the standardised row (SCRE18–23) fall to SEC-IRBA. Conclude that CRM benefit for a securitization exposure only takes effect once run through the correct approach, so verify approach eligibility (and SAMA approval for IRBA) before claiming mitigation, rather than netting protection outside the framework.
- **Grounding — this node (Page 755):** "subject to the credit risk IRB approaches... The row excludes all positions subject to SCRE18 to SCRE23, including securitisation exposures"
- **Grounding — related node (Page 803 / Table CR3):** "Banks must include all CRM techniques used to reduce capital requirements and disclose all secured exposures, irrespective of whether the standardised or IRB approach is used"
- **Caveat:** The CR3 pages concern credit-risk CRM disclosure generally; the specific SEC-IRBA link is inferred from the shared securitization framework rather than a direct textual cross-reference — verify the primary securitization chapters before relying on it.

### [[Dilution Risk Recognition]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When assessing how a mitigant covering both default and dilution risk affects your capital charge for purchased receivables, the dilution-risk recognition rules and the SEC-IRBA are directly linked: para 14.11 requires banks using SEC-IRBA that can calculate an exposure-weighted LGD to do so per para 22.21, and the framework even provides illustrative examples for recognising dilution risk under SEC-IRBA. So a bank's chosen securitisation approach constrains how it treats dilution mitigants. You would check whether your SEC-IRBA eligibility and LGD-calculation capability trigger the specific treatment in 22.21 rather than a general mitigation rule.
- **Grounding — this node (Page 13 / TOC ch.22 & 27):** "Illustrative examples for recognition of dilution risk when applying the Securitization Internal Ratings-Based Approach (SEC-IRBA)"
- **Grounding — related node (Page 180 / Para 14.11):** "banks using the Securitization Internal Ratings-Based Approach (SEC-IRBA) that are able to calculate an exposure-weighted LGD must do so as defined in paragraph 22.21"

### [[Hierarchy of Securitization Approaches]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for a securitization exposure, recognise that SEC-IRBA is the top of the mandated hierarchy of approaches referenced in 18.59-18.62: capital 'as determined by the hierarchy' must generally be computed under IRBA (chapter 22) where the bank can calculate KIRB for the underlying pool, before falling to ERBA/SA. The hierarchy also drives treatment of protected/unprotected sub-tranches and resecuritizations. Conclude that IRBA is not optional where the hierarchy assigns it, and its applicability turns on the bank's ability to derive KIRB and the defined attachment/detachment and supervisory parameters, not on preference.
- **Grounding — this node (Page 13 / Ch.22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB ... Calculation of risk weight"
- **Grounding — related node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62."

### [[KIRB Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether SEC-IRBA is even available for a securitization exposure, remember it is conditional on the bank being able to compute KIRB for the underlying pool: KIRB is the foundational input to the SEC-IRBA formula and is defined at the head of the same chapter 22. Without a valid KIRB the bank cannot apply SEC-IRBA and must move down the hierarchy to SEC-SA or the look-through approach. Conclude that KIRB eligibility (and the method used to derive it) is a gating check for SEC-IRBA — confirm the pool's KIRB can be calculated before treating SEC-IRBA as the applicable approach.
- **Grounding — this node (Page 751):** "securitisation positions subject to the securitisation regulatory framework... reported in row 16"
- **Grounding — related node (Page 13 / ch.22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Caveat:** The node-B excerpts are RWA-template pages; the KIRB–SEC-IRBA dependency is grounded in the chapter 22 contents heading rather than a full formula extract — verify chapter 22 primary text before relying on the precise gating conditions.

### [[Non-Performing Loan (NPL) Securitization]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing the capital approach for an exposure to an NPL securitization (a pool where variable W ≥ 90%), check the explicit SEC-IRBA carve-out before assuming internal-model treatment applies. The NPL provisions state that risk weights may be derived under SEC-IRBA, SEC-SA or the look-through approach, but expressly preclude SEC-IRBA where the bank uses the foundation approach to calculate the underlying pool's KIRB. Conclude that for a foundation-approach bank, SEC-IRBA is off the table for NPL securitizations, and you must fall back to another permitted approach — so confirm which KIRB method the bank uses before selecting SEC-IRBA.
- **Grounding — this node (Page 13 / ch.22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Grounding — related node (Page 330 / 23.3):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach... to calculate the KIRB"

### [[STC-Compliant Securitizations]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital treatment for a securitization that qualifies as STC-compliant, note that the SEC-IRBA chapter contains a dedicated 'Alternative capital treatment for term securitizations and short-term securitizations meeting the STC criteria for capital purposes' — so STC status changes the SEC-IRBA outcome, it is not a separate regime. STC compliance must be independently assessed by both originator/sponsor (disclosure) and investor before any alternative treatment is applied (18.67–18.70), and only then can the SEC-IRBA alternative be used. Conclude that you must first confirm and document STC-compliance status under chapter 18 criteria before claiming the more favorable SEC-IRBA capital treatment.
- **Grounding — this node (Page 13 / Ch 22):** "Alternative capital treatment for term securitizations and short-term securitizations meeting the STC criteria for capital purposes 321"
- **Grounding — related node (Page 260 / 18.66-18.68):** "Exposures to securitizations that are STC-compliant can be subject to alternative capital treatment ... the investor must make its own assessment of the securitization's STC compliance status"

### [[Supervisory Parameter p]] — `references` [EXTRACTED]
- **What this link tells you:** When determining risk weights for securitization exposures under SEC-IRBA, you cannot treat the supervisory parameter (p) as a free input — it is an intrinsic component of the risk-weight formula defined within the SEC-IRBA chapter. The framework's own table of contents lists 'Definition of attachment point (A), detachment point (D) and supervisory parameter (p)' as a sub-section of the SEC-IRBA method (chapter 22), meaning p is prescribed/calibrated by the framework, not chosen by the bank. Conclude that any SEC-IRBA capital calculation must use the p value the regulation dictates for that exposure, and verify the specific calibration in the SEC-IRBA text before applying.
- **Grounding — this node (Page 13 / Ch 22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB ... Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Grounding — related node (Page 13 / Ch 22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p) 315"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
