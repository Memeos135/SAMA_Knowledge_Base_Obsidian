---
source_file: "markdown/SAMA_EN_4283_VER1.md"
type: "concept"
community: "SA-CCR Supervisory Parameters"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/SA-CCR_Supervisory_Parameters
  - graphify/enriched
---

# Adjusted Notional

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **What this link tells you:** When verifying any SA-CCR add-on figure, treat adjusted notional as a required input to effective notional, not an interchangeable concept. The framework defines effective notional as Ai = di × MFi × δi, where di is the adjusted notional — and adjusted notional itself is asset-class-specific (e.g. for FX the foreign-currency leg converted to SAR; for interest rate/credit the notional multiplied by supervisory duration). The consequence: if the adjusted notional is mis-specified (wrong currency leg, missing duration adjustment, or wrong treatment of variable/leveraged notionals under 6.39), every downstream effective notional and add-on is wrong, so a capital-charge review must first confirm the correct adjusted-notional definition was applied per asset class.
- **Grounding — this node (Page 30 / Art 6.37-6.38):** "For foreign exchange derivatives, the adjusted notional is defined as the notional of the foreign currency leg... converted to the Saudi Riyal (SAR)"
- **Grounding — related node (Page 130 / Art 12.31):** "the effective notional for each trade... is calculated using the formula Ai = di * MFi * δi"

#graphify/concept #graphify/EXTRACTED #community/SA-CCR_Supervisory_Parameters #graphify/enriched
