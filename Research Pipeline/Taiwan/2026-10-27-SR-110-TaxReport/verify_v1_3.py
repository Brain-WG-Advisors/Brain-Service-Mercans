# -*- coding: utf-8 -*-
"""Verify v1.3 against the base export: zip parts, XML outside edited cells, cell-by-cell values and styles.
Usage: python -I -X utf8 verify_v1_3.py <base.xlsx> <new.xlsx> <log.txt>
"""
import sys, os, re, zipfile, hashlib
import xml.etree.ElementTree as ET
import openpyxl
def sig(x):
    return ET.tostring(x.to_tree())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits_v1_3 import EDITS

BASE, NEW, LOG = sys.argv[1:4]
out, fails = [], []
def log(s=""): out.append(s)

zb, zn = zipfile.ZipFile(BASE), zipfile.ZipFile(NEW)
nb, nn = [i.filename for i in zb.infolist()], [i.filename for i in zn.infolist()]
log("== 1. Zip parts"); log(f"base parts {len(nb)}, new parts {len(nn)}, same order: {nb == nn}")
if nb != nn: fails.append("zip part list/order differs")
SHEETS = {"Version Control": "xl/worksheets/sheet1.xml", "Report Matrix": "xl/worksheets/sheet2.xml", "Spec": "xl/worksheets/sheet3.xml"}
expected_changed = set(SHEETS[s] for s in EDITS) | {"xl/styles.xml"}
for n in nb:
    a, b = zb.read(n), zn.read(n)
    same = a == b
    if not same and n not in expected_changed: fails.append(f"unexpected change in {n}")
    log(f"  {n}: {'identical' if same else 'CHANGED'} md5 {hashlib.md5(a).hexdigest()[:8]} -> {hashlib.md5(b).hexdigest()[:8]}")

log("\n== 2. XML well-formed + nothing changed outside edited cells")
for n in sorted(expected_changed):
    try: ET.fromstring(zn.read(n)); log(f"  {n}: well-formed")
    except Exception as e: fails.append(f"{n} not well-formed: {e}")
for sheet, part in SHEETS.items():
    if sheet not in EDITS: continue
    a, b = zb.read(part).decode(), zn.read(part).decode()
    for ref in EDITS[sheet]:
        p = re.compile(r'<c r="%s"[^>]*?(?:/>|>.*?</c>)' % ref, re.S)
        a, ka = p.subn(f"@@{ref}@@", a, count=1); b, kb = p.subn(f"@@{ref}@@", b, count=1)
        assert ka == kb == 1, (sheet, ref)
    ok = a == b
    log(f"  {part} ({sheet}) with the {len(EDITS[sheet])} edited cells masked: {'IDENTICAL' if ok else 'DIFFERENT'}")
    if not ok: fails.append(f"{part}: change outside edited cells")
sa, sb = zb.read("xl/styles.xml").decode(), zn.read("xl/styles.xml").decode()
fa = re.search(r'<fills count="(\d+)">(.*?)</fills>', sa, re.S); fb = re.search(r'<fills count="(\d+)">(.*?)</fills>', sb, re.S)
xa = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sa, re.S); xb = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sb, re.S)
styles_ok = (fb.group(2).startswith(fa.group(2)) and xb.group(2).startswith(xa.group(2))
             and sa.replace(fa.group(0), "F").replace(xa.group(0), "X") == sb.replace(fb.group(0), "F").replace(xb.group(0), "X"))
log(f"  xl/styles.xml: only appended fills {fa.group(1)}->{fb.group(1)} and cellXfs {xa.group(1)}->{xb.group(1)}: {styles_ok}")
if not styles_ok: fails.append("styles.xml changed beyond appends")

log("\n== 3. Cell by cell (all sheets, values + fill + font + border + number format + alignment)")
wa, wn = openpyxl.load_workbook(BASE), openpyxl.load_workbook(NEW)
if wa.sheetnames != wn.sheetnames: fails.append("sheet names differ")
total_diff = 0
for ws in wa.worksheets:
    wsn = wn[ws.title]
    exp = EDITS.get(ws.title, {})
    mr, mc = max(ws.max_row, wsn.max_row), max(ws.max_column, wsn.max_column)
    nd, extra = 0, []
    for r in range(1, mr + 1):
        for c in range(1, mc + 1):
            ca, cn = ws.cell(r, c), wsn.cell(r, c)
            ref = ca.coordinate
            va, vn = ca.value, cn.value
            fill_a = ca.fill.fgColor.rgb if ca.fill.fill_type else None
            fill_n = cn.fill.fgColor.rgb if cn.fill.fill_type else None
            if ref in exp:
                want = exp[ref][0]
                okv = (vn == want) or (isinstance(want, float) and isinstance(vn, (int, float)) and abs(vn - want) < 1e-9) \
                      or (ref == "C14" and ws.title == "Version Control" and hasattr(vn, "year") and vn.date().isoformat() == "2026-10-27")
                okf = fill_n == "FFDDEBF7"
                okstyle = (sig(ca.font) == sig(cn.font) and sig(ca.border) == sig(cn.border) and ca.number_format == cn.number_format)
                nd += 1
                log(f"  [{ws.title}!{ref}] value_ok={okv} fill={fill_n} font/border/numfmt_kept={okstyle}")
                log(f"      before: {repr(va)[:300]}")
                log(f"      after : {repr(vn)[:300]}")
                if not (okv and okf and okstyle): fails.append(f"{ws.title}!{ref} not as intended")
            else:
                if va != vn or sig(ca.fill) != sig(cn.fill) or sig(ca.font) != sig(cn.font) \
                   or sig(ca.border) != sig(cn.border) or ca.number_format != cn.number_format \
                   or sig(ca.alignment) != sig(cn.alignment) or sig(ca.protection) != sig(cn.protection):
                    extra.append(ref)
    total_diff += nd
    log(f"  -- {ws.title}: {mr}x{mc} cells compared; edited {nd}; differences outside scope: {len(extra)} {extra[:20]}")
    if extra: fails.append(f"{ws.title}: differences outside scope {extra}")
    if ws.merged_cells.ranges != wsn.merged_cells.ranges and set(map(str, ws.merged_cells.ranges)) != set(map(str, wsn.merged_cells.ranges)):
        fails.append(f"{ws.title}: merged cells differ")
    dva = sorted((str(d.sqref), d.formula1) for d in ws.data_validations.dataValidation)
    dvn = sorted((str(d.sqref), d.formula1) for d in wsn.data_validations.dataValidation)
    if dva != dvn: fails.append(f"{ws.title}: data validations differ")
log(f"\nTotal edited cells: {total_diff}")
log("RESULT: " + ("PASS - no difference outside scope" if not fails else "FAIL"))
for f in fails: log("  FAIL: " + f)
open(LOG, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[-6:]))
