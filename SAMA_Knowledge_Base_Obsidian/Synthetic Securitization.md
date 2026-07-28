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

# Synthetic Securitization

## Connections

### [[Early Amortization Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When structuring or assessing capital relief for a securitization with revolving credit facilities, the early amortization provisions (18.27–18.28, 18.84–18.85) determine whether the originator may exclude underlying exposures from RWA — and these sit within the same Chapter 18 general provisions that also define and cover synthetic securitizations under 18.1's mandate. This link places early amortization treatment inside the shared securitization framework applicable to both traditional and synthetic structures. Conclude that early-amortization analysis is part of the framework-wide scope; confirm which transaction type applies and check that any exclusion of underlying exposures still requires holding regulatory capital against retained securitization exposures, as 18.27 expressly requires.
- **Grounding — this node (Page 230 / 18.1):** "Banks must apply the securitization framework... arising from traditional and synthetic securitizations or similar structures that contain features common to both"
- **Grounding — related node (Page 241 / 18.27):** "an originating bank may exclude the underlying exposures... but must still hold regulatory capital against any securitization exposures they retain in connection with the transaction"
- **Caveat:** Both nodes are in Chapter 18; the early amortization text does not itself single out synthetic structures, so the link is via shared framework scope rather than a direct cross-reference.

### [[Operational Requirements for Recognition of Risk Transference]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** This link appears to connect the operational requirements for recognizing credit risk transference with synthetic securitizations, which is plausible because synthetic securitizations achieve capital relief through transferring credit risk via credit derivatives or guarantees rather than a true sale — so recognition of that transfer would logically depend on operational requirements of the type described in 14.11–14.12. However, the extracted context for node A concerns credit risk mitigation on purchased receivables and guarantees, not the synthetic-securitization-specific risk-transference recognition tests, so the connection is inferred rather than textually established. Before relying on this, verify the primary text for the securitization chapter's own operational requirements for recognition of risk transference in synthetic deals (typically the 18.x significant-risk-transfer provisions) rather than assuming the receivables CRM rules govern.
- **Grounding — this node (Page 230 / 18.3):** "A synthetic securitization is a structure with at least two different stratified risk positions or tranches that reflect different degre[es]"
- **Grounding — related node (Page 173 / 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"
- **Caveat:** INFERRED link; node A's context addresses receivables CRM/guarantees, not synthetic-securitization risk-transfer recognition specifically. Verify the securitization chapter's own risk-transference operational requirements before relying on this edge.

### [[Securitization General Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether the securitization capital framework applies to a given structure, treat synthetic securitizations as squarely in scope: paragraph 18.1 requires banks to apply the securitization framework to both traditional and synthetic securitizations, and 18.3 defines synthetic securitization as a tranched structure. The general provisions (definitions of securitization exposure, originator, resecuritization) therefore govern synthetic deals directly, not by analogy. Conclude that a synthetic transaction cannot escape the framework on the basis of legal form — 18.1 mandates treatment on economic substance — so verify tranching and credit-risk transfer features against the 18.x definitions rather than the transaction's label.
- **Grounding — this node (Page 230 / 18.3):** "A synthetic securitization is a structure with at least two different stratified risk positions or tranches that reflect different degre[es]"
- **Grounding — related node (Page 230 / 18.1):** "Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizations"

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
