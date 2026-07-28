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

# SEC-SA (Standardized Approach)

## Connections

### [[Hierarchy of Securitization Approaches]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital treatment of a securitization exposure, do not select SEC-SA in isolation: it sits inside a mandatory ranking (the 'hierarchy of approaches for securitization exposures') that dictates which method a bank may use and under what conditions. The hierarchy provisions repeatedly point to SEC-SA (chapter 19) as one of the ordered options, and SEC-SA itself carries embedded constraints — a 15% floor risk weight and a rule that an unrated junior exposure cannot be risk-weighted below the next more senior rated tranche. Conclude that eligibility for SEC-SA must first be confirmed against the hierarchy, and that even once SEC-SA applies its floors are non-negotiable, so any SEC-SA output must be tested against these minimums.
- **Grounding — this node (Page 304 / 19.15):** "The resulting risk weight is subject to a floor risk weight of 15%... shall not be lower than the risk weight for the next more senior rated exposure"
- **Grounding — related node (Page 257 / 18.59):** "as determined by the hierarchy of approaches for securitization exposures and according to 18.60 to 18.62"

### [[KSA Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge (RWA) for banking-book securitisation positions, do not treat the KSA/jurisdictional capital requirement as separate from the SEC-SA methodology, because the standardised approach for securitisation (SEC-SA) is the mechanism that produces the risk weight feeding into the Pillar 1 capital charge SAMA imposes. The framework routes securitisation exposures through SCRE18-23 and reports them at row 16 of OV1, with SEC-SA supplying a floor risk weight of 15%. Conclude that any capital-charge figure for these exposures must be reconciled to the SEC-SA calculation and its floors, not asserted independently.
- **Grounding — this node (Page 304 / 19.15):** "The resulting risk weight is subject to a floor risk weight of 15%... when a bank applies the SEC-SA to an unrated junior exposure"
- **Grounding — related node (Page 751):** "Minimum capital requirement T: Pillar 1 capital requirements at the reporting date. This will normally be RWA * 8%"

### [[Non-Performing Loan (NPL) Securitization]] — `references` [EXTRACTED]
- **What this link tells you:** When risk-weighting an exposure to a non-performing loan securitization, note that the NPL rules do not create a standalone method but route the calculation into the existing approaches — SEC-IRBA (ch 22), SEC-SA (ch 19), or the look-through approach — subject to NPL-specific constraints. Crucially, a bank using the foundation IRB approach for the underlying pool is precluded from applying SEC-IRBA to that NPL exposure, which pushes it toward SEC-SA. Conclude that you must first classify the pool as an NPL securitization (W ≥ 90%), then check the eligibility restrictions before choosing SEC-SA versus other methods, and note SAMA may impose a stricter NPL definition.
- **Grounding — this node (Page 755):** "RWA for portfolios where standardised approaches are used (cell 1/b): RWA which result from applying the above-described standardised approach"
- **Grounding — related node (Page 330 / 23.3-23.4):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach ... The risk weight applicable ... Standardized approach (SEC-SA) outlined in chapter 19"

### [[Resecuritization Exposure]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge on a resecuritization exposure, apply the SEC-SA — the standard directs banks to use the SEC-SA methodology (19.1–19.15) for resecuritizations, with specified modifications. This means resecuritizations do not get an independent method; they inherit the standardized approach's formula and its floor risk weight, adjusted upward. Conclude that you should compute the resecuritization risk weight through SEC-SA as modified by 19.16 (rather than an external-ratings or IRB path), and check the specific adjustments that raise the charge relative to a plain securitization.
- **Grounding — this node (Page 304 / 19.16):** "For resecuritization exposures, banks must apply the SEC-SA specified in 19.1 to 19.15, with the fo[llowing adjustments]"
- **Grounding — related node (Page 238 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure"

### [[Securitization Internal Assessment Approach (SEC-IAA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge for ABCP-programme securitization exposures, understand that SEC-IAA maps internal assessments to external-rating equivalents which then feed the risk-weight calculation, while SEC-SA is the standardized fallback in the same securitization framework hierarchy. The two connect because IAA-derived rating equivalents and the SA formula sit within the same ordered method stack (SCRE18–SCRE22), so the approach used depends on eligibility rather than preference. Conclude that where IAA prerequisites are not met, you should verify whether SEC-SA (or another approach in the hierarchy) is the mandated fallback for that exposure.
- **Grounding — this node (Page 755):** "RWA for portfolios where standardised approaches are used (cell 1/b): RWA which result from applying the above-described standardised approach"
- **Grounding — related node (Page 313 / 21.1):** "Internal assessments of exposures provided to ABCP programmes must be mapped to equivalent external ratings of an ECAI. Those rating equivalents are used to determine the [risk weight]"
- **Caveat:** The direct textual cross-reference between SEC-IAA and SEC-SA is inferred from their shared position in the securitization framework hierarchy rather than an explicit citation; verify the ordering rules in the primary text before relying on SA as the fallback.

### [[Special Purpose Entity (SPE)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the SEC-SA to compute risk weights on securitization exposures, the SPE is the issuing vehicle whose tranches those exposures represent, so the standardized approach operates on positions held against SPE structures. This link points you to read the SEC-SA hierarchy alongside the SPE/securitization definitions. Note that the supplied node B context is a capital-instrument disclosure template (Table CCA), not the operative SPE definition, so treat this as an indicative connection and confirm the SEC-SA scope and SPE meaning in the securitization framework (SCRE18–22) before relying on it.
- **Grounding — this node (Page 829 / 21.3):** "Only securitisation exposures that the bank treats under the securitisation framework (SCRE18 to SCRE22) are disclosed in templates SEC3 and SEC4."
- **Grounding — related node (Page 763 (Table CCA)):** "Identifies issuer legal entity ... Specifies the governing law(s) of the instrument"
- **Caveat:** Node B context is an unrelated capital-instrument disclosure template; the SEC-SA/SPE link is inferred and should be verified against the securitization framework text.

#graphify/concept #graphify/EXTRACTED #community/Securitization_Exposures #graphify/enriched
