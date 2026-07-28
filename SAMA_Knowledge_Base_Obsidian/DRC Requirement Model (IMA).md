---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Market Risk Backtesting"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Market_Risk_Backtesting
  - graphify/enriched
---

# DRC Requirement Model (IMA)

## Connections

### [[IRB Approach]] — `references` [EXTRACTED]
- **What this link tells you:** If you are reconciling market-risk and credit-risk capital treatment of the same positions, note that the DRC requirement under the IMA and the IRB approach are analytically related but govern different books: the DRC measures 'the default risk of trading book positions' under SMAR13.18, whereas IRB governs default risk in the banking book, and both draw on default-risk (PD/LGD-type) modelling permitted only with SAMA approval. The reference reflects shared modelling concepts (default risk, internal models subject to supervisory validation) across the same rulebook. For a compliance decision, keep the boundary clear — trading-book default risk falls under the DRC/IMA regime, not the IRB credit-risk regime — and confirm each internal model carries its own SAMA approval, since neither approval transfers to the other.
- **Grounding — this node (Page 845 / row for DRC):** "Default risk capital (DRC) requirement: ... measure of the default risk of trading book positions, except those subject to standardised capital requirements."
- **Grounding — related node (Page 755 / row 1):** "subject to the credit risk IRB approaches (Foundation Internal Ratings-Based (F-IRB), Advanced Internal Ratings-Based (A-IRB) ...)"
- **Caveat:** Link rests on shared 'default risk' modelling concepts across market-risk (IMA/DRC) and credit-risk (IRB) chapters; the two apply to different books. Verify each regime's approval scope separately.

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's IMA market-risk capital, treat the DRC requirement as a mandatory sub-component of the IMA, not an optional add-on. The IMA computation is disclosed across three regulatory models — expected shortfall (ES), DRC, and SES for non-modellable risk factors — and DRC (per SMAR13.18) captures default risk of trading-book positions except those under standardised requirements, covering sovereign, equity and defaulted-debt positions. Conclude that any bank on the IMA must produce and disclose a DRC figure, and verify DRC coverage against SMAR13.18 rather than assuming ES alone satisfies the market-risk capital requirement.
- **Grounding — this node (Page 845):** "Default risk capital (DRC) requirement: in accordance with SMAR13.18, measure of the default risk of trading book positions, except those subject to standardised capital requirements"
- **Grounding — related node (Page 843):** "the percentage of capital requirements covered by the models described for each of the regulatory models (expected shortfall (ES), default risk capital (DRC) requirement and stressed expected shortfall (SES)..."

### [[Liquidity Horizon]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the IMA market-risk capital calculation, note that the DRC requirement and the liquidity-horizon-scaled ES are distinct measures that both feed the aggregate IMA capital number, so the liquidity horizon parameter is not a DRC input in the same way it drives ES. This link appears to connect the two chiefly because both are components disclosed and aggregated under the IMA (ES, DRC, SES), rather than because the liquidity horizon table directly parameterises the DRC model. Verify the primary text of SMAR13.18 (DRC) versus 13.2-13.12 (ES/liquidity horizon) before treating the liquidity horizon as an input to DRC; the cross-reference here looks structural (shared IMA framework) rather than a direct calculation dependency.
- **Grounding — this node (Page 845 / Row 10):** "Default risk capital (DRC) requirement: in accordance with SMAR13.18, measure of the default risk of trading book positions, except those subject to standardised capital requirements."
- **Grounding — related node (Page 475 / 13.4):** "In calculating ES, the liquidity horizons described in [13.12] must be reflected by scaling an ES calculated on a base horizon."
- **Caveat:** Link appears structural (both are IMA capital components) rather than a direct calculation dependency; liquidity horizon scaling is textually tied to ES, not DRC. Verify SMAR13.18 before treating liquidity horizon as a DRC input.

#graphify/document #graphify/EXTRACTED #community/Market_Risk_Backtesting #graphify/enriched
