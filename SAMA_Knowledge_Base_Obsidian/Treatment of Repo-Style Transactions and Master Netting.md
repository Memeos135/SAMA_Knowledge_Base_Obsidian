---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "concept"
community: "IRB CRM & Receivables"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/IRB_CRM__Receivables
  - graphify/enriched
---

# Treatment of Repo-Style Transactions and Master Netting

## Connections

### [[Effective Maturity (M)]] — `references` [INFERRED]
- **What this link tells you:** This link appears to connect the effective-maturity (M) rules with the special maturity treatment of repo-style transactions and master netting; verify the primary text before relying on it as the relation is inferred. The effective-maturity provisions set M generally to 2.5 years under the foundation approach and impose a one-year floor and five-year cap, while explicitly assigning M=0.5 for repo-style transactions; the linked provisions then carve out that one-year floor for short-term collateralized capital-market and repo-style transactions with daily remargining, and defer to minimum holding periods where a master netting agreement applies. The practical conclusion: for repo-style and short-term SFT exposures, do not apply the standard M floor — check paras 12.51–12.54 to confirm the correct M or holding-period floor applies.
- **Grounding — this node (Page 131 / 12.51):** "The one-year floor ... does not apply to certain short-term exposures ... repo-style transactions ... where the documentation contains daily remargining clauses"
- **Grounding — related node (Page 130 / 12.44):** "Effective maturity (M) will be 2.5 years ... except for repo-style transactions where the effective maturity is 6 months (i.e. M=0.5)"
- **Caveat:** Relation is INFERRED; the two nodes are drawn from adjacent maturity provisions but the direct cross-reference should be confirmed against paras 12.44–12.54 in the primary text.

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When estimating EAD for repo-style transactions and SFTs, recognize that on-balance-sheet netting effects flow from the master-netting rules referenced here, not from a stand-alone EAD estimate: EAD must be at least the current drawn amount subject to recognizing on-balance-sheet netting, and the recognition of that netting for SFTs depends on the enforceability conditions in the CRM/master-netting provisions. The repo-style/netting provisions set the legal-enforceability and close-out conditions that must be met before netting benefits can be reflected. Conclude that any EAD reduction claimed through netting on repo-style or SFT exposures is contingent on those enforceability tests being satisfied, so confirm the netting agreement meets paras 9.61 conditions before netting into EAD.
- **Grounding — this node (Page 79 / 9.61):** "The effects of bilateral netting agreements covering SFTs may be recognized ... if the agreements are legally enforceable in each relevant jurisdiction"
- **Grounding — related node (Page 206 / 16.88):** "banks must estimate EAD at no less than the current drawn amount, subject to recognizing the effects of on-balance sheet netting"

### [[VaR Models Approach for SFTs]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing whether a bank may use a VaR models approach for SFTs, do not treat the netting-agreement eligibility criteria as separate from the VaR permission — the VaR approach explicitly incorporates them by reference. Paragraph 12.39 permits VaR only where the master netting agreement satisfies the standardized-approach criteria in paragraphs 9.61–9.62 and collateral is revalued daily, the same enforceability and close-out conditions that govern the comprehensive-approach treatment of SFTs under master netting. Conclude that a bank cannot rely on VaR-based EAD for netted SFTs unless the underlying netting agreement independently meets the legal-enforceability, close-out and set-off requirements of the netting provisions; verify those conditions before accepting the VaR result.
- **Grounding — this node (Page 79 / Para 9.61):** "The effects of bilateral netting agreements covering SFTs may be recognized on a counterparty-by-counterparty basis if the agreements are legally enforceable in each relevant jurisdiction upon the occurrence of an event of default"
- **Grounding — related node (Page 128 / Para 12.39):** "The master netting agreement must satisfy the criteria set out in paragraphs 9.61 and 9.62 of the standardized approach."

#graphify/concept #graphify/EXTRACTED #community/IRB_CRM__Receivables #graphify/enriched
