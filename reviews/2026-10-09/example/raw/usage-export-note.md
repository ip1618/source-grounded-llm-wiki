# Existing export usage

Synthetic evaluation fixture. No real company, customer, or private data.
Author: Example Analytics Team
Published: 2026-10-01
Source type: Usage-data note
Observation window: 2026-09-01 through 2026-09-30 inclusive, UTC.

## Definitions and observations
The current product offers a legacy CSV export on the account list, not saved reports.
export_event: one successful legacy account-list CSV generation. Repeated exports by the same user count separately.
exporting_user: distinct authenticated user with at least one export_event in the observation window.
Observed: 120 export_events from 18 exporting_users.

## Limits
This note contains export events only. It has no count of all active users, no retention comparison, no customer-segment breakdown, and no reason-for-export data. The note cannot establish export adoption rate or a retention effect.
