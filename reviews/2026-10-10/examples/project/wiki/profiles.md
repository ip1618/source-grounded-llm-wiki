# Profile access

Profile access owns who may read customer profiles. It shares the [company boundary](company-boundary.md) with the intended catalog model. [Discussion, 10:22–10:25, lines 9–13](../raw/discussion-export.txt)

## Agreed read rule

**Agreed:** a signed-in member may view customer profiles belonging to their own company and must not read another company's profiles. This is shared company access, rather than access limited to the individual preparing an invoice. [Discussion, 10:25, lines 12–13](../raw/discussion-export.txt)

**Open question:** who may edit or delete a shared profile? Mira explicitly said not to assume that everyone who can read may edit. No edit/delete policy is established by the helper or the available discussion. [Discussion, 10:25, lines 12–13](../raw/discussion-export.txt), [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py)

## Current helper and limit

**Implemented (static evidence):** `can_view_profile(member, profile)` returns whether the two supplied `company_id` values are equal. It makes no login check and does not validate that the supplied member represents an authenticated user. [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py)

The helper is not attached to an endpoint or authentication system. **Derived:** equality expresses the local same-company decision, but it cannot establish enforced access in an application. Authentication and endpoint integration still need implementation evidence. [Discussion, 10:57, lines 33–34](../raw/discussion-export.txt), [profiles, lines 1–5](../raw/repository/ledgerlane/profiles.py), [README, line 5](../raw/repository/README.md)

## Design relationship

The [invoice editor sketch](invoice-editor.md) includes a customer selector displaying the fictional “North Harbor Ops” and a “Profiles” navigation label. **Derived:** a working customer-selection flow would need to respect the agreed same-company profile-read rule; neither a selector nor navigation label proves that rule is enforced. The cover note explicitly says the image demonstrates no access-control behavior. [SVG, lines 7 and 12–14](../raw/design-supply/invoice-editor.svg), [Design cover note, line 5](../raw/design-supply/cover-note.txt), [Discussion, 10:25, lines 12–13](../raw/discussion-export.txt)

## Related code

- [repository/ledgerlane/profiles.py](../repository/ledgerlane/profiles.py) — `can_view_profile`, company-id equality decision; [unchanged reviewed snapshot](../raw/repository/ledgerlane/profiles.py).

See [project context](project.md) for the agreed module relationships and verification limits.
