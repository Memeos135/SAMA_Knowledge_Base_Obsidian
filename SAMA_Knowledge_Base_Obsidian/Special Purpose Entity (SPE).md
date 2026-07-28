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

# Special Purpose Entity (SPE)

## Connections

### [[ABCP Conduit  Programme|ABCP Conduit / Programme]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing an ABCP conduit for capital or STC-criteria purposes, note that SAMA defines the conduit itself as a special purpose vehicle — the SPE concept is the legal-entity form the conduit takes to issue commercial paper. This link tells you the ABCP-specific criteria (conduit-level vs transaction-level) sit on top of the general SPE treatment, so the isolation and bankruptcy-remoteness attributes attaching to SPEs also bear on the conduit analysis. The node B excerpt provided is drawn from an unrelated capital-instrument disclosure template, so verify the actual SPE definition in the securitization chapter (18.x) before relying on the precise scope of the SPE term.
- **Grounding — this node (Page 763 (Table CCA)):** "Identifies issuer legal entity ... Specifies the governing law(s) of the instrument"
- **Grounding — related node (Page 276 / 18.96(1)):** "ABCP conduit/conduit – ABCP conduit, being the special purpose vehicle which can issue commercial paper"
- **Caveat:** Node B context is a capital-instrument disclosure template, not the SPE definition; confirm the primary SPE text in the securitization framework before relying on scope.

### [[Operational Requirements for Risk Transference]] — `references` [EXTRACTED]
- **What this link tells you:** When testing whether an originating bank achieves significant risk transfer (and can therefore exclude securitized assets from RWA), the role of the SPE is central because transfer is normally effected by assigning exposures to a special purpose entity that is legally isolated from the originator. This link signals that the operational risk-transference requirements must be read together with the SPE's legal characteristics. However, the provided contexts for both nodes are market-risk/internal-risk-transfer and capital-instrument disclosure material rather than the securitization risk-transfer articles, so treat the connection as a lead and confirm the actual SCRE18 risk-transfer criteria and SPE definition in the primary text before relying on it.
- **Grounding — this node (Page 763 (Table CCA)):** "Position in subordination hierarchy in liquidation ... of the legal entity concerned"
- **Grounding — related node (Page 381 / 5.26–5.27):** "the banking book leg of the internal risk transfer must be included in the banking book's measure of interest rate risk exposures"
- **Caveat:** Provided contexts do not contain the securitization risk-transfer or SPE-definition articles; the substantive link is inferred and must be verified against SCRE18 primary text.

### [[SEC-SA (Standardized Approach)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the SEC-SA to compute risk weights on securitization exposures, the SPE is the issuing vehicle whose tranches those exposures represent, so the standardized approach operates on positions held against SPE structures. This link points you to read the SEC-SA hierarchy alongside the SPE/securitization definitions. Note that the supplied node B context is a capital-instrument disclosure template (Table CCA), not the operative SPE definition, so treat this as an indicative connection and confirm the SEC-SA scope and SPE meaning in the securitization framework (SCRE18–22) before relying on it.
- **Grounding — this node (Page 763 (Table CCA)):** "Identifies issuer legal entity ... Specifies the governing law(s) of the instrument"
- **Grounding — related node (Page 829 / 21.3):** "Only securitisation exposures that the bank treats under the securitisation framework (SCRE18 to SCRE22) are disclosed in templates SEC3 and SEC4."
- **Caveat:** Node B context is an unrelated capital-instrument disclosure template; the SEC-SA/SPE link is inferred and should be verified against the securitization framework text.

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
