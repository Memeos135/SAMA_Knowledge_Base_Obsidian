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

# Operational Requirements for Risk Transference

## Connections

### [[Clean-up Call]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether an originating bank can stop holding capital against securitized exposures (i.e. recognise risk transference), check the clean-up call conditions in 18.28-18.30, because a non-conforming clean-up call defeats risk transfer and forces the underlying exposures to be treated as if never securitized. The link reflects that the clean-up call criteria are one of the operational risk-transference conditions: a call that serves as credit enhancement is treated as implicit support and deducted from capital. Conclude that risk-transference recognition cannot be relied upon unless the clean-up call is exercisable only at the 10%-or-less threshold and is not structured to avoid loss allocation or to provide enhancement.
- **Grounding — this node (Page 249 / 18.29):** "Securitization transactions that include a clean-up call that does not meet all of the criteria... result in a capital requirement for the originating bank."
- **Grounding — related node (Page 249 / 18.30):** "If a clean-up call, when exercised, is found to serve as a credit enhancement, the exercise of the clean-up call must be considered a form of implicit support... and must be deducted from regulatory capital."
- **Caveat:** Node B's 'Operational Requirements for Risk Transference' context pages surfaced (751/381/490) are unrelated market/counterparty-risk text; the risk-transference link is grounded in the clean-up-call provisions on page 249 rather than the retrieved node-B excerpts.

### [[Special Purpose Entity (SPE)]] — `references` [EXTRACTED]
- **What this link tells you:** When testing whether an originating bank achieves significant risk transfer (and can therefore exclude securitized assets from RWA), the role of the SPE is central because transfer is normally effected by assigning exposures to a special purpose entity that is legally isolated from the originator. This link signals that the operational risk-transference requirements must be read together with the SPE's legal characteristics. However, the provided contexts for both nodes are market-risk/internal-risk-transfer and capital-instrument disclosure material rather than the securitization risk-transfer articles, so treat the connection as a lead and confirm the actual SCRE18 risk-transfer criteria and SPE definition in the primary text before relying on it.
- **Grounding — this node (Page 381 / 5.26–5.27):** "the banking book leg of the internal risk transfer must be included in the banking book's measure of interest rate risk exposures"
- **Grounding — related node (Page 763 (Table CCA)):** "Position in subordination hierarchy in liquidation ... of the legal entity concerned"
- **Caveat:** Provided contexts do not contain the securitization risk-transfer or SPE-definition articles; the substantive link is inferred and must be verified against SCRE18 primary text.

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
