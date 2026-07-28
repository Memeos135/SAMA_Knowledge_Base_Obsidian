---
source_file: "markdown/SAMA_EN_1428_VER1.md"
type: "document"
community: "AML & Payment Regulations"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/AML__Payment_Regulations
  - graphify/enriched
---

# Implementing Regulation to the AML Law

## Connections

### [[Business Risk Assessment Guide (AMLCFTPF)|Business Risk Assessment Guide (AML/CFT/PF)]] — `references` [EXTRACTED]
- **Why:** The Business Risk Assessment Guide (10912) is expressly issued under the authority of the AML Law and its Implementing Regulation (1428), which impose the risk-based approach and CDD obligations that the BRA Guide translates into minimum business-risk assessment factors; the Guide cannot restrict obligations already imposed by 1428.
- **This node (Page 7, section 7/10):** "A financial institution or designated non-financial business and profession may rely on another financial institution… to perform identification and verification of the customer; identification and verification of the beneficial owner; and to take the necessary measures to under…"
- **Related node (Page 1, covering circular):** "ونظام مكافحة غسل الأموال الصادر بالمرسوم الملكي رقم (م/١٠)… لا تُقيّد الالتزامات المقرّرة على المؤسسة المالية بموجب الأنظمة واللوائح والتعليمات ذات العلاقة"
- **Implication:** A financial institution's BRA must be calibrated to at least the floor of CDD and risk-management obligations in the AML Implementing Regulation (1428); any BRA conclusion that reduces CDD intensity below what 1428 requires is non-compliant regardless of the Guide's non-prescriptive framing.

### [[Circular Awqaf Beneficial Owner Verification|Circular: Awqaf Beneficial Owner Verification]] — `references` [EXTRACTED]
- **Why:** The Awqaf beneficial owner circular cites the AML Implementing Regulation's CDD obligations on beneficial owner identification and verification as its direct legal basis, and instructs financial institutions to apply those same measures when using General Authority for Endowments channels for waqf customer due diligence.
- **This node (Page 7 / Art 7/10–7/11):** "A financial institution... may rely on another financial institution... to perform identification and verification of the customer; identification and verification of the beneficial owner... immediately obtains all necessary information as required under Article 7 of the Law"
- **Related node (Page 1):** "إلى اللائحة التنفيذية لنظام مكافحة غسل الأموال... وما تضمنته من التزامات على المؤسسات المالية بتطبيق تدابير العناية الواجبة، وخاصة فيما يتصل بالتعرف والتحقق من بيانات المستفيد الحقيقي"
- **Implication:** KYB workflows for waqf customers must incorporate API integration or certificate verification via the General Authority for Endowments portal as the primary beneficial owner data source, with discrepancy reporting to the Authority and intact STR obligations under AML IR Art 7/9 for unresolved mismatches.

### [[Circular Beneficial Owner Query for NPOs|Circular: Beneficial Owner Query for NPOs]] — `references` [EXTRACTED]
- **Why:** The NPO beneficial owner circular explicitly invokes AML Law implementing regulation obligations on CDD and beneficial owner identification/verification as the legal basis for directing financial institutions to use the NCNP query service, and requires STR filing in case of discrepancies — obligations sourced from the AML IR.
- **This node (Page 7 / Art 7/9):** "shall in all cases consider submitting a suspicious transaction report to the Directorate... and shall submit a suspicious transaction report to the Directorate of financial intelligence, and stating the reasons as to why due diligence was not applied"
- **Related node (Page 1):** "إلى اللائحة التنفيذية لنظام مكافحة غسل الأموال... وما تضمنته من التزامات على المؤسسات المالية بتطبيق تدابير العناية الواجبة، وخاصة فيما يتصل بالتعرف والتحقق من هوية المستفيد الحقيقي"
- **Implication:** Financial institutions' CDD workflow for NPO customers must integrate a mandatory query of the NCNP beneficial owner portal; any undisclosed or mismatched beneficial owner must trigger both the institution's existing STR process under the AML IR and a notification to NCNP via AML-CFT.PL@NCNP.GOV.SA.

