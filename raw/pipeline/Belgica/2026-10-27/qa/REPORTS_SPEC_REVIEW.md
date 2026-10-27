# Belgium Report Specs - Independent Verification Log

9 specs built (BE-NSSO-001/002/003/004/005, BE-FIN-001/002, BE-FEDRIS-001,
BE-FEBELFIN-001), mapped to SIR OUT-01 through OUT-19 (OUT-10/11 folded into
OUT-09 as record-type variants of the same pain.001.001.09 message; 8 outbound
integrations correctly identified as having no file to specify, each with a
specific documented reason - garnishment/vouchers/pension premium have no
public technical spec, GL posting and payslip are not statutory file formats,
Checkinatwork is a presence event, social balance sheet and DB2P are filed by
other parties).

## Independently re-verified
- `verify_specs.py` re-run directly (not just trusted from the build log):
  9/9 PASS - all 9 sheets, 21 columns, correct header/row fill colors, SIR
  OUT-xx cross-reference present in Version Control, population rules >=100
  chars, no F=C without a column G reason.

## Self-correction the build caught in my own prompt
I had instructed the agent to use "Dutch, per CCG Module 1.1's documented
default." This was wrong and the agent caught it rather than complying:
Module 1.1 documents no default - it fixes language by the employer's
region of seat and FORBIDS bilingual documents. Dutch was used anyway for
consistency with the WTC (itself Dutch-only, French flagged as a pending
mandatory second deliverable), and this is stated as a deliberate choice in
each spec's Version Control sheet, not presented as a CCG requirement.

## Genuine finding, independently confirmed with more precision than first stated
"No WTC wage type carries box 360" - confirmed, precisely. The WTC's single
"Fiscal work bonus - withholding tax reduction" wage type's Formula column
correctly describes the bonus splitting across two 281.10 boxes (284 for the
33.14%-credit portion, 360 for the 52.54%-credit portion), but the
STRUCTURED Tax Code column - the field a downstream system would actually
use to route the wage type to a reporting box - carries only "284". A
developer building the Belcotax export from the Tax Code column alone would
never populate box 360. Root cause: one wage type covering a bonus that
statutorily reports to two boxes, with only one box captured in the
structured field. Fix needs its own targeted pass (either split into two
wage types or dual-code the Tax Code column) - not applied here, flagged only.

## Also confirmed via the build's own findings, not independently re-checked
- A source file mislabeling (`FPS-Finance_BV_codenummers_aard_inkomsten.pdf`
  actually contains roerende voorheffing/form-273 codes, not bedrijfsvoorheffing
  income natures) - the build explicitly did not let these leak into
  RevenuNature. Plausible and appropriately cautious; not independently
  re-opened given time, but the protective behavior (checking source content
  against its filename before using it) is exactly right.
- Finprof source dated 2011, currency for IY2026 unresolved - already known
  as SIR gap G13, consistently flagged again here.
- Limosa: 81 DERIVED markers, no sample file - no public technical source
  exists, correctly handled as an honest gap rather than invented detail.

## New follow-up items surfaced (not part of today's build, for later)
- WTC: split or dual-code the fiscal-work-bonus wage type for box 360 (above).
- WTC and SIR both carry "PENDING" placeholders (Form Reference Guide sheet;
  Related Report Spec column on all 19 outbound integrations) that can now
  be completed since Report Specs exists - this is its own follow-up pass,
  deliberately not done during this build per the build's own instructions.

**Status: substantively verified.** Structural re-check passed independently;
the one flagged cross-artifact finding was confirmed with more precision than
originally stated, not just accepted at face value.

---

## FINAL REVIEW PASS - requested explicitly as "one last time," content-level not just structural

### Verified clean - the mislabeled-PDF concern did not leak into operative content
Confirmed the flagged source file (FPS-Finance_BV_codenummers_aard_inkomsten.pdf) genuinely
contains roerende voorheffing content (rates of 25%/15%, VAK II classification structure - matches
form 273, NOT the 26.75%/42.80%/48.15%/53.50% bedrijfsvoorheffing scale verified extensively
elsewhere in this project). Searched all 9 spec files for any trace of this wrong-context content
leaking into operative Field Options or Sheet 4 content: only 4 hits total, all in ONE file
(Finprof274), and all of them are the build's OWN transparent documentation of the mislabeling
(in Version Control) or an explicit out-of-scope exclusion note (in Payroll Scope Summary) - not
leaked wrong codes. Confirms the build's protective claim was accurate.

### Verified clean and mathematically correct - cross-spec identifier consistency
- INSZ/NISS (employee national registry number): identical field definition (length 11, format,
  and the SAME example "85073003328") across all 6 specs that carry it (FEDRIS, Dimona, DmfA, DmfA
  Modification, DRS - appearing at every record type within each). Independently recomputed the
  check digit (97 - (850730033 mod 97) = 97-69 = 28) - matches the example's own last two digits
  exactly. Limosa correctly shows NOT FOUND for the same field, consistent with its documented
  lack of a public technical source.
