---
source_file: "markdown/SAMA_EN_2788_VER1.md"
type: "concept"
community: "Large Exposure Limits"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Level 2 Assets

## Connections

### [[Covered Bonds]] — `semantically_similar_to` [INFERRED]
- **What this link tells you:** These two concepts *appear* related only at a surface level — both are prudential asset classifications carrying haircuts and preferential treatment — but they sit in different regimes and serve different purposes. 'Covered bonds' in Appendix VIII of the LEX Rules concern exposure-value assignment for large-exposure (concentration) limits, whereas 'Level 2 assets' in the LCR document concern the composition and 40% cap of a bank's high-quality liquid asset stock for liquidity coverage. Treat this as a thematic lead, not an operative link: do not assume covered-bond eligibility under LEX affects HQLA/Level 2 classification, and verify each regime's own criteria independently before relying on any overlap.
- **Grounding — this node (Page 12):** "'Level 1' assets can be included without limit, while 'Level 2' assets can only comprise up to 40% of the total ... stock."
- **Grounding — related node (Page 33 / Appendix VIII):** "A covered bond ... may be assigned an exposure value of no less than 20% of the nominal value of the bank's covered bond holding."
- **Caveat:** Inferred/semantic link across two different regimes (large-exposure limits vs. LCR liquidity). No cross-reference exists between them in the provided text; do not treat as an operative connection.

### [[High Quality Liquid Assets (HQLA)]] — `references` [EXTRACTED]
- **What this link tells you:** When building the HQLA stock, treat Level 2 as a capped sub-category of HQLA subject to haircuts, distinct from uncapped Level 1: Level 2 assets 'can only comprise up to 40% of the total,' any Level 2B is limited to 15% and sits within that 40% cap, and the caps are measured after required haircuts. For KSA specifically, the guidance notes a deep, large and active market exists 'only' for Saudi shares/equity, so eligibility of other Level 2 instruments is not automatic. You should therefore conclude that Level 2 contributions to HQLA must be tested against both the composition caps and post-haircut valuation before counting them toward the LCR.
- **Grounding — this node (Page 15 / para 51-52):** "Level 2 assets ... comprise no more than 40% of the overall stock after haircuts ... A 15% haircut is applied ... to each Level 2A asset"
- **Grounding — related node (Page 12 / para 46-48):** "'Level 2' assets can only comprise up to 40% of the total ... The 40% cap on Level 2 assets ... should be determined after the application of required haircuts"

### [[Stock of HQLA]] — `references` [EXTRACTED]
- **What this link tells you:** When determining whether a bank's LCR numerator is correctly composed, treat the Level 2 asset definition and the HQLA-stock reporting rules as one calculation, not two: the SAMA LCR standard (2788) defines Level 2 assets and imposes the 40% cap (and 15% Level 2B sub-cap) on the total HQLA stock, while the reporting return (3417) operationalises the same caps through the adjusted-amount and cap line items and Annex 1 methodology. The link matters because the caps are binding only after haircuts and after unwinding short-term securities-financing and collateral-swap transactions maturing within 30 days. Conclude that eligibility of a Level 2 holding cannot be assessed in isolation from the stock-level cap arithmetic in the return; verify both the qualifying-asset criteria and the cap adjustment before treating an asset as HQLA.
- **Grounding — this node (Page 12 / para 46-48):** ""Level 2" assets can only comprise up to 40% of the total (level 1 and level 2) stock ... the 15% cap on Level 2B assets should be determined after the application of required haircuts"
- **Grounding — related node (Page 58 / Annex 1):** "the calculation of the 40% cap on Level 2 assets should take into account the impact on the stock of HQLA ... The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets"

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
