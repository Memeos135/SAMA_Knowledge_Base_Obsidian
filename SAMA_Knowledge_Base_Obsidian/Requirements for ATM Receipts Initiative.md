---
source_file: "markdown/SAMA_EN_11076_VER1.md"
type: "document"
community: "ATM Transaction Requirements"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/ATM_Transaction_Requirements
  - graphify/enriched
---

# Requirements for ATM Receipts Initiative

## Connections

### [[Cash Withdrawal Transaction Stream]] — `references` [EXTRACTED]
- **What this link tells you:** This is an intra-document parent-to-section link: the Cash Withdrawal Transaction Stream (section 3.1) is one of the two operational streams defined within the ATM Receipts Initiative requirements binding on mada Members. For compliance scoping, read the stream requirements — two separate transactions ('Cash Withdrawal' without receipt on the Home page, and 'Cash Withdrawal with Receipt' under 'Others') — as mandatory rules the parent document says members 'must comply with... at all times', not optional design suggestions. Conclude that the receipt-suppression default and the on-request receipt availability both derive their force from the same requirements document, so the stream cannot be assessed apart from the initiative's overall scope and audience.
- **Grounding — this node (Page 5 / Section 2):** "The new enhancement on ATM screen flow runs into two streams: (1) Cash Withdrawal transaction stream, and (2) 'Non-cash transactions stream."
- **Grounding — related node (Page 6 / Section 3.1):** "there will be two separate transactions for Cash Withdrawal: (1) ... 'Cash Withdrawal' ... should not provide a receipt ... (2) 'Cash Withdrawal with Receipt'"

### [[Non-cash Transactions Stream]] — `references` [EXTRACTED]
- **What this link tells you:** This is an intra-document parent-to-section link: the Non-cash Transactions Stream (section 3.2) is the second of the two streams governed by the ATM Receipts Initiative and covers Balance Enquiry, Mini Statement, and Cash Deposit. For compliance scoping, note the requirement here differs from the cash stream — no receipt is auto-printed, but a 'collect a receipt and exit' option must be offered, preserving the parent document's guarantee that paper receipts remain available on request. Conclude that both streams share the same binding source and objective (receipt reduction) but impose distinct screen-flow obligations, so map them separately while treating both as mandatory for mada Members.
- **Grounding — this node (Page 5 / Section 2):** "However, paper receipts shall still be available and provided to Cardholders whenever requested."
- **Grounding — related node (Page 7 / Section 3.2):** "a receipt will not be automatically printed. However, an option to 'collect a receipt and exit' will be given to the Cardholder"

#graphify/document #graphify/EXTRACTED #community/ATM_Transaction_Requirements #graphify/enriched
