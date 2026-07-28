---
source_file: "markdown/SAMA_EN_10621_VER1.md"
type: "document"
community: "Interest Rate Shock Scenarios"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Interest_Rate_Shock_Scenarios
  - graphify/enriched
---

# Standardised Interest Rate Shock Scenarios

## Connections

### [[Long Rate Shock Scenario]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which shock calculations a bank must perform for IRRBB, treat the long rate shock as one component of the mandated set rather than a standalone requirement. The Standardised Interest Rate Shock Scenarios prescribe six scenarios per material currency, and the long rate shock is explicitly defined only within that framework and used solely inside the rotational (steepener/flattener) shocks. For compliance scoping you would conclude that the long rate shock is not applied on its own but is invoked through the rotation scenarios; verify the parameterisation for each material currency against Table 1.
- **Grounding — this node (Page 2 / para 1):** "Banks should apply six prescribed interest rate shock scenarios to capture parallel and nonparallel gap risks for EVE"
- **Grounding — related node (Page 3 / para 2(3)):** "Long rate shock for currency c (note: this is used only in the rotational shocks): Here the shock is greatest at the longest tenor midpoint"

### [[Parallel Shock Scenario]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping the mandatory IRRBB measurements, the parallel shock (up and down) is directly enumerated among the six prescribed scenarios banks must apply per material currency. The parent framework references it as a constant shock across all time buckets, and its currency-specific magnitude comes from Table 1. You would conclude that parallel shock up and parallel shock down are two of the six non-optional EVE scenarios and check that the applied basis points match the currency-specific values in Table 1.
- **Grounding — this node (Page 2 / para 1):** "1) Parallel shock up; 2) Parallel shock down; ... The six shock scenarios reflect currency-specific absolute shocks as specified in Table 1"
- **Grounding — related node (Page 3 / para 2(1)):** "Parallel shock for currency c: a constant parallel shock up or down across all time buckets."

### [[Short Rate Shock Scenario]] — `references` [EXTRACTED]
- **What this link tells you:** For scoping IRRBB obligations, the short rate shock (up and down) is a mandated component of the six-scenario framework and also feeds the rotational shocks. The parent framework lists 'Short rates shock up' and 'Short rates shock down' explicitly, and defines the short shock as greatest at the shortest tenor midpoint, decaying via the shaping scalar. You would conclude the short shock is required both as a standalone scenario and as an input to steepener/flattener calculations; confirm the decay parameter x=4 unless SAMA determines otherwise.
- **Grounding — this node (Page 2 / para 1):** "5) Short rates shock up; and 6) Short rates shock down."
- **Grounding — related node (Page 3 / para 2(2)):** "Short rate shock for currency c: shock up or down that is greatest at the shortest tenor midpoint."

#graphify/document #graphify/EXTRACTED #community/Interest_Rate_Shock_Scenarios #graphify/enriched
