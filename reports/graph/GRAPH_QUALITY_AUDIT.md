# Graph Quality Audit

> Generated: 2026-07-27T20:36:52+00:00
> Graph: `graphify-out/graph.json` — 1816 nodes, 1848 edges
> Method: deterministic structural audit + verbatim excerpt grounding (no LLM)

## Overall grade: **B**

| Dimension | Grade | Value | Note |
|---|---|---|---|
| Grounding (verbatim excerpts) | B | 86.7% | excerpts found verbatim in cited source |
| Extraction coverage | A | 100.0% | A-grade docs adequately covered |
| Garbled-source exposure | A | 0.0% | share of nodes from Grade-C/D sources (lower=better) |
| Structure / connectivity | C | 52.8% | nodes with degree >= 2 |
| Dedup cleanliness | D | 72.0% | nodes not in a duplicate-label cluster |
| Enrichment coverage | A | 100.0% | edges+communities enriched |

## Integrity (graphify diagnose multigraph)
- Result: CLEAN — no dangling/missing/collapsed/self-loop edges

## Layer 2 — Verbatim grounding of enrichment excerpts
- Checkable excerpts: **3680** (of 3680 total)
- Grounded verbatim: **3192** → rate **86.7%**

_Method: each excerpt is normalised (lowercased, punctuation/quotes/dashes and Arabic diacritics stripped, ellipsis/bracket splices tested fragment-by-fragment) and matched as a substring of its cited source. This tests wording, not typography. Ungrounded items concentrate in Grade-B/C Arabic sources where bidi/OCR breakage reorders the source text — i.e. an OCR-fidelity limit, not model hallucination — whereas Grade-A English sources ground at ~90%._

By source grade:
| Grade | Grounded | Checkable | Rate |
|---|---|---|---|
| ? | 3192 | 3680 | 87% |

<details><summary>Ungrounded excerpts (488) — click to expand</summary>

