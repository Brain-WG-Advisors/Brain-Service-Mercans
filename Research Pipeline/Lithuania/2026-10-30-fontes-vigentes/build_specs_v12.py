# -*- coding: utf-8 -*-
"""build_specs_v12.py - SAM v1.1 -> v1.2 e GPM313 v1.2 -> v1.3 por cirurgia XML no zip.

Nunca usa openpyxl.save(). Le o valor atual de cada celula (openpyxl, so leitura), aplica
substituicoes de trecho (assert de que o trecho antigo existe), grava a celula como inlineStr
com estilo azul FFDDEBF7 e reempacota o zip copiando as demais partes sem alteracao.
Uso: python build_specs_v12.py
"""
import re, sys, zipfile, pathlib, hashlib
from xml.sax.saxutils import escape
import openpyxl

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "2026-10-29-correcoes"

SHEETFILE = {"Version Control": "sheet1", "Report Matrix": "sheet2", "SAM Spec": "sheet4",
             "GPM313 Spec": "sheet4", "Population Rules": "sheet7", "Example Analysis": "sheet8",
             "Sample File": "sheet9", "Field Options": "sheet6"}

# ----------------------------------------------------------------------------- SAM v1.2
SAM_EDITS = [
    ("Report Matrix", "G2", 13, [
        ("(EDAS) (points 8 and 249)", "(EDAS) (point 8)"),
        ("data structure description (point 250) and must be signed with a qualified electronic signature (",
         "data structure description (point 8; annex 'SAM aprašas v07' to V-243) and must be signed with a qualified electronic signature (point 8; "),
    ]),
    ("Report Matrix", "I2", 13, [
        ("consolidated redaction in force from 2026-01-01 - SOURCE NOT ARCHIVED: that consolidated text (and the SAM-V243-consolidado.pdf cited in v1.0) is not on disk, and e-TAR / e-seimas return HTTP 403 to automated download (tested 2026-10-29); point references to it in this spec (8, 52, 84.1, 86.6-86.8, 88, 91.3.1, 92.4, 95.4, 96.4, 249, 250) remain as in v1.0 pending archiving. Archived locally: the 2015-09-17 wording (lrs494520), whose numbering differs (PT-SAM3SD / PT-SAM3SDP annexes = points 103.6-103.7; late filing = 104.2; non-working-day deadline = 111); ",
         "consolidated redaction in force from 2026-10-03 (e-TAR TAR.34A6775CE75B), archived by Mercans Global Compliance on 2026-10-30 (file 2026-10-30-V-243-suvestine-2026-10-03). The Rules end at point 127; every point cited in this spec was re-checked against that text on 2026-10-30. Renumbering from the 2015-09-17 wording (lrs494520): PT-SAM3SD / PT-SAM3SD-M / PT-SAM3SDP annexes = points 86.6-86.8 (were 103.6-103.7); late filing = point 52 with 91.3.1 (was 104.2); non-working-day deadline = point 125 (was 111); "),
    ]),
    ("Population Rules", "C4", 13, [
        ("with the corrected period stated in the annex (point 92.4) and only the affected insured persons listed (points 95.4 and 96.4).",
         "with the corrected period stated in the annex (point 92.4). P35 belongs to the written (paper) correction route (points 93-97): the employer files a written request together with a new SAM marked 'x' in P35 (points 93-94), P14T and P17T give the corrected year and month (points 95.1-95.2), and the annexes list only the insured persons whose data change (points 95.3-95.4; points 96.3-96.4 for quarters up to 2009-12-31)."),
    ]),
    ("Population Rules", "D4", 13, [
        ("correction affecting one employee only, where points 95.4 and 96.4 require a partial annex;",
         "correction affecting one employee only, where on the written route with P35 the annexes list only the insured persons whose data change (points 95.3-95.4; 96.3-96.4 for quarters up to 2009-12-31);"),
    ]),
    ("Population Rules", "C13", 13, [
        ("Points 8 and 249: SD notifications", "Point 8: SD notifications"),
        ("Point 250 and the SAM v07 data structure description (DSA, V-243 in the V-624 wording)",
         "Point 8 and the SAM v07 data structure description (DSA, annex 'SAM aprašas v07' to V-243, in the V-624 wording)"),
        ("The file must be signed with a qualified electronic signature by the manager",
         "The file must be signed with a qualified electronic signature (point 8) by the manager"),
        ("Point 84.1 notes the employer is informed of acceptance through EDAS.",
         "Point 84.1: the employer is informed through EDAS of the territorial branch decision on data correction or on not recording the submitted data (within 3 working days, point 84); acceptance of the SAM file itself is shown by the DataService status (getDocumentStatus)."),
    ]),
    ("Population Rules", "D13", 13, [
        ("(the archived 2015 wording, point 111, moves the deadline to the next working day; the numbering in force is not archived)",
         "(point 125 moves the end of the deadline to the next working day for SD notifications, which include SAM under point 4.7)"),
    ]),
    ("Population Rules", "D7", 13, [
        ("whether the Guarantee Fund, the Long-term Employment Benefit Fund and the 3 % pension accumulation also stop at the ceiling is an open item (no source read);",
         "position, to confirm with Sodra/BAU how the SAM reports the month the ceiling is crossed (P3, A11, A12): the Guarantee Fund 0,16 % (Law XII-2604 art. 5(3)), the Long-term Employment Benefit Fund 0,16 % (art. 14(3)) and, for participants, the 3 % pension accumulation contribution (Law IX-1691 art. 8(1)) are charged on the income on which social insurance contributions are calculated, at rates set by those laws and not by the budget-indicators law, so they continue above the ceiling together with PSD 6,98 %;"),
        ("position, to confirm with Sodra/BAU how the SAM reports the month the ceiling is crossed (P3, A11, A12): the Guarantee Fund",
         "in the month the ceiling is crossed the SAM keeps A12 = A11 x P3 and Sodra recalculates automatically and notifies the new rate (see C7); position on what continues above the ceiling: the Guarantee Fund"),
    ]),
    ("SAM Spec", "M13", 13, [
        ("Points 95.4 and 96.4 add that in a correction the SAM3SDP annex lists ONLY the insured whose information changes, not the whole population.",
         "P35 itself belongs to the written correction route (points 93-97): a new SAM marked 'x' in P35 is filed with a written request (points 93-94), and its SAM3SDP annex then lists ONLY the insured persons whose data change, not the whole population (point 95.4; point 96.4 for quarters up to 2009-12-31)."),
    ]),
    ("SAM Spec", "T13", 13, [
        ("since points 86 and 91-96 describe PT as the correction mechanism.",
         "since points 86-92 describe PT as the electronic correction mechanism and points 93-97 the written route with P35."),
    ]),
    ("SAM Spec", "M29", 13, [
        ("which point 88 and the signing provision require.",
         "which point 8 requires (point 88 sets the same requirement for PT requests)."),
    ]),
    ("SAM Spec", "T46", 14, [
        ("Residual only: confirm whether the 3 % pension-accumulation contribution (employees in the additional accumulation scheme) is included in P3, and the legal basis of the Guarantee Fund and Long-term Employment Benefit Fund rates (read on the Sodra tariff page only).",
         "Residual only: (a) whether the 3 % pension-accumulation contribution (participants in the accumulation scheme, Law IX-1691 art. 8(1)) is included in P3; (b) how the SAM reports the month in which the 60 VDU ceiling is crossed (P3, A11, A12) - to confirm with Sodra/BAU. Legal basis now read: Guarantee Fund 0,16 % (Law XII-2604 art. 5(3)) and Long-term Employment Benefit Fund 0,16 % (art. 14(3)), both charged on the income on which social insurance contributions are calculated. Position on the ceiling: I-1336 art. 10(9) applies the 0 % rate above 60 VDU only to contributions at rates approved by the annual budget-indicators law and excludes PSD; the Guarantee Fund, Long-term Employment Benefit Fund and 3 % rates are set by XII-2604 and IX-1691, so PSD 6,98 %, Guarantee Fund 0,16 %, Long-term Employment Benefit Fund 0,16 % and, for participants, 3 % continue above the ceiling."),
        ("Residual only: (a) whether the 3 % pension-accumulation contribution (participants in the accumulation scheme, Law IX-1691 art. 8(1)) is included in P3; (b) how the SAM reports the month in which the 60 VDU ceiling is crossed (P3, A11, A12) - to confirm with Sodra/BAU.",
         "Residuals closed on 2026-10-30: (a) the 3 % pension-accumulation contribution (participants, Law IX-1691 art. 8(1)) is included in P3 - the Sodra tariff table gives a separate total 'Bendras su 3 % kaupimu' (e.g. 24,27 against 21,27); (b) in the month the 60 VDU ceiling is crossed the SAM keeps A12 = A11 x P3, Sodra recalculates that month automatically and notifies the employer of the person's new rate, which is P3 from the next month (Sodra page 'Įdarbinimas, pranešimai, įmokos ir tarifai', 2026-05-19; point 55.5). The rate Sodra notifies is authoritative for the months after the ceiling."),
    ]),
    ("Report Matrix", "J2", 13, [
        ("(1) how A11/P3/A12 are filled in the month the 60 VDU annual ceiling is crossed and where the MMA minimum base applies (I-1336 art. 10(7)-(9)); (2) P3 composition for SAM3SDP reason codes 06, 09 and 10 and whether the +3 % pension accumulation is part of P3; legal basis of the Guarantee Fund and Long-term Employment Benefit Fund rates (read on the Sodra tariff page only);",
         "(1) how A11/P3/A12 are filled where the MMA minimum base applies (I-1336 art. 10(7)-(8)); the ceiling month was closed on 2026-10-30 (Population Rules C7: A12 = A11 x P3, Sodra recalculates and notifies the new rate); (2) P3 composition for SAM3SDP reason codes 06, 09 and 10 (the 3 % accumulation is part of P3, and the Guarantee Fund and Long-term Employment Benefit Fund rates rest on Law XII-2604 art. 5(3) and 14(3), both closed on 2026-10-30);"),
    ]),
    ("SAM Spec", "M47", 13, [
        ("Two statutory cases where the plain identity does not hold and the filling rule is still open: the annual ceiling of 60 VDU (I-1336 art. 10(9); 2026 EUR 138 729,00, 0 % above it except PSD) and the MMA minimum base (art. 10(7)-(8); 2026 EUR 1 153) - see Population Rules row 7.",
         "Two statutory cases where the contributions due differ from A11 x P3: the annual ceiling of 60 VDU (I-1336 art. 10(9); 2026 EUR 138 729,00, 0 % above it except PSD) - the SAM keeps A12 = A11 x P3 and Sodra recalculates that month automatically; and the MMA minimum base (art. 10(7)-(8); 2026 EUR 1 153) - filling rule still open. See Population Rules row 7."),
    ]),
    ("Field Options", "E53", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E54", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E55", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E56", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E57", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E58", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E59", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    ("Field Options", "E60", 13, [
        ("its inclusion in P3 is NOT VERIFIED (open item).",
         "its inclusion in P3 is confirmed by the same page, which gives a separate total 'Bendras su 3 % kaupimu' for participants (2026-10-30)."),
    ]),
    # --- 2026-10-30 (tarde): B11 teto, 3 % no P3, TaxRate 5, dia util no Report Matrix
    ("Population Rules", "C7", 13, [
        ("In the month the ceiling is crossed, and after it, A12 differs from A11 x full P3.",
         "In the month the ceiling is crossed the contributions actually due differ from A11 x full P3; the SAM does not show that difference (see the end of this rule)."),
        ("How Sodra expects A11, P3 and A12 to be filled in cases (i) and (ii) is NOT stated in the SAM instruction or the DSA - open item for source research before the build.",
         "Case (i), ceiling: A11, P3 and A12 follow points 55.1, 55.5 and 55.2 unchanged (A12 = A11 x P3, as C2344 checks). When a SAM, 1-SD, 2-SD or 13-SD brings the insured person's income to the ceiling, Sodra recalculates that month's VSD contributions automatically and informs every employer of that person, through the employer's Sodra account, of the change in the person's contribution rate; from the next month P3 is the rate so notified (point 55.5). Source: Sodra page 'Įdarbinimas, pranešimai, įmokos ir tarifai', section on the ceiling ('tą mėnesį VSD įmokos būtų perskaičiuojamos automatiškai'), updated 2026-05-19, archived as an extract by Mercans Global Compliance on 2026-10-30. Case (ii), minimum base: how A11 and A12 show the top-up is NOT stated in the SAM instruction or the DSA - open item."),
    ]),
    ("SAM Spec", "J69", 13, [
        ("Number, 5 characters (MXFD; DSA section 7 lists 11), 2 dp",
         "Number, 5 characters (MXFD; DSA section 7 lists 11, not material - see M69), 2 dp"),
    ]),
    ("SAM Spec", "M69", 13, [
        ("LENGTH DIVERGENCE BETWEEN THE TWO OFFICIAL SOURCES: the DSA section 7 (p. 11) lists P3 TaxRate on SAM3SDP as 'Skaičius 11', while DSA section 6 (the same field on SAM3SD) and the MXFD (SAM-v07.mxfd, FormDef 2018-12-20, PageDef 3, FieldDataDef TaxRate_1..3, CellsInRowCount 5) give 5. Length kept at 5 (column I); a rate such as 21,27 fits both.",
         "LENGTH: the DSA section 7 (p. 11) lists P3 TaxRate on SAM3SDP as 'Skaičius 11', while DSA section 6 (the same field on SAM3SD) and the MXFD give 5. Resolved on 2026-10-30 against the form in force (SAM-v07.mxfd inside Sodra's SAM-v07.zip published 2026-02, FormDef created 2025-12-31; the same in the 2018 and 2025-07 files): 5 cells with 2 decimal places, and the form script rejects any rate outside 0,01-99,99 ('Tarifas turi būti skaičius nuo 0,01 iki 99,99'). A valid rate therefore never exceeds 5 characters and fits both sources. Length kept at 5 (column I)."),
    ]),
    ("Report Matrix", "F2", 13, [
        ("and 9-SD and/or 12-SD notifications were filed for the whole reporting period.",
         "and 9-SD and/or 12-SD notifications were filed for the whole reporting period. If the 15th falls on a Saturday, Sunday or public holiday, the deadline is the next working day (point 125)."),
    ]),
]
SAM_VC = (3, [("A", "LT-SODRA-003", 12), ("B", "1.2", 12), ("C", "2026-10-30", 12),
              ("D", "Mercans Global Compliance", 12),
              ("E", "V-243 point references re-checked against the consolidated text in force from 2026-10-03: points 249/250 replaced by point 8; non-working-day rule = point 125; scope of points 84.1, 88, 95.4/96.4 corrected. 60 VDU ceiling: Guarantee Fund, Long-term Employment Benefit Fund and 3 % read as continuing (XII-2604 art. 5(3), 14(3); IX-1691 art. 8(1)); ceiling month: SAM keeps A12 = A11 x P3, Sodra recalculates and notifies the new rate; 3 % included in P3; TaxRate length 5 confirmed on the 2025-12-31 MXFD (rate 0,01-99,99); next-working-day rule added to Report Matrix F2.", 12)])

# ----------------------------------------------------------------------------- GPM313 v1.3
GPM_EDITS = [
    ("Example Analysis", "D5", 44, [
        ("15 August 2026, which is a Saturday. No primary source held for this build states whether the deadline moves to the next working day (the Law on Tax Administration is not in the source folder), so the date is kept as written and the point stays open.",
         "15 August 2026, which is a Saturday. Under the Law on Tax Administration No. IX-2112 art. 162(6) (consolidated redaction in force from 2026-07-01), where the last day of a term falls on a non-working day or public holiday the term ends on the next working day, so this return is due by Monday 17 August 2026."),
    ]),
    # --- 2026-10-30 (tarde): exemplo e Report Matrix alinhados ao dia util
    ("Sample File", "B4", 45, [
        ("Pateikimo terminas: 2026-08-15", "Pateikimo terminas: 2026-08-17"),
    ]),
    ("Report Matrix", "F2", 44, [
        ("By the 15th day of the month following the reporting month (rule 12, on the basis of GPMI art. 24(2)).",
         "By the 15th day of the month following the reporting month (rule 12, on the basis of GPMI art. 24(2)); where that day is a non-working day or public holiday, the next working day (Law on Tax Administration No. IX-2112 art. 162(6)), e.g. the July 2026 return is due Monday 17 August 2026."),
    ]),
]
GPM_VC = (4, [("A", "LT-VMI-001", 49), ("B", "1.3", 49), ("C", "2026-10-30", 49),
              ("D", "Mercans Global Compliance", 49),
              ("E", "Example Analysis D5: July 2026 return due Monday 17 Aug 2026 (15 Aug is a Saturday; Law IX-2112 art. 162(6) moves the deadline to the next working day); Sample File B4 and Report Matrix F2 aligned.", 47)])


def cell_xml(ref, text, style):
    assert not text.startswith("="), ref
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'


def build(src, dst, edits, vc):
    wb = openpyxl.load_workbook(src)  # leitura apenas
    parts = {}
    zin = zipfile.ZipFile(src)
    log = []
    for sheet, ref, style, reps in edits:
        old = wb[sheet][ref].value
        new = old
        for a, b in reps:
            assert new.count(a) == 1, (sheet, ref, a[:60])
            new = new.replace(a, b)
        f = f"xl/worksheets/{SHEETFILE[sheet]}.xml"
        x = parts.get(f) or zin.read(f).decode("utf-8")
        pat = re.compile(r'<c r="%s"[^>]*?(?:/>|>.*?</c>)' % ref, re.S)
        assert len(pat.findall(x)) == 1, ref
        x = pat.sub(lambda m: cell_xml(ref, new, style), x)
        parts[f] = x
        log.append((sheet, ref, old, new))
    # Version Control: nova linha depois da ultima linha preenchida
    after, cells = vc
    f = "xl/worksheets/sheet1.xml"
    x = parts.get(f) or zin.read(f).decode("utf-8")
    r = after + 1
    assert f'<row r="{r}"' not in x
    end = x.index("</row>", x.index(f'<row r="{after}"')) + len("</row>")
    row = f'<row r="{r}">' + "".join(cell_xml(f"{c}{r}", t, s) for c, t, s in cells) + "</row>"
    parts[f] = x[:end] + row + x[end:]
    for c, t, s in cells:
        log.append(("Version Control", f"{c}{r}", None, t))
    with zipfile.ZipFile(dst, "w") as zout:
        for info in zin.infolist():
            data = parts[info.filename].encode("utf-8") if info.filename in parts else zin.read(info.filename)
            zout.writestr(info, data, compress_type=info.compress_type)
    print(dst.name, hashlib.md5(dst.read_bytes()).hexdigest(), "parts changed:", sorted(parts))
    return log


if __name__ == "__main__":
    import json
    out = {}
    out["SAM"] = build(SRC / "LT-SODRA-003-SAM-Spec_v1.1.xlsx", HERE / "LT-SODRA-003-SAM-Spec_v1.2.xlsx", SAM_EDITS, SAM_VC)
    out["GPM313"] = build(SRC / "LT-VMI-001-GPM313-Spec_v1.2.xlsx", HERE / "LT-VMI-001-GPM313-Spec_v1.3.xlsx", GPM_EDITS, GPM_VC)
    (HERE / "_edits_log.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
