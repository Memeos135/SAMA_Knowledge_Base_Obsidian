---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Securitization Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Credit Risk Mitigation for Securitization Exposures

## Connections

### [[SEC-IRBA (Securitization Internal Ratings-Based Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank buys or provides credit protection on a securitization tranche, note that recognizing that mitigation feeds directly into the RWA computation performed under the chosen securitization method — which for internally-modelled pools is the SEC-IRBA. The CRM framework and the securitization approaches are not separate silos: protected/unprotected sub-tranches are each risk-weighted under the applicable securitization approach, and where the bank has SAMA approval for IRB, exposures excluded from the standardised row (SCRE18–23) fall to SEC-IRBA. Conclude that CRM benefit for a securitization exposure only takes effect once run through the correct approach, so verify approach eligibility (and SAMA approval for IRBA) before claiming mitigation, rather than netting protection outside the framework.
- **Grounding — this node (Page 803 / Table CR3):** "Banks must include all CRM techniques used to reduce capital requirements and disclose all secured exposures, irrespective of whether the standardised or IRB approach is used"
- **Grounding — related node (Page 755):** "subject to the credit risk IRB approaches... The row excludes all positions subject to SCRE18 to SCRE23, including securitisation exposures"
- **Caveat:** The CR3 pages concern credit-risk CRM disclosure generally; the specific SEC-IRBA link is inferred from the shared securitization framework rather than a direct textual cross-reference — verify the primary securitization chapters before relying on it.

### [[Synthetic Securitization]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalizing a synthetic securitization, recognize that its credit protection is achieved through the CRM framework rather than through a true sale, so eligibility and haircut rules for guarantees and credit derivatives directly govern the capital outcome. A synthetic securitization tranches risk using credit derivatives or guarantees, and the securitization framework applies based on economic substance rather than legal form. Conclude that the recognition standards for financial guarantees and credit derivatives (the same CRM techniques disclosed in Table CR3) determine whether the transferred risk actually reduces RWA, so verify CRM eligibility and haircut treatment before assuming capital relief on the protected portion.
- **Grounding — this node (Page 803 / Table CR3):** "Banks must include all CRM techniques used to reduce capital requirements and disclose all secured exposures, irrespective of whether the standardised or IRB approach is used"
- **Grounding — related node (Page 237 / 18.3):** "A synthetic securitization is a structure with at least two different stratified risk positions or tranches that reflect different degre[es]"

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
