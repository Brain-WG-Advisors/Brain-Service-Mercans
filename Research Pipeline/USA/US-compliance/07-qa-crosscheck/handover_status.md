# US handover status (2026-11-05, release round 2)

**State: RELEASED-LOCAL (not uploaded), 2026-11-05.** The package is `10-release/`: 26 files, version 1.0, issue date 2026-11-05. C47 passes with 0 findings. CCG C71 passes, and its md5_final is sealed at 20307cd3. Every gate passes. Nothing goes to the Drive without the owner's approval. QA report section 13.1 has the details. Items still open before production (none blocks the release): re-read T51 UT from a US IP; RC-5; pin `LIMITATION_KEYS`; owner confirmations US-OWN-009, US-OWN-010 and US-OWN-011.

## Artifacts
All of CCG, SCOPE, RSPEC, DD, WTC, SIR, PSL, SKILL and DESIGN pass QA. The latest rebuilds were each given a targeted review:

| Artifact | Review | Result |
|---|---|---|
| CCG | `_qa/CCG-review-r7.json` | PASS, md5 333e8ee6 |
| RSPEC | `_qa/RSPEC-review-r3d.json` | PASS |
| SIR | `_qa/SIR-review-r5.json` | PASS |
| SKILL | `_qa/SKILL-review-r6.json` | PASS; F28 closed |

The md5 of every deliverable matches its md5_final.

## Blocking item
None.

C39 was closed on 2026-11-05: the user opened T46 IN, T49 NC, T50 KY, T55 TX and T56 OR live on the official hosts through a VPN, and the auditor checked each quote in the saved files (QA report section 12).

**Non-blocking, before production:** re-read T51 (UT income tax 2026 = 4.45 %, [US-UTS5-001]) from a US IP, add the quote to `US-TEST0.json`, and re-run `test0_check.py`.

## C-checks
| Kind | Checks | Result |
|---|---|---|
| Deterministic | C37, C38, C40, C41, C42, C43, C45, C46 (period-aware), C53, C56, C57, C69, C70, C71 | PASS |
| Deterministic | C39 | PASS, 55/56 = 98.2 % (T51 UT still UNVERIFIED, non-blocking) |
| Deterministic | C44 | The shared check SKIPs; the crosswalk check passes 20/20 |
| Deterministic, owner-exempted | C34–C36 (US-OWN-010); C46 package-wide, C48, C49, C50 (US-OWN-011) | Only the exempted items remain |
| Run-local | tag_sync, vocabulary lint, C29 over the whole package, md5, validate_contract | 0 stale, 0 hits, all OK, PASS |
| Manual | C5, C6, C7, C9, C21 | Run by hand in the per-artifact reviews |
| At release | C47, C73 | Not yet applicable |

## Still open (named, not blocking)
**Findings:**
- RC-4 (F27 Form 940), RC-1 (CCG citations, WI under-citation included) and RC-6 (SIR Ohio wording): **closed** in re-check 3 (`_qa/SIR-review-r5.json`, `_qa/CCG-review-r7.json`, `_qa/SKILL-review-r6.json`; CCG md5 333e8ee6). New minor finding: `03-statutory-integrations/_build/f44_lib.py` `LIMITATION_KEYS` skips F44 for 2 keys whatever their value; it is accepted for 1.0, and the skip should be pinned to the current value at the next SIR build.
- **RC-5 (major):** in the register, US-RIS5-008, US-OHR3C-001 and US-OHP52-001 are closed-period sources shown as active with no end date. RIS5-008 also has a false start date. The fix is status `historical`, plus a C41 skip in the shared checker.

**Open gaps and limitations:**
- Open gaps and limitations by artifact, as listed in QA report section 6.
- TY2025-labelled federal items: Form 940 2026 instructions, 1094-C/1095-C, and the 2026 FUTA credit-reduction list (due from the DOL around 2026-11-10).
- Access-blocked sources.
- DESIGN-RQ-02 and DESIGN-RQ-05, which have fallbacks.
- Two change requests for DD 1.1.
- US-OWN-009, and the owner-default exemptions US-OWN-010/011, still need explicit owner confirmation.
- The `effective_from` dates taken from the retrieval date are lower bounds and must not be used to select periods.

## Shared files
Nothing was written under `~/mercans-pipeline`. The proposed appends are in `07-qa-crosscheck/SHARED-APPENDS-PROPOSED.md`. Two more proposals are added below: the C41 `historical` skip and the C39 browser route.
