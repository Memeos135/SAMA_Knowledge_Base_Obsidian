---
source_file: "markdown/SAMA_EN_3467_VER1.md"
type: "concept"
community: "LCR & NSFR Metrics"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/LCR__NSFR_Metrics
  - graphify/enriched
---

# Available Stable Funding (ASF)

## Connections

### [[NSFR Derivative Liabilities]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating Available Stable Funding, note that NSFR derivative liabilities are integrated into the ASF side on a net basis: the ASF prudential-return table includes 'NSFR derivative liabilities net of NSFR derivative assets' as a category (with a 0% ASF factor), and the netting is computed against derivative assets per the Required Stable Funding section. Because the standard also assigns a 20% RSF factor to derivative liabilities — a discretion SAMA expressly declined to lower below the 5% floor — the same derivative positions appear on both ASF and RSF sides. Conclude that you must apply the netting rule and the fixed 20% factor as specified, and cannot lower it by invoking national discretion.
- **Grounding — this node (Page 18 / Prudential Returns 1):** "NSFR derivative liabilities net of NSFR derivative assets if NSFR derivative li[abilities]... 0%"
- **Grounding — related node (Page 15):** "The NSFR assigns a 20% "required stable funding" factor to derivative liabilities... SAMA has decided not to exercise this discretion."

### [[Net Stable Funding Ratio (NSFR)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing NSFR compliance, ASF is not a peripheral concept but the numerator of the ratio itself — the NSFR is defined as available stable funding relative to required stable funding, required to be at least 100% on an ongoing basis. The ASF factors (100%, 95%, 90%, 50%, 0%) applied to liability categories in Table 1 directly determine that numerator, calibrated by funding tenor and counterparty stability. For a compliance decision, conclude that any mischaracterisation of a liability's ASF category (e.g. treating wholesale funding as retail) directly distorts the reported NSFR; verify the counterparty and residual-maturity classification against the Table 1 factors.
- **Grounding — this node (3467 / Page 18, Table 1):** "Stable non-maturity (demand) deposits and term deposits with residual maturity of less than one year provided by retail and small business customers — 95%"
- **Grounding — related node (3467 / Page 5, section 4):** "The NSFR is defined as the amount of available stable funding relative to the amount of required stable funding. This ratio should be equal to at least 100% on an ongoing basis."

#graphify/concept #graphify/EXTRACTED #community/LCR__NSFR_Metrics #graphify/enriched
