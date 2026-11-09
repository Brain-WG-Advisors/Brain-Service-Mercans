# US v1.1 QA review, round 1 of 3 (2026-11-06)

**Verdict: FAIL.** The review found 0 blockers, 8 majors and 12 minors. The full record is `V11-review-r1.json` (schema review 1.4.0, validated).
Files reviewed: all 26 entries in `_pipeline/V11-md5.txt`, md5 OK. Each was compared with its `_v1.0/` copy. C43 was not counted, as instructed.

## The 9 focus items
| # | Item | Result |
|---|---|---|
| 1 | 74 rows with the default effective_from 2026-01-01 (the log says 75) | 25 sampled: **4 wrong** (CAV6-002 is a 2027 rate; FEDV6-042 is a proposed rule; CAV6-008 is a dead bill; FLV6-001 is dated 2026-09-28), **2 unsupported** (FLV6-002, NYV6-004). The other 19 are right for 2026 but drop the earlier date shown in the source. |
| 2 | 57 authority renames | All 57 checked: **2 wrong** (FEDV6-022 is IRS Pub 957, not SSA; OHV6B-002 is legislature.ohio.gov, not codes.ohio.gov). Ohio still has 2 spellings. |
| 3 | GA split 2026-05-11; GA e-file from 2026-08-09 | Values and dates are consistent across m06, annex GA, WTC, m11, SIR and RSPEC. **Stale annex notes** still say the e-file rule is "proposed / not verified". The oracle date is wrong. The minimum-wage exemptions rest on a 2021 non-enacted bill. |
| 4 | NY.2 per-period tables | 60+ values checked against the NYS and NYC (1/26) copies, **0 mismatches**. Two problems: the quarterly/semiannual "limitation" is contradicted by p.23 of the same publication (which closes RQ-598), and **OK/VT notes were dropped** by the new collisions. |
| 5 | TX 204.0025 | Not mandatory everywhere. One DD wording contradiction ("in force for 2026" next to "proposed only"). |
| 6 | Change-log rows | **Inaccurate.** 19 of 20 RSPEC rows claim GA/TX changes they do not contain. The CCG claims research wording was removed (156 "not read" lines remain). WTC claims MI with no change. DD claims "all jurisdictions". SIR leaves 2 changes unlogged. |
| 7 | Research wording in deliverables | Still present in the pilot annexes (TX, OH, IL, MI, GA, FL) and in 3 pilot fact values. WI figures are spelled out in words to get past the collision guard. |
| 8 | C48/C49/C50 | Re-run: each FAIL is the accepted v1.0 exemption. The C49 location moved from table 206 to 207, so the owner should update the scope. |
| 9 | RQ-598, RQ-40 | Noted, not failed on their own. |

## Owners
- **artifact-builder:** change logs (RSPEC x19, CCG, WTC, DD, SIR); OK/VT dropped notes; GA tags; SIR Appendix A (GAS5-005, TXV6-005); SIR GA and DD TX parentheticals.
- **compliance-source-hunter:** register effective_from (6 rows plus the 49 unsampled) and the count; 2 authority names; GA stale notes and oracle date; GA minimum-wage source; RQ-598 from p.23; WI figures as bound facts; TX status wording; CA V-07 and PA V-06 not carried.
