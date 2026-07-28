---
source_file: "markdown/SAMA_EN_2888_VER1.md"
type: "document"
community: "Digital Onboarding Security"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Digital_Onboarding_Security
  - graphify/enriched
---

# Minimum Verification Controls

## Connections

### [[Biometric Authentication for Remote Onboarding]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two instruments appear to connect on the theme of authenticating a user/customer identity, but they address different regulatory moments and should not be conflated. The biometric circular mandates that financial institutions use biometric verification via Nafath at 'high' assurance or above when *establishing a relationship remotely* — i.e. onboarding/identity verification tied to CDD; the minimum verification controls set MFA and OTP requirements for *ongoing transactional and login security* of wallets (transfers, bill payments, account reactivation). A compliance reader should verify the primary text before treating them as one obligation set: biometric onboarding does not satisfy the transactional MFA/OTP controls, and vice versa.
- **Grounding — this node (Page 5 / 4.8):** "Multi Factor Authentication (MFA) should be implemented to authenticate each log in."
- **Grounding — related node (Page 1):** "التحقق من السمات الحيوية ... عند بدء/إنشاء العلاقة "عن بعد" على أن يكون مستوى التحقق مرتفع فأعلى"
- **Caveat:** Link is INFERRED / conceptually related only; the two texts govern distinct stages (remote onboarding vs. transaction/login security) and may apply to different addressees — verify scope in each primary source.

### [[E-Wallet Security Controls]] — `references` [EXTRACTED]
- **What this link tells you:** When scoping which controls apply to an E-wallet provider, read the minimum verification controls as directly binding on wallet operations, not as generic background. The document's Statement of Applicability covers 'member organization that provide E-wallet,' and the verification/OTP controls expressly govern wallet-to-wallet transfers, IBAN transfers and reactivations (Arts 4.9–4.10), plus onboarding via NSSO with username, password and OTP (Art 3.3.b). A reader assessing an E-wallet business should conclude these transaction-level OTP and dual-channel requirements are mandatory triggers keyed to defined-value thresholds, and should confirm the 'Defined Value' circulated by SAMA memo before relying on any specific limit.
- **Grounding — this node (Page 5 / Art 4.10):** "Any transaction between wallets exceeding (Defined Value) as a daily limit (for first time as minimum for each beneficiary)"
- **Grounding — related node (Page 3 / Statement of Applicability):** "controls...applies to any member organization that provide E-wallet, lending products, crowdfunding or other fintech business model under SAMA supervision"

### [[Lending Application Special Controls]] — `references` [EXTRACTED]
- **What this link tells you:** When advising a lending company, do not treat the Section 5 lending-specific controls as its complete obligation set — they are additive to the minimum verification controls. Section 5 expressly states its controls apply 'in addition to the above mention controls,' so IBAN-ownership verification, trusted digital signature and Nafith promissory-note handling stack on top of the general OTP/verification and onboarding requirements (including strong authentication from an independent trusted party for lending platforms, Art 3.3.a). A reader scoping a lending platform should conclude both layers apply cumulatively and that the loan-recipient IBAN check (5.1) complements, rather than replaces, the general IBAN-transfer OTP rule.
- **Grounding — this node (Page 5 / Art 4.10.b):** "transfer to IBAN (for first time as minimum for each beneficiary)"
- **Grounding — related node (Page 6 / Section 5):** "The controls below should be implemented by lending companies in addition to the above mention controls."

### [[Multi Factor Authentication (MFA)]] — `references` [EXTRACTED]
- **What this link tells you:** When identifying login and authentication obligations, read MFA (Art 4.8) as a distinct mandatory control within the minimum verification set, separate from transaction-level OTP. The document requires MFA 'to authenticate each log in,' while OTP requirements attach to specific transactions and account changes (Arts 4.9–4.10); the single-device rule (3.8) further requires OTP per login where an app is not confined to one device. A reader should conclude that per-login MFA and per-transaction OTP are cumulative requirements — satisfying transaction OTP does not discharge the login MFA obligation.
- **Grounding — this node (Page 4 / Art 3.8):** "an (OTP) should be implemented for each login, as well as disabling concurrent login"
- **Grounding — related node (Page 5 / Art 4.8):** "Multi Factor Authentication (MFA) should be implemented to authenticate each log in."

### [[One-Time-Password Mechanism (OTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When determining when OTP is mandatory, treat OTP as the operative mechanism through which much of the minimum verification regime is discharged, and note it is triggered at two distinct points: onboarding/registration verification and specific transactions. Art 3.5 requires OTP 'as a form of verification' sent to a trusted-party-verified phone number, while Arts 4.9–4.10 mandate OTP (and dual-channel OTP for higher-risk or above-threshold transfers) for enumerated processes such as wallet transfers, bill payments, password resets and IBAN/international transfers. A reader should conclude OTP obligations are event-specific and threshold-linked, and should confirm the 'Defined Value' governing when single-channel versus dual-channel OTP applies, since that value is set by separate SAMA memo.
- **Grounding — this node (Page 5 / Art 4.9):** "One-time-password mechanism (OTP) should be implemented for the following processes"
- **Grounding — related node (Page 4 / Art 3.5):** "The (OTP) must be send to a verified phone number as per point (3.4)."

### [[SAMA Cybersecurity Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** When determining what a fintech member organization must implement under this SAMA cybersecurity document, treat the general cybersecurity requirement (Art 4.1) as the umbrella obligation and the specific verification/OTP controls (Arts 3.4–3.9, 4.9–4.10) as its concrete mandatory content. The document states members 'should implement regulatory SAMA cybersecurity requirements' and then itemizes verification controls (trusted-party phone-ownership checks via Tahaqaq, OTP as a form of verification), so compliance with 4.1 is not abstract — it is satisfied through these enumerated controls. A reader scoping obligations should conclude that meeting the general cybersecurity requirement necessarily entails the minimum verification controls, and that all controls must be reflected in board-approved internal policies (4.16).
- **Grounding — this node (Page 4 / Art 3.5):** "registration process includes one-time-password mechanism (OTP) as a form of verification"
- **Grounding — related node (Page 4 / Art 4.1):** "Member organization should implement regulatory SAMA cybersecurity requirements."

#graphify/document #graphify/EXTRACTED #community/Digital_Onboarding_Security #graphify/enriched
