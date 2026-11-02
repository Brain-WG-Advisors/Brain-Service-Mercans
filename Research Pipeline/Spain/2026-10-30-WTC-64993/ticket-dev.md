**Summary:** Spain: 64993 Contractual Extra Pay hard-coded to 62100 (all Spain clients) — from HRBS-16407

@lli Spain is live. 64993 Contractual Extra Pay is `$62100.amount` in WTC V4.8, so:
- it is zero when the client sends the salary through 64430/64440 and not 62100;
- the extra paid in June/December is base salary only, while the accrual (64556/58140) uses 64440, so the SS base and the amount paid don't match.

What the extras include is set by the collective agreement, not by law (ET art. 31); the Spain CCG says the composition "must be configurable per pay group; it cannot be hard-coded to base salary".

Proposed change (WTC V4.9):
1. Country level: 64993 = 58140 × 12 ÷ number of extras (2, or 3 when 58209 = 1), the rule agreed on 16/09.
2. Entity level: override where the agreement sets another composition (e.g. STG: 62100 + 62182).

Please confirm two points before Dev builds it: how this works for starters, leavers and partial months (58140 carries the day factors), and that 64440 doesn't already include the prorated extras (62147) for clients paying them monthly.
