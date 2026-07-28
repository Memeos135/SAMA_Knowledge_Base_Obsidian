---
source_file: "markdown/SAMA_EN_10621_VER1.md"
type: "concept"
community: "Interest Rate Shock Scenarios"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Interest_Rate_Shock_Scenarios
  - graphify/enriched
---

# Long Rate Shock Scenario

## Connections

### [[Rotation Shocks (SteepenerFlattener)|Rotation Shocks (Steepener/Flattener)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining where the long rate shock applies, note it is used exclusively inside the rotation shocks and never as a standalone scenario. The document states the long rate shock 'is used only in the rotational shocks,' and the steepener/flattener formulas take the absolute value of the long shock as a weighted input at each tenor. For calculation and scope you would conclude the long shock is not a standalone required scenario but a mathematical component of the steepener and flattener; confirm the weighting factors against the primary formulas.
- **Grounding — this node (Page 3 / para 2(3)):** "Long rate shock for currency c (note: this is used only in the rotational shocks)"
- **Grounding — related node (Page 3 / para 2(4)):** "ASsteepener,c = −0.65·|ASshort,c(tk)| + 0.9·|ASlong,c(tk)|"

### [[Standardised Interest Rate Shock Scenarios]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which shock calculations a bank must perform for IRRBB, treat the long rate shock as one component of the mandated set rather than a standalone requirement. The Standardised Interest Rate Shock Scenarios prescribe six scenarios per material currency, and the long rate shock is explicitly defined only within that framework and used solely inside the rotational (steepener/flattener) shocks. For compliance scoping you would conclude that the long rate shock is not applied on its own but is invoked through the rotation scenarios; verify the parameterisation for each material currency against Table 1.
- **Grounding — this node (Page 3 / para 2(3)):** "Long rate shock for currency c (note: this is used only in the rotational shocks): Here the shock is greatest at the longest tenor midpoint"
- **Grounding — related node (Page 2 / para 1):** "Banks should apply six prescribed interest rate shock scenarios to capture parallel and nonparallel gap risks for EVE"

#graphify/concept #graphify/EXTRACTED #community/Interest_Rate_Shock_Scenarios #graphify/enriched
