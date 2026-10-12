# Shared company boundary

**Agreed:** company membership is the shared boundary for reading customer profiles: signed-in members may read their own company's profiles and must not read another company's. [Discussion, 10:25, lines 12–13](../raw/discussion-export.txt)

**Agreed direction:** the service catalog should also be shared by staff preparing the same company's invoices, so service names and default prices stay consistent. Per-person copies were rejected because they would drift and require repeated maintenance. [Discussion, 10:36–10:39, lines 21–25](../raw/discussion-export.txt)

These responsibilities have separate policy owners:

- [Profile access](profiles.md) owns the read rule and unresolved edit/delete permissions.
- [Masterdata](masterdata.md) owns catalog editing and storage decisions.
- [Billing](billing.md) owns calculation; this discussion does not establish invoice-access or publishing permissions.

**Implemented (static evidence):** the profile helper compares supplied company IDs. The static catalog has no company partition, so code evidence covers only the local profile decision. Neither helper establishes authentication or enforced isolation in an application. [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py), [masterdata, lines 1–6](../raw/repository/ledgerlane/masterdata.py), [README, line 5](../raw/repository/README.md)
