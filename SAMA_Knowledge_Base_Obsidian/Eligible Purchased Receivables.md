---
source_file: "markdown/SAMA_EN_3502_VER1.md"
type: "document"
community: "IRB CRM & Receivables"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/IRB_CRM__Receivables
  - graphify/enriched
---

# Eligible Purchased Receivables

## Connections

### [[IRB Approach Overview]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying purchased receivables for capital purposes, recognise that they are a distinct asset class within the IRB framework whose treatment straddles corporate and retail rules. The IRB overview lists corporate purchased receivables and retail purchased receivables as separate asset classes for the roll-out obligation, and specifies that eligible corporate receivables can use F-IRB or A-IRB (A-IRB only for obligors otherwise eligible), while retail receivables are A-IRB only. You would conclude that the available approach depends on both the receivable type and whether individual obligor default risk can be assessed, and should check paragraphs 10.25–10.29 and 14.6–14.7 before assuming the top-down treatment applies.
- **Grounding — this node (Page 105 / 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available... For eligible retail receivables... only the A-IRB approach is available."
- **Grounding — related node (Page 105 / 10.43):** "the relevant assets classes are as follows... (5) Corporate purchased receivables... (9) Retail purchased receivables."

### [[RWA for Default Risk (Purchased Receivables)]] — `references` [EXTRACTED]
- **What this link tells you:** When capitalising purchased receivables, treat the default-risk RWA method and the eligibility definition as a chained test: the receivables must first qualify as 'eligible purchased receivables' (retail vs corporate, with the corporate top-down route limited to cases of undue burden), and only then is the chapter 14 default-risk risk-weight function applied. Chapter 14 expressly presupposes eligibility — it 'presents the method of calculating the unexpected loss capital requirements for purchased receivables' with 'IRB capital charges for both default risk and dilution risk' — while chapter 10 defines which receivables and which approach (F-IRB vs A-IRB) are available. Conclude that a reviewer must confirm the eligibility classification and permitted approach before accepting the default-risk RWA calculation.
- **Grounding — this node (Page 105 / Para 10.42):** "For eligible corporate receivables, both a foundation and advanced approach are available ... For eligible retail receivables ... only the A-IRB approach is available."
- **Grounding — related node (Page 168 / Para 14.1–14.2):** "there are internal ratings-based (IRB) capital charges for both default risk and dilution risk ... the IRB risk weight for default risk is based on the risk-weight function applicable to that particular exposure type"

### [[RWA for Dilution Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining capital for a purchased-receivables or securitization portfolio, do not scope dilution-risk RWA as a stand-alone calculation — it only arises within the 'eligible purchased receivables' treatment and its recognition of mitigants feeds directly into the purchased-receivables/securitization capital chain (SEC-IRBA, KIRB). The dilution-risk provisions govern how collateral or guarantees covering dilution or default losses are recognized, while the purchased-receivables definition (paras 10.25–10.29) sets which retail/corporate receivables and top-down approaches even qualify. Conclude that you must confirm the receivables meet the eligibility and operational requirements before applying any dilution-risk mitigant treatment; the two provisions must be read together for a defensible RWA figure.
- **Grounding — this node (Page 313 / 22.6):** "the treatment for eligible purchased receivables described in paragraphs 10.25 to 10.29, 14.2 to 14.7 ... may be used"
- **Grounding — related node (Page 173 / 14.11):** "When collateral or partial guarantees obtained on receivables provide first loss protection ... and these mitigants cover default losses, dilution losses, or both"

### [[Treatment of Guarantees and Credit Derivatives (CRM)]] — `references` [EXTRACTED]
- **What this link tells you:** When crediting a guarantee or credit derivative against a purchased-receivables pool, apply the general CRM guarantee/credit-derivative rules rather than a bespoke receivables carve-out, because the receivables treatment explicitly channels seller or third-party guarantees back to the existing IRB/CRM framework regardless of whether they cover default risk, dilution risk, or both. The CRM chapter sets which guarantees and credit derivatives are eligible (e.g. only CDS and total return swaps providing guarantee-equivalent protection; nth-to-default derivatives excluded), and those eligibility limits govern any protection asserted on the receivables pool. Conclude that a mitigant which fails the CRM eligibility tests gives no capital relief on the receivables, so check the guarantee against the CRM rules before substituting the guarantor's risk weight.
- **Grounding — this node (Page 100 / 10.27):** "the purchasing bank's programme for corporate receivables complies with both the criteria for eligible receivables and the minimum operational requirements"
- **Grounding — related node (Page 88 / 9.76-9.77):** "Only credit default swaps and total return swaps that provide credit protection equivalent to guarantees are eligible for recognition"

#graphify/document #graphify/EXTRACTED #community/IRB_CRM__Receivables #graphify/enriched
