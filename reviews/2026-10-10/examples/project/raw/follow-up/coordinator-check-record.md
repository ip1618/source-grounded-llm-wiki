# Coordinator fixture check record

Date: 2026-10-10. This record describes a synthetic local fixture, not a production application.

The coordinator applied the supplied billing.patch to repository/ledgerlane/billing.py after the design wiki update. The original discussion accurately said the patch was unapplied when delivered; the current local checkout now includes it. Original discussion, patch and earlier stored evidence were not rewritten.

The coordinator imported the updated helper with Python and ran six direct assertions: default zero discount retained subtotal/tax/total amounts (10,000/1,000/11,000 cents); a 1,000-cent pre-tax discount returned taxable/tax/total amounts of 9,000/900/9,900; a discount equal to subtotal gave a zero total; a 5-cent subtotal at 1,000 basis points rounded half a cent up to one cent; a negative discount raised ValueError; a discount above subtotal raised ValueError. All six passed in this local execution.

These are bounded helper checks, not a full test suite. No UI rendering/interaction, authentication, persistence, HTTP integration, publishing, or deployment was tested. No UI code was added.

Reviewed current billing.py SHA256: cda3bc6b9a238234ab4eeadd693eaf2a3d84a463f06082de1d9320f21c4dd777
