# Billing

Billing owns invoice amount calculation and is intended eventually to hold invoice state. That responsibility was agreed; persistence is not implemented in this checkout. Catalog service names and default prices belong to [masterdata](masterdata.md). [Discussion, 10:22–10:25, lines 9–13; 10:57, lines 33–34](../raw/discussion-export.txt)

## Agreed money rules and reasons

- **Agreed:** use integer cents for this prototype. Dev recommended this because binary floating-point can introduce small differences for ordinary decimal prices and make totals and reconciliation harder to explain. Cents fit the amounts currently needed and the catalog's whole-cent prices. [Discussion, 10:29–10:32, lines 15–19](../raw/discussion-export.txt)
- **Agreed:** tax uses basis points, where 100 basis points equals 1 percent. Round the tax amount once to the nearest cent, with halves rounded up. [Discussion, 10:29–10:32, lines 15–19](../raw/discussion-export.txt)
- **Open future scope:** revisit precision if currencies or units later need something other than whole cents. No currency support or additional precision is approved in the available discussion. [Discussion, 10:32, lines 18–19](../raw/discussion-export.txt)

## Fixed invoice discount

**Business need:** some invoice drafts need a goodwill discount. Mira requested discount support for that purpose. [Follow-up discussion, 09:12, lines 4–5](../raw/follow-up/discussion-export.txt)

**Agreed:** support only a fixed invoice discount in cents, deducted from subtotal before tax. Preserve original subtotal and expose `discount_cents` and `taxable_cents`; reject a discount below zero or above subtotal. Default the discount to zero so existing callers retain the earlier subtotal/tax/total amounts. [Follow-up discussion, 09:16–09:20, lines 7–11](../raw/follow-up/discussion-export.txt)

**Reason and alternatives:** Mira initially asked about percentage discounts on rows plus a fixed invoice discount. Dev explained that combining them requires stacking and rounding rules, so the agreed small change uses only the fixed amount. Percentage discounts and combining discounts remain later proposals, not approved behavior. Dev also considered banker's rounding, but Mira reaffirmed the existing halves-up tax rule because the alternative would change some half-cent totals. [Follow-up discussion, 09:12–09:29, lines 4–17](../raw/follow-up/discussion-export.txt)

## Current helper

**Implemented (static evidence):** `calculate_invoice(lines, tax_basis_points, discount_cents=0)` now:

1. Sums `unit_price_cents × quantity` into the original `subtotal_cents`.
2. Raises `ValueError` if discount is below zero or above subtotal.
3. Sets `taxable_cents = subtotal_cents - discount_cents`.
4. Calculates tax as `(taxable_cents × tax_basis_points + 5000) // 10000`.
5. Returns `subtotal_cents`, `discount_cents`, `taxable_cents`, `tax_cents`, and `total_cents = taxable_cents + tax_cents`.

[Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [Supplied patch, lines 7–22](../raw/follow-up/billing.patch)

**Derived:** for non-negative integer taxable amounts and tax inputs, tax still rounds once to the nearest cent with halves up. Zero discount preserves the original three amounts, while the result dictionary now also contains two additional fields; amount compatibility does not mean an identical return shape. The code validates the discount range but does not enforce integer types or validate all line quantities, prices, or tax rates. [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [Earlier billing, lines 4–11](../raw/repository/ledgerlane/billing.py)

The helper still receives prices/quantities directly and does not fetch catalog prices, read customer profiles, save invoice state, enforce login, or publish invoices. Catalog defaults and profile policy remain separate responsibilities. [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py), [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py)

## Bounded verification

**Checked, coordinator-reported:** six direct assertions passed in local Python execution on 2026-10-10. They cover these cases. [Coordinator record, lines 3–7](../raw/follow-up/coordinator-check-record.md)

| Case | Recorded result, cents |
| --- | --- |
| Zero/default discount | Subtotal 10000, tax 1000, total 11000 |
| Discount 1000 on subtotal 10000 at 1000 tax basis points | Taxable 9000, tax 900, total 9900 |
| Discount equal to subtotal | Zero total |
| Subtotal 5 at 1000 tax basis points | Half-cent tax rounded up to 1 |
| Negative discount | `ValueError` |
| Discount above subtotal | `ValueError` |

The current source SHA-256 is `cda3bc6b9a238234ab4eeadd693eaf2a3d84a463f06082de1d9320f21c4dd777`, matching the coordinator's reviewed hash. This wiki update verified source identity and inspected the record; it did not rerun the assertions. These checks are not a full test suite and cover no UI, authentication, persistence, HTTP integration, publishing, or deployment. [Coordinator record, lines 9–11](../raw/follow-up/coordinator-check-record.md), [Follow-up source records](../raw/follow-up/source-records.md)

## Delivery history

**Superseded as current status:** the earlier helper taxed the entire subtotal and returned only subtotal/tax/total. Its unchanged snapshot remains available for history; the current helper above includes the discount. [Earlier billing, lines 4–11](../raw/repository/ledgerlane/billing.py), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py)

**Explained:** at 2026-08-19 delivery, Dev said the patch was unapplied/unrun and the 10000/1000/1000 example was a worked calculation, not a test result. Mira said there was no runtime or deployment evidence then. On 2026-10-10 the coordinator applied the patch and executed the bounded checks. The dates explain the differing statuses; delivery statements remain valid historical evidence. Deployment is still unverified. [Follow-up discussion, 09:35–09:48, lines 19–26](../raw/follow-up/discussion-export.txt), [Coordinator record, lines 3–11](../raw/follow-up/coordinator-check-record.md)

## Design relationship

The [invoice editor sketch](invoice-editor.md) displays service amounts, subtotal, tax, and total. **Derived:** its fictional example still agrees with the current helper at the default zero discount: `7500 × 1 + 4200 × 2 = 15900` cents; 10% (`1000` basis points) gives `1590` cents tax and `17490` cents total. This supports consistency of that sample, not an implemented editor or an approved universal 10% tax rate. [SVG, lines 19–31](../raw/design-supply/invoice-editor.svg), [masterdata, lines 3–6](../raw/repository/ledgerlane/masterdata.py), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [Design cover note, line 5](../raw/design-supply/cover-note.txt)

The old sketch has no discount row. Anika proposed adding one later; “Goodwill adjustment” versus “Discount” remains open. The new result fields can support displaying the adjustment and taxable amount, but no new artwork or UI code is supplied, and publishing remains unapproved. [Follow-up discussion, 09:16–09:20, lines 7–11; 09:42–09:48, lines 22–26](../raw/follow-up/discussion-export.txt), [Coordinator record, line 9](../raw/follow-up/coordinator-check-record.md)

“Save draft” visually relates to billing's eventual invoice-state responsibility, but the control is design evidence only. No persistence is demonstrated, and the current helper remains calculation-only. [SVG, lines 32–33](../raw/design-supply/invoice-editor.svg), [Discussion, 10:22, lines 9–10; 10:57, lines 33–34](../raw/discussion-export.txt), [Design cover note, line 5](../raw/design-supply/cover-note.txt)

## Related code

- [repository/ledgerlane/billing.py](../repository/ledgerlane/billing.py) — `calculate_invoice`, current arithmetic and discount helper; [current reviewed snapshot](../raw/repository-after-discount/ledgerlane/billing.py), [supplied patch](../raw/follow-up/billing.patch), [earlier snapshot](../raw/repository/ledgerlane/billing.py).
- [Masterdata](masterdata.md) — owns defaults intended to feed invoice preparation; current helper integration is absent.

See [project context](project.md) for the open publishing action and limits beyond the coordinator's bounded helper checks.