### [[Circular Waatheq Beneficial Owner Verification|Circular: Waatheq Beneficial Owner Verification]] — `references` [EXTRACTED]
- **Why:** The Waatheq circular (10959) mandates technical integration with the Ministry of Commerce's beneficial-owner data service specifically to fulfil beneficial-owner identification and verification obligations imposed on financial institutions by the AML Law and its Implementing Regulation (1428), which it explicitly cites as its legal basis.
- **This node (Page 7, section 7/10):** "A financial institution… may rely on another financial institution or designated non-financial business and profession to perform identification and verification of the customer; identification and verification of the beneficial owner"
- **Related node (Page 1):** "واللائحة التنفيذية لنظام مكافحة غسل الأموال الصادرة بموجب قرار رئاسة أمن الدولة رقم (١٤٥٢٥)… وقواعد المستفيد الحقيقي الصادرة بقرار معالي وزير التجارة رقم (٩٩)"
- **Implication:** Financial institutions must configure their KYB/CDD workflows to consume Waatheq API data for beneficial-owner verification of corporate customers, and must log discrepancies (undisclosed or mismatched beneficial owners) as CDD exceptions with an STR-consideration trigger per 1428 section 7/9.

### [[Implementation Rules for Banking Control Law]] — `conceptually_related_to` [INFERRED]
- **Why:** The AML Implementing Regulation governs customer/beneficial owner CDD obligations across all SAMA-supervised financial institutions, while the Banking Control Law Implementation Rules govern governance, fit-and-proper, reporting, and inspection obligations specifically for banks — both instruments apply concurrently to licensed banks and share supervisory enforcement through SAMA.
- **This node (Page 12 / Art 14/3):** "Where the anti-money laundering requirements of a foreign country are less strict... a financial institution... shall ensure that its branches and majority-owned subsidiaries operating in that foreign country apply measures consistent with the requirements under the Law and this…"
- **Related node (Page 1):** "rules for implementing the following provisions of the Banking Control Law: Article (12) regarding appointment to boards of directors and senior positions in banks... Article (18) regarding banking inspections conducted by SAMA, the behavior of the bank staff, and compliance wit…"
- **Implication:** Banks' compliance frameworks must evidence both AML IR CDD controls and Banking Control Law governance controls (fit-and-proper, inspection cooperation, board disclosures) as co-applicable obligations — SAMA examiners reviewing one regime will cross-reference adherence to the other.
- **Caveat:** The conceptually_related_to relation is INFERRED; no express cross-reference between these two documents appears in the provided excerpts.

### [[Implementing Regulations of the Law of Combating Terrorist Crimes and its Financing]] — `conceptually_related_to` [INFERRED]
- **Why:** Both documents implement parallel CDD, STR, internal controls, and cross-border compliance obligations for financial institutions under KSA's dual AML/CTF framework; the CTF Implementing Regulations and the AML Implementing Regulation share overlapping scope (financial institutions, designated non-financial businesses, NPOs) and impose consistent but separately enacted obligations that must be read together.
- **This node (Page 7 / Art 7/9):** "shall in all cases consider submitting a suspicious transaction report to the Directorate... submit a suspicious transaction report to the Directorate of financial intelligence, and stating the reasons as to why due diligence was not applied"
- **Related node (Page 10 / Article 18):** "financial institutions, designated non-financial businesses and professions, and non-profit organizations shall include therein... procedures for reporting suspicious transactions... an independent audit procedure to test the effectiveness and adequacy of policies, procedures, a…"
- **Implication:** Compliance programs must maintain a unified control framework that satisfies both AML IR and CTF IR simultaneously — an STR policy, internal audit scope, and cross-border subsidiary requirements must be documented and tested against both instruments to satisfy a SAMA examination covering either regime.
- **Caveat:** The conceptually_related_to relation is INFERRED; no direct cross-citation between the two implementing regulations appears in the provided excerpts.

#graphify/document #graphify/EXTRACTED #community/AML__Payment_Regulations #graphify/enriched
