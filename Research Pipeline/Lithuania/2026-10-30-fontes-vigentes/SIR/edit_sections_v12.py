# -*- coding: utf-8 -*-
"""edit_sections_v12.py - edicoes da v1.2 nas copias de sections/ (cada trecho antigo deve existir 1 vez)."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
S = pathlib.Path(__file__).resolve().parent / "sections"

E = {
"s00_control.md": [
    ("| Version | v1.1 |", "| Version | v1.2 |"),
    ("Report Specifications LT-SODRA-003 (SAM) v1.1, LT-VMI-001 (GPM313) v1.2 and LT-VMI-002 (GPM312) v1.2 (A1 to A3)",
     "Report Specifications LT-SODRA-003 (SAM) v1.2, LT-VMI-001 (GPM313) v1.3 and LT-VMI-002 (GPM312) v1.2 (A1 to A3)"),
    ("Sodra source status stated (G16); references to A1 v1.1, A2 v1.2 and A3 v1.2 |\n",
     "Sodra source status stated (G16); references to A1 v1.1, A2 v1.2 and A3 v1.2 |\n"
     "| v1.2 | 2026-10-30 | Mercans Compliance Regulations Team | Sources in force archived and read: Sodra SD notice rules V-243, consolidated text from 2026-10-03 (S13), and the Law on Tax Administration IX-2112, consolidated text from 2026-07-01 (S14). Non-working-day deadline rule stated for SAM (S13 point 125), GPM313 and GPM312 (S14 art. 162(6)); G15 closed. SAM late filing and correction routes stated from S13 (5.1, 6.3); G10 narrowed; G16 narrowed to the non-V-243 Sodra originals; references to A1 v1.2, A2 v1.3 and A3 v1.2 |\n"),
    ("Version 1.1 follows an independent review of version 1.0 and refers to the specification versions issued at the same time (A1 v1.1, A2 v1.2, A3 v1.2).",
     "Version 1.1 followed an independent review of version 1.0. Version 1.2 adds the Sodra and VMI texts in force (S13, S14) and refers to the specification versions issued at the same time (A1 v1.2, A2 v1.3, A3 v1.2)."),
    ("Cited by source key S1 to S12;", "Cited by source key S1 to S14;"),
    ("S11 and S12 were read on 29 October 2026. The Sodra sources S1 to S4 are held as extracts only; the originals are not archived (Appendix A, G16).",
     "S11 and S12 were read on 29 October 2026, S13 and S14 on 30 October 2026. The SAM and NP-SD2 filling rules behind S1 and S4 are now archived in the V-243 text in force (S13); the other Sodra originals are held as extracts only (Appendix A, G16)."),
],
"s02_outbound.md": [
    ("| OUT-01 | Monthly, by the **15th of the following month** (S1 point 52) |",
     "| OUT-01 | Monthly, by the **15th of the following month** (S13 point 52); if that day is a Saturday, Sunday or public holiday, the next working day (S13 point 125) |"),
    ("(GPM313 rules §16, §17). Whether a deadline falling on a non-working day moves to the next working day: G15 |",
     "(GPM313 rules §16, §17). A deadline falling on a non-working day or public holiday moves to the next working day (S14 art. 162(6)) |"),
    ("(GPM312 rules §61, §62). Non-working-day rule: G15 |",
     "(GPM312 rules §61, §62). A deadline falling on a non-working day or public holiday moves to the next working day (S14 art. 162(6)) |"),
],
"s05_errors.md": [
    ("| Correction of filed SAM data | The SAM data-structure description version 07 carries a revised-notice flag (P35 *\"Patikslintas pranešimas\"*) and the revised period (P14T year, P17T month). The 2015 consolidated text of the SD rules required an incorrect SD notice to be corrected without delay (point 76) and provided the PT annexes PT-SAM3SD and PT-SAM3SDP (points 103.6, 103.7); A1 records PT annexes and PT reason code 01 for late SAM data. The text of the SD rules in force today was not available, so which route applies now is open (G10) | S11 page 10; S12 points 76, 103.6, 103.7; A1 |",
     "| Correction of filed SAM data | The SD rules in force (S13) provide two routes. Electronic: a PT request through EDAS, filed without delay when the employer finds incorrect data or files late (points 87, 88), with the annex PT-SAM3SD, PT-SAM3SD-M (whole calendar year) or PT-SAM3SDP (points 86.6-86.8); a late SAM needs a PT request with reason code 01 (points 52, 91.3.1). Written: a written request with a new SAM marked 'x' in P35 (*\"Patikslintas pranešimas\"*), the corrected year and month in P14T and P17T, and only the insured persons whose data change (points 93-95; S11 page 10). Which route an employer system should automate is open (G10) | S11 page 10; S13 points 52, 86.6-86.8, 87, 88, 91.3.1, 93-95; A1 |"),
    ("content validation codes C23xx as cited by A1; correction through the revised-notice fields or PT annexes, current route not confirmed | G10, G14 |",
     "content validation codes C23xx as cited by A1; correction through PT annexes (electronic) or a new SAM with P35 (written), S13 points 86-95; route for automation open | G10, G14 |"),
],
"s06_sla.md": [
    ("| OUT-01 | SAM | Monthly | 15th of the following month | S1 point 52 |",
     "| OUT-01 | SAM | Monthly | 15th of the following month | S13 point 52 |"),
    ("The VMI instructions and the SAM instruction state the deadline as a calendar day. Whether a deadline that falls on a non-working day moves to the next working day for OUT-01, OUT-03 and OUT-04 is not stated in the sources read for this register (G15); only the NP-SD2 instruction states it (S4 point 57).",
     "The VMI instructions and the SAM instruction state the deadline as a calendar day. Where the last day falls on a non-working day (Saturday or Sunday) or an official public holiday, the deadline moves to the next working day: for SD notices, SAM included, under S13 point 125; for GPM313 and GPM312 under the Law on Tax Administration, S14 art. 162(6). Example: the GPM313 for July 2026 is due on Monday 17 August 2026, because 15 August 2026 is a Saturday. The NP-SD2 rule states the same (S4, S13 point 57)."),
    ("| OUT-01 SAM | Not established: current correction route open (G10) | S11; S12 |",
     "| OUT-01 SAM | A PT request is filed without delay once incorrect data are found or a SAM is filed late (S13 point 87); late SAM: PT reason code 01 (S13 points 52, 91.3.1). Route for automation open (G10) | S11; S13 |"),
],
"s07_sources.md": [
    ("All sources were read on 27 October 2026; S11 and S12 were added on 29 October 2026. The VMI sources S5 to S10 and the Sodra text S12 are archived in the Compliance knowledge base. The Sodra sources S1 to S4 were read in a browser because sodra.lt refuses scripted downloads: only extracts are kept and the originals are not archived (G16), so their page and point references can be re-checked only on the live pages.",
     "All sources were read on 27 October 2026; S11 and S12 were added on 29 October 2026 and S13 and S14 on 30 October 2026. The VMI sources S5 to S10, the Sodra texts S12 and S13 and the law S14 are archived in the Compliance knowledge base. The SAM and NP-SD2 filling rules cited from S1 (points 48-56) and S4 (points 57-76) are points of the V-243 text in force and can be re-checked in S13. The other Sodra sources (the S1 page and `sam-v07.mxfd`, S2, S3) were read in a browser because sodra.lt refuses scripted downloads: only extracts are kept and the originals are not archived (G16)."),
    ("| A1 | LT-SODRA-003-SAM-Spec | v1.1 |", "| A1 | LT-SODRA-003-SAM-Spec | v1.2 |"),
    ("| A2 | LT-VMI-001-GPM313-Spec | v1.2 |", "| A2 | LT-VMI-001-GPM313-Spec | v1.3 |"),
    ("| S12 | Sodra SD notice rules (order V-243 of 4 June 2010), consolidated text in force from 2015 | 2015 consolidation; superseded text, used only to show the earlier correction route | Correction of SD notices (points 76, 103.6, 103.7) |",
     "| S12 | Sodra SD notice rules (order V-243 of 4 June 2010), consolidated text in force from 2015 | 2015 consolidation; superseded by S13, kept only for the earlier numbering | Earlier numbering of the correction points (76, 103.6, 103.7) |\n"
     "| S13 | Sodra SD notice rules (order V-243 of 4 June 2010, in the wording of order V-683 of 23 December 2016, as amended), consolidated text in force from 2026-10-03, e-TAR TAR.34A6775CE75B | In force from 2026-10-03; archived 2026-10-30 | SAM filling rules and deadline (points 48-56, 52), NP-SD2 (points 57-76), PT correction (points 86-92), written correction with P35 (points 93-97), non-working-day deadline (point 125) |"),
    ("| S10 | EDS help items on notification contacts",
     "| S14 | Law on Tax Administration No. IX-2112, consolidated text in force from 2026-07-01 | In force from 2026-07-01; archived 2026-10-30 | Non-working-day deadline for GPM313 and GPM312 (art. 162(6)) |\n| S10 | EDS help items on notification contacts"),
],
"s08_gaps.md": [
    ("| G10 | OUT-01 | Late filing and correction of SAM: the SAM data-structure description has a revised-notice flag (S11); the 2015 text of the SD rules used PT annexes (S12); A1 records PT annexes and PT reason code 01 for late data. The SD rules in force today were not available, so the current route is not confirmed | Error handling | Sodra |",
     "| G10 | OUT-01 | Correction of SAM: the SD rules in force (S13) set a PT electronic route (points 86-92; late SAM with reason code 01, points 52, 91.3.1) and a written route with a new SAM marked P35 (points 93-97). Not confirmed: which route Sodra expects an employer system to automate, and whether DataService accepts PT requests | Error handling | Sodra |"),
    ("| G15 | OUT-01, OUT-03, OUT-04 | Whether a filing deadline that falls on a non-working day moves to the next working day; the rule is not in the sources read (VMI instructions, SAM instruction), and the general rule (Law on Tax Administration; general SD notice rules) was not available | Deadline | VMI; Sodra |\n",
     ""),
    ("| G16 | S1 to S4 | Sodra originals not archived: the pages and the DataService instruction were read in a browser and are held as extracts only. To close: save the DataService PDF, `sam-v07.mxfd` and the S2 and S4 pages with checksums | Source archiving | Mercans Compliance |",
     "| G16 | S1 to S3 | Sodra originals not archived: the S1 page with `sam-v07.mxfd`, the S2 page and the DataService instruction (S3) were read in a browser and are held as extracts only. The V-243 rules behind S1 and S4 are archived as S13. To close: save the DataService PDF, `sam-v07.mxfd` and the S1 and S2 pages with checksums | Source archiving | Mercans Compliance |"),
    ("- It does not claim the current Sodra correction route for SAM (G10) or the SAM validation catalogue (G14) beyond what A1 records.\n- It does not claim a next-working-day shift for the SAM, GPM313 or GPM312 deadlines (G15).",
     "- It does not claim which SAM correction route Sodra expects an employer system to automate (G10), or the SAM validation catalogue (G14) beyond what A1 records.\n\n## 8.4 Gaps closed in version 1.2\n\n- G15 (non-working-day deadline): closed. SAM and other SD notices: S13 point 125. GPM313 and GPM312: S14 art. 162(6). See Section 6.1."),
],
}

for fn, reps in E.items():
    p = S / fn
    t = p.read_text(encoding="utf-8")
    for a, b in reps:
        assert t.count(a) == 1, (fn, a[:80], t.count(a))
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8")
    print("ok", fn, len(reps))
