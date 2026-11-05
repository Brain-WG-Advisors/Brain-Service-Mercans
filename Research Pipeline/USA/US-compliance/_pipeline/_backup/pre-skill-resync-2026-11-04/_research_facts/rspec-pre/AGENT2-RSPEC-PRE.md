# Agent 2: RSPEC pre-build research close (2026-11-03)

Scope: SCOPE r3 finding 3, the RSPEC re-syncs from CCG propagation, and triage of the 22 blocking `unresolved[]` items in `_research/RSPEC-facts.json`. I wrote nothing under `01-ccg/`, `04-reports-spec/` or `scope_manifest.json`. Backups of the register, RSPEC facts, RSPEC pack and gaps.json from before this pass are in `_research/rspec-pre/_backup/`.

## 1. SCOPE r3 finding 3: EFW2C Pub. 42-014
- `US-FIL-002` `figure_or_rule_carried` now reads "EFW2 Publication 42-007 and EFW2C Publication 42-014 for tax year 2026 …". `verified_on` is 2026-11-03. `verification_method` = second independent authority. `consumed_by` now includes SCOPE and RSPEC.
- Basis for the number 42-014:
  - the SSA EFW2&EFW2C page, read in Chrome on 2026-10-29 (recorded in gated row US-FEDP52-013);
  - SCDOR W-2 & 1099 Upload page: "For EFW2C file specifications, see SSA Publication No. 42-014" (US-SCS5-016, local html);
  - WI DOR Pub 172 (1/26) (US-WIS5-015).
- The held FED EFW2 TY2026 PDF (`ccg-sources/FED/FED_SSA_EFW2_TY2026_Pub42-007_2026-11-02.pdf`) names the "Correction (EFW2C) file format" and Appendix B, but it does **not** print "42-014" (inspected by text search). It confirms the rule but not the number.
- `26efw2c.pdf` returned curl HTTP 403 on 2026-11-03. It is not held, so the EFW2C record layouts stay out of the pack.
- New fact `fed.efw2c.publication` [US-FIL-002].
- `US-WVS5-002` `consumed_by` now includes SCOPE and RSPEC.

## 2. Re-syncs (PROPAGATION-LEDGER rows 31-36)
| key | CCG | RSPEC | register_id |
|---|---|---|---|
| oh.newhire.report_days | 20 | 20 (unchanged) | US-OHS5-014 (same) |
| ri.report.w2.efile_threshold | 25 | 25 (unchanged) | US-RIS5-018 (same) |
| tx.newhire.report_days | 20 | 20 (unchanged) | US-TXS5-017 (same) |
| fed.fica.oasdi.wage_base | 184,500 (2026) / 192,300 (2027) | added, both periods | US-FEDS5-005 / US-FEDB5-401 |
| ca.sdi.employee.rate | 1.3 % (2026) / 1.4 % (2027) | added, both periods | US-CAP7-002 |

RSPEC was added to `consumed_by` on all five rows. The ledger rows 32-34 "pending RSPEC" can be marked done by agent 4.

## 3. Blocking triage: 22 down to 0
**Closed with keyed facts (4):**
- `rspec.ca.ui_qtr.de9c_file_spec`: `rspec.ca.ui_qtr.file_formats` [US-FIL-006, DE 8300 already on the register].
- `rspec.nc.w2_state.ty2026_spec`: `rspec.nc.w2_state.ty2026_rs_layout` [US-NCS6-001] and `rspec.nc.annual_recon.ty2026_nc3_layout` [US-NCS6-002]. These are the TY2026 PDFs, rev. 09-01-2026, downloaded to `00-official-sources/spec-sources/NC/`. US-NCS5-027 (10-2020) is now superseded.
- `rspec.tx.ui_qtr.due_date`: `rspec.tx.ui_qtr.due` [US-TXS6-002, 40 TAC 815.109] and `rspec.tx.ui_qtr.electronic_media_required` [US-TXS6-001, 815.107]. Confidence is medium because the text comes from the LII reproduction: the SOS viewer moved to an Appian portal.
- `rspec.vt.w2_state.format`: `rspec.vt.w2_state.format` [US-VTS6-001, VT EFW-2 spec page]. Confidence is medium: the RS table is headed "2025" and its positions are inconsistent.

**Narrowed:**
- `rspec.ky.ui_qtr.upload_formats` [US-KYS6-001]: KUIP accepts ICESA or CSV.
- `rspec.mn.ui_qtr.due` [US-MNS5-015 widened, 268.044 subd. 1(a)].

**Correction:** for OK, the earlier closing source "40 O.S. 3-111" was repealed effective 2016-11-01. 40 O.S. 3-102(A) delegates the due date to OESC rules [US-OKS6-001]. The item now points at OAC 240:10-5.

**Documented limitations (18, blocking=false).** Each `why` starts with `[documented_limitation: <reason>]`, and the 2026-11-03 attempts were added to `attempted[]`. Mirrored in `_research/gaps.json` → `RSPEC`.
- access (non-US exit), 11: CO, ID, IL, IN (XML schema), KY (RS), LA, ME, MN (format), MT, OK, WA L&I
- behind employer portal login, 5: DE, IA, NM, OH, UT
- not yet published (TY2026 spec), 2: GA TY2026 layout, TX enhanced layout (51 TexReg 5161 proposed, not adopted; US-TXB5-301)

The access items are independent per-state lookups from a US exit and can be fanned out in parallel. The login items need the operations team or a TPA account.

## 4. Files and validation
- Register: 2,669 rows before, 2,676 after; 7 new rows (US-NCS6-001/-002, US-TXS6-001/-002, US-OKS6-001, US-KYS6-001, US-VTS6-001); all rows have 20 columns; the pre-edit round-trip was byte-identical.
- `RSPEC-facts.json`: 425 facts (13 new); 43 unresolved, 0 blocking. `validate_contract.py facts` gives PASS. Every fact resolves to a register row with RSPEC in `consumed_by`. No fact cites a tier-B or superseded row.
- `RSPEC-research-pack.md`:
  - the 41 "Open for this jurisdiction" lines were regenerated from `unresolved[]` (some were stale since Synthesis D);
  - new section "RSPEC pre-build close (2026-11-03)";
  - the Open questions block was regenerated in full.
- `gaps.json` → `RSPEC`: 18 documented_limitation, 25 open_non_blocking (carried over, not re-triaged), 4 closed. The CCG `gaps[]` list is untouched.
- New source files in `00-official-sources/spec-sources/` (NC, TX, OK, VT), 896 KB. The full OK Title 40 RTF (2.8 MB) was not kept; only the excerpts are.
