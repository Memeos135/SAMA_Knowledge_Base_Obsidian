---
source_file: "markdown/SAMA_EN_1713_VER1.md"
type: "concept"
community: "Foreign Bank Branch Regulation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Foreign_Bank_Branch_Regulation
  - graphify/enriched
---

# Liquidity Coverage Ratio (LCR)

## Connections

### [[Alternative Liquidity Approaches (ALA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a bank may rely on alternative liquidity approaches, treat ALA as a conditional supplement that only becomes relevant because the LCR standard itself requires HQLA the jurisdiction cannot supply. Within SAMA_EN_3623 the ALA framework and the LCR are part of one standard: ALA usage is defined and constrained by reference to the LCR (reporting to supervisor, no usage above the shortfall, possible specific approval). Conclude that ALA eligibility flows from the LCR's HQLA requirements and supervisory framework, so any reliance on ALA should be verified against the LCR reporting duties and the jurisdiction's documented supervisory oversight and periodic self-assessment.
- **Grounding — this node (Page 10 / Part 1):** "The LCR should be a key component of the supervisory approach to liquidity risk, but must be supplemented by detailed supervisory assessments."
- **Grounding — related node (Page 69 / Annex 3):** "general and specific rules governing banks' usage of the options are for the guidance of supervisors in developing relevant standards for their banks."

### [[Alternative Liquidity Approaches (ALA) Options]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's LCR compliance in a jurisdiction with insufficient HQLA, read the ALA options guidance as subordinate to and conditioned by the LCR standard, not as a free-standing alternative. Both live in the same SAMA/Basel LCR document (SAMA_EN_3623): the ALA options exist only to meet the LCR where eligible HQLA is short, and Annex 3 caps their use to the actual shortfall and imposes supervisory reporting. Conclude that a bank cannot use ALA options above the level needed to meet its LCR, must report usage to the supervisor regularly, and that certain options (e.g. Option 1 committed facilities) may require specific central-bank approval.
- **Grounding — this node (Page 7 / Introduction):** "ensuring that banks have an adequate stock of unencumbered high-quality liquid assets (HQLA)... to meet their liquidity needs for a 30 calendar day liquidity stress scenario."
- **Grounding — related node (Page 69 / Annex 3):** "A bank should not use an alternative treatment to meet its LCR more than its actual need as reflected by the shortfall of eligible HQLA."

### [[Basel II Framework]] — `cites` [EXTRACTED]
- **What this link tells you:** When determining which assets qualify as HQLA and how the LCR scope applies, do not read the LCR standard in isolation — it explicitly borrows definitions and thresholds from the Basel II Framework. Level 1 asset eligibility turns on the '0% risk-weight under the Basel II Standardised Approach for credit risk', and the LCR's scope of application 'follow[s] the existing scope of application set out in Part I of the Basel II Framework'. Practically, you must confirm an asset's Basel II risk-weight treatment and the Basel II consolidation scope before concluding a position qualifies for HQLA or that an entity falls within LCR reporting.
- **Grounding — this node (Page 44 / para 164):** "The application of the requirements in this document follow the existing scope of application set out in Part I (Scope of Application) of the Basel II Framework"
- **Grounding — related node (Page 18):** "assigned a 0% risk-weight under the Basel II Standardised Approach for credit risk"

### [[Basel III Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing LCR compliance or any jurisdiction-level alternative treatment options, treat the LCR as one component of the broader Basel III liquidity framework rather than a standalone rule. The document itself is titled a Basel III reform and directs that alternative-treatment approaches be 'in line with the alternative treatment set out in the Basel III liquidity framework'. You should therefore check the parent Basel III liquidity provisions (and, in due course, the NSFR) when interpreting HQLA-insufficiency options, not just the LCR text.
- **Grounding — this node (Page 7 / Introduction):** "one of the Basel Committee's key reforms to develop a more resilient banking sector: the Liquidity Coverage Ratio (LCR)"
- **Grounding — related node (Page 61 / para 17):** "in line with the alternative treatment set out in the Basel III liquidity framework (see paragraphs 55 to 62)"

