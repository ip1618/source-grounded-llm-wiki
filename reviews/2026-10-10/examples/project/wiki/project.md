# Project context

## Purpose and current scope

**Agreed:** operations staff should turn an agreed list of services into a clear invoice without retyping spreadsheet prices. Customers should be able to understand the charges. The first prototype prepares invoices; sending one to a customer is a later step. [Discussion, 10:18, lines 6–7](../raw/discussion-export.txt)

**Agreed responsibilities:** [billing](billing.md) calculates amounts and is intended eventually to hold invoice state; [profile access](profiles.md) decides which company members can read a customer profile; [masterdata](masterdata.md) owns service names and default prices so an editor can select an existing service. Mira agreed to this division. [Discussion, 10:22–10:25, lines 9–13](../raw/discussion-export.txt)

**Derived relationship:** the intended editor would select catalog services and use their defaults to prepare invoice amounts. Profile access supplies the customer-read boundary. The current three helpers have no connecting application flow or imports; the relationship is an agreed design responsibility, not demonstrated integration. [Discussion, 10:18–10:25, lines 6–13](../raw/discussion-export.txt), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [profiles, lines 4–5](../raw/repository/ledgerlane/profiles.py), [masterdata, lines 3–6](../raw/repository/ledgerlane/masterdata.py)

**Agreed and now implemented:** a fixed invoice discount in cents, deducted before tax, with zero as the default, added amount fields, and rejection outside zero through subtotal. Percentage discounts and combining discounts remain unapproved future proposals. [Billing](billing.md) owns the full behavior, reasons, history, and check scope. [Follow-up discussion, 09:12–09:20, lines 4–11](../raw/follow-up/discussion-export.txt), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py)

## Supplied UI design

The [invoice editor design](invoice-editor.md) supplies a static “Prepare invoice” composition with customer selection, service rows and quantities, subtotal/tax/total, and “Save draft” and “Publish invoice” controls. It connects the discussed responsibilities in a proposed presentation, not a working application. The designer states that prices and customer names are fictional examples and that no persistence, access, sending, or publishing behavior is demonstrated. [Design cover note, lines 1–5](../raw/design-supply/cover-note.txt), [SVG, lines 9–36](../raw/design-supply/invoice-editor.svg)

The supplied sketch predates the discount feature and has no discount row. Anika offered to add one later; there is no updated artwork or UI implementation. Its eventual label remains open. [Follow-up discussion, 09:42–09:48, lines 22–26](../raw/follow-up/discussion-export.txt), [Coordinator record, line 9](../raw/follow-up/coordinator-check-record.md)

## Open decisions

- **Publishing action and wording:** the delivered sketch shows “Publish invoice,” and the cover note confirms it is an unapproved placeholder. Whether that means visibility to colleagues or sending to the customer remains unanswered. Mira explicitly left both the audience and action open and did not sign off the wording or publishing flow. Preparing an invoice is agreed; the placeholder does not approve sending. [Discussion, 10:46–10:50, lines 27–31; 11:04, lines 36–37](../raw/discussion-export.txt), [Design cover note, line 5](../raw/design-supply/cover-note.txt), [SVG, lines 34–36](../raw/design-supply/invoice-editor.svg)
- **Profile editing/deletion:** read access does not establish edit or delete permission. [Profile access](profiles.md) owns this open policy. [Discussion, 10:25, lines 12–13](../raw/discussion-export.txt)
- **Catalog editing/storage:** the shared company catalog is the direction; its editing policy and storage design remain open. [Masterdata](masterdata.md) owns the decision and reason. [Discussion, 10:39, lines 24–25](../raw/discussion-export.txt)
- **Future precision:** revisit whole-cent amounts if later currencies or units need another precision. The current agreement applies to this prototype and catalog. [Discussion, 10:32, lines 18–19](../raw/discussion-export.txt)
- **Discount UI wording:** choose between “Goodwill adjustment” and “Discount.” Only the calculation scope is agreed; no new discount-row layout or publishing/sending flow is approved. [Follow-up discussion, 09:42–09:48, lines 22–26](../raw/follow-up/discussion-export.txt)

## Implementation and verification limits

**Implemented (static evidence):** the checkout contains invoice arithmetic with a fixed pre-tax discount, a company-id equality helper, and a hard-coded catalog. The helpers do not save invoices or enforce login; the profile helper is not attached to an endpoint. [Current billing, lines 1–16](../raw/repository-after-discount/ledgerlane/billing.py), [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py), [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py), [Discussion, 10:57, lines 33–34](../raw/discussion-export.txt)

**Checked, coordinator-reported:** on 2026-10-10 the coordinator imported the updated helper and ran six passing direct assertions: zero discount, a pre-tax discount, discount equal to subtotal, a half-cent tax round-up, negative-discount rejection, and above-subtotal rejection. The current billing hash matches the record. This wiki inspected that record and code; it did not independently rerun the helper. [Coordinator record, lines 3–11](../raw/follow-up/coordinator-check-record.md), [Follow-up source records](../raw/follow-up/source-records.md)

The checks cover only local helper execution. No UI rendering/interaction, authentication, persistence, HTTP integration, publishing, or deployment was tested; no UI code was added. The repository remains a helper-only prototype without the application components listed in its earlier README. Neither that README's earlier “no runtime results” statement nor the delivery discussion's “not applied or run” statement describes the latest helper-check status. [Coordinator record, lines 5–9](../raw/follow-up/coordinator-check-record.md), [README, line 5](../raw/repository/README.md), [Follow-up discussion, 09:35–09:48, lines 19–26](../raw/follow-up/discussion-export.txt)

## Evidence coverage

The first export begins midway through the 2026-08-06 discussion. Earlier messages and attachments are missing, so earlier alternatives and approvals cannot be reconstructed. The 2026-08-07 sketch and subsequent 2026-08-19 discount discussion are included, but neither recovers that missing window. [Initial export, lines 1–4](../raw/discussion-export.txt), [Design cover note, lines 1–5](../raw/design-supply/cover-note.txt), [Follow-up export, lines 1–2](../raw/follow-up/discussion-export.txt)

**Explained history:** the README and follow-up delivery discussion describe the patch as unapplied, and the delivery worked example was expressly not a test. The coordinator later applied it and recorded bounded execution. Different observation dates explain the status change; there is no open disagreement. Earlier unapplied/no-runtime statements are superseded as current status, while their historical attribution remains valid. Original artifacts and existing stored records are preserved. [README, line 7](../raw/repository/README.md), [Follow-up discussion, 09:35–09:48, lines 19–26](../raw/follow-up/discussion-export.txt), [Coordinator record, lines 3–11](../raw/follow-up/coordinator-check-record.md)

See [earlier source records](../raw/source-records.md) for the initial/design capture and [follow-up source records](../raw/follow-up/source-records.md) for current code and verification provenance. Earlier source records retain their capture-time scope; this page and billing own the latest status.
