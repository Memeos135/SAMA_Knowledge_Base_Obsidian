---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "Securitization IRB Approach"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Securitization_IRB_Approach
  - graphify/enriched
---

# Securitization Internal Ratings-Based Approach (SEC-IRBA)

## Connections

### [[Attachment Point A and Detachment Point D]] — `references` [EXTRACTED]
- **What this link tells you:** When determining SEC-IRBA risk weights for a securitization tranche, treat attachment point A and detachment point D as mandatory inputs to that calculation, not standalone concepts. The framework's table of contents groups the 'Definition of attachment point (A), detachment point (D) and supervisory parameter (p)' directly under the SEC-IRBA chapter, and the worked examples feed A/D per tranche into the resulting risk weight. Conclude that any SEC-IRBA capital number a bank reports must be traceable to correctly derived A and D for each tranche's position in the loss waterfall.
- **Grounding — this node (Page 6 / ch.22):** "Internal ratings-based approach (SEC-IRBA)... Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Grounding — related node (Page 339 / Table 2):** "Attachment and detachment points for each tranche... Tranche A 30% 100%; Tranche B 5% 30%; Tranche C 0% 5%"

### [[Hierarchy of Approaches for Securitization Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge for a bank's securitization exposure under this SAMA capital framework, you must first apply the mandated hierarchy of approaches, and SEC-IRBA is the top-ranked method in that sequence. The hierarchy governs whether a bank may use SEC-IRBA at all — it is only available where the bank can compute KIRB for the underlying pool; failing that, the bank falls through to SEC-ERBA/SEC-IAA and then SEC-SA. Conclude that you cannot select SEC-IRBA freely: verify eligibility against the hierarchy's ordering rules (chapters 18–22) before treating an SEC-IRBA risk weight as valid.
- **Grounding — this node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Grounding — related node (Page 244 / Art 18.35):** "Regulatory capital is required for banks' securitization exposures... as set forth in the following sections."

### [[Internal Assessment Approach (SEC-IAA)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may use the Internal Assessment Approach for unrated ABCP-programme exposures, note SEC-IAA is conditioned on the bank's IRB standing: para 21.1 permits internal assessments 'provided that the bank has at least one approved IRB model,' and internal assessments feed the 'IRB capital requirement' arising from those exposures. SEC-IAA thus sits within the IRB family alongside SEC-IRBA and is only reached where a bank cannot rate the exposure directly (18.44). Conclude that SEC-IAA eligibility hinges on approved IRB model status; without it, the internal-assessment route is closed and the exposure must be handled under the remaining hierarchy methods.
- **Grounding — this node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Grounding — related node (Page 306 / Art 21.1):** "provided that the bank has at least one approved IRB model... to determine the IRB capital requirement"

### [[KIRB Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When applying SEC-IRBA, KIRB is the pool-level capital charge that anchors the whole calculation, so a bank cannot use SEC-IRBA at all unless it can compute KIRB for the underlying exposures. The framework lists 'Definition of KIRB' under the SEC-IRBA chapter, and the caps provision fixes KP=KIRB (per 22.2–22.13) for an IRB pool. Conclude that inability to calculate KIRB for part of a mixed pool forces exposure-weighted use of KSA for that portion, changing which capital approach is even available.
- **Grounding — this node (Page 6 / ch.22):** "Internal ratings-based approach (SEC-IRBA)... Definition of KIRB"
- **Grounding — related node (Page 249 / 18.54(2)(a)):** "For an IRB pool, KP equals KIRB as defined in 22.2 to 22.13."

### [[Look-Through Approach (LTA)]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the Look-Through Approach (used for equity investments in funds and referenced for NPL securitizations), note that the framework explicitly links LTA to banks using the IRB approach — the table of contents flags 'Application of the LTA and MBA to banks using the IRB approach.' The connection to SEC-IRBA is definitional: LTA relies on the bank's IRB parameters/KIRB machinery, so a bank's ability to look through depends on its IRB capability. Conclude that LTA is not a standalone alternative independent of IRB standing; check whether the bank meets the IRB approach requirements (chapter 10) before treating LTA-derived risk weights as available.
- **Grounding — this node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Grounding — related node (Page 6 / Chapter 24):** "Application of the LTA and MBA to banks using the IRB approach 329"
- **Caveat:** The LTA node's context is the funds chapter (24); the specific interaction with SEC-IRBA for securitizations is inferred from the cross-reference rather than a direct operative clause — verify chapters 22 and 24 before relying on it.

### [[RWA for Dilution Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When first-loss mitigants cover dilution risk (alone or with default risk) on securitized receivables, apply the SEC-IRBA LGD rule, not just the receivables chapter. Para 14.11 states that where the same mitigant covers both default and dilution risk, banks using SEC-IRBA that can calculate an exposure-weighted LGD must do so as defined in para 22.21, and chapter 27 gives illustrative examples specifically for recognizing dilution risk under SEC-IRBA. Conclude that the dilution-risk treatment and the securitization approach are linked through the LGD calculation, so you should determine the SEC-IRBA LGD inputs before finalizing dilution capital where these mitigants exist.
- **Grounding — this node (Page 6 / chapter 27 heading):** "Illustrative examples for recognition of dilution risk when applying the Securitization Internal Ratings-Based Approach (SEC-IRBA) to securitization"
- **Grounding — related node (Page 173 / para 14.11):** "When the same mitigant covers both default and dilution risk, banks using the Securitization Internal Ratings-Based Approach (SEC-IRBA) that are able to calculate an exposure-weighted LGD must do so as defined in paragraph 22.21."

