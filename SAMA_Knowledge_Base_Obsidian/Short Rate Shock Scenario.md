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

# Short Rate Shock Scenario

## Connections

### [[Rotation Shocks (SteepenerFlattener)|Rotation Shocks (Steepener/Flattener)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the steepener and flattener scenarios, you cannot treat them as independent of the short rate shock, because the rotation formulas take the absolute value of the short rate shock as a direct input. The document defines rotation shocks as involving both long and short rates, and the steepener/flattener formulas apply weighted absolute short-shock terms at each tenor midpoint. For calculation you would conclude the short rate shock must be derived first, then combined per the rotation formulas; verify the coefficients (e.g. −0.65 and 0.8) against the primary text.
- **Grounding — this node (Page 3 / para 2(2)):** "Short rate shock for currency c: shock up or down that is greatest at the shortest tenor midpoint."
- **Grounding — related node (Page 3 / para 2(4)):** "Rotation shocks... whereby both the long and short rates are shocked... ASsteepener,c = −0.65·|ASshort,c(tk)| + 0.9·|ASlong,c(tk)|"

### [[Standardised Interest Rate Shock Scenarios]] — `references` [EXTRACTED]
- **What this link tells you:** For scoping IRRBB obligations, the short rate shock (up and down) is a mandated component of the six-scenario framework and also feeds the rotational shocks. The parent framework lists 'Short rates shock up' and 'Short rates shock down' explicitly, and defines the short shock as greatest at the shortest tenor midpoint, decaying via the shaping scalar. You would conclude the short shock is required both as a standalone scenario and as an input to steepener/flattener calculations; confirm the decay parameter x=4 unless SAMA determines otherwise.
- **Grounding — this node (Page 3 / para 2(2)):** "Short rate shock for currency c: shock up or down that is greatest at the shortest tenor midpoint."
- **Grounding — related node (Page 2 / para 1):** "5) Short rates shock up; and 6) Short rates shock down."

#graphify/concept #graphify/EXTRACTED #community/Interest_Rate_Shock_Scenarios #graphify/enriched
