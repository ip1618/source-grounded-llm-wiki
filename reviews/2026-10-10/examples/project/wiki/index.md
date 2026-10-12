# LedgerLane wiki

LedgerLane is a fictional invoice-preparation prototype. Start with [project context](project.md) for purpose, agreed scope, open decisions, and verification limits.

- [Billing](billing.md) — invoice arithmetic, the fixed pre-tax discount, unchanged tax rounding, and bounded helper checks.
- [Profile access](profiles.md) — the agreed read rule, its local helper, and unsettled editing rights.
- [Masterdata](masterdata.md) — service names and default prices, the shared-catalog decision, and the static implementation.
- [Shared company boundary](company-boundary.md) — the brief rule connecting profile access and catalog ownership.
- [Invoice editor design](invoice-editor.md) — supplied static layout, sample amounts, and its relationships to the system responsibilities.

The current checkout includes the agreed fixed invoice discount. The coordinator reports six passing local helper assertions; this is bounded arithmetic evidence, not working UI or deployment proof. [Current billing, lines 4–16](../raw/repository-after-discount/ledgerlane/billing.py), [Coordinator record, lines 5–11](../raw/follow-up/coordinator-check-record.md)

The discussion, checkout, UI sketch, patch, and check record are separate kinds of evidence. See [earlier source records](../raw/source-records.md) for the initial/design capture and [follow-up source records](../raw/follow-up/source-records.md) for the later discussion, patch, checks, and current code hash. Earlier records remain unchanged and describe their capture-time scope; the follow-up record and current topic pages own the latest status.

Wiki maintenance: [schema](schema.md) · [append-only activity log](log.md).
