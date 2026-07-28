---
source_file: "markdown/SAMA_EN_3487_VER1.md"
type: "document"
community: "Leverage Ratio Exposures"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Leverage_Ratio_Exposures
  - graphify/enriched
---

# Leverage Ratio Framework

## Connections

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing a bank's leverage ratio compliance, treat the exposure measure as the mandated denominator of that ratio rather than a standalone concept — the LR1 and LR2 templates require reconciling published accounting assets to the leverage ratio exposure measure, and the ratio (row 25) is computed as Tier 1 capital over total exposures. Because both sit within the same SLEV/Pillar 3 disclosure framework and reference identical scope of regulatory consolidation, the exposure measure's adjustments (e.g. central bank reserve exemptions, fiduciary assets) directly change the reported ratio. A reviewer should therefore verify that the exposure measure has been built per SLEV6/SLEV7 before concluding the disclosed leverage ratio meets the national minimum in row 26.
- **Grounding — this node (Page 873 / rows 24-26):** "Total exposures (sum of rows 7, 13, 18 and 22)... Leverage ratio... National minimum leverage ratio requirement"
- **Grounding — related node (Page 870 / Template LR1):** "To reconcile the total assets in the published financial statements with the leverage ratio exposure measure."

### [[Off-Balance Sheet Items]] — `references` [EXTRACTED]
- **What this link tells you:** When checking whether the leverage ratio denominator is complete, off-balance sheet items cannot be omitted: the LR2 template explicitly folds them in as row 22 (sum of rows 19-21) and includes that figure in total exposures at row 24. The framework requires off-balance sheet exposures to be converted to credit-equivalent amounts and to have specific/general provisions deducted from Tier 1 capital netted out. A reviewer should confirm guarantees and irrevocable loan commitments have been captured (gross of CCF/CRM per the CR1 definitions) so the leverage exposure is not understated.
- **Grounding — this node (Page 873 / rows 19-24):** "Off-balance sheet items (sum of rows 19 to 21)... Total exposures (sum of rows 7, 13, 18 and 22)"
- **Grounding — related node (Page 797 / Template CR1 Definitions):** "Off-balance sheet items must be measured according to the following criteria: (a) guarantees given... Irrevocable loan commitments"

### [[Pillar 3 Disclosure Requirements Framework]] — `references` [INFERRED]
- **What this link tells you:** When determining the legal authority and issuing basis for the leverage ratio templates, treat the Leverage Ratio Framework as a component of the broader Pillar 3 Disclosure Requirements Framework rather than an independent instrument — the Pillar 3 framework expressly lists leverage ratio disclosures among its revised requirements and is issued under the Central Bank Law and Banking Control Law, superseding prior Pillar 3 instructions. This link appears to establish the hierarchy (SAMA statutory authority → Pillar 3 framework → leverage ratio templates), so a reviewer should treat the leverage disclosures as mandatory Pillar 3 obligations for banks. Verify the primary text, as this relationship is inferred from thematic listing rather than an explicit cross-reference in the leverage templates themselves.
- **Grounding — this node (Page 738 / Introduction):** "key revisions to the Pillar 3 framework include disclosure requirements related to: a) Credit risk, operational risk, the leverage ratio and credit valuation adjustment (CVA) risk"
- **Grounding — related node (Page 872 / Template LR2):** "Template LR2- Leverage ratio common disclosure template... The table is mandatory for all banks."
- **Caveat:** Relationship is INFERRED from the Pillar 3 framework listing leverage ratio among its disclosure topics; the leverage templates do not contain an explicit citation to the Pillar 3 introduction. Confirm hierarchy in the primary text.

### [[Saudi Central Bank (SAMA)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining who sets and enforces the leverage ratio and its disclosure obligations, treat the Leverage Ratio Framework as a component of SAMA's Basel Framework rather than a free-standing standard. SAMA issues and applies the Basel Framework — which the guidance note defines to include 'leverage' standards — to all local banks on a standalone and consolidated basis under authority derived from the Central Bank Law and Banking Control Law. You would conclude that leverage-ratio requirements (including the CDC disclosure template referencing the leverage ratio buffer) are enforceable SAMA prudential obligations and should be read within SAMA's scope-of-application rules, not as a stand-alone Basel-only norm.
- **Grounding — this node (Page 779 / Template CDC):** "the leverage ratio inclusive of leverage ratio buffer requirement"
- **Grounding — related node (Page 4 / Definition):** "The Framework: Refers to SAMA Basel Framework which includes the minimum risk-based capital and the relevant capital buffers, leverage, liquidity..."

### [[Securities Financing Transaction Exposures Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** When reviewing a bank's leverage ratio disclosures, SFT exposures are a distinct component of the denominator that carries its own explanatory obligation: LR2 requires banks to describe material differences between the SFTs included in the Pillar 1 leverage exposure measure and the mean SFT values disclosed in row 28. Because SFTs receive dedicated adjustments (e.g. row 4 for securities received under SFTs recognised as an asset) and separate mean/quarter-end reporting, a reviewer should check that SFT figures reconcile across rows and that the accompanying narrative explains any divergence before relying on the reported ratio.
- **Grounding — this node (Page 872 / Template LR2):** "key factors that explain any material differences between the amounts of securities financing transactions (SFTs) that are included in the bank's Pillar 1 leverage ratio exposure measure and the mean values"
- **Grounding — related node (Page 873 / rows 28-29):** "Mean value of gross SFT assets, after adjustment for sale accounting transactions and netted of amounts of associated cash payables and cash receivables"

#graphify/document #graphify/EXTRACTED #community/Leverage_Ratio_Exposures #graphify/enriched
