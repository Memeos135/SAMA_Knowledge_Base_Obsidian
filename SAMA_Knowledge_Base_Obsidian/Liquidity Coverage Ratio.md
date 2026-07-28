---
source_file: "markdown/SAMA_EN_2788_VER1.md"
type: "document"
community: "Large Exposure Limits"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Large_Exposure_Limits
  - graphify/enriched
---

# Liquidity Coverage Ratio

## Connections

### [[Cash Inflows]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the LCR, cash inflows reduce total net cash outflows in the denominator, but only contractual inflows from fully performing exposures with no expected default within 30 days may be recognised — and pre-payments and contingent inflows are excluded. Inflows are also subject to the no-double-count rule and, in practice, an aggregate cap under the Basel III LCR framework. Conclude that you cannot recognise all expected receipts as LCR inflows: verify each inflow is contractual, fully performing, within the 30-day horizon, and not already reflected in the HQLA stock before including it in the calculation.
- **Grounding — this node (Page 37 / Row 316):** "Contractual inflows from securities... maturing ≤ 30 days that are not already included in any other item of the LCR framework, provided that they are fully performing."
- **Grounding — related node (Page 31 / para 142):** "the bank should only include contractual inflows... that are fully performing... Pre-payments on loans (not due within 30 days) should not be included."

### [[Cash Outflows]] — `references` [EXTRACTED]
- **What this link tells you:** When assembling the LCR calculation, cash outflows are the core component of 'total net cash outflows' (the denominator), and this document sets prescribed run-off/drawdown rates per outflow category — e.g. 5% drawdown on undrawn committed facilities to retail and small business customers, 100% for uncovered short positions covered by unsecured borrowing. Each outflow line ties to a specific Basel III LCR paragraph (131(a), 141, 147). Conclude that computing the LCR requires applying the correct categorised run-off factor to each outflow line, and you should verify the applicable paragraph reference (e.g. 131(a) for the 5% rate) rather than assuming a uniform treatment.
- **Grounding — this node (Page 24 / Row 228):** "Balances of undrawn committed credit and liquidity facilities... Banks should assume a 5% drawdown of the undrawn portion of these facilities."
- **Grounding — related node (Page 30 / Row 265):** "Any other contractual cash outflows within the next 30 calendar days should be captured in this standard, such as... uncovered short positions."

### [[SAMA Specific Guidance for Amended LCR Prudential Returns]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what this SAMA guidance actually obligates a bank to do, treat the Liquidity Coverage Ratio as the core prudential metric the document exists to operationalize: the guidance specifies how the LCR must be calculated, reported, and applied. The document imposes concrete supervisory obligations tied to the ratio — reporting to SAMA at least monthly (with capacity to escalate to weekly/daily in stress), a reporting lag ideally under two weeks, and immediate notification if the LCR has fallen or is expected to fall below 100%. Conclude that the LCR threshold and its reporting cadence are enforceable supervisory requirements set out in this guidance, not merely descriptive of the Basel III standard it implements.
- **Grounding — this node (Page 24):** "Refer to Paragraph 131(a) of Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools – Jan 2013"
- **Grounding — related node (Page 48 / para 162-163):** "The LCR should be reported to supervisors at least monthly... Banks should also notify supervisors immediately if their LCR has fallen, or is expected to fall, below 100%."

### [[Stock of HQLA]] — `references` [EXTRACTED]
- **What this link tells you:** When applying the LCR, understand that the stock of HQLA is the numerator of the ratio: its composition, caps, and haircuts directly determine whether a bank meets the 100% LCR requirement. The guidance's HQLA rules — Level 1 uncapped, Level 2 subject to the 40% cap, Level 2B within the 15% cap — feed straight into the LCR calculation reported to SAMA. Conclude that any adjustment to eligible HQLA (through the caps in Annex 1 or exclusion of transfer-restricted assets) mechanically changes the reported LCR, so HQLA classification decisions are LCR-compliance decisions, not separate exercises.
- **Grounding — this node (Page 24):** "Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools – Jan 2013"
- **Grounding — related node (Page 58 / Annex 1 para 2):** "the calculation of the 40% cap on Level 2 assets should take into account the impact on the stock of HQLA..."

#graphify/document #graphify/EXTRACTED #community/Large_Exposure_Limits #graphify/enriched