- KBO/BCE (general enterprise number): identical field definition (length 10, format N(10), same
  example "0123456749") across FEDRIS, Dimona, DmfA, DmfA Modification, DRS. Independently
  recomputed the check digit (97 - (01234567 mod 97) = 97-48 = 49) - matches exactly.

### Genuinely unresolved, not a confirmed defect - NSSO-specific employer number check digit
The separate 9-digit "NSSO Employer Registration Number" field (distinct from KBO/BCE, format
NNNNNNNCC) uses the same example "123456702" consistently across every spec that carries it -
internally consistent. Attempted to verify its check digit using the documented RSZ-number
algorithm (base x100, mod 97, subtract from 96 rather than 97) - this does NOT reproduce "02" for
base 1234567 (yields 49 instead). However, Wikipedia's own documented RSZ-number formats are 7
digits total (a specific public-sector sub-registration only) or 12 digits (the general case) -
neither matches this field's own documented 9-digit (7+2) structure exactly, so the algorithm
found may not be the one that actually applies to this specific NSSO glossary field. Not
confirmed as an error; flagged as a genuinely open question for the eventual alignment-patch
stage, where it can be checked directly against the source NSSO glossary file rather than a
general-purpose secondary explainer.

**Final assessment: the build withstands content-level scrutiny, not just structural self-check.**
Two independent, mathematically-verified consistency checks passed cleanly across every relevant
file; the one previously-flagged risk (mislabeled source) was confirmed not to have caused any
actual leakage; one new item surfaced genuine ambiguity worth a future targeted check, not a
confirmed defect. No new errors requiring correction were found in this final pass.

---

## Follow-up finding from the DD build's cross-check (14 August, later same day)

While cross-checking all 9 report specs against the newly-built Data Dictionary, an
incidental structural issue was surfaced in BE-NSSO-003-DmfAModification-Spec.xlsx:
Sheet 4 block 90169 is still labelled "DMFA ORIGINAL - DECLARATION TYPE CONTAINER"
rather than a modification-specific container label. Given this spec's whole purpose
is to document the MODIFICATION variant of the DmfA declaration (distinct from
BE-NSSO-002, the original), a block still carrying the "ORIGINAL" label suggests
either a copy-paste artifact from building NSSO-003 off NSSO-002's structure, or a
genuine ambiguity in whether this specific block's semantics actually change between
the original and modification declaration types. Not investigated further at time
of logging - flagged for a dedicated Report Specs revision pass.


---

## REGRESSION AUDIT FINDINGS AND FIX (16 August)

A focused, per-artifact regression audit found 2 blockers, 4 majors, 4 minors across
the 9 Report Specs. Both blockers are now fixed and independently verified.

### BE-RSPEC-002 (blocker) - FIXED and verified
538 System Mapping cells said NOT FOUND despite 318 of them being answerable from
DD-CROSSCHECK-TABLE.md column 7. First fix attempt (combined with BE-RSPEC-003
research) hit a genuine connection drop before any file was touched - confirmed via
git diff showing zero changes, not assumed from the interrupted log. Split into a
separate, purely mechanical re-attempt: 318 cells filled (matched by crosscheck row
number AND field-name verification, 538/538 exact, zero mismatches), 220 correctly
left as NOT FOUND. Reconciles exactly: 153+122+122+141=538, 318+220=538.
Independently re-verified: validate_workbook.py PASS on all 9 files.

### BE-RSPEC-003 (blocker) - FIXED and verified
BE-NSSO-003-DmfAModification-Spec.xlsx had all 32 section headers byte-identical to
BE-NSSO-002-DmfA-Spec.xlsx, including block 90169 still labelled as the ORIGINAL
declaration container. Researched properly (NSSO glossary + SFTP manual): confirmed
90169/DmfAOriginal is genuinely original-only, but the correct modification-specific
block number/label does not exist in any held source - honestly marked NOT FOUND
rather than invented. Only 1 of 32 headers changed; the other 31 are legitimately
identical because a DmfA modification restates the corrected quarter in full. Also
fixed the root cause in build_03_dmfa_mod.py (which had been inheriting build_02's
header spine wholesale) so a future rebuild will not regress this.
Independently re-verified: validate_workbook.py PASS, git diff shows exactly the
expected 1-file change, cell-by-cell diff against backup shows exactly 92 changed
cells (89 from the write-back/version fixes, 3 from this fix, nothing else touched).

### Also fixed in the same pass
- Version references updated from BE-DD-001-v1.0 to v1.1 across all 9 specs (62
  cells) - the DD's actual current version.
- A now-false "no DD cross-check was performed" remark (made false by the write-back
  fix) corrected in all 9 specs.
- A v1.2 changelog row added per spec recording both fixes.

### Still open from this regression round (majors/minors, not yet actioned)
- WTC join-key (the code column fixed earlier) is referenced by 0 specs by code,
  168 by name only - the specs don't yet use the new join key.
- 13 field rows where the field NAME itself is NOT FOUND (not just the mapping).
- 148 of 166 Belcotax Query-to-RA rows bulk-filled with one generic sentence.
- 2 minors from the original P1 structure pass, not detailed here.

**Status: both blockers fixed and independently confirmed. Several majors/minors
remain open, lower priority than the two blockers that are now closed.**
