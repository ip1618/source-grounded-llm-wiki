# Invoice editor design

This page owns the supplied UI composition and its relationships to the existing responsibilities. Anika delivered it on 2026-08-07 as a static sketch, not a working interface. Service prices and customer names are fictional. [Design cover note, lines 1–5](../raw/design-supply/cover-note.txt)

Source artwork: [unchanged invoice-editor.svg](../raw/design-supply/invoice-editor.svg). Its declared canvas is 1100 × 760. The description below comes from the SVG markup and cover note; no interactive application was evaluated. [SVG, line 1](../raw/design-supply/invoice-editor.svg)

## Supplied composition

- A dark left navigation rail contains the LedgerLane name and “Invoices,” “Profiles,” and “Service catalog.” The main heading is “Prepare invoice,” with a static-sketch/synthetic-examples subtitle. [SVG, lines 2–10](../raw/design-supply/invoice-editor.svg)
- A white editor card begins with a customer selector displaying “North Harbor Ops.” Service, quantity, and amount columns sit below it. [SVG, lines 11–18](../raw/design-supply/invoice-editor.svg)
- Sample rows show Site visit, quantity 1, $75.00; and Document review, quantity 2, $84.00. The totals area shows subtotal $159.00, Tax (10%) $15.90, and total $174.90. [SVG, lines 19–31](../raw/design-supply/invoice-editor.svg)
- At the lower right, “Save draft” appears beside a filled “Publish invoice” button. A footer states that button wording and audience remain under discussion. These are drawn controls, not demonstrated actions. [SVG, lines 32–36](../raw/design-supply/invoice-editor.svg), [Design cover note, line 5](../raw/design-supply/cover-note.txt)

## Connections to the system

**Derived mapping:** the sketch presents the responsibilities together; the current helpers are still unconnected. The mapping describes what the layout relates to, rather than approval of new behavior. [Discussion, 10:22–10:25, lines 9–13](../raw/discussion-export.txt), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py), [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py)

| Sketch element | Owning topic and supported relationship |
| --- | --- |
| Customer selector / Profiles navigation | [Profile access](profiles.md): customer reading must follow the agreed company rule; the drawing demonstrates no enforcement. |
| Service rows / Service catalog navigation | [Masterdata](masterdata.md): displayed names and example amounts align with the sample defaults; no lookup or editing flow is demonstrated. |
| Subtotal, tax, total | [Billing](billing.md): the fictional sample is arithmetically consistent with the current helper's default zero discount and stored catalog. |
| Save draft | [Billing](billing.md): relates to eventual invoice state, but saving remains unimplemented and the image proves no persistence. |
| Publish invoice | [Project context](project.md): action, audience, and wording remain open; the label is an unapproved placeholder. |

## Later discount feature

**Agreed calculation, pending design:** the later feature adds a fixed invoice discount before tax, preserves subtotal, and supplies `discount_cents` and `taxable_cents` so the UI can explain the adjustment. Percentage/combined discounts remain unapproved. The current helper implements that scope, and the coordinator reports bounded arithmetic checks; no UI code was added. [Follow-up discussion, 09:16–09:20, lines 7–11](../raw/follow-up/discussion-export.txt), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [Coordinator record, lines 7–9](../raw/follow-up/coordinator-check-record.md)

The supplied 2026-08-07 sketch has no discount row and remains unchanged. Anika offered a later row, with “Goodwill adjustment” versus “Discount” still undecided. This is a dated layout gap, not a disagreement about the current calculation. Do not infer a new placement, input control, or approved label. Publishing wording and sending remain unresolved. [SVG, lines 15–36](../raw/design-supply/invoice-editor.svg), [Follow-up discussion, 09:42–09:48, lines 22–26](../raw/follow-up/discussion-export.txt)

## Approval and verification boundaries

**Proposed design:** the composition provides material for layout discussion. **Agreed scope:** invoice preparation. **Open question:** what the publishing button does and for whom. The designer's cover note and Mira's discussion agree that “Publish invoice” is not an approved action or wording; the delivered label does not contradict the preparation-only prototype scope. [Design cover note, line 5](../raw/design-supply/cover-note.txt), [Discussion, 10:18, lines 6–7; 10:46–10:50, lines 27–31; 11:04, lines 36–37](../raw/discussion-export.txt)

No persistence, access control, sending, or publishing is demonstrated by the image. This wiki update implements none of them. The dollar amounts and 10% tax are examples, not new monetary requirements. [Design cover note, line 5](../raw/design-supply/cover-note.txt), [SVG, lines 19–35](../raw/design-supply/invoice-editor.svg)

See [project context](project.md) for missing earlier evidence, [earlier source records](../raw/source-records.md) for the unchanged artwork, and [follow-up source records](../raw/follow-up/source-records.md) for the discount discussion/current code/check evidence.