### [[SAMA Circular No. BCS 242 (ECAI Mapping)]] — `cites` [EXTRACTED]
- **What this link tells you:** This link appears to connect the SEC-IRBA capital approach to SAMA's ECAI rating-to-risk-weight mapping, but verify before relying on it: SEC-IRBA is the internal-ratings method, whereas ECAI mapping (Circular BCS 242, ch.8) governs external-ratings approaches such as SEC-ERBA and SEC-IAA. The cited pages address ECAI eligibility, conflicts of interest, and how SAMA assigns ECAI ratings to standardized risk weights — the SEC-IAA cross-reference on Page 307 is the plausible bridge, not SEC-IRBA itself. Treat this as a lead and confirm which securitization approach actually invokes the ECAI mapping before applying it to a SEC-IRBA exposure.
- **Grounding — this node (Page 6 / ch.22):** "Internal ratings-based approach (SEC-IRBA)"
- **Grounding — related node (Page 55 / 8.6):** "SAMA will be assigning eligible ECAIs' ratings to the risk weights available under the standardized risk weighting framework"
- **Caveat:** Relationship is uncertain: ECAI mapping primarily supports external-ratings approaches (SEC-ERBA/SEC-IAA), not SEC-IRBA; confirm the intended cross-reference in the primary text.

### [[Securitization of Non-Performing Loans]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for an exposure to a non-performing loan securitization, the NPL rules directly scope and limit SEC-IRBA availability. Para 23.3 precludes applying SEC-IRBA to an NPL securitization exposure where the bank uses the foundation approach to calculate the KIRB of the underlying pool, and 23.4 lists SEC-IRBA (chapter 22), SEC-SA (chapter 19) and the look-through approach as the eligible routes. Conclude that for NPL securitizations you must first check the F-IRB carve-out in 23.3: if the underlying KIRB was computed under the foundation approach, SEC-IRBA is unavailable and you fall to SEC-SA or LTA.
- **Grounding — this node (Page 6 / Chapter 22):** "Internal ratings-based approach (SEC-IRBA) 311; Definition of KIRB 311"
- **Grounding — related node (Page 323 / Art 23.3):** "A bank is precluded from applying the SEC-IRBA to an exposure to an NPL securitization where the bank uses the foundation approach... to calculate the KIRB"

### [[Simple, Transparent and Comparable (STC) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When a securitization qualifies as STC-compliant, the SEC-IRBA calculation is modified rather than replaced, so check STC status before finalizing capital. The STC framework expressly points to the SEC-IRBA alternative-treatment paragraphs (22.27 to 22.29) as the provisions engaged for STC exposures, and the SEC-IRBA chapter contains a dedicated 'alternative capital treatment' section for STC securitizations. Conclude that eligibility hinges on the originator/sponsor disclosure and the investor's own STC assessment (18.67–18.68) — without that, the standard SEC-IRBA parameters, not the reduced ones, apply.
- **Grounding — this node (Page 6 / ch.22):** "Alternative capital treatment for term securitizations and short-term securitizations meeting the STC criteria for capital purposes"
- **Grounding — related node (Page 253 / 18.66):** "Exposures to securitizations that are STC-compliant can be subject to alternative capital treatment as determined by 19.20 to 19.22, 20.11 to 20.14 and 22.27 to 22.29."

### [[Supervisory Parameter p]] — `references` [EXTRACTED]
- **What this link tells you:** When computing a SEC-IRBA risk weight, the supervisory parameter p is a defined, non-discretionary input whose value derives from N, KIRB, LGD, MT and the A–E lookup table by pool type (wholesale/retail, senior/non-senior, granular/non-granular). The framework defines p 'in the context of the SEC-IRBA' with a 0.3 floor. Conclude that a bank must first classify the pool correctly to pick the right A–E row, since misclassification changes p and therefore the reported capital charge.
- **Grounding — this node (Page 6 / ch.22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Grounding — related node (Page 317 / 22.17):** "The supervisory parameter p in the context of the SEC-IRBA is expressed as follows, where: (1) 0.3 denotes the p-parameter floor"

### [[Tranched Credit Protection Decomposition]] — `references` [EXTRACTED]
- **What this link tells you:** When determining a bank's capital treatment for tranched credit protection on a securitization exposure, do not treat protected and unprotected slices as one position: paragraph 18.59 requires the original tranche to be decomposed into protected and unprotected sub-tranches, with each sub-tranche's capital requirement then set 'as determined by the hierarchy of approaches for securitization exposures' — which includes SEC-IRBA at the top of that hierarchy. The link tells you that SEC-IRBA is the calculation engine applied to each resulting sub-tranche where the bank qualifies to use it. You would conclude that eligibility and the KIRB inputs of SEC-IRBA must be re-tested at the sub-tranche level, not assumed from the parent tranche.
- **Grounding — this node (Page 311 / Ch.22):** "Internal ratings-based approach (SEC-IRBA) ... Definition of KIRB ... Calculation of risk weight"
- **Grounding — related node (Page 250 / 18.59):** "In the case of tranched credit protection, the original securitization tranche will be decomposed into protected and unprotected sub-tranches"

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
