# -*- coding: utf-8 -*-
"""edit_sections_v12b.py - 2a rodada da v1.2 (30/10 tarde): G10 (S13 p. 77.1.1) e G16 (sam-v07.mxfd arquivado).
Aplica sobre as secoes ja editadas pela edit_sections_v12.py; cada trecho antigo deve existir 1 vez."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
S = pathlib.Path(__file__).resolve().parent / "sections"
E = {
"s05_errors.md": [
    ("Which route an employer system should automate is open (G10) |",
     "From 2010 onward data are corrected only electronically (S13 point 77.1.1), so an employer system automates the PT route; whether DataService accepts PT requests is open (G10) |"),
    ("S13 points 52, 86.6-86.8, 87, 88, 91.3.1, 93-95; A1 |", "S13 points 52, 77.1.1, 86.6-86.8, 87, 88, 91.3.1, 93-95; A1 |"),
    ("or a new SAM with P35 (written), S13 points 86-95; route for automation open |",
     "or a new SAM with P35 (written), S13 points 86-95; from 2010 only the electronic PT route applies (S13 point 77.1.1); DataService acceptance of PT open |"),
],
"s06_sla.md": [
    ("Route for automation open (G10) |",
     "From 2010 onward only the electronic PT route applies (S13 point 77.1.1); DataService acceptance of PT open (G10) |"),
],
"s07_sources.md": [
    ("| Form version 07; extract only |",
     "| Form version 07; instruction held as an extract; `sam-v07.mxfd` archived on 30 October 2026 (form definition created 2025-12-31, from Sodra's SAM-v07.zip) |"),
],
"s08_gaps.md": [
    ("Not confirmed: which route Sodra expects an employer system to automate, and whether DataService accepts PT requests |",
     "From 2010 onward data are corrected only electronically (S13 point 77.1.1), so the PT route is the one to automate. Not confirmed: whether DataService accepts PT requests (`getPossibleDocuments`) |"),
    ("| G16 | S1 to S3 | Sodra originals not archived: the S1 page with `sam-v07.mxfd`, the S2 page and the DataService instruction (S3) were read in a browser and are held as extracts only. The V-243 rules behind S1 and S4 are archived as S13. To close: save the DataService PDF, `sam-v07.mxfd` and the S1 and S2 pages with checksums |",
     "| G16 | S2, S3 | Sodra originals not archived: the S2 page and the DataService instruction (S3) were read in a browser and are held as extracts only. Archived: the V-243 rules behind S1 and S4 (S13) and, on 30 October 2026, `sam-v07.mxfd` (form definition created 2025-12-31). To close: save the DataService PDF and the S2 page with checksums |"),
    ("- It does not claim which SAM correction route Sodra expects an employer system to automate (G10),",
     "- It does not claim that DataService accepts PT requests (G10),"),
],
"s00_control.md": [
    ("G16 narrowed to the non-V-243 Sodra originals; references to A1 v1.2, A2 v1.3 and A3 v1.2 |",
     "G16 narrowed to the S2 page and the DataService instruction (`sam-v07.mxfd` archived); G10 narrowed to DataService acceptance of PT requests (S13 point 77.1.1); references to A1 v1.2, A2 v1.3 and A3 v1.2 |"),
],
}
for fn, reps in E.items():
    p = S / fn
    t = p.read_text(encoding="utf-8")
    for a, b in reps:
        assert t.count(a) == 1, (fn, a[:70], t.count(a))
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8")
    print("ok", fn, len(reps))
