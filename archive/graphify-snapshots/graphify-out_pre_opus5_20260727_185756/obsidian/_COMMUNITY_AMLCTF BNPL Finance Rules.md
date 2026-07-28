---
type: community
cohesion: 0.13
members: 17
enriched: true
---

# AML/CTF BNPL Finance Rules

**Cohesion:** 0.13 - loosely connected
**Members:** 17 nodes

## Why this community

This community covers the AML/CTF compliance obligations imposed on Buy-Now-Pay-Later (BNPL) companies under SAMA's regulatory perimeter, sitting at the intersection of the Rules for Regulating BNPL Companies, the Finance Companies Control Law, the Anti-Money Laundering Law, and the Law on Combating the Financing of Terrorism. The central compliance problem is that BNPL companies, as SAMA-licensed finance entities, inherit the full AML/CTF obligation stack — including CDD, STR/FIU reporting, and preventive measures — while also carrying consumer credit and credit-bureau registration duties.

## How members connect

- The Rules for Regulating BNPL Companies bind BNPL Company to the Finance Companies Control Law, establishing the licensing basis that triggers SAMA supervisory authority and the AML/CTF compliance obligations.
- BNPL Company's direct reference to AML/CTF Compliance Requirements creates the obligation chain into both the Anti-Money Laundering Law and the Law on Combating the Financing of Terrorism as the primary legislative sources.
- The AML Law defines Predicate Offense, Due Diligence Measures, Confiscation, and the General Directorate of Financial Intelligence (GDFI) as the STR-receiving authority, forming the core ML control and enforcement vocabulary that BNPL firms must operationalise.
- The CTF Law mirrors and extends AML obligations through Preventive Measures (CTF) and a separate GDFI (CTF) reporting channel, with the Permanent Committee for Combating Terrorism and its Financing providing the inter-agency enforcement layer; the shared_data_with edge between Preventive Measures (CTF) and Due Diligence Measures signals overlapping CDD obligations across both regimes.
- Consumer Due Diligence Program (not 'Customer' CDD) reflects the BNPL-specific defined-term tension: BNPL rules use 'Consumer', while AML rules use 'Customer', requiring firms to map their onboarding workflow to satisfy both definitional scopes.
- Credit Information Registration sits alongside AML/CTF obligations on the BNPL Company node, flagging a cross-regime data obligation where onboarding and CDD data feeds must also satisfy SIMAH/credit bureau reporting requirements.
## Members
- [[AMLCTF Compliance Requirements]] - concept - markdown/SAMA_EN_6523_VER1.md
- [[Anti-Money Laundering Law_2]] - document - markdown/SAMA_EN_791_VER1.md
- [[BNPL Company]] - concept - markdown/SAMA_EN_6523_VER1.md
- [[Confiscation]] - concept - markdown/SAMA_EN_791_VER1.md
- [[Consumer Due Diligence Program]] - concept - markdown/SAMA_EN_6523_VER1.md
- [[Credit Information Registration]] - concept - markdown/SAMA_EN_6523_VER1.md
- [[Due Diligence Measures_1]] - concept - markdown/SAMA_EN_791_VER1.md
- [[Finance Companies Control Law]] - concept - markdown/SAMA_EN_6523_VER1.md
- [[General Directorate of Financial Intelligence]] - concept - markdown/SAMA_EN_791_VER1.md
- [[General Directorate of Financial Intelligence (CTF)]] - concept - markdown/SAMA_EN_853_VER1.md
- [[Law on Combating the Financing of Terrorism]] - document - markdown/SAMA_EN_853_VER1.md
- [[Permanent Committee for Combating Terrorism and its Financing]] - concept - markdown/SAMA_EN_853_VER1.md
- [[Predicate Offense]] - concept - markdown/SAMA_EN_791_VER1.md
- [[Preventive Measures (CTF)]] - concept - markdown/SAMA_EN_853_VER1.md
- [[Rules for Regulating BNPL Companies]] - document - markdown/SAMA_EN_6523_VER1.md
- [[Supervisory Authority]] - concept - markdown/SAMA_EN_791_VER1.md
- [[Terrorism Financing Crime]] - concept - markdown/SAMA_EN_853_VER1.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AML/CTF_BNPL_Finance_Rules
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bank Fraud Combating Rules]]
- 1 edge to [[_COMMUNITY_Personal Data Protection]]

## Top bridge nodes
- [[Anti-Money Laundering Law_2]] - degree 8, connects to 1 community
- [[Credit Information Registration]] - degree 2, connects to 1 community