### [[High Quality Liquid Assets (HQLA)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When computing the LCR, understand that HQLA is not a related concept but the numerator itself — the ratio cannot be assessed without applying the HQLA characteristics, operational requirements, level classifications, caps and haircuts. The standard states 'The numerator of the LCR is the "stock of HQLA"' and that banks 'must hold a stock of unencumbered HQLA to cover the total net cash outflows … over a 30-day period'. Any judgement about whether the LCR is met depends first on correctly qualifying assets as HQLA (e.g. unencumbered, Level 1/2 caps), so errors in HQLA eligibility flow directly into the ratio result.
- **Grounding — this node (Page 10 / para 14):** "ensuring that they have sufficient HQLA to survive a significant stress scenario lasting 30 calendar days"
- **Grounding — related node (Page 13 / para 23):** "The numerator of the LCR is the "stock of HQLA". Under the standard, banks must hold a stock of unencumbered HQLA"

### [[LCR by Significant Currency]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When determining what a bank must monitor beyond the headline ratio, note that the LCR itself 'is required to be met in one single currency,' but the document adds a separate expectation that banks and supervisors 'should also monitor the LCR in significant currencies' to capture currency-mismatch risk. The by-currency metric is a monitoring supplement, not an additional binding minimum, so a bank cannot substitute foreign-currency LCR compliance for the single-currency requirement. Conclude that both must be tracked, and check whether SAMA has designated significant currencies or set mismatch limits.
- **Grounding — this node (Page 51 / para 209):** "While the LCR is required to be met in one single currency ... banks and supervisors should also monitor the LCR in significant currencies"
- **Grounding — related node (Page 51 / para 209-210):** "Foreign Currency LCR = Stock of HQLA in each significant currency / Total net cash outflows over a 30-day time period in each significant currency"

### [[Net Stable Funding Ratio (NSFR)]] — `conceptually_related_to` [EXTRACTED]
- **What this link tells you:** When scoping liquidity obligations, treat the LCR and NSFR as complementary but distinct standards addressing different horizons — the LCR covers a 30-day stress window while the NSFR addresses longer-term stable funding. The LCR text states it 'must be supplemented by … in due course, the NSFR', signalling the two are separate metrics rather than substitutes. You should not assume LCR compliance satisfies stable-funding expectations; confirm the NSFR's own requirements separately once it applies.
- **Grounding — this node (Page 10 / para 15):** "must be supplemented by … the use of the monitoring tools included in Part 2, and, in due course, the NSFR"
- **Grounding — related node (Page 48 / para 188):** "encourages the diversification of funding sources recommended in the Committee's Sound Principles"
- **Caveat:** NSFR here appears only as a cross-reference within the LCR document; the LCR text does not fully set out NSFR requirements, so verify the separate NSFR standard before relying on its scope.

### [[Principles for Sound Liquidity Risk Management and Supervision]] — `cites` [EXTRACTED]
- **What this link tells you:** When assessing whether meeting the LCR discharges a bank's liquidity-risk obligations, do not treat the LCR as self-standing: the standard expressly states it 'must be supplemented' by supervisory assessment of the broader liquidity-risk framework 'in line with the Sound Principles.' The LCR is one quantitative floor within the wider qualitative regime, and supervisors may impose more stringent parameters based on their assessment of compliance with the Sound Principles. Conclude that LCR compliance alone is not a complete defence — the qualitative Sound Principles remain a separate, enforceable supervisory benchmark.
- **Grounding — this node (Page 10 / para 15):** "The LCR should be a key component of the supervisory approach to liquidity risk, but must be supplemented by detailed supervisory assessments ... in line with the Sound Principles"
- **Grounding — related node (Page 10 / para 15):** "supervisors may require an individual bank to adopt more stringent standards or parameters ... the supervisor's assessment of its compliance with the Sound Principles"

### [[Total Net Cash Outflows]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the LCR you must apply Total Net Cash Outflows as the denominator, and its precise formula constrains the outcome. The standard defines it as 'total expected cash outflows minus total expected cash inflows' over 30 days, with inflows capped at 75% of outflows, and prohibits double-counting (an asset in the HQLA stock cannot also count its inflows). For decision purposes, verify the run-off/draw-down and inflow factors in Annex 4 and the 75% cap, since misapplying either the cap or the no-double-count rule directly distorts the ratio.
- **Grounding — this node (Page 13 / para 23):** "banks must hold a stock of unencumbered HQLA to cover the total net cash outflows (as defined below) over a 30-day period"
- **Grounding — related node (Page 26 / para 69):** "total net cash outflows … total expected cash outflows minus total expected cash inflows … up to an aggregate cap of 75% of total expected cash outflows"

#graphify/concept #graphify/EXTRACTED #community/Foreign_Bank_Branch_Regulation #graphify/enriched
