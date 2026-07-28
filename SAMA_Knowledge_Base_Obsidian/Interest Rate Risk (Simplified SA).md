---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Market Risk Sensitivities"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Market_Risk_Sensitivities
  - graphify/enriched
---

# Interest Rate Risk (Simplified SA)

## Connections

### [[Duration Method]] — `references` [EXTRACTED]
- **What this link tells you:** This link appears to connect the Duration Method concept to the Interest Rate Risk (Simplified SA) node, but the provided context for the Duration Method node is dominated by counterparty-credit-risk / internal-models-method text (SA-CCR, EAD estimation), not by an interest-rate duration methodology. On the evidence shown, the substantive relationship to interest-rate risk is not textually demonstrated, so treat this as a lead rather than a confirmed cross-reference. Verify against the primary SSA interest-rate paragraphs ([14.3]–[14.40]) before relying on the Duration Method as the operative interest-rate measurement technique.
- **Grounding — this node (Page 361):** "Risk factor: A principal determinant of the change in value of an instrument (eg an exchange rate or interest rate)."
- **Grounding — related node (Page 597 / para 7.1):** "A bank that wishes to adopt an internal models method to measure exposure or exposure at default (EAD) for regulatory capital purposes must seek SAMA approval."
- **Caveat:** Node A's provided context is counterparty-credit-risk/IMM material and does not contain interest-rate duration-method text; the labelled 'Duration Method' link to interest-rate risk is not grounded in the excerpts shown — confirm against the primary SSA interest-rate provisions before relying.

### [[General Market Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the market-risk regime, read General Market Risk as the umbrella under which interest-rate risk (including GIRR) is one recognised risk class, all captured within the same SAMA standardised approach. Both nodes are in SAMA_EN_3487_VER1: [6.1] mandates that all banks (D-SIBs and non-D-SIBs) compute the market-risk charge using the Standardised Approach, and the definitions node lists general interest rate risk among the risk classes forming that charge. Conclude that interest-rate risk cannot be treated under a separate optional regime — it is a mandatory component of the standardised market-risk capital requirement applicable to every bank.
- **Grounding — this node (Page 361):** "A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk..."
- **Grounding — related node (Page 382 / para 6.1):** "all Banks (D-SIBs and Non D-SIBs) are required to calculate the market risk capital charge by using the Standardised Approach."

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When mapping the SAMA_EN_3487 capital framework, note that the simplified standardised approach to interest-rate (market) risk and the IRB approach to credit risk are distinct methodologies addressing different risk classes within the same rulebook — 'general interest rate risk' is a defined market-risk class, while IRB governs credit RWA. The reference reflects their co-location in one comprehensive capital document rather than an operative dependency between them. For a compliance decision, do not treat interest-rate-risk measurement under the simplified SA as governed by IRB rules or vice versa; verify each methodology's own eligibility and SAMA-approval conditions against its own chapter before relying.
- **Grounding — this node (Page 361 / definitions):** "Risk class: ... general interest rate risk, credit spread risk (non-securitisation) ... FX risk, equity risk and commodity risk."
- **Grounding — related node (Page 755 / row 1):** "the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) ...)"
- **Caveat:** The two nodes address different risk classes (market interest-rate risk vs credit risk); the link appears to reflect shared-document co-location rather than a substantive cross-obligation. Confirm against each respective chapter.

### [[Maturity Method]] — `references` [EXTRACTED]
- **What this link tells you:** When measuring interest rate risk capital under the simplified standardised approach, treat the maturity method as the mechanism by which those positions are slotted and offset — the two are linked because the interest rate risk charge under [14.3]–[14.40] is computed by allocating positions to maturity time bands and applying maturity-based weightings. A compliance reviewer verifying an IRR capital calculation should confirm positions were assigned to the correct maturity bands (with the sub-three-month floor where relevant), rather than treating IRR measurement and maturity slotting as independent steps. Verify against the specific band and floor rules in the market-risk chapter before relying on any single figure.
- **Grounding — this node (Page 361):** "Risk factor: A principal determinant of the change in value of an instrument (eg an exchange rate or interest rate)."
- **Grounding — related node (Page 434 / 8.18):** "maturity weighting applied to the JTD for any sort of product with a maturity of less than three months ... is floored at ... three months"

### [[Simplified Standardised Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating market-risk capital for interest-rate positions, treat interest-rate risk as the first of the four risk classes that the Simplified Standardised Approach sums, governed by the same instrument's definitions of risk factor/risk class. Both nodes are in SAMA_EN_3487_VER1; the SSA aggregates the interest-rate charge at [14.3]–[14.40] together with equity, FX and commodity charges, and commodity funding exposures that create interest-rate risk are explicitly routed back into these same measures. Conclude that interest-rate risk under the SSA must be quantified using the referenced paragraphs and cannot be double-counted or omitted where it arises from commodity or FX funding.
- **Grounding — this node (Page 361):** "Risk class: general interest rate risk, credit spread risk (non-securitisation)... FX risk, equity risk and commodity risk."
- **Grounding — related node (Page 514 / para 14.65(4)):** "the relevant positions should be included in the measures of interest rate and FX risk described in [14.3] to [14.40] and [14.53] to [14.62]"

### [[Specific Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising interest rate positions, do not conflate general interest rate risk with specific/credit-spread risk — they are distinct components that must both be captured. The link reflects the framework's 'risk class' taxonomy, which separately lists general interest rate risk and credit spread risk, and the internal-risk-transfer rules that isolate GIRR from other market risks in the trading book. A reviewer should confirm that a bond's specific (issuer/credit-spread) risk charge is calculated in addition to its general interest rate charge, and not assume the general IRR figure covers the whole position.
- **Grounding — this node (Page 361):** "Risk class: A defined list of risks ... general interest rate risk, credit spread risk (non-securitisation) ..."
- **Grounding — related node (Page 381 / 5.26):** "separate from any other Generalised Interest Rate Risk (GIRR) or other market risks generated by activities in the trading book"

#graphify/document #graphify/EXTRACTED #community/Market_Risk_Sensitivities #graphify/enriched
