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

# Securitization Standardized Approach (SEC-SA)

## Connections

### [[Attachment Point A and Detachment Point D]] — `references` [EXTRACTED]
- **What this link tells you:** When determining tranche risk weights for a securitization exposure, treat the attachment point (A) and detachment point (D) as core inputs feeding the securitization approaches, including SEC-SA. The corpus defines A and D within chapter 22's SEC-IRBA machinery but the same tranche-position concept drives the SEC-SA calculation used for SA pools and resecuritizations. Conclude that when you assess how much loss a tranche absorbs before and after impairment, you must reference the defined A/D points regardless of which approach applies, and cross-check the specific formula section for the approach you are actually using rather than assuming the illustrative SEC-IRBA examples govern SEC-SA.
- **Grounding — this node (Page 231 / 18.4):** "Banks' exposures to a securitization are hereafter referred to as "securitization exposures""
- **Grounding — related node (Page 6 / Ch 22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Caveat:** Link is structural: A/D are defined in the SEC-IRBA chapter; verify the parallel SEC-SA formula section before applying to an SA pool.

### [[Hierarchy of Approaches for Securitization Exposures]] — `references` [EXTRACTED]
- **What this link tells you:** When you cannot qualify a securitization exposure for the higher-ranked methods, the hierarchy directs you to SEC-SA as the standardized fallback, and its computation carries specific constraints. SEC-SA is defined in chapter 19 (paras 19.1–19.17) and applies a 15% floor risk weight plus special adjustments for resecuritizations (supervisory parameter p set to 1.5). Conclude that reaching SEC-SA is not a free choice but a consequence of the hierarchy; once there, apply the floor and the resecuritization adjustments rather than the ordinary parameters.
- **Grounding — this node (Page 297 / Art 19.15):** "The resulting risk weight is subject to a floor risk weight of 15%."
- **Grounding — related node (Page 244 / Art 18.35):** "Regulatory capital is required for banks' securitization exposures... as set forth in the following sections."

### [[KSA Capital Charge]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the capital charge cap for a bank holding securitization exposures over an SA pool, you must use KSA as the underlying-pool capital charge (KP) feeding the SEC-SA calculation. Paragraph 18.54(2)(b) fixes KP equal to KSA as defined in 19.2 to 19.5 for an SA pool, and 18.53 confirms SEC-SA users may cap capital at the pre-securitization charge. Conclude that the SEC-SA output cannot be assessed without first deriving KSA on the underlying exposures, and for mixed pools you blend KSA and KIRB on an exposure-weighted basis per 18.54(2)(c).
- **Grounding — this node (Page 248 / 18.53):** "An originating or sponsor bank using the SEC-ERBA or SEC-SA ... may apply a maximum capital requirement ... equal to the capital requirement that would have been assessed against the underlying exposures"
- **Grounding — related node (Page 249 / 18.54(2)(b)):** "For an SA pool, KP equals KSA as defined in 19.2 to 19.5."

### [[Mandate-Based Approach (MBA)]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears to place the Mandate-Based Approach (MBA) and the Securitization Standardized Approach (SEC-SA) together as parts of the same hierarchy of RWA approaches within this framework, but they sit in different chapters — MBA is a fund look-through/fall-back method (Ch.24, equity investments in funds) while SEC-SA is a securitization approach (Ch.19). The provided excerpts are chiefly table-of-contents listings and do not show a direct cross-reference between the two. Treat the connection as thematic (both are RWA calculation approaches) rather than an operative cross-reference, and verify the primary text in Ch.19 and Ch.24 before relying on any interaction between MBA and SEC-SA.
- **Grounding — this node (Page 6 / Contents (Ch.19)):** "Standardized approach (SEC-SA) outlined in chapter 19"
- **Grounding — related node (Page 6 / Contents):** "The mandate-based approach 326 ... Application of the LTA and MBA to banks using the IRB approach"
- **Caveat:** Evidence is limited to contents/TOC listings; no direct textual cross-reference between MBA and SEC-SA is shown, so treat the link as thematic and confirm in the primary chapters.

### [[Resecuritization Exposures Treatment]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a resecuritization exposure — a securitization whose underlying pool is itself tranched and includes at least one securitization exposure (18.5) — the treatment feeds into the SEC-SA framework, but resecuritizations carry distinct, harsher capital rules and cannot use the full menu of ordinary securitization approaches. The provided excerpts define resecuritization (18.5) and identify SEC-SA as a securitization approach (Ch.19) but do not, in this context, quote the specific paragraph that assigns resecuritizations to SEC-SA. Treat this as a lead that resecuritization exposures are handled under the SEC-SA-based rules and verify the operative resecuritization risk-weight provisions in the primary text before relying on it.
- **Grounding — this node (Page 231 / 18.4):** "Banks' exposures to a securitization are hereafter referred to as 'securitization exposures'"
- **Grounding — related node (Page 231 / 18.5):** "Resecuritization exposure is a securitization exposure in which the risk associated with an underlying pool of exposures is tranched and at least one of the underlying exposures is a securitization exposure"
- **Caveat:** The excerpts define resecuritization and identify SEC-SA generally but do not quote the specific provision mandating SEC-SA for resecuritizations; confirm the operative resecuritization treatment in the primary text.

### [[Securitization of Non-Performing Loans]] — `references` [EXTRACTED]
- **What this link tells you:** When setting the risk weight for an exposure to a non-performing-loan securitization, SEC-SA is one of the permitted calculation routes: paragraph 23.4 expressly lists the SEC-SA 'outlined in chapter 19' alongside SEC-IRBA and the look-through approach as the methods applicable to NPL securitization exposures. Note the constraint next door — 23.3 precludes SEC-IRBA where the bank uses the foundation approach for the pool's KIRB — so SEC-SA may be the fallback in that case. You would conclude the choice of approach for an NPL securitization is governed by the Ch.23 hierarchy and its carve-outs, and should confirm which of SEC-IRBA/SEC-SA/LTA is actually available before applying a risk weight.
- **Grounding — this node (Page 6 / Ch.19):** "Standardized approach (SEC-SA) outlined in chapter 19"
- **Grounding — related node (Page 323 / 23.4):** "The risk weight applicable to exposures to NPL securitizations according to ... Standardized approach (SEC-SA) outlined in chapter 19"

### [[Simple, Transparent and Comparable (STC) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When applying SEC-SA to an exposure you have assessed as STC-compliant, you must substitute the STC alternative treatment: 19.21 sets p to 0.5 and 19.22 lowers the floor risk weight to 10% for senior tranches, applying instead of the ordinary 19.12/19.15 values. Eligibility is gated by 18.66-18.70, which limit STC to traditional securitizations and require the investor to make its own STC assessment before applying the alternative treatment. Conclude that the beneficial SEC-SA parameters are contingent on documented STC compliance at all times; if STC status is not established or lapses, you revert to the standard SEC-SA parameters and floor.
- **Grounding — this node (Page 298 / 19.20-19.21):** "when the SEC-SA is used, 19.21 and 19.22 are applicable instead of 19.12 and 19.15 ... p ... is set equal to 0.5"
- **Grounding — related node (Page 253 / 18.66):** "Exposures to securitizations that are STC-compliant can be subject to alternative capital treatment as determined by 19.20 to 19.22"

### [[Supervisory Parameter p]] — `references` [EXTRACTED]
- **What this link tells you:** When applying SEC-SA to a securitization exposure, the supervisory parameter p is an integral input to the risk-weight formula, so you cannot compute the SEC-SA risk weight without fixing p for that exposure. Note the corpus specifies p differently by approach: the p-formula with floor 0.3 shown at 22.17 is the SEC-IRBA context, while under SEC-SA p is set to a supervisory value (e.g. 0.5 for STC exposures per 19.21). Conclude that you must apply the SEC-SA-specific p value in chapter 19 and not carry over the SEC-IRBA p-formula from 22.17.
- **Grounding — this node (Page 6 / Ch 19-22):** "Definition of attachment point (A), detachment point (D) and supervisory parameter (p)"
- **Grounding — related node (Page 317 / 22.17):** "The supervisory parameter p in the context of the SEC-IRBA is expressed as follows, where: (1) 0.3 denotes the p-parameter floor"
- **Caveat:** The quoted p-formula at 22.17 is SEC-IRBA-specific; the SEC-SA value of p is set separately (e.g. 19.21). Verify the chapter 19 SEC-SA provision for the applicable p.

#graphify/concept #graphify/EXTRACTED #community/Securitization_IRB_Approach #graphify/enriched
