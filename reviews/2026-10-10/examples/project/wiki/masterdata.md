# Masterdata

Masterdata owns service names and default prices so an invoice editor can select an existing service. This supports the goal of preparing clear invoices without retyping spreadsheet prices. The responsibility was agreed with [billing](billing.md) and [profile access](profiles.md). [Discussion, 10:18–10:25, lines 6–13](../raw/discussion-export.txt)

## Shared catalog decision

**Agreed direction:** staff preparing invoices for the same company need the same service names and defaults. The catalog should therefore be shared at the [company boundary](company-boundary.md). [Discussion, 10:39, lines 24–25](../raw/discussion-export.txt)

**Rejected alternative:** Dev suggested duplicating a private service catalog for each staff member to avoid shared price changes. Mira rejected it because per-person copies would create diverging prices and repeated maintenance. This is a recorded alternative in the available window; missing earlier alternatives cannot be reconstructed. [Discussion, 10:36–10:39, lines 21–25](../raw/discussion-export.txt), [Export, lines 3–4](../raw/discussion-export.txt)

**Open questions:** who may edit the shared catalog, and how should it be stored? Mira explicitly said the static catalog establishes neither policy nor storage design. [Discussion, 10:39, lines 24–25](../raw/discussion-export.txt)

## Current catalog

**Implemented (static evidence):** `SERVICE_CATALOG` is a hard-coded dictionary with no editing flow. It supplies these defaults in integer cents. [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py)

| Service key | Display name | Default unit price, cents |
| --- | --- | --- |
| `site-visit` | Site visit | 7500 |
| `review` | Document review | 4200 |

**Derived limit:** the dictionary has no company key, persistence, or price-editing mechanism. Its presence supports available sample defaults, not a stored catalog per company or enforcement of the agreed shared-company model. The current billing helper still receives prices directly; its fixed invoice discount changes the taxable amount rather than the catalog defaults. No catalog selection is connected in this snapshot. [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py), [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py)

## Design relationship

The [invoice editor sketch](invoice-editor.md) shows “Service catalog” navigation and rows for Site visit and Document review. **Derived:** these names and sample amounts align with the stored catalog: one Site visit at 7500 cents is shown as $75.00; two Document reviews at 4200 cents each are shown as $84.00. The dollar display and sample prices are fictional design content, not evidence of approved currency support or a live catalog lookup. [SVG, lines 8 and 19–24](../raw/design-supply/invoice-editor.svg), [masterdata, lines 3–6](../raw/repository/ledgerlane/masterdata.py), [Design cover note, line 5](../raw/design-supply/cover-note.txt)

The sketch supplies no catalog editing or storage behavior and does not settle the open shared-catalog policy. [Design cover note, line 5](../raw/design-supply/cover-note.txt), [Discussion, 10:39, lines 24–25](../raw/discussion-export.txt)

## Related code

- [repository/ledgerlane/masterdata.py](../repository/ledgerlane/masterdata.py) — `SERVICE_CATALOG`, sample names and prices; [unchanged reviewed snapshot](../raw/repository/ledgerlane/masterdata.py).
- [Billing](billing.md) — owns arithmetic and the agreed whole-cent precision rule.
