---
source_file: "markdown/SAMA_EN_6523_VER1.md"
type: "concept"
community: "AML/CTF BNPL Finance Rules"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AML/CTF_BNPL_Finance_Rules
  - graphify/enriched
---

# Credit Information Registration

## Connections

### [[BNPL Company]] — `references` [EXTRACTED]
- **Why:** Article 19(3) imposes a standing obligation on the BNPL Company to register each consumer's credit information with licensed credit information companies and keep it current, creating a direct regulatory link between the BNPL Company's operational activity and the credit information registration regime.
- **This node (Page 9 / Article 19(3)):** "Register the consumer's credit information, with their consent, at one or more of the companies licensed to collect credit information according to the relevant laws, regulations and instructions. Such information must be updated throughout the period of dealing with the consume…"
- **Related node (Page 3 / Article 1):** "BNPL Company: A joint stock company licensed by SAMA to engage in BNPL activity."
- **Implication:** The BNPL company's origination workflow must capture consumer consent at onboarding, trigger real-time or periodic data feeds to licensed credit bureaus, and maintain an audit trail showing registration and ongoing update events per the finance contract lifecycle; this is independently verifiable by SAMA during supervisory visits under Art. 28.

### [[Credit Information Law]] — `references` [INFERRED]
- **Why:** BNPL Rules Art. 19(3) mandates registration of consumer credit information with licensed credit-information companies and Art. 26(10) requires consumer consent in the finance contract; these obligations are directly governed by the Credit Information Law, which defines the licensing regime, member duties, consent requirements, and accuracy/update obligations for exactly such registrations.
- **This node (Page 9 / Art. 19(3)):** "Register the consumer's credit information, with their consent, at one or more of the companies licensed to collect credit information according to the relevant laws, regulations and instructions. Such information must be updated throughout the period of dealing with the consume…"
- **Related node (Page 4 / Art. 5(1)-(2)):** "Each member shall exchange credit information in its possession with the company it has a contract with and shall be liable for the accuracy and updating of such information. A member may obtain a copy of the consumer credit record from companies subject to the written consent o…"
- **Implication:** A BNPL company acting as a 'Member' under the Credit Information Law must maintain a membership agreement with at least one licensed credit-information company, embed consumer consent capture in its onboarding and finance-contract workflow (Art. 26(10)), and implement automated update feeds to satisfy both BNPL Rules Art. 19(3) accuracy obligations and Credit Information Law Art. 5(1) member liability for accuracy.

#graphify/concept #graphify/EXTRACTED #community/AML/CTF_BNPL_Finance_Rules #graphify/enriched
