---
source_file: "markdown/SAMA_EN_9618_VER1.md"
type: "document"
community: "Shariah-Compliant Capital"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Shariah-Compliant_Capital
  - graphify/enriched
---

# Additional Capital Adequacy Requirements for Shari'ah Compliant Banking

## Connections

### [[Ijarah]] — `references` [EXTRACTED]
- **What this link tells you:** When capital-weighting a lease-based Islamic exposure, use this document's Ijarah definition and its stage tables (Operating Ijarah 5J, Ijarah Muntahia Bi Al Tamlik 5K) to decide when credit vs market risk applies across the contract lifecycle. Critically, note the carve-out: Table 5K does not apply to real estate finance exposures, which continue under the existing SAMA Basel methodology. Conclude that Ijarah treatment is stage-dependent and asset-type-dependent, so verify whether your exposure is real-estate finance before applying these tables.
- **Grounding — this node (Page 7 / §5):** "additional requirements for mapping Shari'ah compliant assets to SAMA's Basel framework ... through the various stages of the contract"
- **Grounding — related node (Page 11 / Table 5K note (1)):** "Table 5K does not apply to real estate finance exposures. All ijarah structured real estate finance exposures shall continue using the methodology ... in the existing SAMA Basel framework"

### [[Istisna]] — `references` [EXTRACTED]
- **What this link tells you:** When weighting Istisna' exposures, this document distinguishes several sub-cases that carry different risk weights: with vs without Parallel Istisna', and project-finance variants (Tables 5F–5I). The defined term Istisna' (and Parallel Istisna') governs which table applies, and stages such as 'unbilled work-in-process inventory' vs 'amounts receivable after contract billings' switch between market-risk and credit-risk weighting. Conclude that you must first classify the exact Istisna' structure and contract stage, since a mis-classification (e.g. treating a non-parallel istisna' as parallel) changes the applicable capital charge.
- **Grounding — this node (Page 7 / §5):** "This section provides additional requirements for mapping Shari'ah compliant assets to SAMA's Basel framework, given their structure ... through the various stages of the contract"
- **Grounding — related node (Page 5 / Definitions; Page 9 Tables 5F–5G):** "Istisna: The sale of a specified asset, with an obligation on the part of the seller to manufacture/construct it ... to be paid in one lump sum or instalments"

### [[Mudarabah]] — `references` [EXTRACTED]
- **What this link tells you:** When capital-treating a Mudarabah position, note that this document classifies it as an equity exposure rather than routing it through the contract-stage credit/market tables: Musharakah/Mudarabah/Wakalah are weighted under the equity and transition arrangements of SAMA's Basel framework. The defined term Mudarabah (partnership where losses fall on the capital provider absent misconduct) supports that equity characterisation. Conclude that Mudarabah RWAs are determined by the Basel equity treatment, not the murabahah/istisna-style stage tables, so apply the correct branch of the framework.
- **Grounding — this node (Page 6 / Definitions):** "Mudarabah: A partnership contract between the capital provider (rabb al-mal) and an entrepreneur (mudarib) ... losses are to be borne solely by the capital provider"
- **Grounding — related node (Page 11 / §6 Equity Exposures):** "Banks are required to calculate risk weights assets for equity exposure (i.e. Musharakah/Mudarabah/Wakalah) in accordance to the treatment of equity ... in SAMA's Basel framework"

### [[Murabahah]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital treatment of a Murabahah exposure, treat the Murabahah definition and the capital-adequacy instrument as a single reading: the defined contract stages drive whether a credit or market risk-weight applies. The document defines Murabahah and then, in Tables 5A/5B, prescribes stage-specific treatment — before sale the asset attracts market risk (non-binding) or credit risk (binding); after sale/transfer the receivable attracts credit risk. You should conclude the binding vs non-binding purchase order distinction in the definition is dispositive for which capital charge the bank must hold, and check which stage a given exposure sits at before assigning a risk-weight.
- **Grounding — this node (Page 7 / Section 5, Tables 5A-5B):** "Table 5A: Murabahah and non-binding purchase order... Table 5B: Murabahah and binding purchase order"
- **Grounding — related node (Page 5 / Definitions):** "Murabahah: A sale contract whereby the bank sells to a customer a specified asset, whereby the selling price is the sum of the cost price and an agreed profit margin."

