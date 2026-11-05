# SIR fix R1 - facts ready (2026-11-04, source hunter)

Lock `_research/facts.lock` taken. Backups `_research/sir-fix/_backup-r1/` (register + 5 facts files). Budget: <=25 official-host fetches.

## Findings so far (inspected local copies first)
- Web: KDOR www.ksrevenue.gov unreachable from this machine (curl timeout; WebFetch ECONNREFUSED 2026-11-04); IRS i940.pdf and i109495c.pdf downloaded live 2026-11-04, both still TY2025 editions (md5 1b224db0.../1e96baf7...). Fetches used: 4 of 25.

## Blockers
1. `dd.state.new_hire.dob` (US-NJS5-018): every one of the 10 States has a saved copy that names date of birth, so none is dropped. `_also_register_ids` = US-GAS5-012 (GA FAQ), US-IAS5-012 (Iowa Code 252G.3), US-MES5-016 (19-A MRSA 2154), US-MSS5-007 (MS SDNH fundamentals), US-OHS5-014 (ORC 3121.892), US-ORS5-016 (OR DOJ form PDF), US-WAS5-018 (RCW 26.23), US-WIS5-013 (WI UCB-201 handbook), US-WVS5-016 (WV handbook).
2. `sir.de.withholding.returns`: US-DES5-009 (WTH-REC instructions Rev. 02/03/26, md5 35c2d67950640de7f7c2c2cf2e8eaab5) bound as also-id; value now the copy's words 'filed on or before the last day of January ... duplicate of each ... W-2'.
3. Kansas: `sir.ks.withholding.returns` and `sir.ks.w2.format` re-bound to active row US-KSS5-001 (KW-100 web edition, decompressed copy: KW-5 per period, KW-3/W-2s/1099s due by January 31, KW-3 electronic, KW-2CSV). US-KS-001 removed from both. 'no CF/SF' removed (in neither copy). Live ksrevenue.gov unreachable (unresolved `sir.ks.live_kw100_page`).

## 11 restorations (value in the copy's words, periods unchanged)
dd.ga.new_hire.extra (US-GAS5-012), dd.ia.new_hire.health (US-IAS5-012), multi.iwo.governing_law (US-MULTIS5-007, 42 USC 666 items I-V), sir.dc.ui.agent_authorization (OUCTAX-1; 'statutory' dropped), sir.ga.withholding.agent_authorization (RD-1061/1062/1063), sir.id.ui.agent_authorization, sir.md.withholding.agent_authorization (548P), sir.mn.withholding.returns, sir.nh.ui.agent_authorization ('TPA registration in NHUIS' removed, not in copy -> unresolved `sir.nh.ui.tpa_registration`), sir.nj.ui.agent_authorization, sir.wy.service_supplier (27-3-502 items iv-v).

## Other unverified keys
- sir.la.ui.wage_report: 'Quarterly, mandatory electronic via LWC online services' (US-LAS5-007); LAWATS removed; `_also` US-LAP52-005 dropped.
- rspec.dc.pfml_qtr.channel: 'same due dates as UI' dropped; due dates Apr 30/Jul 31/Oct 31/Jan 31 from US-DCS5-019 table.
- dd.multi.sui_state: US-MULTIS5-017 (UIPL 20-04) added as also-id.
- sir.ms.ui.wage_report: 'or EFW2 RS' dropped; US-MSP51-005 removed; US-MSS5-014 added.
- rspec.co.pfml_qtr.form: effective_from 2026-01-01 with `_effective_from_basis` (FAMLI brief 2026-09-30: 2026 Q3 reports due Oct 31).
- rspec.fed.form940.due, fed.aca.efile_threshold: remain limitations. Live IRS i940.pdf and i109495c.pdf re-downloaded 2026-11-04 are byte-identical to the saved 2025 editions; 2026 finals not published. Values relabelled TY2025 rule; rows stay partial; four unresolved entries added.

## Gaps from SIR-QA1-04 (21 substantive)
Closed by re-binding to a saved authority copy (15): RQ-01 (US-CTS5-016 added), RQ-04 (fed.iwo.priority -> US-FEDP6-002 IWO form), RQ-06 (AK: '1M' -> '$1 million'), RQ-08 (CO TPA page saved, US-COP52-003), RQ-09 (CT batch page saved, new row US-CTS5-036: 'XML or CSV'), RQ-12 (FL RT XML guide extracted from the retained zip; XSD confirmed; both samples re-validated True, needs %20 in schemaLocation), RQ-14 (HI reworded; CPA removed), RQ-24 (MO page saved, US-MOP52-008), RQ-31 (OHID removed), RQ-34 (OR page saved, US-ORP51-005), RQ-35 (PA reworded from US-PAP51-004), RQ-36 (UC-2A in US-PAS5-013), RQ-37 (US-PAS5-009 '10 or more'), RQ-45 (TN page saved: POAs no longer needed; May 27, 2025), RQ-49 (WA PEO page saved, US-FEDP51-016).
Still open (6), each an `unresolved` entry in SIR-facts with attempts and what would close it: RQ-11 FL RTS-9; RQ-19 MA M-2848 (mass.gov 403); RQ-25 MS J-9 (image-only PDF, 0 chars); RQ-27 NE Form 33; RQ-32 OH 2,399 / 200; RQ-33 OH JFS-20106 (page is script-rendered).
New copies (md5 in register verification_method): CO TPA page dfe65ff0..., MO POA (Wayback 2026-06-12) ffaea3d3..., OR OR-AUTH 3a2daa94..., TN TPA FAQ cc1e53d4..., WA PEO 2e767bd9..., CT batch page 846dbe96..., FL RT XML guide 680ed626... (all under 00-official-sources/ccg-sources/<ST>/, each < 200 KB).

## Close-out
Fetches: 15 of 25 (KS x2 failed host unreachable, IRS x2, CO, MO, MA 403, OH, OR, TN, WA, CT batch; FL zip read locally). Facts files rewritten in their original line-ending style; register 2,707 rows x 20 columns; `consumed_by` and `verified_on` (2026-11-04) stamped on all 55 rows cited. `validate_contract --all`: PASS (96 files). Ledger: 5 lines appended to PROPAGATION-LEDGER.md. Lock `_research/facts.lock` taken and released; backups in `_research/sir-fix/_backup-r1/`. Docx untouched. Still partial and unverified for the SIR: rspec.fed.form940.due, fed.aca.efile_threshold (2026 finals unpublished), plus the 6 gaps above.
Builder next: regenerate SIR/RSPEC, close SIR-RQ entries listed above, SIR-QA1-05 RSPEC wording.

STATUS: COMPLETE
