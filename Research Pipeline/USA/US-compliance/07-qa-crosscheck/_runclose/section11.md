

## 11. Re-check 3: F27 fix, minor fixes and skill round 6 (2026-11-04)

This section supersedes section 10 wherever the two differ.

**Verdict: BLOCKED, by C39 only.** C39 Test 0 is unchanged at 50/56 = 89.3 %. Nothing new blocks release.

| Item | Result | Review |
|---|---|---|
| RC-4 (F27): Form 940 rule, RSPEC vs SIR | **Closed.** The SIR Form 940 cells now print `[[FACT:rspec.fed.form940.due]]` with the same text as RSPEC IRS-004 | `_qa/SIR-review-r5.json` |
| RC-6: SIR wording for the Ohio school district code | **Closed.** The SIR prints the fact followed by the DD limitation sentence (based on the 2025 list US-OHS5-019, effective to 2025-12-31) | `_qa/SIR-review-r5.json` |
| RC-1: SC citation in the CCG | **Closed.** The SC, WI, NE, OH, CT and MA practice rows in m06 and m13, and the m05 MA PFML decision line, now cite their `_also` rows. The WI row was also under-cited before this fix: its W-166 rates 3.54/4.65 are only in US-WIS5-011. The fix corrects that too | `_qa/CCG-review-r7.json` (md5 333e8ee60a3d97a9b229b859c4f5da7c) |
| `f44_lib.py` `LIMITATION_KEYS` | **Accepted for 1.0, minor finding.** It skips F44 for the two keys whatever their value. The auditor checked by hand that the skip is safe today: US-FEDS5-031 contains "February 2, 2026" and "February 10", US-OHS5-019 contains "9999", and the TY2026 dates re-derive. A later change of value would not be checked, so pin the skip to the current value (or to the derived elements only) at the next SIR build | `_qa/SIR-review-r5.json` |
| Skill round 6 (6 files) | **PASS.** The diff from `pre-skill-b4` maps to the same CCG citation changes, the SIR changes, the review ids and the gap counts. Selfcheck and selfcheck_strict show 0 misses | `_qa/SKILL-review-r6.json` |

**Diff mapping:**
- **CCG (24 lines).** Only the citation cells changed; the tag text is unchanged.
- **SIR (208 raw lines).** The SIR-RQ ids were renumbered by -2 because the two F44 gaps were removed. With the ids masked, 12 lines changed, and each maps to a stated cause. `gaps.json` (39 SIR-RQ entries) and the skill's `14-known-gaps.md` agree id by id.

**Gates re-run:**
- tag_sync: 0 stale.
- C41: PASS. C40: PASS. C70: PASS. C53: PASS.
- C71: 0 differences.
- C38: PASS, 0 mismatches.
- Period-aware C46: 12,224 tags, 0 mismatches.
- C29: 0. Vocabulary lint: 0.
- SIR f44_self: 409 tags, 0 misses.
- md5 vs md5_final:
  - WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99.
  - CCG is 333e8ee6, reviewed in r7.

**Still open and not blocking:**
- RC-5 (major): register rows US-RIS5-008, US-OHR3C-001 and US-OHP52-001 (section 10).
- The `LIMITATION_KEYS` pin (minor).
- Everything named in section 6.

The C39 options are unchanged: either a US reader confirms the 6 pages, or the owner records an exemption with the content set out in section 10.
