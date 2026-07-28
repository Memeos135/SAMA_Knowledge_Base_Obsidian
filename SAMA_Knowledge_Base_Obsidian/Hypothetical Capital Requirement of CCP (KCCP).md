---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "concept"
community: "Credit Risk & CCP Capital"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Credit_Risk__CCP_Capital
  - graphify/enriched
---

# Hypothetical Capital Requirement of CCP (KCCP)

## Connections

### [[Default Fund Exposure Capital Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the capital charge for a clearing member's default-fund exposure to a qualifying CCP, the hypothetical capital of the CCP (KCCP) is an input you must obtain before the charge can be derived — the default-fund requirement is a function of KCCP, not a standalone figure. Both belong to the same SAMA CCR capital framework governing CCP exposures. For a capital calculation you would conclude that the KCCP value drives the default-fund charge and must be sourced/verified from the CCP disclosure rather than estimated.
- **Grounding — this node:** _(source text unavailable / OCR-garbled — consult original)_
- **Grounding — related node (Page 751):** "Counterparty credit risk: RWA and capital charges according to the counterparty credit risk chapters of the Basel framework (SCCR3 to SCCR10)."
- **Caveat:** The provided contexts do not contain the substantive KCCP/default-fund formula text; the dependency is inferred from the Basel/SAMA CCP capital design. Verify the primary CCR chapter before relying on the KCCP-to-default-fund linkage.

### [[Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for exposures to a central counterparty (CCP), the hypothetical capital requirement of the CCP (KCCP) is a component within the counterparty-credit-risk chapters that sit alongside the Minimum Capital Requirements for Credit Risk; the framework routes CCR RWA and capital charges through the SCCR chapters (rows 6-9) as distinct from the general credit-risk standard (SCRE). This means KCCP feeds the calculation of a bank's default-fund and CCP-exposure capital rather than the ordinary credit-risk RWA lines. Conclude that CCP-related charges must be computed under the CCR provisions and reported separately from standard credit risk, so do not fold KCCP-driven exposures into the general SCRE credit-risk lines.
- **Grounding — this node (Page 751):** "Credit risk (excluding counterparty credit risk)... with the exceptions of RWA and capital requirements related to: (i) counterparty credit risk (reported in row 6)"
- **Grounding — related node (Page 751 / row 6-9):** "Counterparty credit risk: RWA and capital charges according to the counterparty credit risk chapters of the Basel framework (SCCR3 to SCCR10)"

#graphify/concept #graphify/EXTRACTED #community/Credit_Risk__CCP_Capital #graphify/enriched