### [[Musharakah]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping capital treatment for a Musharakah position, do not map it to the contract-stage tables used for sale/lease products; the instrument routes Musharakah through the equity-exposure regime instead. The document defines Musharakah as a capital-contribution partnership and then, in Section 6, requires banks to risk-weight Musharakah/Mudarabah/Wakalah 'in accordance to the treatment of equity and transition arrangements in SAMA's Basel framework.' You should conclude that equity-exposure rules and transition arrangements — not the murabahah/salam/istisna tables — govern these positions, and verify which Basel equity treatment applies.
- **Grounding — this node (Page 11 / Section 6 Equity Exposures):** "Banks are required to calculate risk weights assets for equity exposure (i.e. Musharakah/Mudarabah/Wakalah) in accordance to the treatment of equity and transition arrangements in SAMA's Basel framework."
- **Grounding — related node (Page 6 / Definitions):** "Musharakah: A partnership contract in which the partners agree to contribute capital to an enterprise, whether existing or new."

### [[SAMA Basel Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital adequacy for a Shari'ah-compliant bank, do not read this Additional Requirements document as a self-contained regime: it is expressly subordinate to and must be read alongside SAMA's Basel framework (circular no. 44047144, 28 Dec 2022, and subsequent updates), supplying only mapping rules for Islamic products. RWA calculations for credit and market risk still follow the Basel framework, while this document tells you which stage of each Islamic contract attracts credit vs market risk weighting. Conclude that both instruments must be applied together, and always use the current Basel framework version since these additions defer to it.
- **Grounding — this node (Page 7 / §5 Prudential Treatment):** "Calculations for risk weighted assets (RWAs) ... are to follow the prudential treatment as per the applicable SAMA's Basel framework"
- **Grounding — related node (Page 4 / §2 Objective):** "which are to be read alongside the applicable SAMA's Basel framework issued via circular no. 44047144 dated 04-06-1444AH ... and any subsequent updates"

### [[Salam]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing capital held against a Salam exposure, use the defined contract structure together with the stage tables, because whether a Parallel Salam exists changes the treatment. The document defines Salam and Parallel Salam and then splits treatment across Table 5D (with Parallel Salam) and Table 5E (without) — at payment of purchase price both credit and market risk-weights apply, while receipt of the commodity is N/A for credit risk. You should conclude the presence or absence of a matched Parallel Salam and the contract stage both determine the charge, and confirm which table governs before assigning a risk-weight.
- **Grounding — this node (Page 8-9 / Tables 5D-5E):** "Table 5D: Salam with Parallel Salam... Table 5E: Salam without Parallel Salam... Payment of purchase price by the bank to a salam customer/seller — Refer to Minimum Capital Requirements for Credit Risk"
- **Grounding — related node (Page 5 / Definitions):** "Salam: The sale of a specified commodity that is of a known type, quantity and attributes for a known price paid at the time of signing the contract for its delivery in the future"

### [[Tawarruq  Commodity Murabahah Transaction|Tawarruq / Commodity Murabahah Transaction]] — `references` [EXTRACTED]
- **What this link tells you:** When determining the capital charge for a Tawarruq/CMT, note the treatment turns on whether there is a binding purchase promise and enforceable documentation. The document defines CMT as a liquidity-generating commodity murabahah and Table 5C provides that with a binding promise and legally enforceable documentation there is no market-risk charge, whereas absent that promise commodities on balance sheet attract market risk and delivered commodities attract credit risk. You should conclude that the legal enforceability of the counterparty's purchase undertaking directly reduces the capital requirement, and verify the documentation actually meets the enforceability condition before relying on the nil charge.
- **Grounding — this node (Page 8 / Table 5C: CMTs):** "In the presence of a binding promise from the counterparty to purchase, and legally enforceable contract documentation, there will be no capital charge for market risk"
- **Grounding — related node (Page 5 / Definitions):** "Tawarruq or Commodity Murabahah Transaction (CMT): A murabahah transaction based on the purchase of a commodity... for the purpose of obtaining liquidity, provided that there are no links between the two contracts."

#graphify/document #graphify/EXTRACTED #community/Shariah-Compliant_Capital #graphify/enriched
