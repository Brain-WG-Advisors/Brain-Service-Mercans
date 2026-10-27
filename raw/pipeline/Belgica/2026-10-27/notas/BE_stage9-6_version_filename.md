# BELGIUM — STAGE 9.6: RESOLVE VERSION-vs-FILENAME MISMATCH, PROPAGATE, VERIFY

Run this locally on F5A4T8E, via Claude Code. This closes one specific
follow-up item from the Stage 9.5 handover: the three artefacts' internal
version-control metadata disagrees with their own filenames.

## SCOPE FENCE — WIDER THAN STAGE 9.5, STILL BOUNDED

You may read, edit, rename, and commit:
- `BE-DD-001-v1.3.xlsx` (and its renamed successor)
- `BE-WTC-001-v1.0.xlsx` (and its renamed successor)
- `BE-CCG-001-v1.1.docx` (and its renamed successor, if a rename turns out
  to be needed — see Step 2)
- The 9 files in `04-reports-spec/`, ONLY to update a version-string
  citation that Step 3 confirms points at one of the three files above
- `scope_manifest.json`, same condition
- `handover_status.md`, to record this item as closed

Do not touch `mercans_pipeline_v2_9.sh`, `shared/country_failure_log.md`,
or any file in the working tree not listed above, even if it looks related
or convenient to fix while you're in the area. If propagation surfaces a
citation in a file not on this list, stop and report it rather than
editing it.

## STEP 0 — BASELINE COMMIT

```bash
cd ~/mercans-pipeline/BE-compliance
git add BE-DD-001-v1.3.xlsx BE-WTC-001-v1.0.xlsx BE-CCG-001-v1.1.docx
git add 04-reports-spec/ scope_manifest.json handover_status.md
git commit -m "Pre-rename baseline, version/filename mismatch closure"
```
(If any listed path doesn't exist or isn't tracked yet, add what does
exist by name — don't fall back to `-A`.)

## STEP 1 — CONFIRM THE ACTUAL MISMATCH, DON'T INHERIT THE HANDOVER'S WORDING

Open each file's own Version Control sheet/section and read the current
version number directly. Do not carry over "DD is 1.4, WTC is 1.1, CCG
stays 1.1 but has a 16 Sep revision" from the prior handover as fact —
that is exactly the kind of pre-compaction claim the project's own
standing rule says to re-verify, not trust. Confirm live for each of the
three:
- What version does the Version Control sheet/section actually say, right now?
- What version does the filename actually say, right now?
- Do they match or not?

Produce a small table: File | Internal version (as read) | Filename version | Mismatch Y/N.

For the CCG specifically: if the Version Control section shows a genuine
version bump is owed (content changed 16 Sep but the version number
wasn't incremented), that is a different fix from a pure rename — bump
the version number in the document first, per whatever versioning
convention the CCG's own Version Control section already uses, before
treating it the same as the DD/WTC rename cases.

## STEP 2 — RENAME EACH MISMATCHED FILE

For each file where Step 1 confirmed a real mismatch:
1. Rename the file so the filename matches the confirmed internal version
   (e.g. `BE-DD-001-v1.3.xlsx` → `BE-DD-001-v1.4.xlsx` if internal says 1.4)
2. Do not create a second "previous final" copy or move anything to
   `Archived/` for this specific action — this is a filename correction to
   match already-existing content, not a new version superseding an old
   one. If you find an actual outdated prior-version file still sitting in
   the artifact folder root that this rename would now leave stale, flag
   it, don't silently archive it without saying so.
3. `git mv` rather than a plain OS rename, so the rename itself is tracked

## STEP 3 — PROPAGATE, AND MEASURE BEFORE PROMISING A NUMBER

Search `04-reports-spec/` and `scope_manifest.json` for any citation of
the OLD filename/version string for each renamed file (e.g. a report spec
cell reading `BE-DD-001-v1.3 — 'Field X' (Sheet Y)`). Per the project's
own standing rule on this exact kind of task: measure the real hit count
first, don't assume it's confined to one sheet or one file. Update every
confirmed hit to the new version string. Produce a count: File | Old
string | Hits found | Hits updated. If found = updated for every row,
propagation is complete; if not, say which ones didn't get fixed and why.

## STEP 4 — RE-MEASURE ANYTHING THAT COUNTS AGAINST THE RENAMED FILE

If `scope_manifest.json` or any other file stores a coverage percentage,
mapper-block count, or similar figure computed FROM one of the three
artifacts, re-measure it against the renamed file's actual current
content — don't carry over a pre-rename number. Report old vs. new for
each such figure found; most likely no numeric figure actually changed
(only the filename did), but confirm this rather than assuming it.

## STEP 5 — VERIFY WITH GIT DIFF

```bash
git diff --stat
git diff -- 04-reports-spec/ scope_manifest.json
```
Confirm every propagation hit from Step 3 actually shows in the diff.
Flagged is not fixed — if a hit was reported as "updated" in Step 3 but
doesn't appear in the diff, it didn't land; re-apply it.

## STEP 6 — UPDATE handover_status.md

Add a short, factual note (not a new full report) recording: the
confirmed pre-rename state from Step 1, the renames performed, the
propagation count from Step 3, and that this closes the "version of
record differs from file name" follow-up item from the Stage 9.5 pass.
Leave the rest of the document as-is.

## OUTPUT

Report back: the Step 1 table, the Step 2 renames performed, the Step 3
propagation count table, and confirmation that Step 5's diff matches
Step 3's claims.