| Node | Source | Grade | Caveat? | Excerpt (truncated) |
|---|---|---|---|---|
| Standards for Systemically Important Payment Systems | SAMA_EN_10175_VER1 |  | yes | the Saudi Arabian Payments Network (mada): ATM services and electronic payment via POS; an |
| E-Commerce Payment Support Companies Handling | SAMA_EN_10245_VER1 |  | yes | إنهاء إجراءات التسوية المالية وإيداع الأموال في الحساب البنكي للتاجر (excluded from suppor |
| SARIE Operating Hours During Ramadan and Eid | SAMA_EN_10398_VER1 |  | yes | أوقات عمل النظام السعودي للتحويلات المالية السريعة خلال شهر رمضان المبارك (SARIE operating |
| ATM Feeding and Cash Transport Hours During Ramadan | SAMA_EN_10399_VER1 |  | yes | أوقات عمل تغذية وصيانة أجهزة الصرف الآلي ونقل الأموال خلال شهر رمضان (ATM feeding/maintena |
| Update of Collection Regulations and Procedures for Individual Customers | SAMA_EN_10400_VER1 |  | yes | الموضوع: تحديث ضوابط وإجراءات التحصيل للعملاء الأفراد (Subject: Update of Collection Regul |
| Update of Collection Regulations and Procedures for Individual Customers (dup) | SAMA_EN_10417_VER1 |  | yes | الموضوع: تحديث ضوابط وإجراءات التحصيل للعملاء الأفراد (identical subject and content) |
| Rules for Issuing and Operating Credit Cards | SAMA_EN_10465_VER1 |  | yes | الاستخدام غير المصرّح به العمليات التي تتم باستخدام بطاقة الائتمان دون موافقة أو تفويض من  |
| Counter-Fraud Fundamental Requirements Guide Circular | SAMA_EN_10529_VER1 |  | yes | يتعين على شركات التمويل وشركات خدمات المدفوعات الالتزام بما ورد فيه (finance companies and |
| Reportable Life Cycle Events | SAMA_EN_10592_VER1 |  | no | List of reportable life cycle events for OTC derivative transactions: New (N)... Modify (M |
| OTC Derivative Life Cycle Events | SAMA_EN_10593_VER1_0 |  | no | List of reportable life cycle events for OTC derivative transactions: New (N)... Modify (M |
| Rotation Shocks (Steepener/Flattener) | SAMA_EN_10621_VER1 |  | no | Rotation shocks... whereby both the long and short rates are shocked... ASsteepener,c = −0 |
| Rotation Shocks (Steepener/Flattener) | SAMA_EN_10621_VER1 |  | no | ASsteepener,c = −0.65·/ASshort,c(tk)/ + 0.9·/ASlong,c(tk)/ |
| Alert Handling and Escalation | SAMA_EN_10667_VER1 |  | no | الفصل الخامس: التعامل مع التنبيهات وتصعيدها |
| Targeted Financial Sanctions Rules | SAMA_EN_10667_VER1 |  | no | وتشمل إجراءات تجميد الأصول وعمليات الحظر ... لصالح الأشخاص والكيانات المدرجة أسماؤهم |
| Targeted Financial Sanctions Rules | SAMA_EN_10667_VER1 |  | no | تهدف لوضع الحد الأدنى من الالتزامات ذات الصلة بتطبيق العقوبات المالية المستهدفة ... وتُطبق |
| Financial Institutions Services Tariff Guide | SAMA_EN_10681_VER1 |  | no | مرافق لكم دليل تعرفة خدمات المؤسسات المالية ... الالتزام ... عند فرض رسوم مقابل الخدمات وا |
| Consumer Finance Controls | SAMA_EN_10681_VER1 |  | yes | المادة (4) من ضوابط التمويل الاستهلاكي المحدثة بموجب التعميم رقم ... |
| Implementing Regulation of Finance Companies Control Law | SAMA_EN_10698_VER1 |  | yes | شركة الدفع الآجل: الشركة الحاصلة على ترخيص لممارسة نشاط الدفع الآجل ... شركة التمويل متناه |
| Exposure Limits | SAMA_EN_10698_VER1 |  | yes | التعرض الكبير: التعرض لمستفيد واحد بنسبة (..) أو أكثر من رأس مال شركة التمويل المدفوع واحت |
| Implementing Regulation of Finance Companies Control Law | SAMA_EN_10698_VER1 |  | yes | عقد التمويل: عقد يُمنح بمقتضاه الائتمان للأنشطة المنصوص عليها في النظام واللائحة |
| Financing Policies and Procedures | SAMA_EN_10698_VER1 |  | yes | النشاط أو الأنشطة التمويلية: نوع أو أكثر من أنواع التمويل المنصوص عليها في المادة العاشرة  |
| Finance Company Licensing Requirements | SAMA_EN_10698_VER1 |  | no | شركة الدفع الآجل: الشركة الحاصلة على ترخيص لممارسة نشاط الدفع الآجل دون غيره من الأنشطة ال |
| Implementing Regulation of Finance Companies Control Law | SAMA_EN_10698_VER1 |  | no | الإدارة العليا: ... والمسؤولون عن وظائف إدارة المخاطر والمراجعة الداخلية والالتزام في شركة |
| Risk Management | SAMA_EN_10698_VER1 |  | no | التعرض: قيمة الأصل المعرض لأي مخاطر ائتمانية. مثل مخاطر عدم السداد أو انخفاض التصنيف الائت |
| Finance Contract Requirements | SAMA_EN_10698_VER1 |  | yes | عقد التمويل: عقد يُمنح بمقتضاه الائتمان للأنشطة المنصوص عليها في النظام واللائحة |
| Annual Percentage Rate Formula | SAMA_EN_10698_VER1 |  | no | معدل النسبة السنوي: معدل الخصم محسوباً وفق أحكام المادة الخامسة والثمانون من هذه اللائحة |
| Rules for Licensing Finance Support Activities | SAMA_EN_10721_VER1 |  | no | يقصد بالألفاظ والعبارات الواردة في هذه القواعد المعاني المبيّنة لها في نظام مراقبة شركات ا |
| Implementing Regulations of the Finance Companies Control Law | SAMA_EN_10831_VER1 |  | yes | شركة الدفع الآجل: الشركة الحاصلة على ترخيص لممارسة نشاط الدفع الآجل دون غيره من الأنشطة ال |
| Implementing Regulations of the Finance Companies Control Law | SAMA_EN_10831_VER1 |  | no | التعديلات الواردة على اللائحة التنفيذية لنظام مراقبة شركات التمويل ... وقواعد الترخيص للنش |
| Implementing Regulations of the Finance Companies Control Law | SAMA_EN_10831_VER1 |  | yes | الإدارة العليا ... والمسؤولون عن وظائف إدارة المخاطر والمراجعة الداخلية والالتزام في شركة  |
| Circular on Outsourcing Debt Collection Operations | SAMA_EN_10866_VER1 |  | no | يكون إسناد عمليات تحصيل ديون البنوك والمصارف وشركات التمويل ... بعد الحصول على خطاب عدم مم |
| Circular on Outsourcing Debt Collection Operations | SAMA_EN_10866_VER1 |  | yes | on contracting with a party carrying out debt collection activity without requiring it to  |
| Raising BNPL Financing Ceiling | SAMA_EN_10888_VER1 |  | yes | رفع الحد الأعلى ... ليصبح بما لا يتجاوز مبلغ (10,000) عشرة آلاف ريال |
| Business Risk Assessment Guide for ML/TF/PF | SAMA_EN_10911_VER1 |  | yes | كافة المؤسسات المالية الخاضعة لرقابة وإشراف البنك المركزي السعودي |
| Technical Integration with Waathiq Beneficial Owner Verification Service | SAMA_EN_10959_VER1 |  | yes | reference to the AML Law issued by Royal Decree M/20 and its Implementing Regulation, as b |
| Beneficial Owner Verification | SAMA_EN_10959_VER1 |  | yes | Technical integration with the 'Waathiq' service to verify the identity of the beneficial  |
| Technical Integration with Waathiq Beneficial Owner Verification Service | SAMA_EN_10959_VER1 |  | yes | where a beneficial owner is undisclosed or information differs, the FI applies its own due |
| Technical Integration with Waathiq Beneficial Owner Verification Service | SAMA_EN_10959_VER1 |  | yes | reference to the SAMA Central Bank Law issued by Royal Decree M/36 and SAMA's competence t |
| Technical Integration with Waathiq Beneficial Owner Verification Service | SAMA_EN_10959_VER1 |  | yes | integration with the 'Waathiq' service for beneficial-owner verification of companies; not |
| Beneficial Owner Verification | SAMA_EN_10959_VER1 |  | yes | الربط التقني مع خدمة 'وثاق' للتحقق من هوية المستفيد الحقيقي (source Arabic is OCR-garbled; |
| Saudi Real Estate Refinance Company | SAMA_EN_10971_VER1 |  | no | استثناء المحافظ العقارية المباعة لصالح الشركة السعودية لإعادة التمويل العقاري من متطلب الح |
| Anti-Money Laundering Law | SAMA_EN_11005_VER1 |  | yes | نظام مكافحة غسل الأموال الصادر بالمرسوم الملكي رقم (م/٢٠) ... التزامات على المؤسسات المالي |
| Beneficial Owner Inquiry Service for Nonprofits | SAMA_EN_11005_VER1 |  | yes | وفي حال وجود مستفيد حقيقي غير مفصح عنه ... على المؤسسة المالية اتخاذ تدابير العناية الواجب |
| Responsible Retail Financing Principles | SAMA_EN_11009_VER1 |  | no | نظام مراقبة شركات التمويل الصادر بالمرسوم الملكي رقم م/51 وتاريخ 1433/8/13ه ولائحته التنفي |
| Responsible Retail Financing Principles | SAMA_EN_11009_VER1 |  | no | نظام التمويل العقاري الصادر بالمرسوم الملكي رقم م/50 وتاريخ 1433/8/13ه ولائحته التنفيذية |
| Digital Brokerage Activity Instructions | SAMA_EN_11010_VER1 |  | no | أصدر البنك المركزي هذه التعليمات استنادًا للصلاحيات المخولة له بموجب نظام مراقبة شركات الت |
| Real Estate Refinance Companies Regulation Rules | SAMA_EN_11011_VER1 |  | no | تخضع شركة إعادة التمويل العقاري لإشراف ورقابة البنك المركزي وفقاً ... ونظام مراقبة شركات ا |
| Real Estate Refinance Companies Regulation Rules | SAMA_EN_11011_VER1 |  | no | تخضع شركة إعادة التمويل العقاري لإشراف ورقابة البنك المركزي ... وما يصدره البنك المركزي من |
| Advertising Controls for Financial Products and Services | SAMA_EN_11015_VER1 |  | no | حماية عملاء المؤسسات المالية وتعزيز مبدأ الإفصاح والشفافية |
| Outsourcing Rules for Finance Companies | SAMA_EN_11017_VER1 |  | yes | إشارةً إلى الصلاحيات الممنوحة ... بموجب نظام مراقبة شركات التمويل الصادر بالمرسوم الملكي ر |
| Outsourcing to External Service Providers | SAMA_EN_11017_VER1 |  | no | إسناد مهام إلى مقدم خدمات خارجي: أي عقد أو اتفاق يتعهد بموجبه مقدم خدمة خارجي بتقديم مهام  |
| Outsourcing Rules for Finance Companies | SAMA_EN_11017_VER1 |  | no | قواعد إسناد المهام الخاصة بشركات التمويل الصادرة بموجب تعميم البنك المركزي رقم (…) |
| Outsourcing to External Service Providers | SAMA_EN_11017_VER1 |  | yes | على شركة التمويل إعداد سياسة مكتوبة تنظم إسناد المهام … ويتم اعتمادها من مجلس الإدارة وتحد |
| SAMA Central Bank Law (Royal Decree M/36) | SAMA_EN_11021_VER1 |  | yes | استناداً إلى الصلاحيات المنوطة به بموجب نظامه الصادر بالمرسوم الملكي رقم (م/٣٦) |
| SAMA Central Bank Law (Royal Decree M/36) | SAMA_EN_11021_VER1 |  | yes | استناداً إلى الصلاحيات المنوطة به بموجب [النظام] الصادر بالمرسوم الملكي (governing authori |
| SAMA Central Bank Law (Royal Decree M/36) | SAMA_EN_11021_VER1 |  | yes | واستناداً إلى الصلاحيات المنوطة به بموجب [النظام] الصادر بالمرسوم الملكي رقم (م/36) |
| SAMA Central Bank Law (Royal Decree M/36) | SAMA_EN_11021_VER1 |  | no | واستناداً إلى الصلاحيات المنوطة به بموجب نظامه الصادر بالمرسوم الملكي رقم (م/36) |
| Instructions for Financiers Dealing with Promissory Notes | SAMA_EN_11022_VER1 |  | no | في حال إسناد مهام التنفيذ على السند لأمر لطرف ثالث، على جهة التمويل الالتزام بما ورد في تع |
| Instructions for Financiers Dealing with Promissory Notes | SAMA_EN_11022_VER1 |  | yes | ونظام مراقبة شركات التمويل الصادر بالمرسوم الملكي رقم (م/51) وتاريخ … |
| CCTV Specifications for Financial Sector | SAMA_EN_11037_VER1 |  | no | The following specifications shall be used to define surveillance objectives for CCTV equi |
| CCTV Surveillance Objectives (Identification/Recognition/Detection) | SAMA_EN_11037_VER1 |  | no | Full coverage of cash counters — Identification; Full coverage of parking areas — Detectio |
| Red Teaming Regulatory Framework Circular | SAMA_EN_11039_VER1 |  | yes | SAMA will conduct periodic tests applying the framework; financial entities must independe |
| Cyber Security Framework | SAMA_EN_11039_VER1 |  | yes | وفق متطلبات الدليل التنظيمي لأمن المعلومات (Cyber Security Framework) |
| Red Teaming Regulatory Framework Circular | SAMA_EN_11039_VER1 |  | yes | SAMA adopts the regulatory framework for simulating cyber-attack scenarios (Financial Enti |
| Compliance Principles for Finance Companies | SAMA_EN_11043_VER1 |  | no | لا تخل هذه المبادئ بالمتطلبات ... الأخرى ذات العلاقة ... مبادئ السلوك وأخلاقيات العمل في ا |
| Internal Audit Principles for Finance Companies | SAMA_EN_11044_VER1 |  | yes | وظيفة المراجعة الداخلية / نشاط ... مستقل يقدم تأكيدات وخدمات استشارية موضوعية ومستقلة عن ج |
| Internal Audit Principles for Finance Companies | SAMA_EN_11044_VER1 |  | no | وظيفة المراجعة الداخلية / نشاط ... مستقل يقدم تأكيدات وخدمات استشارية موضوعية ومستقلة عن ج |
| Internal Audit Principles for Finance Companies | SAMA_EN_11044_VER1 |  | yes | internal audit function: an independent activity providing objective assurance on the qual |
| Internal Audit Principles for Finance Companies | SAMA_EN_11044_VER1 |  | yes | issued under the powers granted by the Finance Companies Control Law issued by Royal Decre |
| Shariah Governance Instructions for Finance Companies | SAMA_EN_11045_VER1 |  | yes | يُعد التزام شركة التمويل بممارسة أعمال التمويل بما لا يتعارض مع أحكام الشريعة الإسلامية أح |
| Shariah Governance Instructions for Finance Companies | SAMA_EN_11045_VER1 |  | yes | issued these instructions under the powers vested by the Finance Companies Control Law iss |
| IT Governance Framework | SAMA_EN_11051_VER1 |  | yes | To ensure IT risks are properly managed throughout the Member Organizations. |
| SAMA Business Continuity Management Framework | SAMA_EN_11051_VER1 |  | yes | SAMA Business Continuity Management Framework (distinct mandated framework referenced as a |
| SAMA Cyber Security Framework | SAMA_EN_11051_VER1 |  | yes | SAMA Cyber Security Framework (separate SAMA-mandated framework addressing cyber risk) |
| Finance Lease Law | SAMA_EN_11067_VER1 |  | no | استنادًا إلى الصلاحيات المنوطة بالبنك المركزي بموجب نظام الإيجار التمويلي الصادر بالمرسوم  |
| Cash Withdrawal Transaction Stream | SAMA_EN_11076_VER1 |  | no | there will be two separate transactions for Cash Withdrawal: (1) ... 'Cash Withdrawal' ... |
| Contract Registration Controls | SAMA_EN_11079_VER1_1 |  | yes | Terms in these Controls carry the meanings assigned in the Finance Lease Law and its Imple |
| Finance Lease Law and Implementing Regulation | SAMA_EN_11079_VER1_1 |  | yes | issued pursuant to the Finance Lease Law (Royal Decree M/48) and Article 30 of its Impleme |
| Loan Classification and Provisioning | SAMA_EN_11081_VER1 |  | yes | Where the impairment charges computed under International Financial Reporting Standards (I |
| Appendix B: Liquidity Statement | SAMA_EN_11081_VER1 |  | yes | The deposit liabilities of a DTFC shall not exceed 15 times its total capital... within on |
| Inactive and Dormant Accounts | SAMA_EN_11081_VER1 |  | no | If a General Account completes an one year period with no movement... must consider such G |
| Bank Accounts for Non-Resident Real Estate Owners | SAMA_EN_11101_VER1 |  | yes | opening bank accounts for the category of non-resident customers covered by the Non-Saudi  |
| Beneficial Owner Data Verification (Awqaf) | SAMA_EN_11104_VER1 |  | yes | the General Authority for Awqaf has made available a number of channels enabling financial |
| Beneficial Owner Data Verification (Awqaf) | SAMA_EN_11104_VER1 |  | yes | obligations on financial institutions to apply due diligence measures, particularly relati |
| Banking Control Law | SAMA_EN_1429_VER1 |  | yes | Implementation Rules for Banking Control Law ... Article (12) regarding appointment to boa |
| Licensing of Payment Service Providers | SAMA_EN_1430_VER1 |  | yes | إصدار اللائحة التنفيذية لنظام المدفوعات وخدماتها (issuance of the Implementing Regulation  |
| Implementing Regulation for Payments Law (SAMA 1430) | SAMA_EN_1430_VER1 |  | no | النظام: نظام المدفوعات وخدماتها، الصادر بالمرسوم الملكي رقم (م/26) |
| Implementing Regulation for Payments Law (SAMA 1430) | SAMA_EN_1430_VER1 |  | no | ويؤكد البنك المركزي على مقدمي خدمات المدفوعات ومشغلي نظم المدفوعات الخاضعين للنظام واللائح |
| Payment Systems Classification | SAMA_EN_1430_VER1 |  | no | الفصل الأول - تصنيف نُظم المدفوعات المهمة ... الفصل الثاني -متطلبات مبادئ البنى التحتية لل |
| Payment Systems Classification | SAMA_EN_1430_VER1 |  | no | الفصل الأول - تصنيف نُظم المدفوعات المهمة |
| Credit Information Law | SAMA_EN_1608_VER1 |  | no | إتاحة الوصول إلى السجلات أو المعلومات الائتمانية للمستهلكين ... إلا بعد استيفاء نسخة من ال |
| Credit Information Law | SAMA_EN_1608_VER1 |  | yes | أن يتضمن نشاط شركة التقنية المالية الذي تسعى لمزاولته دخولها في علاقة ائتمانية مع المستهلك |
| Model Consumer Finance Contract (SAMA 1611) | SAMA_EN_1611_VER1 |  | yes | sama_en_1611_ver1.pdf (no substantive text available in context) |
| Model Consumer Finance Contract (SAMA 1611) | SAMA_EN_1611_VER1 |  | yes | الصيغة النموذجية لعقد التمويل الاستهلاكي للأفراد ... تلتزم جهات التمويل كافة الالتزام بها |
| Annual Percentage Rate (APR) | SAMA_EN_1611_VER1 |  | no | معدل النسبة السنوي (APR) معدل الخصم الذي تكون فيه القيمة الحالية لجميع الأقساط ... محسوبًا |
| Model Consumer Finance Contract (SAMA 1611) | SAMA_EN_1611_VER1 |  | yes | which all financiers must comply with ... and not enter into any contracts contradicting i |
| Consumer Protection Principles | SAMA_EN_1611_VER1 |  | yes | من جهود البنك المركزي المستمرة لحماية عملاء المؤسسات المالية وتعزيز عدالة التعاملات في الق |
| Model Consumer Finance Contract (SAMA 1611) | SAMA_EN_1611_VER1 |  | yes | أحكام السداد المبكر المادة (10) (Early repayment provisions — Article 10, in the finance s |
| Early Repayment Provisions | SAMA_EN_1611_VER1 |  | yes | المادة (10): أحكام السداد المبكر (Article 10: Early Repayment Provisions, table of content |
| Model Consumer Finance Contract (SAMA 1611) | SAMA_EN_1611_VER1 |  | yes | licensed under ... and subject to the control and supervision of the Saudi Central Bank (ا |
| Finance Companies Control Law | SAMA_EN_1611_VER1 |  | yes | شركات التمويل العاملة في المملكة (finance companies operating in the Kingdom — distributio |
| Government Entity Account Rules | SAMA_EN_1644_VER1 |  | no | Signatories of the accounts of Saudi government entities and agencies shall be Saudis only |
| SAMA (Saudi Central Bank) | SAMA_EN_1644_VER1 |  | no | Rules for Bank Accounts ... refer to SAMA's website for the last updated and amended versi |
| Collection Controls for Individual Customers Circular | SAMA_EN_1652_VER1 |  | yes | The finance company bears responsibility for verifying external service providers' complia |
| Real Estate Financier Obligations Circular | SAMA_EN_1657_VER1 |  | yes | The real estate financier is not exempted from performing its obligations upon transferrin |
| Record Keeping | SAMA_EN_1704_VER1 |  | no | The financial institution shall keep records for a period of no less than ten years from t |
| Regulations for Foreign Banks Branches (FBB) | SAMA_EN_1713_VER1 |  | no | SAMA considers retail banking activities to be significant where an FBB: Has more than SAR |
| RWA and Funding Report (Attachment D) | SAMA_EN_1713_VER1 |  | yes | Net cash outflows ... Total retail deposits ... Total unsecured wholesale funding (Attachm |
| Banking Control Law | SAMA_EN_1734_VER1 |  | yes | Banking Control Law, issued by Royal Decree No. M/5 dated 22/02/1386H. |
| Banking Agent | SAMA_EN_1734_VER1 |  | no | The Agent shall apply for and receive necessary approval from the relevant supervisory and |
| Regulation of Agent Banking in KSA | SAMA_EN_1734_VER1 |  | no | The Regulation is issued pursuant to powers granted to SAMA under the following laws and r |
| Banking Agent | SAMA_EN_1734_VER1 |  | no | Exclusive Agent: an Agent that entered into an agency agreement with one Bank to exclusive |
| Banking Agent | SAMA_EN_1734_VER1 |  | no | Description of processes for customer due diligence, including KYC and compliance with AML |
| Implementing Regulation of the Real Estate Finance Law | SAMA_EN_190_VER1 |  | yes | Provide stability and growth in the secondary market for real estate finance; Provide liqu |
| Compliance Certification Requirement for Finance Company Compliance Managers | SAMA_EN_2125_VER1 |  | yes | compliance managers in finance companies must obtain the 'Compliance for the Finance Compa |
| Head of Counter-Fraud | SAMA_EN_2217_VER1 |  | no | The Head of Counter-Fraud should be accountable for: Developing, implementing, and maintai |
| Authentication Standard | SAMA_EN_2217_VER1 |  | no | Member Organisations should take note of the following Control Requirements outlined in Th |
| Guidelines for Applying for Debt-Based Crowdfunding Licensing | SAMA_EN_2348_VER1 |  | no | SAMA's Fit and Proper Form for each founding member ... and for each candidate member in t |
| Third-Party Service Provider | SAMA_EN_2389_VER1 |  | no | An entity undertaking the outsourced activity on behalf of the Banks. (Head Offices and Re |
| Rules for Engaging in Debt-Based Crowdfunding | SAMA_EN_2675_VER1_0 |  | yes | All candidates for supervisory and executive positions ... must meet the professional elig |
| Basel III: The Liquidity Coverage Ratio and Liquidity Monitoring Tools Jan 2013 | SAMA_EN_2788_VER1 |  | no | (Refer to footnotes 19 and 20 of Basel III: The Liquidity Coverage Ratio and liquidity ris |
| Liquidity Coverage Ratio | SAMA_EN_2788_VER1 |  | no | (Refer to footnotes 19 and 20 of Basel III: The Liquidity Coverage Ratio and liquidity ris |
| Alternative Liquidity Approaches (ALA) | SAMA_EN_2788_VER1 |  | no | To qualify for the alternative treatment, a jurisdiction should be able to demonstrate tha |
| Liquidity Coverage Ratio | SAMA_EN_2788_VER1 |  | no | (Refer to footnotes 19 and 20 of Basel III: The Liquidity Coverage Ratio and liquidity ris |
| Internal Capital Adequacy Assessment Plan (ICAAP) | SAMA_EN_2797_VER1 |  | no | an important purpose of the ICAAP document is for senior management to inform the Board of |
| Financial Awareness and Education Unit | SAMA_EN_2864_VER1 |  | yes | the Department must consist of at least three units ... including the awareness and financ |
| Customer Care Department (Bank) | SAMA_EN_2864_VER1 |  | yes | enhancing financial education and awareness for them by the bank (paraphrase of consumer-p |
| Complaints Handling Unit | SAMA_EN_2864_VER1 |  | yes | replaces the previously referenced controls on handling and establishing complaints units  |
| Customer Care Department (Bank) | SAMA_EN_2864_VER1 |  | yes | the Department must comprise at minimum a complaints handling unit ... reporting to the mo |
| Customer Care Department (Bank) | SAMA_EN_2864_VER1 |  | yes | حصولهم كحد أدنى على الشهادة المهنية في أساسيات مصرفية الأفراد والشهادة المهنية للمستشار ال |
| Credit Advisor Professional Certificate | SAMA_EN_2885_VER1 |  | no | الموظفون الملزمون بالحصول على الشهادة المهنية للمستشار الائتماني: موظفو البنوك والمصارف وش |
| Professional Certificates Requirement | SAMA_EN_2885_VER1 |  | no | الموضوع: تأكيد الاستمرار في تحقيق متطلب الحصول على الشهادات المهنية |
| Cyber Kill Chain Methodology | SAMA_EN_2898_VER1 |  | no | The Cyber Kill Chain provides a conceptual model to describe an attack... seven (7) stages |
| Cyber Kill Chain Methodology | SAMA_EN_2898_VER1 |  | no | The Cyber Kill Chain provides a conceptual model to describe an attack. The term "chain" r |
| Real Estate Financing Contract Subjection Circular | SAMA_EN_3080_VER1 |  | yes | Confirms real estate financing contracts concluded between the real estate financier and i |
| Acceptance of Family Record from Absher and Tawakkalna | SAMA_EN_3244_VER1 |  | yes | Follow-on to circular... on acceptance of digital identity from Absher and Tawakkalna; all |
| Real Estate Debt Transfer Time Periods Circular | SAMA_EN_3245_VER1 |  | yes | Refers to circular no. 410545379 dated 1441 concerning the subjection of real estate finan |
| Loans to Deposits Ratio (LDR) | SAMA_EN_3343_VER1 |  | no | net loans divided by deposits after applying weights: Net loans / LDR Weighted Deposits |
| Acceptance of Digital ID from Absher and Tawakkalna | SAMA_EN_3365_VER1_0 |  | yes | Subject: Acceptance of digital identity from Absher platform and Tawakkalna application; f |
| Banks Investment Rules | SAMA_EN_3366_VER1 |  | no | These Rules are issued in accordance with the authority vested in SAMA under the Central B |
| Central Bank Law | SAMA_EN_3366_VER1 |  | yes | استناداً إلى نظام البنك المركزي السعودي الصادر بالمرسوم الملكي رقم (م/36) |
| Level 1 Assets | SAMA_EN_3417_VER1 |  | no | A)a) Level 1 assets — Coins and banknotes currently held by the bank that are immediately  |
| Available Stable Funding (ASF) | SAMA_EN_3467_VER1 |  | no | Stable non-maturity (demand) deposits and term deposits with residual maturity of less tha |
| BCBS NSFR Document Oct 2014 | SAMA_EN_3467_VER1 |  | no | based on the BCBS document entitled "Basel III: The Net Stable Funding Ratio" of October 2 |
| Net Stable Funding Ratio (NSFR) | SAMA_EN_3467_VER1 |  | no | The first is to promote the short-term resilience of a bank's liquidity risk profile... kn |
| Available Stable Funding (ASF) | SAMA_EN_3467_VER1 |  | no | NSFR derivative liabilities net of NSFR derivative assets if NSFR derivative li[abilities] |
| NSFR Derivative Assets | SAMA_EN_3467_VER1 |  | no | In calculating NSFR derivative assets, collateral received in connection with derivative c |
| Basel II Circular BCS 290 (June 2006) | SAMA_EN_3487_VER1 |  | no | Circular No.BCS290 dated June 2006, all local banks were required to apply the SAMA's Base |
| Credit Risk Mitigation (CRM) | SAMA_EN_3487_VER1 |  | no | Credit risk mitigation: Table CRC - Qualitative disclosure related to credit risk mitigati |
| Template CR4 - Standardised Approach Credit Risk Exposure and CRM | SAMA_EN_3487_VER1 |  | no | Template CR4 - Standardised Approach Credit Risk Exposure and CRM |
| IRB Approach | SAMA_EN_3487_VER1 |  | no | RWA for modelled approaches that banks have SAMA approval to use... subject to the credit  |
| IRB Approach | SAMA_EN_3487_VER1 |  | yes | subject to the credit risk IRB approaches (F-IRB, A-IRB and supervisory slotting approache |
| Look-Through Approach (LTA) | SAMA_EN_3487_VER1 |  | yes | A look-through approach must always be used for indices... banks must apply a look-through |
| External Credit Assessment Institution (ECAI) | SAMA_EN_3487_VER1 |  | no | an eligible credit assessment... must be publicly available, on a non-selective basis and  |
| Credit Risk Mitigation (CRM) | SAMA_EN_3487_VER1 |  | no | Credit risk mitigation: Table CRC - Qualitative disclosure related to credit risk mitigati |
| Supervisory Haircuts (Table 14) | SAMA_EN_3487_VER1 |  | yes | paraphrase: supervisory collateral haircuts applied under the comprehensive approach, scal |
| Exposure at Default (EAD) | SAMA_EN_3487_VER1 |  | yes | paraphrase: exposure at default is the exposure amount fed into the credit/counterparty-cr |
| IRB Risk Components (PD, LGD, EAD, M) | SAMA_EN_3487_VER1 |  | yes | IRB Risk Components (PD, LGD, EAD, M) |
| IRB Risk Components (PD, LGD, EAD, M) | SAMA_EN_3487_VER1 |  | no | IRB Risk Components (PD, LGD, EAD, M) |
| IRB Risk Components (PD, LGD, EAD, M) | SAMA_EN_3487_VER1 |  | no | IRB Risk Components (PD, LGD, EAD, M) |
| Qualifying Revolving Retail Exposures (QRRE) | SAMA_EN_3487_VER1 |  | no | three sub-classes of exposures: (1) Residential mortgage loans... (2) Qualifying revolving |
| Retail Exposures | SAMA_EN_3487_VER1 |  | no | the retail exposure class consists of the follow three sets of exposures: 'Regulatory reta |
| Saudi Central Bank (SAMA) | SAMA_EN_3487_VER1 |  | no | all local banks were required to apply the SAMA's Basel requirements on a standalone and c |
| PD Estimation Requirements | SAMA_EN_3487_VER1 |  | yes | all banks using the IRB approaches must estimate a PD for each internal borrower grade |
| Recognition of Leasing | SAMA_EN_3487_VER1 |  | no | Leasing activity meets or exceeds projections. The project should achieve stabilisation in |
| Counterparty Credit Risk (CCR) | SAMA_EN_3487_VER1 |  | yes | banks must calculate their counterparty credit risk exposure, or exposure at default (EAD) |
| Internal Risk Transfer | SAMA_EN_3487_VER1 |  | no | A banking book short credit position or ... short equity position created by an internal r |
| Interest Rate Risk (Simplified SA) | SAMA_EN_3487_VER1 |  | no | Risk class: general interest rate risk, credit spread risk (non-securitisation)... FX risk |
| Simplified Approach for Options | SAMA_EN_3487_VER1 |  | no | Simplified approach: capital requirements ... the sum of specific and general market risk  |
| Supervisory Delta Adjustment | SAMA_EN_3487_VER1 |  | yes | The supervisory delta adjustment (α_i) parameters are also defined at the trade level and  |
| Business Indicator (BI) | SAMA_EN_3487_VER1 |  | no | the Business Indicator (BI) — a financial-statement-based proxy for operational risk |
| Business Indicator Component (BIC) | SAMA_EN_3487_VER1 |  | no | the Business Indicator Component (BIC) — calculated by multiplying the BI by a set of regu |
| Internal Loss Multiplier (ILM) | SAMA_EN_3487_VER1 |  | no | Details of operational risk capital calculation ... Are losses used to calculate the ILM ( |
| Effective Expected Positive Exposure (Effective EPE) | SAMA_EN_3487_VER1 |  | yes | Effective Expected Positive Exposure (concept associated with counterparty credit risk exp |
| Exposure at Default (EAD) | SAMA_EN_3487_VER1 |  | no | alpha = 1.4 ... EAD = alpha * (RC + PFE) |
| Replacement Cost (RC) | SAMA_EN_3487_VER1 |  | no | the formulation of replacement cost for margined trades, as set out in 6.20: RC = max{V −  |
| Add-on for Foreign Exchange Derivatives | SAMA_EN_3487_VER1 |  | no | The prescribed supervisory factor in the HS foreign exchange derivative asset class is set |
| Effective Notional | SAMA_EN_3487_VER1 |  | no | The effective notional for each trade in the netting set (𝐴𝑖) is calculated using the form |
| Effective Notional | SAMA_EN_3487_VER1 |  | no | For the interest rate add-on, the effective notional for each trade (𝐴𝑖 = 𝑐𝑖 ∗ 𝑀𝐴𝑖 ∗ 𝛼𝑖) . |
| Supervisory Delta Adjustment | SAMA_EN_3487_VER1 |  | no | The supervisory delta adjustment (𝛼𝑖) parameters are... applied to the adjusted notional a |
| CCR in the Trading Book | SAMA_EN_3487_VER1 |  | no | The credit exposure in the banking book is deemed to be hedged for capital requirement pur |
| Minimum Haircut Floors for SFTs | SAMA_EN_3487_VER1 |  | yes | SFTs with central banks are not subject to the haircut floors. Cash-collateralized securit |
| Reduced Version of BA-CVA | SAMA_EN_3487_VER1 |  | yes | The capital requirement for CVA risk under the reduced version of the BA-CVA... where the  |
| Eligible CVA Hedges | SAMA_EN_3487_VER1 |  | no | Eligibility criteria for CVA hedges are specified in 11.17 to 11.19 for the BA-CVA and in  |
| Regulatory Capital | SAMA_EN_3487_VER1 |  | no | CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and an |
| Template CMS1 - Modelled vs Standardised RWA at Risk Level | SAMA_EN_3487_VER1 |  | no | Template CMS1 – Comparison of modelled and standardised RWA at risk level; Template CMS2 – |
| Template SEC1: Securitisation exposures in the banking book | SAMA_EN_3487_VER1 |  | no | all terms used in section 21 are used consistently with the definitions in SCRE18 ... Cove |
| Template IRRBB1: Quantitative information on IRRBB | SAMA_EN_3487_VER1 |  | no | Table IRRBBA... risk management objective and policies; Template IRRBB1 – Quantitative inf |
| Tranche Maturity | SAMA_EN_3502_VER1 |  | yes | tranche maturity (𝑀𝑇) is the tranche’s remaining effective maturity in years... will have  |
| Specialized Lending | SAMA_EN_3502_VER1 |  | no | Exposures described in paragraph 7.41 will be classified in one of the following three sub |
| Land Acquisition Development and Construction Exposures | SAMA_EN_3502_VER1 |  | no | Land ADC exposures refers to loans to companies or SPVs financing any of the land acquisit |
| Eligible Credit Assessment Institution (ECAI) | SAMA_EN_3502_VER1 |  | no | an eligible credit assessment... must be publicly available, on a non-selective basis and  |
| Collateralized Transactions | SAMA_EN_3502_VER1 |  | no | fully or nearly-fully collateralized capital market-driven transactions ... and repo-style |
| Collateralized Transactions | SAMA_EN_3502_VER1 |  | yes | comprising fully or nearly-fully collateralized capital market-driven transactions ... and |
| IRB Approach Overview | SAMA_EN_3502_VER1 |  | no | For each of the asset classes covered under the IRB framework, there are three key element |
| PD Estimation Requirements | SAMA_EN_3502_VER1 |  | no | all IRB banks must produce their own estimates of probability of default (PD) and must adh |
| Risk Quantification | SAMA_EN_3502_VER1 |  | no | Generally, all banks using the IRB approaches must estimate a PD for each internal borrowe |
| SAMA Circular No. 341000015689 (Regulatory Capital Under Basel III) | SAMA_EN_3502_VER1 |  | yes | SAMA Circular No. 341000015689 (Regulatory Capital Under Basel III) |
| Internal Assessment Approach (SEC-IAA) | SAMA_EN_3502_VER1 |  | no | provided that the bank has at least one approved IRB model... to determine the IRB capital |
| KIRB Capital Charge | SAMA_EN_3502_VER1 |  | no | For a mixed pool, KP equals the exposure-weighted average capital charge ... using KSA ... |

</details>

## Layer 1 — Per-document coverage
Median nodes/page across A+B docs: **0.0**

| Source | Nodes | Pages | Nodes/pg | Grade | Flags |
|---|---|---|---|---|---|
| SAMA_EN_3487_VER1 | 292 |  |  |  | bad_source |
| SAMA_EN_3502_VER1 | 133 |  |  |  | bad_source |
| SAMA_EN_4234_VER1 | 79 |  |  |  | bad_source |
| SAMA_EN_3553_VER1 | 57 |  |  |  | bad_source |
| SAMA_EN_4283_VER1 | 46 |  |  |  | bad_source |
| SAMA_EN_1644_VER1 | 41 |  |  |  | bad_source |
| SAMA_EN_5888_VER1 | 40 |  |  |  | bad_source |
| SAMA_EN_3623_VER1 | 34 |  |  |  | bad_source |
| SAMA_EN_3575_VER1 | 29 |  |  |  | bad_source |
| SAMA_EN_2217_VER1 | 28 |  |  |  | bad_source |
| SAMA_EN_5885_VER1 | 27 |  |  |  | bad_source |
| SAMA_EN_9492_VER1 | 23 |  |  |  | bad_source |
| SAMA_EN_11081_VER1 | 20 |  |  |  | bad_source |
| SAMA_EN_1704_VER1 | 20 |  |  |  | bad_source |
| SAMA_EN_11051_VER1 | 19 |  |  |  | bad_source |
| SAMA_EN_3417_VER1 | 19 |  |  |  | bad_source |
| SAMA_EN_3837_VER1 | 17 |  |  |  | bad_source |
| SAMA_EN_8383_VER1 | 17 |  |  |  | bad_source |
| SAMA_EN_6073_VER1 | 15 |  |  |  | bad_source |
| SAMA_EN_2340_VER1 | 14 |  |  |  | bad_source |
| SAMA_EN_2788_VER1 | 14 |  |  |  | bad_source |
| SAMA_EN_11055_VER1 | 13 |  |  |  | bad_source |
| SAMA_EN_1430_VER1 | 13 |  |  |  | bad_source |
| SAMA_EN_2898_VER1 | 13 |  |  |  | bad_source |
| SAMA_EN_3709_VER1 | 13 |  |  |  | bad_source |
| SAMA_EN_1428_VER1 | 12 |  |  |  | bad_source |
| SAMA_EN_1713_VER1 | 12 |  |  |  | bad_source |
| SAMA_EN_3467_VER1 | 11 |  |  |  | bad_source |
| SAMA_EN_9618_VER1 | 11 |  |  |  | bad_source |
| SAMA_EN_10698_VER1 | 10 |  |  |  | bad_source |
| SAMA_EN_3526_VER1 | 10 |  |  |  | bad_source |
| SAMA_EN_4041_VER1 | 10 |  |  |  | bad_source |
| SAMA_EN_5565_VER1 | 10 |  |  |  | bad_source |
| SAMA_EN_10577_VER1 | 9 |  |  |  | bad_source |
| SAMA_EN_3726_VER1 | 9 |  |  |  | bad_source |
| SAMA_EN_4066_VER1 | 9 |  |  |  | bad_source |
| SAMA_EN_4226_VER1 | 9 |  |  |  | bad_source |
| SAMA_EN_8357_VER1 | 9 |  |  |  | bad_source |
| SAMA_EN_10592_VER1 | 8 |  |  |  | bad_source |
| SAMA_EN_10667_VER1 | 8 |  |  |  | bad_source |
| SAMA_EN_1717_VER1 | 8 |  |  |  | bad_source |
| SAMA_EN_2675_VER1_0 | 8 |  |  |  | bad_source |
| SAMA_EN_3689_VER1 | 8 |  |  |  | bad_source |
| SAMA_EN_791_VER1 | 8 |  |  |  | bad_source |
| SAMA_EN_1734_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_1822_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_2274_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_2797_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_3144_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_3366_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_3372_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_5491_VER1 | 7 |  |  |  | bad_source |
| SAMA_EN_10530_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_10593_VER1_0 | 6 |  |  |  | bad_source |
| SAMA_EN_2389_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_2757_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_2888_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_4303_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_5419_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_6324_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_853_VER1 | 6 |  |  |  | bad_source |
| SAMA_EN_10621_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_1611_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_2864_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_2926_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_2948_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_3032_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_3468_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_4376_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_6314_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_7136_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_7908_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_8294_VER1 | 5 |  |  |  | bad_source |
| SAMA_EN_8320_VER1_0 | 5 |  |  |  | bad_source |
| SAMA_EN_11078_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_1195_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_123_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_1429_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_1868_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_2659_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_4736_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_5765_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_6306_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_6398_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_6505_VER1_1 | 4 |  |  |  | bad_source |
| SAMA_EN_6523_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_9451_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_961_VER1 | 4 |  |  |  | bad_source |
| SAMA_EN_10681_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_11039_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_11076_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_1293_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_132_VER1_0 | 3 |  |  |  | bad_source |
| SAMA_EN_1715_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_190_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_1949_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_2327_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_3276_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_3343_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_4878_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5437_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5448_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5525_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5547_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5594_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5840_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_5879_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_6561_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_9068_VER1 | 3 |  |  |  | bad_source |
| SAMA_EN_10575_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_10959_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_10971_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11005_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11015_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11017_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11021_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5028_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5410_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11037_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11067_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_11079_VER1_1 | 2 |  |  |  | bad_source |
| SAMA_EN_11101_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_1272_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_1608_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_1948_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_1989_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_1997_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_2081_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_2348_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_2883_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_2885_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_4843_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5085_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5404_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5425_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5438_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5441_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5452_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5455_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5464_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5467_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5477_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5480_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5513_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5530_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5544_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5636_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5708_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5709_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5838_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_5858_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_7278_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_6738_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_8356_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_8673_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_8684_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_8984_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_9381_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_9538_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_9671_VER1 | 2 |  |  |  | bad_source |
| SAMA_EN_10175_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10211_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10212_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10220_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10227_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1023_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10241_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10244_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10245_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10319_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10320_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10322_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10335_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10356_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10372_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10394_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10395_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10398_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10399_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10400_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10417_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10419_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10426_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10427_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10464_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10465_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10529_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10559_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10623_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10640_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10646_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10647_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10668_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10697_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10721_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1073_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10831_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10832_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10865_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10866_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10888_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10908_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10910_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10911_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10912_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10928_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10941_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10944_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10949_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10950_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10951_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10967_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10969_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_10973_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11008_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11009_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11010_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11011_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11022_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11025_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11026_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11027_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11038_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11043_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11044_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11045_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11065_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_11104_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1648_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1652_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1653_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1654_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1657_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1722_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_1897_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2125_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2572_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2875_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2879_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2880_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_2884_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3080_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3081_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3154_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3165_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3169_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3178_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3193_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3214_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3223_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3243_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3244_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3245_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3246_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3365_VER1_0 | 1 |  |  |  | bad_source |
| SAMA_EN_3490_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3517_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3519_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3521_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_3522_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4128_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4437_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4721_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4725_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4778_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4790_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4809_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4824_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4826_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4827_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4829_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4830_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4833_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4834_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4838_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4897_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4923_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4924_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4926_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4929_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4939_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4949_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4957_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4962_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4969_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4983_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_4987_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5021_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5030_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5031_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5081_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5096_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5379_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5384_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5392_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5393_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5403_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5408_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5409_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5454_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5471_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5473_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5475_VER1_1 | 1 |  |  |  | bad_source |
| SAMA_EN_5476_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5526_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5536_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5630_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5645_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5712_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5783_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5856_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5860_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5863_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5864_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_5866_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_6493_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_6595_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_6713_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_6734_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_6865_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_7355_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8359_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8679_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8722_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8724_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8725_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8726_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8727_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8729_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8731_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_8732_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9660_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9662_VER1_0 | 1 |  |  |  | bad_source |
| SAMA_EN_9663_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9665_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9666_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9667_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9668_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9669_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9670_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9672_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9673_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9799_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_9809_VER1 | 1 |  |  |  | bad_source |
| SAMA_EN_996_VER1 | 1 |  |  |  | bad_source |
| fit and proper form | 1 |  |  |  | bad_source |
| gdbc-000042007671-1442h | 1 |  |  |  | bad_source |
| gdbc-381000095091-1438h | 1 |  |  |  | bad_source |
| sama_en_10528_ver | 1 |  |  |  | bad_source |
| sama_en_10397_ver | 1 |  |  |  | bad_source |
| sama_en_10555_ver | 1 |  |  |  | bad_source |
| sama_en_10556_ver | 1 |  |  |  | bad_source |
| sama_rd 637_en | 1 |  |  |  | bad_source |
| sama_rd m142_en | 1 |  |  |  | bad_source |
| إصدار وتحديث وتجديد معرّف الكيانات القانونية من خلال مؤسسة مالية | 1 |  |  |  | bad_source |
| الدليل الإرشادي لاستخدام نظام البيانات الإشرافية_0 | 1 |  |  |  | bad_source |
| تعديل نظام حماية البيانات الشخصية-م148 | 1 |  |  |  | bad_source |
| قرار وزاري رقم 112203 تاريخ 18 06 1442 | 1 |  |  |  | bad_source |
| النموذج الربعي للعملات وبيانات أكبر العملاء والعملات المزورة وبيانات الموظفين | 1 |  |  |  | bad_source |
| النموذج السنوي للبيانات التنظيمية | 1 |  |  |  | bad_source |
| نموذج البيانات الشهرية للمبيعات والمشتريات | 1 |  |  |  | bad_source |
| نموذج المقارنة للقوائم المالية الربعية و السنوية | 1 |  |  |  | bad_source |
| sama circular no (gdbc-341000107020-1434h)en | 1 |  |  |  | bad_source |
| sama circular no (gdbc-361000009335-1436h) | 1 |  |  |  | bad_source |
| report on total remunerations for the board of directors and committees | 1 |  |  |  | bad_source |

## Garbled-source exposure
- Grade-C/D source stems: none
- Nodes originating from those sources: **0 / 1816** (0.0%)

## Structure & connectivity
- Isolated (0 edges): **152**
- Degree-1 nodes: **705** (39% of graph)
- source_location populated: **0 / 1816**
- Top hubs: Standardized Approach for CCR (SA-CCR) (17), Template OV1: Overview of RWA (14), Standardized Approach (14), Minimum Capital Requirements for Credit Risk (14), Default Risk Capital (DRC) Requirement (14), Business Continuity Management Framework (14)

## Edges
- Confidence: INFERRED=162, EXTRACTED=1683, AMBIGUOUS=3
- Relations: references=1534, conceptually_related_to=162, cites=103, semantically_similar_to=26, shares_data_with=17, implements=6
- Orphan/dangling edges: 0 · self-loops: 0

## Duplicate-label clusters
| norm_label | count | labels (sources) |
|---|---|---|
| finance companies control law | 12 | Finance Companies Control Law [SAMA_EN_1023_VER1]; Finance Companies Control Law [SAMA_EN_11055_VER1]; Finance Companies Control Law [SAMA_EN_11081_VER1]; Finance Companies Control Law [SAMA_EN_1611_VER1]; Finance Companies Control Law [SAMA_EN_1949_VER1]; Finance Companies Control Law [SAMA_EN_2327_VER1]; Finance Companies Control Law [SAMA_EN_5419_VER1]; Finance Companies Control Law [SAMA_EN_5441_VER1]; Finance Companies Control Law [SAMA_EN_5765_VER1]; Finance Companies Control Law [SAMA_EN_5885_VER1]; Finance Companies Control Law [SAMA_EN_8357_VER1]; Finance Companies Control Law [SAMA_EN_9381_VER1] |
| banking control law | 11 | Banking Control Law [SAMA_EN_1429_VER1]; Banking Control Law [SAMA_EN_1713_VER1]; Banking Control Law [SAMA_EN_1734_VER1]; Banking Control Law [SAMA_EN_1868_VER1]; Banking Control Law [SAMA_EN_2340_VER1]; Banking Control Law [SAMA_EN_3366_VER1]; Banking Control Law [SAMA_EN_3575_VER1]; Banking Control Law [SAMA_EN_5437_VER1]; Banking Control Law [SAMA_EN_5491_VER1]; Banking Control Law [SAMA_EN_9671_VER1]; Banking Control Law [SAMA_EN_996_VER1] |
| anti-money laundering law | 7 | Anti-Money Laundering Law [SAMA_EN_10667_VER1]; Anti-Money Laundering Law [SAMA_EN_11005_VER1]; Anti-Money Laundering Law [SAMA_EN_1704_VER1]; Anti-Money Laundering Law [SAMA_EN_3372_VER1]; Anti-Money Laundering Law [SAMA_EN_5565_VER1]; Anti-Money Laundering Law [SAMA_EN_791_VER1]; Anti-Money Laundering Law [SAMA_EN_853_VER1] |
| finance lease law | 5 | Finance Lease Law [SAMA_EN_1073_VER1]; Finance Lease Law [SAMA_EN_11067_VER1]; Finance Lease Law [SAMA_EN_123_VER1]; Finance Lease Law [SAMA_EN_5438_VER1]; Finance Lease Law [SAMA_EN_5885_VER1] |
| real estate finance law | 5 | Real Estate Finance Law [SAMA_EN_5410_VER1]; Real Estate Finance Law [SAMA_EN_1272_VER1]; Real Estate Finance Law [SAMA_EN_190_VER1]; Real Estate Finance Law [SAMA_EN_5452_VER1]; Real Estate Finance Law [SAMA_EN_5885_VER1] |
| sama cyber security framework | 5 | SAMA Cyber Security Framework [SAMA_EN_11051_VER1]; SAMA Cyber Security Framework [SAMA_EN_1868_VER1]; SAMA Cyber Security Framework [SAMA_EN_2898_VER1]; SAMA Cyber Security Framework [SAMA_EN_4066_VER1]; SAMA Cyber Security Framework [SAMA_EN_5888_VER1] |
| implementing regulation of finance companies control law | 4 | Implementing Regulation of Finance Companies Control Law [SAMA_EN_10698_VER1]; Implementing Regulation of Finance Companies Control Law [SAMA_EN_5448_VER1]; Implementing Regulation of Finance Companies Control Law [SAMA_EN_5455_VER1]; Implementing Regulation of Finance Companies Control Law [SAMA_EN_6324_VER1] |
| board of directors | 4 | Board of Directors [SAMA_EN_1293_VER1]; Board of Directors [SAMA_EN_1717_VER1]; Board of Directors [SAMA_EN_2274_VER1]; Board of Directors [SAMA_EN_5888_VER1] |
| saudi central bank (sama) | 4 | Saudi Central Bank (SAMA) [SAMA_EN_2217_VER1]; Saudi Central Bank (SAMA) [SAMA_EN_3487_VER1]; Saudi Central Bank (SAMA) [SAMA_EN_3689_VER1]; Saudi Central Bank (SAMA) [SAMA_EN_4283_VER1] |
| fit and proper form | 4 | Fit and Proper Form [SAMA_EN_2327_VER1]; Fit and Proper Form [SAMA_EN_2348_VER1]; Fit and Proper Form [SAMA_EN_5765_VER1]; Fit and Proper Form [fit and proper form] |
| loss given default (lgd) | 3 | Loss Given Default (LGD) [SAMA_EN_11055_VER1]; Loss Given Default (LGD) [SAMA_EN_3487_VER1]; Loss Given Default (LGD) [SAMA_EN_3553_VER1] |
| regulations for consumer financing | 3 | Regulations for Consumer Financing [SAMA_EN_11078_VER1]; Regulations for Consumer Financing [SAMA_EN_5419_VER1]; Regulations for Consumer Financing [SAMA_EN_5491_VER1] |
| liquidity requirements | 3 | Liquidity Requirements [SAMA_EN_11081_VER1]; Liquidity Requirements [SAMA_EN_1713_VER1]; Liquidity Requirements [SAMA_EN_8383_VER1] |
| saudi central bank law | 3 | Saudi Central Bank Law [SAMA_EN_1293_VER1]; Saudi Central Bank Law [SAMA_EN_1715_VER1]; Saudi Central Bank Law [SAMA_EN_1717_VER1] |
| consumer protection principles | 3 | Consumer Protection Principles [SAMA_EN_1611_VER1]; Consumer Protection Principles [SAMA_EN_1989_VER1]; Consumer Protection Principles [SAMA_EN_5404_VER1] |
| liquidity coverage ratio (lcr) | 3 | Liquidity Coverage Ratio (LCR) [SAMA_EN_1713_VER1]; Liquidity Coverage Ratio (LCR) [SAMA_EN_3467_VER1]; Liquidity Coverage Ratio (LCR) [SAMA_EN_3623_VER1] |
| net stable funding ratio (nsfr) | 3 | Net Stable Funding Ratio (NSFR) [SAMA_EN_1713_VER1]; Net Stable Funding Ratio (NSFR) [SAMA_EN_3467_VER1]; Net Stable Funding Ratio (NSFR) [SAMA_EN_3623_VER1] |
| look-through approach (lta) | 3 | Look-Through Approach (LTA) [SAMA_EN_2340_VER1]; Look-Through Approach (LTA) [SAMA_EN_3487_VER1]; Look-Through Approach (LTA) [SAMA_EN_3502_VER1] |
| level 1 assets | 3 | Level 1 Assets [SAMA_EN_2788_VER1]; Level 1 Assets [SAMA_EN_3417_VER1]; Level 1 Assets [SAMA_EN_3623_VER1] |
| stress testing | 3 | Stress Testing [SAMA_EN_2797_VER1]; Stress Testing [SAMA_EN_4226_VER1]; Stress Testing [SAMA_EN_4283_VER1] |
| exposure at default (ead) | 3 | Exposure at Default (EAD) [SAMA_EN_3487_VER1]; Exposure at Default (EAD) [SAMA_EN_3502_VER1]; Exposure at Default (EAD) [SAMA_EN_4283_VER1] |
| fraud risk assessment | 2 | Fraud Risk Assessment [SAMA_EN_10530_VER1]; Fraud Risk Assessment [SAMA_EN_2217_VER1] |
| credit card issuance and operation rules | 2 | Credit Card Issuance and Operation Rules [SAMA_EN_10575_VER1]; Credit Card Issuance and Operation Rules [sama_en_10528_ver] |
| record keeping | 2 | Record Keeping [SAMA_EN_10667_VER1]; Record Keeping [SAMA_EN_1704_VER1] |
| consumer finance controls | 2 | Consumer Finance Controls [SAMA_EN_10681_VER1]; Consumer Finance Controls [SAMA_EN_6561_VER1] |
| finance companies control law (m/51) | 2 | Finance Companies Control Law (M/51) [SAMA_EN_5028_VER1]; Finance Companies Control Law (M/51) [SAMA_EN_6324_VER1] |
| saudi real estate refinance company | 2 | Saudi Real Estate Refinance Company [SAMA_EN_10971_VER1]; Saudi Real Estate Refinance Company [SAMA_EN_190_VER1] |
| services for persons with disabilities instructions | 2 | Services for Persons with Disabilities Instructions [SAMA_EN_11025_VER1]; Services for Persons with Disabilities Instructions [SAMA_EN_4926_VER1] |
| shariah governance instructions for finance companies | 2 | Shariah Governance Instructions for Finance Companies [SAMA_EN_11045_VER1]; Shariah Governance Instructions for Finance Companies [SAMA_EN_6324_VER1] |
| it governance framework | 2 | IT Governance Framework [SAMA_EN_11051_VER1]; IT Governance Framework [SAMA_EN_2217_VER1] |
| it governance maturity model | 2 | IT Governance Maturity Model [SAMA_EN_11051_VER1]; IT Governance Maturity Model [SAMA_EN_4066_VER1] |
| cyber security framework | 2 | Cyber Security Framework [SAMA_EN_11039_VER1]; Cyber Security Framework [SAMA_EN_2217_VER1] |
| system change management | 2 | System Change Management [SAMA_EN_11051_VER1]; System Change Management [SAMA_EN_4066_VER1] |
| expected credit loss provisioning | 2 | Expected Credit Loss Provisioning [SAMA_EN_11055_VER1]; Expected Credit Loss Provisioning [SAMA_EN_8357_VER1] |
| ifrs 9 | 2 | IFRS 9 [SAMA_EN_11055_VER1]; IFRS 9 [SAMA_EN_8357_VER1] |
| eligible collateral and valuation | 2 | Eligible Collateral and Valuation [SAMA_EN_11055_VER1]; Eligible Collateral and Valuation [SAMA_EN_8357_VER1] |
| rules governing calculation of apr | 2 | Rules Governing Calculation of APR [SAMA_EN_11078_VER1]; Rules Governing Calculation of APR [SAMA_EN_5419_VER1] |
| capital requirements | 2 | Capital Requirements [SAMA_EN_11081_VER1]; Capital Requirements [SAMA_EN_8383_VER1] |
| corporate governance and risk management | 2 | Corporate Governance and Risk Management [SAMA_EN_11081_VER1]; Corporate Governance and Risk Management [SAMA_EN_8383_VER1] |
| know your customer (kyc) | 2 | Know Your Customer (KYC) [SAMA_EN_11081_VER1]; Know Your Customer (KYC) [SAMA_EN_8383_VER1] |
| inactive and dormant accounts | 2 | Inactive and Dormant Accounts [SAMA_EN_11081_VER1]; Inactive and Dormant Accounts [SAMA_EN_8383_VER1] |
| deposit taking finance company (dtfc) | 2 | Deposit Taking Finance Company (DTFC) [SAMA_EN_11081_VER1]; Deposit Taking Finance Company (DTFC) [SAMA_EN_8383_VER1] |
| accounts operating rules | 2 | Accounts Operating Rules [SAMA_EN_11081_VER1]; Accounts Operating Rules [SAMA_EN_8383_VER1] |
| sama (saudi central bank) | 2 | SAMA (Saudi Central Bank) [SAMA_EN_11081_VER1]; SAMA (Saudi Central Bank) [SAMA_EN_1644_VER1] |
| implementing regulation of finance lease law | 2 | Implementing Regulation of Finance Lease Law [SAMA_EN_123_VER1]; Implementing Regulation of Finance Lease Law [SAMA_EN_6398_VER1] |
| credit information law | 2 | Credit Information Law [SAMA_EN_1608_VER1]; Credit Information Law [SAMA_EN_961_VER1] |
| annual percentage rate (apr) | 2 | Annual Percentage Rate (APR) [SAMA_EN_1611_VER1]; Annual Percentage Rate (APR) [SAMA_EN_5885_VER1] |
| financial action task force (fatf) | 2 | Financial Action Task Force (FATF) [SAMA_EN_1704_VER1]; Financial Action Task Force (FATF) [SAMA_EN_1822_VER1] |
| due diligence measures | 2 | Due Diligence Measures [SAMA_EN_1704_VER1]; Due Diligence Measures [SAMA_EN_791_VER1] |
| board of directors responsibilities | 2 | Board of Directors Responsibilities [SAMA_EN_1704_VER1]; Board of Directors Responsibilities [SAMA_EN_6324_VER1] |
| contingency funding plan (cfp) | 2 | Contingency Funding Plan (CFP) [SAMA_EN_1713_VER1]; Contingency Funding Plan (CFP) [SAMA_EN_3144_VER1] |
| executive management | 2 | Executive Management [SAMA_EN_1717_VER1]; Executive Management [SAMA_EN_2274_VER1] |
| nomination and remuneration committee | 2 | Nomination and Remuneration Committee [SAMA_EN_1717_VER1]; Nomination and Remuneration Committee [SAMA_EN_2926_VER1] |
| executive committee | 2 | Executive Committee [SAMA_EN_1717_VER1]; Executive Committee [SAMA_EN_6505_VER1_1] |
| requirements for appointments to senior positions | 2 | Requirements for Appointments to Senior Positions [SAMA_EN_1997_VER1]; Requirements for Appointments to Senior Positions [SAMA_EN_8294_VER1] |
| fit and proper criteria | 2 | Fit and Proper Criteria [SAMA_EN_1997_VER1]; Fit and Proper Criteria [SAMA_EN_8294_VER1] |
| shariah committee | 2 | Shariah Committee [SAMA_EN_2274_VER1]; Shariah Committee [SAMA_EN_6324_VER1] |
| liquidity coverage ratio | 2 | Liquidity Coverage Ratio [SAMA_EN_2788_VER1]; Liquidity Coverage Ratio [SAMA_EN_3417_VER1] |
| high quality liquid assets (hqla) | 2 | High Quality Liquid Assets (HQLA) [SAMA_EN_2788_VER1]; High Quality Liquid Assets (HQLA) [SAMA_EN_3623_VER1] |
| alternative liquidity approaches (ala) | 2 | Alternative Liquidity Approaches (ALA) [SAMA_EN_2788_VER1]; Alternative Liquidity Approaches (ALA) [SAMA_EN_3623_VER1] |
| total net cash outflows | 2 | Total Net Cash Outflows [SAMA_EN_2788_VER1]; Total Net Cash Outflows [SAMA_EN_3623_VER1] |
| retail deposit run-off | 2 | Retail Deposit Run-off [SAMA_EN_2788_VER1]; Retail Deposit Run-off [SAMA_EN_3623_VER1] |
| unsecured wholesale funding run-off | 2 | Unsecured Wholesale Funding Run-off [SAMA_EN_2788_VER1]; Unsecured Wholesale Funding Run-off [SAMA_EN_3623_VER1] |
| secured funding run-off | 2 | Secured Funding Run-off [SAMA_EN_2788_VER1]; Secured Funding Run-off [SAMA_EN_3623_VER1] |
| operational deposits | 2 | Operational Deposits [SAMA_EN_2788_VER1]; Operational Deposits [SAMA_EN_3623_VER1] |
| internal capital adequacy assessment plan (icaap) | 2 | Internal Capital Adequacy Assessment Plan (ICAAP) [SAMA_EN_2797_VER1]; Internal Capital Adequacy Assessment Plan (ICAAP) [SAMA_EN_4226_VER1] |
| basel ii framework | 2 | Basel II Framework [SAMA_EN_2797_VER1]; Basel II Framework [SAMA_EN_3623_VER1] |
| level 2b assets | 2 | Level 2B Assets [SAMA_EN_3417_VER1]; Level 2B Assets [SAMA_EN_3623_VER1] |
| cash outflows | 2 | Cash Outflows [SAMA_EN_3417_VER1]; Cash Outflows [SAMA_EN_3623_VER1] |
| cash inflows | 2 | Cash Inflows [SAMA_EN_3417_VER1]; Cash Inflows [SAMA_EN_3623_VER1] |
| liquidity monitoring tools | 2 | Liquidity Monitoring Tools [SAMA_EN_3417_VER1]; Liquidity Monitoring Tools [SAMA_EN_3623_VER1] |
| contractual maturity mismatch | 2 | Contractual Maturity Mismatch [SAMA_EN_3417_VER1]; Contractual Maturity Mismatch [SAMA_EN_3623_VER1] |
| lcr by significant currency | 2 | LCR by Significant Currency [SAMA_EN_3417_VER1]; LCR by Significant Currency [SAMA_EN_3623_VER1] |
| market-related monitoring tools | 2 | Market-related Monitoring Tools [SAMA_EN_3417_VER1]; Market-related Monitoring Tools [SAMA_EN_3623_VER1] |
| sama basel framework | 2 | SAMA Basel Framework [SAMA_EN_3487_VER1]; SAMA Basel Framework [SAMA_EN_9618_VER1] |
| external credit risk assessment approach (ecra) | 2 | External Credit Risk Assessment Approach (ECRA) [SAMA_EN_3487_VER1]; External Credit Risk Assessment Approach (ECRA) [SAMA_EN_3502_VER1] |
| standardized credit risk assessment approach (scra) | 2 | Standardized Credit Risk Assessment Approach (SCRA) [SAMA_EN_3487_VER1]; Standardized Credit Risk Assessment Approach (SCRA) [SAMA_EN_3502_VER1] |
| real estate exposure class | 2 | Real Estate Exposure Class [SAMA_EN_3487_VER1]; Real Estate Exposure Class [SAMA_EN_3502_VER1] |
| loan-to-value ratio (ltv) | 2 | Loan-to-Value Ratio (LTV) [SAMA_EN_3487_VER1]; Loan-to-Value Ratio (LTV) [SAMA_EN_3502_VER1] |
| master netting agreements for sfts | 2 | Master Netting Agreements for SFTs [SAMA_EN_3487_VER1]; Master Netting Agreements for SFTs [SAMA_EN_3502_VER1] |
| standardized approach for ccr (sa-ccr) | 2 | Standardized Approach for CCR (SA-CCR) [SAMA_EN_3487_VER1]; Standardized Approach for CCR (SA-CCR) [SAMA_EN_4283_VER1] |
| on-balance sheet netting | 2 | On-Balance Sheet Netting [SAMA_EN_3487_VER1]; On-Balance Sheet Netting [SAMA_EN_3502_VER1] |
| irb risk components (pd, lgd, ead, m) | 2 | IRB Risk Components (PD, LGD, EAD, M) [SAMA_EN_3487_VER1]; IRB Risk Components (PD, LGD, EAD, M) [SAMA_EN_3502_VER1] |
| high-volatility commercial real estate (hvcre) | 2 | High-Volatility Commercial Real Estate (HVCRE) [SAMA_EN_3487_VER1]; High-Volatility Commercial Real Estate (HVCRE) [SAMA_EN_3502_VER1] |
| effective maturity (m) | 2 | Effective Maturity (M) [SAMA_EN_3487_VER1]; Effective Maturity (M) [SAMA_EN_3502_VER1] |
| rating system design | 2 | Rating System Design [SAMA_EN_3487_VER1]; Rating System Design [SAMA_EN_3502_VER1] |
| counterparty credit risk (ccr) framework | 2 | Counterparty Credit Risk (CCR) Framework [SAMA_EN_3487_VER1]; Counterparty Credit Risk (CCR) Framework [SAMA_EN_3502_VER1] |
| securitization general provisions | 2 | Securitization General Provisions [SAMA_EN_3487_VER1]; Securitization General Provisions [SAMA_EN_3502_VER1] |
| pd estimation requirements | 2 | PD Estimation Requirements [SAMA_EN_3487_VER1]; PD Estimation Requirements [SAMA_EN_3502_VER1] |
| definition of default | 2 | Definition of Default [SAMA_EN_3487_VER1]; Definition of Default [SAMA_EN_3502_VER1] |
| validation of internal estimates | 2 | Validation of Internal Estimates [SAMA_EN_3487_VER1]; Validation of Internal Estimates [SAMA_EN_3502_VER1] |
| supervisory lgd and ead estimates | 2 | Supervisory LGD and EAD Estimates [SAMA_EN_3487_VER1]; Supervisory LGD and EAD Estimates [SAMA_EN_3502_VER1] |
| commercial and residential real estate collateral | 2 | Commercial and Residential Real Estate Collateral [SAMA_EN_3487_VER1]; Commercial and Residential Real Estate Collateral [SAMA_EN_3502_VER1] |
| other physical collateral | 2 | Other Physical Collateral [SAMA_EN_3487_VER1]; Other Physical Collateral [SAMA_EN_3502_VER1] |
| irb disclosure requirements | 2 | IRB Disclosure Requirements [SAMA_EN_3487_VER1]; IRB Disclosure Requirements [SAMA_EN_3502_VER1] |
| traditional securitization | 2 | Traditional Securitization [SAMA_EN_3487_VER1]; Traditional Securitization [SAMA_EN_3502_VER1] |
| synthetic securitization | 2 | Synthetic Securitization [SAMA_EN_3487_VER1]; Synthetic Securitization [SAMA_EN_3502_VER1] |
| kirb capital charge | 2 | KIRB Capital Charge [SAMA_EN_3487_VER1]; KIRB Capital Charge [SAMA_EN_3502_VER1] |
| ksa capital charge | 2 | KSA Capital Charge [SAMA_EN_3487_VER1]; KSA Capital Charge [SAMA_EN_3502_VER1] |
| caps for securitization exposures | 2 | Caps for Securitization Exposures [SAMA_EN_3487_VER1]; Caps for Securitization Exposures [SAMA_EN_3502_VER1] |
| supervisory parameter p | 2 | Supervisory Parameter p [SAMA_EN_3487_VER1]; Supervisory Parameter p [SAMA_EN_3502_VER1] |
| equity investments in funds | 2 | Equity Investments in Funds [SAMA_EN_3487_VER1]; Equity Investments in Funds [SAMA_EN_3502_VER1] |
| mandate-based approach (mba) | 2 | Mandate-Based Approach (MBA) [SAMA_EN_3487_VER1]; Mandate-Based Approach (MBA) [SAMA_EN_3502_VER1] |
| fall-back approach (fba) | 2 | Fall-Back Approach (FBA) [SAMA_EN_3487_VER1]; Fall-Back Approach (FBA) [SAMA_EN_3502_VER1] |
| counterparty credit risk (ccr) | 2 | Counterparty Credit Risk (CCR) [SAMA_EN_3487_VER1]; Counterparty Credit Risk (CCR) [SAMA_EN_4283_VER1] |
| credit valuation adjustment (cva) | 2 | Credit Valuation Adjustment (CVA) [SAMA_EN_3487_VER1]; Credit Valuation Adjustment (CVA) [SAMA_EN_3553_VER1] |
| internal models approach (ima) | 2 | Internal Models Approach (IMA) [SAMA_EN_3487_VER1]; Internal Models Approach (IMA) [SAMA_EN_3553_VER1] |
| sensitivities-based method | 2 | Sensitivities-Based Method [SAMA_EN_3487_VER1]; Sensitivities-Based Method [SAMA_EN_3553_VER1] |
| residual risk add-on (rrao) | 2 | Residual Risk Add-On (RRAO) [SAMA_EN_3487_VER1]; Residual Risk Add-On (RRAO) [SAMA_EN_3553_VER1] |
| delta risk | 2 | Delta Risk [SAMA_EN_3487_VER1]; Delta Risk [SAMA_EN_3553_VER1] |
| vega risk | 2 | Vega Risk [SAMA_EN_3487_VER1]; Vega Risk [SAMA_EN_3553_VER1] |
| curvature risk | 2 | Curvature Risk [SAMA_EN_3487_VER1]; Curvature Risk [SAMA_EN_3553_VER1] |
| trading desk | 2 | Trading Desk [SAMA_EN_3487_VER1]; Trading Desk [SAMA_EN_3553_VER1] |
| internal risk transfer | 2 | Internal Risk Transfer [SAMA_EN_3487_VER1]; Internal Risk Transfer [SAMA_EN_3553_VER1] |
| correlation trading portfolio (ctp) | 2 | Correlation Trading Portfolio (CTP) [SAMA_EN_3487_VER1]; Correlation Trading Portfolio (CTP) [SAMA_EN_3553_VER1] |
| equity risk | 2 | Equity Risk [SAMA_EN_3487_VER1]; Equity Risk [SAMA_EN_3553_VER1] |
| jump-to-default (jtd) risk | 2 | Jump-to-Default (JTD) Risk [SAMA_EN_3487_VER1]; Jump-to-Default (JTD) Risk [SAMA_EN_3553_VER1] |
| drc for non-securitisations | 2 | DRC for Non-Securitisations [SAMA_EN_3487_VER1]; DRC for Non-Securitisations [SAMA_EN_3553_VER1] |
| drc for securitisations (ctp) | 2 | DRC for Securitisations (CTP) [SAMA_EN_3487_VER1]; DRC for Securitisations (CTP) [SAMA_EN_3553_VER1] |
| hedge benefit ratio (hbr) | 2 | Hedge Benefit Ratio (HBR) [SAMA_EN_3487_VER1]; Hedge Benefit Ratio (HBR) [SAMA_EN_3553_VER1] |
| risk factor eligibility test (rfet) | 2 | Risk Factor Eligibility Test (RFET) [SAMA_EN_3487_VER1]; Risk Factor Eligibility Test (RFET) [SAMA_EN_3553_VER1] |
| non-modellable risk factor (nmrf) | 2 | Non-Modellable Risk Factor (NMRF) [SAMA_EN_3487_VER1]; Non-Modellable Risk Factor (NMRF) [SAMA_EN_3553_VER1] |
| backtesting | 2 | Backtesting [SAMA_EN_3487_VER1]; Backtesting [SAMA_EN_3553_VER1] |
| p&l attribution (pla) test | 2 | P&L Attribution (PLA) Test [SAMA_EN_3487_VER1]; P&L Attribution (PLA) Test [SAMA_EN_3553_VER1] |
| risk-theoretical p&l (rtpl) | 2 | Risk-Theoretical P&L (RTPL) [SAMA_EN_3487_VER1]; Risk-Theoretical P&L (RTPL) [SAMA_EN_3553_VER1] |
| hypothetical p&l (hpl) | 2 | Hypothetical P&L (HPL) [SAMA_EN_3487_VER1]; Hypothetical P&L (HPL) [SAMA_EN_3553_VER1] |
| actual p&l (apl) | 2 | Actual P&L (APL) [SAMA_EN_3487_VER1]; Actual P&L (APL) [SAMA_EN_3553_VER1] |
| spearman correlation metric | 2 | Spearman Correlation Metric [SAMA_EN_3487_VER1]; Spearman Correlation Metric [SAMA_EN_3553_VER1] |
| kolmogorov-smirnov test metric | 2 | Kolmogorov-Smirnov Test Metric [SAMA_EN_3487_VER1]; Kolmogorov-Smirnov Test Metric [SAMA_EN_3553_VER1] |
| stressed expected shortfall (ses) | 2 | Stressed Expected Shortfall (SES) [SAMA_EN_3487_VER1]; Stressed Expected Shortfall (SES) [SAMA_EN_3553_VER1] |
| liquidity horizon | 2 | Liquidity Horizon [SAMA_EN_3487_VER1]; Liquidity Horizon [SAMA_EN_3553_VER1] |
| simplified standardised approach | 2 | Simplified Standardised Approach [SAMA_EN_3487_VER1]; Simplified Standardised Approach [SAMA_EN_3553_VER1] |
| maturity method | 2 | Maturity Method [SAMA_EN_3487_VER1]; Maturity Method [SAMA_EN_3553_VER1] |
| duration method | 2 | Duration Method [SAMA_EN_3487_VER1]; Duration Method [SAMA_EN_3553_VER1] |
| specific risk | 2 | Specific Risk [SAMA_EN_3487_VER1]; Specific Risk [SAMA_EN_3553_VER1] |
| general market risk | 2 | General Market Risk [SAMA_EN_3487_VER1]; General Market Risk [SAMA_EN_3553_VER1] |
| simplified approach for options | 2 | Simplified Approach for Options [SAMA_EN_3487_VER1]; Simplified Approach for Options [SAMA_EN_3553_VER1] |
| delta-plus method | 2 | Delta-plus Method [SAMA_EN_3487_VER1]; Delta-plus Method [SAMA_EN_3553_VER1] |
| scenario approach | 2 | Scenario Approach [SAMA_EN_3487_VER1]; Scenario Approach [SAMA_EN_3553_VER1] |
| gamma risk capital requirement | 2 | Gamma Risk Capital Requirement [SAMA_EN_3487_VER1]; Gamma Risk Capital Requirement [SAMA_EN_3553_VER1] |
| backtesting green/amber/red zones | 2 | Backtesting Green/Amber/Red Zones [SAMA_EN_3487_VER1]; Backtesting Green/Amber/Red Zones [SAMA_EN_3553_VER1] |
| risk factor modellability | 2 | Risk Factor Modellability [SAMA_EN_3487_VER1]; Risk Factor Modellability [SAMA_EN_3553_VER1] |
| minimum capital requirements for operational risk | 2 | Minimum Capital Requirements for Operational Risk [SAMA_EN_3487_VER1]; Minimum Capital Requirements for Operational Risk [SAMA_EN_4041_VER1] |
| business indicator (bi) | 2 | Business Indicator (BI) [SAMA_EN_3487_VER1]; Business Indicator (BI) [SAMA_EN_4041_VER1] |
| business indicator component (bic) | 2 | Business Indicator Component (BIC) [SAMA_EN_3487_VER1]; Business Indicator Component (BIC) [SAMA_EN_4041_VER1] |
| internal loss multiplier (ilm) | 2 | Internal Loss Multiplier (ILM) [SAMA_EN_3487_VER1]; Internal Loss Multiplier (ILM) [SAMA_EN_4041_VER1] |
| loss component (lc) | 2 | Loss Component (LC) [SAMA_EN_3487_VER1]; Loss Component (LC) [SAMA_EN_4041_VER1] |
| operational risk capital (orc) | 2 | Operational Risk Capital (ORC) [SAMA_EN_3487_VER1]; Operational Risk Capital (ORC) [SAMA_EN_4041_VER1] |
| detailed loss event type classification | 2 | Detailed Loss Event Type Classification [SAMA_EN_3487_VER1]; Detailed Loss Event Type Classification [SAMA_EN_4041_VER1] |
| internal models method (imm) | 2 | Internal Models Method (IMM) [SAMA_EN_3487_VER1]; Internal Models Method (IMM) [SAMA_EN_4283_VER1] |
| replacement cost (rc) | 2 | Replacement Cost (RC) [SAMA_EN_3487_VER1]; Replacement Cost (RC) [SAMA_EN_4283_VER1] |
| netting set | 2 | Netting Set [SAMA_EN_3487_VER1]; Netting Set [SAMA_EN_4283_VER1] |
| hedging set | 2 | Hedging Set [SAMA_EN_3487_VER1]; Hedging Set [SAMA_EN_4283_VER1] |
| effective notional | 2 | Effective Notional [SAMA_EN_3487_VER1]; Effective Notional [SAMA_EN_4283_VER1] |
| supervisory delta adjustment | 2 | Supervisory Delta Adjustment [SAMA_EN_3487_VER1]; Supervisory Delta Adjustment [SAMA_EN_4283_VER1] |
| add-on for interest rate derivatives | 2 | Add-on for Interest Rate Derivatives [SAMA_EN_3487_VER1]; Add-on for Interest Rate Derivatives [SAMA_EN_4283_VER1] |
| add-on for foreign exchange derivatives | 2 | Add-on for Foreign Exchange Derivatives [SAMA_EN_3487_VER1]; Add-on for Foreign Exchange Derivatives [SAMA_EN_4283_VER1] |
| add-on for credit derivatives | 2 | Add-on for Credit Derivatives [SAMA_EN_3487_VER1]; Add-on for Credit Derivatives [SAMA_EN_4283_VER1] |
| add-on for equity derivatives | 2 | Add-on for Equity Derivatives [SAMA_EN_3487_VER1]; Add-on for Equity Derivatives [SAMA_EN_4283_VER1] |
| add-on for commodity derivatives | 2 | Add-on for Commodity Derivatives [SAMA_EN_3487_VER1]; Add-on for Commodity Derivatives [SAMA_EN_4283_VER1] |
| margin period of risk (mpor) | 2 | Margin Period of Risk (MPOR) [SAMA_EN_3487_VER1]; Margin Period of Risk (MPOR) [SAMA_EN_4283_VER1] |
| wrong-way risk | 2 | Wrong-way Risk [SAMA_EN_3487_VER1]; Wrong-Way Risk [SAMA_EN_4283_VER1] |
| qualifying ccp (qccp) | 2 | Qualifying CCP (QCCP) [SAMA_EN_3487_VER1]; Qualifying CCP (QCCP) [SAMA_EN_4283_VER1] |
| net independent collateral amount (nica) | 2 | Net Independent Collateral Amount (NICA) [SAMA_EN_3487_VER1]; Net Independent Collateral Amount (NICA) [SAMA_EN_4283_VER1] |
| basel iii framework | 2 | Basel III Framework [SAMA_EN_3487_VER1]; Basel III Framework [SAMA_EN_3623_VER1] |
| minimum capital requirements for credit risk | 2 | Minimum Capital Requirements for Credit Risk [SAMA_EN_3487_VER1]; Minimum Capital Requirements for Credit Risk [SAMA_EN_3502_VER1] |
| cross-product netting rules | 2 | Cross-Product Netting Rules [SAMA_EN_3487_VER1]; Cross-Product Netting Rules [SAMA_EN_4283_VER1] |
| minimum haircut floors for sfts | 2 | Minimum Haircut Floors for SFTs [SAMA_EN_3487_VER1]; Minimum Haircut Floors for SFTs [SAMA_EN_4283_VER1] |
| credit valuation adjustment (cva) framework | 2 | Credit Valuation Adjustment (CVA) Framework [SAMA_EN_3487_VER1]; Credit Valuation Adjustment (CVA) Framework [SAMA_EN_4283_VER1] |
| basic approach for cva (ba-cva) | 2 | Basic Approach for CVA (BA-CVA) [SAMA_EN_3487_VER1]; Basic Approach for CVA (BA-CVA) [SAMA_EN_4283_VER1] |
| eligible cva hedges | 2 | Eligible CVA Hedges [SAMA_EN_3487_VER1]; Eligible CVA Hedges [SAMA_EN_4283_VER1] |
| regulatory cva calculation | 2 | Regulatory CVA Calculation [SAMA_EN_3487_VER1]; Regulatory CVA Calculation [SAMA_EN_4283_VER1] |
| sa-ccr sample portfolio examples | 2 | SA-CCR Sample Portfolio Examples [SAMA_EN_3487_VER1]; SA-CCR Sample Portfolio Examples [SAMA_EN_4283_VER1] |
| leverage ratio exposure measure | 2 | Leverage Ratio Exposure Measure [SAMA_EN_3487_VER1]; Leverage Ratio Exposure Measure [SAMA_EN_4303_VER1] |
| rwa for credit risk | 2 | RWA for Credit Risk [SAMA_EN_3487_VER1]; RWA for Credit Risk [SAMA_EN_4376_VER1] |
| rwa for market risk | 2 | RWA for Market Risk [SAMA_EN_3487_VER1]; RWA for Market Risk [SAMA_EN_4376_VER1] |
| pillar 3 disclosure requirements framework | 2 | Pillar 3 Disclosure Requirements Framework [SAMA_EN_3487_VER1]; Pillar 3 Disclosure Requirements Framework [SAMA_EN_4234_VER1] |
| sope - minimum capital requirements for operational risk | 2 | SOPE - Minimum Capital Requirements for Operational Risk [SAMA_EN_3487_VER1]; SOPE - Minimum Capital Requirements for Operational Risk [SAMA_EN_4234_VER1] |
| template cr4: standardised approach credit risk exposure and crm effects | 2 | Template CR4: Standardised approach credit risk exposure and CRM effects [SAMA_EN_3487_VER1]; Template CR4: Standardised Approach Credit Risk Exposure and CRM Effects [SAMA_EN_4234_VER1] |
| template cr5: standardised approach exposures by asset classes and risk weights | 2 | Template CR5: Standardised approach exposures by asset classes and risk weights [SAMA_EN_3487_VER1]; Template CR5: Standardised Approach Exposures by Asset Classes and Risk Weights [SAMA_EN_4234_VER1] |
| template cre: qualitative disclosure related to irb models | 2 | Template CRE: Qualitative disclosure related to IRB models [SAMA_EN_3487_VER1]; Template CRE: Qualitative Disclosure Related to IRB Models [SAMA_EN_4234_VER1] |
| template cr6: irb credit risk exposures by portfolio and pd range | 2 | Template CR6: IRB credit risk exposures by portfolio and PD range [SAMA_EN_3487_VER1]; Template CR6: IRB Credit Risk Exposures by Portfolio and PD Range [SAMA_EN_4234_VER1] |
| template cr7: irb effect on rwa of credit derivatives used as crm | 2 | Template CR7: IRB effect on RWA of credit derivatives used as CRM [SAMA_EN_3487_VER1]; Template CR7: IRB Effect on RWA of Credit Derivatives Used as CRM [SAMA_EN_4234_VER1] |
| template cr8: rwa flow statements of credit risk exposures under irb | 2 | Template CR8: RWA flow statements of credit risk exposures under IRB [SAMA_EN_3487_VER1]; Template CR8: RWA Flow Statements of Credit Risk Exposures Under IRB [SAMA_EN_4234_VER1] |
| template cr9: irb backtesting of pd per portfolio | 2 | Template CR9: IRB backtesting of PD per portfolio [SAMA_EN_3487_VER1]; Template CR9: IRB Backtesting of PD Per Portfolio [SAMA_EN_4234_VER1] |
| table ccra: qualitative disclosure related to ccr | 2 | Table CCRA: Qualitative disclosure related to CCR [SAMA_EN_3487_VER1]; Table CCRA: Qualitative Disclosure Related to CCR [SAMA_EN_4234_VER1] |
| template ccr1: analysis of ccr exposures by approach | 2 | Template CCR1: Analysis of CCR exposures by approach [SAMA_EN_3487_VER1]; Template CCR1: Analysis of CCR Exposures by Approach [SAMA_EN_4234_VER1] |
| template ccr3: standardised approach ccr exposures by portfolio and risk weights | 2 | Template CCR3: Standardised approach CCR exposures by portfolio and risk weights [SAMA_EN_3487_VER1]; Template CCR3: Standardised Approach CCR Exposures by Portfolio and Risk Weights [SAMA_EN_4234_VER1] |
| template ccr4: irb ccr exposures by portfolio and pd scale | 2 | Template CCR4: IRB CCR exposures by portfolio and PD scale [SAMA_EN_3487_VER1]; Template CCR4: IRB CCR Exposures by Portfolio and PD Scale [SAMA_EN_4234_VER1] |
| template ccr6: credit derivatives exposures | 2 | Template CCR6: Credit derivatives exposures [SAMA_EN_3487_VER1]; Template CCR6: Credit Derivatives Exposures [SAMA_EN_4234_VER1] |
| template ccr7: rwa flow statements of ccr exposures under imm | 2 | Template CCR7: RWA flow statements of CCR exposures under IMM [SAMA_EN_3487_VER1]; Template CCR7: RWA Flow Statements of CCR Exposures Under IMM [SAMA_EN_4234_VER1] |
| template ccr8: exposures to central counterparties | 2 | Template CCR8: Exposures to central counterparties [SAMA_EN_3487_VER1]; Template CCR8: Exposures to Central Counterparties [SAMA_EN_4234_VER1] |
| template mr3: market risk simplified standardised approach | 2 | Template MR3: Market risk simplified standardised approach [SAMA_EN_3487_VER1]; Template MR3: Market Risk Simplified Standardised Approach [SAMA_EN_4234_VER1] |
| template or1: historical losses | 2 | Template OR1: Historical losses [SAMA_EN_3487_VER1]; Template OR1: Historical Losses [SAMA_EN_4234_VER1] |
| template or2: business indicator and subcomponents | 2 | Template OR2: Business indicator and subcomponents [SAMA_EN_3487_VER1]; Template OR2: Business Indicator and Subcomponents [SAMA_EN_4234_VER1] |
| template or3: minimum required operational risk capital | 2 | Template OR3: Minimum required operational risk capital [SAMA_EN_3487_VER1]; Template OR3: Minimum Required Operational Risk Capital [SAMA_EN_4234_VER1] |
| table liqa: liquidity risk management | 2 | Table LIQA: Liquidity risk management [SAMA_EN_3487_VER1]; Table LIQA: Liquidity Risk Management [SAMA_EN_4234_VER1] |
| template liq1: liquidity coverage ratio | 2 | Template LIQ1: Liquidity Coverage Ratio [SAMA_EN_3487_VER1]; Template LIQ1: Liquidity Coverage Ratio [SAMA_EN_4234_VER1] |
| template liq2: net stable funding ratio | 2 | Template LIQ2: Net Stable Funding Ratio [SAMA_EN_3487_VER1]; Template LIQ2: Net Stable Funding Ratio [SAMA_EN_4234_VER1] |
| template ov1: overview of rwa | 2 | Template OV1: Overview of RWA [SAMA_EN_3487_VER1]; Template OV1: Overview of RWA [SAMA_EN_4234_VER1] |
| template km1: key metrics | 2 | Template KM1: Key metrics [SAMA_EN_3487_VER1]; Template KM1: Key Metrics [SAMA_EN_4234_VER1] |
| early warning signals | 2 | Early Warning Signals [SAMA_EN_3526_VER1]; Early Warning Signals [SAMA_EN_3575_VER1] |
| npl strategy | 2 | NPL Strategy [SAMA_EN_3526_VER1]; NPL Strategy [SAMA_EN_3575_VER1] |
| workout unit | 2 | Workout Unit [SAMA_EN_3526_VER1]; Workout Unit [SAMA_EN_3575_VER1] |
| workout plan | 2 | Workout Plan [SAMA_EN_3526_VER1]; Workout Plan [SAMA_EN_3575_VER1] |
| sama cyber security framework (referenced) | 2 | SAMA Cyber Security Framework (referenced) [SAMA_EN_3689_VER1]; SAMA Cyber Security Framework (referenced) [SAMA_EN_3709_VER1] |
| business continuity management framework | 2 | Business Continuity Management Framework [SAMA_EN_3709_VER1]; Business Continuity Management Framework [SAMA_EN_4066_VER1] |
| member organization | 2 | Member Organization [SAMA_EN_3709_VER1]; Member Organization [SAMA_EN_3837_VER1] |
| cyber security leadership and governance | 2 | Cyber Security Leadership and Governance [SAMA_EN_3726_VER1]; Cyber Security Leadership and Governance [SAMA_EN_5888_VER1] |
| cyber security operations and technology | 2 | Cyber Security Operations and Technology [SAMA_EN_3726_VER1]; Cyber Security Operations and Technology [SAMA_EN_5888_VER1] |
| cyber security maturity model | 2 | Cyber Security Maturity Model [SAMA_EN_3837_VER1]; Cyber Security Maturity Model [SAMA_EN_5888_VER1] |
| chief information security officer (ciso) | 2 | Chief Information Security Officer (CISO) [SAMA_EN_3837_VER1]; Chief Information Security Officer (CISO) [SAMA_EN_5888_VER1] |
| cyber security committee | 2 | Cyber Security Committee [SAMA_EN_3837_VER1]; Cyber Security Committee [SAMA_EN_5888_VER1] |
| cyber security risk management process | 2 | Cyber Security Risk Management Process [SAMA_EN_3837_VER1]; Cyber Security Risk Management Process [SAMA_EN_5888_VER1] |
| swift customer security controls framework | 2 | SWIFT Customer Security Controls Framework [SAMA_EN_3837_VER1]; SWIFT Customer Security Controls Framework [SAMA_EN_5888_VER1] |
| siem | 2 | SIEM [SAMA_EN_3837_VER1]; SIEM [SAMA_EN_5888_VER1] |
| security operations center (soc) | 2 | Security Operations Center (SOC) [SAMA_EN_3837_VER1]; Security Operations Center (SOC) [SAMA_EN_5888_VER1] |
| basel iii post-crisis reforms | 2 | Basel III Post-Crisis Reforms [SAMA_EN_4041_VER1]; Basel III Post-Crisis Reforms [SAMA_EN_4234_VER1] |
| potential future exposure (pfe) | 2 | Potential Future Exposure (PFE) [SAMA_EN_4283_VER1]; Potential Future Exposure (PFE) [SAMA_EN_9068_VER1] |
| banking control law (m/5) | 2 | Banking Control Law (M/5) [SAMA_EN_4878_VER1]; Banking Control Law (M/5) [SAMA_EN_7136_VER1] |
| cash and precious metals transport law | 2 | Cash and Precious Metals Transport Law [SAMA_EN_5437_VER1]; Cash and Precious Metals Transport Law [SAMA_EN_5513_VER1] |
| registered real estate mortgage law | 2 | Registered Real Estate Mortgage Law [SAMA_EN_5464_VER1]; Registered Real Estate Mortgage Law [SAMA_EN_5885_VER1] |
| legal entity identifier (lei) / gleif | 2 | Legal Entity Identifier (LEI) / GLEIF [SAMA_EN_5765_VER1]; Legal Entity Identifier (LEI) / GLEIF [SAMA_EN_5879_VER1] |
| early ownership provisions | 2 | Early Ownership Provisions [SAMA_EN_5885_VER1]; Early Ownership Provisions [SAMA_EN_7136_VER1] |
| ownership transfer certificate | 2 | Ownership Transfer Certificate [SAMA_EN_5885_VER1]; Ownership Transfer Certificate [SAMA_EN_7136_VER1] |
| credit information company | 2 | Credit Information Company [SAMA_EN_5885_VER1]; Credit Information Company [SAMA_EN_961_VER1] |
| general directorate of financial intelligence | 2 | General Directorate of Financial Intelligence [SAMA_EN_791_VER1]; General Directorate of Financial Intelligence [SAMA_EN_853_VER1] |
| supervisory authority powers | 2 | Supervisory Authority Powers [SAMA_EN_791_VER1]; Supervisory Authority Powers [SAMA_EN_853_VER1] |

## Enrichment coverage
- Edges enriched: **1848 / 1848**
- Communities enriched: **336 / 336**

## Prioritized fix recommendations
1. **Grounding at 87%** (< 90%): review ungrounded excerpts above; most failures should correlate with garbled sources — treat those quotes as unreliable.
2. **No node has source_location** — citations rely solely on enrichment excerpts. Consider an extraction pass that captures page/article locators, or keep enrichment as the citation layer.
3. **Merge duplicate-label nodes** (228 clusters, e.g. "finance companies control law" ×12) if you want one canonical node per entity across documents.
4. **705 degree-1 nodes (39%)** — consider a --mode deep re-pass or manual linking to reduce fragmentation.
