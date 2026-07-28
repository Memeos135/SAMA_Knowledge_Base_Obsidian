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

# High Quality Liquid Assets (HQLA)

## Connections

### [[Level 1 Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating the numerator of the LCR, treat Level 1 assets as the core sub-category of HQLA against which caps on lower tiers are measured: the maximum adjusted Level 2 holdings equal 'two-thirds of the adjusted amount of Level 1 assets after haircuts.' Level 1 defines the base of the qualifying stock, and its adjusted amount (after unwinding short-term secured transactions) drives the eligibility ceilings for Level 2 and 2B. Conclude that Level 1 quantum must be computed first and correctly, because errors there propagate directly into the permissible amount of every lower asset tier.
- **Grounding — this node (Page 13 / para 23):** "The numerator of the LCR is the 'stock of HQLA'. Under the standard, banks must hold a stock of unencumbered HQLA"
- **Grounding — related node (Page 54 / Annex 1 para 2):** "The maximum amount of adjusted Level 2 assets in the stock of HQLA is equal to two-thirds of the adjusted amount of Level 1 assets after haircuts"

### [[Level 2A Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When composing the HQLA stock, treat Level 2A as a capped, haircut-bearing component of HQLA: Level 2 assets (including 2A) are subject to the 40% cap and a 15% haircut, with an additional 20% (5% higher) haircut applying to Level 2A held under the domestic-currency shortfall option. Level 2A is a defined sub-tier of HQLA whose inclusion is quantity-limited and quality-conditioned. Conclude that you must verify both the applicable haircut and whether the 40%-cap or the higher-haircut option regime governs the specific holdings before counting them toward the ratio.
- **Grounding — this node (Page 24):** "supervisors may choose to allow banks that evidence a shortfall of HQLA in the domestic currency ... to hold additional Level 2A assets in the stock"
- **Grounding — related node (Page 24):** "These additional Level 2A assets would be subject to a minimum haircut of 20%, ie 5% higher than the 15% haircut applicable to Level 2A assets"

### [[Level 2B Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When counting HQLA, treat Level 2B as the most restricted sub-category: it is subject to a separate 15% cap within the overall 40% Level 2 cap, so 'adjusted Level 2B assets in the stock of HQLA is equal to 15/85 of the sum of the adjusted amounts of Level 1 and Level 2 assets.' Level 2B is a defined tier of HQLA whose eligible amount is a function of the Level 1 and Level 2 quantities. Conclude that Level 2B eligibility must be tested against both its own 15% cap and the binding 40% cap, and cannot be maximised independently of the higher-tier holdings.
- **Grounding — this node (Page 13 / para 23):** "banks must hold a stock of unencumbered HQLA to cover the total net cash outflows ... over a 30-day period"
- **Grounding — related node (Page 54 / Annex 1 para 3):** "The maximum amount of adjusted Level 2B assets in the stock of HQLA is equal to 15/85 of the sum of the adjusted amounts of Level 1 and Level 2 assets"

### [[Liquidity Coverage Ratio (LCR)]] — `shares_data_with` [EXTRACTED]
- **What this link tells you:** When computing the LCR, understand that HQLA is not a related concept but the numerator itself — the ratio cannot be assessed without applying the HQLA characteristics, operational requirements, level classifications, caps and haircuts. The standard states 'The numerator of the LCR is the "stock of HQLA"' and that banks 'must hold a stock of unencumbered HQLA to cover the total net cash outflows … over a 30-day period'. Any judgement about whether the LCR is met depends first on correctly qualifying assets as HQLA (e.g. unencumbered, Level 1/2 caps), so errors in HQLA eligibility flow directly into the ratio result.
- **Grounding — this node (Page 13 / para 23):** "The numerator of the LCR is the "stock of HQLA". Under the standard, banks must hold a stock of unencumbered HQLA"
- **Grounding — related node (Page 10 / para 14):** "ensuring that they have sufficient HQLA to survive a significant stress scenario lasting 30 calendar days"

### [[Option 3 Additional Level 2A Assets|Option 3: Additional Level 2A Assets]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank can lawfully count HQLA held under the alternative liquidity approach, you must read the HQLA definition together with Option 3, because Option 3 is a conditional expansion of what qualifies as the HQLA stock. HQLA is the LCR numerator that must be unencumbered and highly liquid; Option 3 permits Level 2A assets to exceed the ordinary 40% cap only where SAMA (as the jurisdiction) allows it and only against a higher (minimum 20%) haircut and comparable-quality criteria. Conclude that Option 3 holdings are not free extra HQLA — they count only within a supervisor-set usage limit, at the higher haircut, and require SAMA's documented framework before a bank may rely on them.
- **Grounding — this node (Page 13, para 23):** "banks must hold a stock of unencumbered HQLA to cover the total net cash outflows ... over a 30-day period under the prescribed stress scenario"
- **Grounding — related node (Page 24 / Page 64):** "additional Level 2A assets would be subject to a minimum haircut of 20% ... beyond the 40% cap"

### [[Treatment for Shari'ah Compliant Banks]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the LCR to a Shari'ah-compliant bank facing a shortage of conventional HQLA, do not assume the HQLA definition is simply waived — the Shari'ah treatment is a bounded alternative sitting under the same insufficient-HQLA regime. The document ties treatment for Shari'ah compliant banks to the same supervisory monitoring and disclosure obligations set out for jurisdictions with insufficient HQLA. Conclude that Shari'ah-compliant assets used to meet the LCR are subject to equivalent oversight, disclosure and self-assessment obligations, so a bank cannot rely on Shari'ah status alone to relax the underlying HQLA quality and control requirements.
- **Grounding — this node (Page 13, para 23):** "the numerator of the LCR is the "stock of HQLA" ... assets should be liquid in markets during a time of stress"
- **Grounding — related node (Page 26):** "treatment for Shari'ah compliant banks should comply with supervisory monitoring and disclosure obligations similar to those set out in paragraph 66"

#graphify/concept #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
