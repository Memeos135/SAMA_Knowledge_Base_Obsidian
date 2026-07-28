---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "Securitization Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Securitization_Exposures
  - graphify/enriched
---

# Operational Requirements for Recognition of Risk Transference

## Connections

### [[Clean-up Call Conditions]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether an originating bank may exclude securitized exposures from RWA, do not treat the clean-up call conditions as a standalone test — they are one of the operational requirements for recognition of risk transference. Para 18.24(5) makes clean-up calls satisfying 18.28 a condition of the broader operational-requirements set that permits capital relief, and the transference framework also governs when significant credit risk must be transferred to third parties. Conclude that a defective clean-up call breaks the transference chain and, per 18.29–18.30, forces the bank to hold capital as if unsecuritized (or deduct implicit support), so the two provisions must be checked together, not in isolation.
- **Grounding — this node (Page 239 / Art 18.24(5), 18.25(4)):** "Clean-up calls must satisfy the conditions set out in 18.28... Banks must transfer significant credit risk associated with the underlying exposures to third parties."
- **Grounding — related node (Page 242 / Art 18.29):** "Securitization transactions that include a clean-up call that does not meet all of the criteria stated in 18.28 above result in a capital requirement for the originating bank."

### [[Early Amortization Provisions]] — `references` [EXTRACTED]
- **What this link tells you:** When judging whether an early amortization feature still allows an originator to exclude underlying exposures from RWA, read 18.27 together with the operational requirements for risk transference in 18.24/18.25 — the exclusion is only available where those requirements are 'met'. The listed early-amortization examples (replenishment structures, term-mimicking structures, investor-borne drawdowns, non-performance triggers) are carve-outs that preserve genuine risk transfer; if the provision instead returns risk to the bank or subordinates its interest, transference is not recognized. Conclude that early-amortization eligibility is contingent on satisfying the transference conditions, and the bank must still hold capital against any retained securitization exposures.
- **Grounding — this node (Page 239 / Art 18.24-18.25):** "Banks must transfer significant credit risk associated with the underlying exposures to third parties."
- **Grounding — related node (Page 241 / Art 18.27):** "If a securitization transaction contains one of the following examples of an early amortization provision and meets the operational requirements set forth in 18.24 or 18.25, an originating bank may exclude the underlying exposures... but must still hold regulatory capital agains…"

### [[Synthetic Securitization]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** This link appears to connect the operational requirements for recognizing credit risk transference with synthetic securitizations, which is plausible because synthetic securitizations achieve capital relief through transferring credit risk via credit derivatives or guarantees rather than a true sale — so recognition of that transfer would logically depend on operational requirements of the type described in 14.11–14.12. However, the extracted context for node A concerns credit risk mitigation on purchased receivables and guarantees, not the synthetic-securitization-specific risk-transference recognition tests, so the connection is inferred rather than textually established. Before relying on this, verify the primary text for the securitization chapter's own operational requirements for recognition of risk transference in synthetic deals (typically the 18.x significant-risk-transfer provisions) rather than assuming the receivables CRM rules govern.
- **Grounding — this node (Page 173 / 14.12):** "a guarantee provided by the seller or a third party will be treated using the existing IRB rules for guarantees, regardless of whether the guarantee covers default risk, dilution risk, or both"
- **Grounding — related node (Page 230 / 18.3):** "A synthetic securitization is a structure with at least two different stratified risk positions or tranches that reflect different degre[es]"
- **Caveat:** INFERRED link; node A's context addresses receivables CRM/guarantees, not synthetic-securitization risk-transfer recognition specifically. Verify the securitization chapter's own risk-transference operational requirements before relying on this edge.

#graphify/document #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
