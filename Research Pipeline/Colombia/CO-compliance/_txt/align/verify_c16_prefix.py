# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - SUPPLEMENTARY VERIFIER.

verify_alignment.py (first pass of this stage) covers CHECK 1-6, but two of its
tests are narrower than the stage brief:

  * CHECK 3 / v2.4 C16 was enforced only in the direction  DD note -> spec ID.
    The rule as written is symmetric: "if A's condition mentions B, then B's
    notes must mention A". This module tests that spec-INTERNAL direction over
    all 563 fields.

  * CHECK 6 tested a HARDCODED list of eight coded identifiers. This module
    sweeps every field whose Example is a letter-prefixed administradora code,
    and additionally requires the Data Dictionary to state the same pattern for
    the fields the two documents share.
"""
import os
import re

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
SP = os.path.join(BASE, "04-reports-spec")
DDF = os.path.join(BASE, "05-data-dictionary", "CO-DD-001-v1.0.xlsx")

SPEC_SHEET = {
    "CO-DIAN-001-NominaElectronica-Spec.xlsx": ("Nomina Electronica Spec", "CO-DIAN-001"),
    "CO-DIAN-002-Formulario350-Spec.xlsx": ("Formulario 350 Spec", "CO-DIAN-002"),
    "CO-PILA-003-AportesSeguridadSocial-Spec.xlsx": ("PILA Spec", "CO-PILA-003"),
    "CO-DIAN-004-Formulario220-Spec.xlsx": ("Formulario 220 Spec", "CO-DIAN-004"),
    "CO-DIAN-005-Formato2276-Spec.xlsx": ("Formato 2276 Spec", "CO-DIAN-005"),
    "CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx": ("Consignacion Cesantias Spec",
                                                     "CO-CESANTIAS-006"),
}
COLS = ["EN", "ES", "RecType", "FieldPos", "PayrollYN", "Mand", "CondReason", "PosFile",
        "Len", "Format", "Example", "SysMap", "Explanation", "RelPayroll", "OptionValues",
        "Rounding", "Neg", "ValType", "Freq", "QueryRA", "RAComments"]

spec, byid = {}, {}
for bk, (sh, sid) in SPEC_SHEET.items():
    wb = openpyxl.load_workbook(os.path.join(SP, bk), read_only=True)
    ws = wb[sh]
    recs = []
    for i, r in enumerate(ws.iter_rows(min_row=3, max_row=ws.max_row, max_col=21,
                                       values_only=True), start=3):
        v = ["" if c is None else str(c).strip() for c in r]
        if not any(v):
            continue
        if v[0].startswith("====") or (v[0] and not any(v[1:])):
            continue
        d = {"row": i, "sid": sid}
        d.update(dict(zip(COLS, v)))
        recs.append(d)
    spec[sid] = recs
    for d in recs:
        if d["FieldPos"]:
            byid.setdefault((sid, d["FieldPos"]), d)
    wb.close()

fails = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("  " + detail) if detail else ""))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------------------
print("\n=== CHECK 3 (extended)  C16 IN THE SPEC-INTERNAL DIRECTION ===")
ID = re.compile(r"(NIA?E\d{3}|T2R\d-\d{3}|A1-\d{3})")
RANGES = (r"(NIA?E)(\d{3})\s*(?:-|to)\s*(?:NIA?E)?(\d{3})",
          r"(T2R\d-)(\d{3})\s*(?:-|to)\s*(?:T2R\d-)?(\d{3})",
          r"(A1-)(\d{3})\s*(?:-|to)\s*(?:A1-)?(\d{3})")


def covered(aid, blob):
    """Does blob reference field aid, directly or via an ID range?"""
    if aid in blob:
        return True
    # a field whose own ID is itself a range ("NIAE001-NIAE213") may be cited
    # in prose as "NIAE001 to NIAE213"
    if re.sub(r"\s*-\s*", " to ", aid) in blob:
        return True
    m0 = re.match(r"^(NIA?E|T2R\d-|A1-)(\d{3})$", aid)
    if not m0:
        # a compound / prose FieldPos label such as "NIAE236, NIAE237 et seq."
        # is reciprocated by a reference to its leading field ID
        lead = ID.search(aid)
        return bool(lead) and lead.group(0) in blob
    for rx in RANGES:
        for m in re.finditer(rx, blob):
            if m.group(1) == m0.group(1) and \
                    int(m.group(2)) <= int(m0.group(2)) <= int(m.group(3)):
                return True
    return False


norev = []
pairs = 0
for sid, recs in spec.items():
    for r in recs:
        if r["Mand"] != "C" or not r["CondReason"]:
            continue
        for t in sorted(set(ID.findall(r["CondReason"]))):
            k = (sid, t)
            if k not in byid or t == r["FieldPos"]:
                continue
            pairs += 1
            o = byid[k]
            if covered(r["FieldPos"], o["CondReason"] + " " + o["Explanation"]):
                continue
            norev.append("%s %s -> %s" % (sid, r["FieldPos"], t))
check("every conditional cross-reference is reciprocated by its target",
      not norev, "%d of %d pairs unreciprocated %s" % (len(norev), pairs, norev[:5]))

nc = [(sid, r["FieldPos"]) for sid, recs in spec.items() for r in recs
      if r["Mand"] == "C" and not r["CondReason"]]
check("every Mandatory=C field still carries a conditional reason", not nc, str(nc[:6]))

# the reverse-reference sentences must not have landed a conditional reason on
# an unconditional row of the two artefacts this patch touched
yc = [(sid, r["FieldPos"]) for sid in ("CO-DIAN-001", "CO-PILA-003")
      for r in spec[sid] if r["Mand"] != "C" and r["CondReason"]]
check("no unconditional row on CO-DIAN-001 / CO-PILA-003 gained a conditional reason",
      not yc, str(yc[:6]))

# ---------------------------------------------------------------------------
print("\n=== CHECK 6 (extended)  FULL PREFIX SWEEP, SPEC AND DD ===")
PC = re.compile(r"^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$")
cands = [(sid, r) for sid, recs in spec.items() for r in recs
         if PC.match(r["Example"].strip())]
nopat = ["%s %s (%s)" % (sid, r["FieldPos"], r["Example"]) for sid, r in cands
         if "attern" not in r["Format"]]
check("every prefixed administradora example states its pattern in column J",
      not nopat, "%d candidates, missing=%s" % (len(cands), nopat))

viol = []
for sid, recs in spec.items():
    for r in recs:
        m = re.search(r"\^[^\s]+\$", r["Format"])
        ex = r["Example"].strip()
        if not m or not ex or ex == "-":
            continue
        try:
            if not re.match(m.group(0), ex):
                viol.append((sid, r["FieldPos"], m.group(0), ex))
        except re.error:
            viol.append((sid, r["FieldPos"], "UNCOMPILABLE", m.group(0)))
check("no example violates the regex its own column J states", not viol, str(viol[:5]))

wb = openpyxl.load_workbook(DDF, read_only=True)
ddfmt = []
for shname, ncol, fcol in (("ID Information", 22, 2), ("Country Fields", 33, 3)):
    ws = wb[shname]
    for r in ws.iter_rows(min_row=5, max_row=ws.max_row, max_col=ncol, values_only=True):
        v = ["" if c is None else str(c).strip() for c in r]
        if any(v):
            ddfmt.append((v[fcol], " ".join(v)))
wb.close()
adm = [n for n, blob in ddfmt if "administradoras catalogue" in blob]
ddnop = [n for n, blob in ddfmt if "administradoras catalogue" in blob
         and "prefix pattern" not in blob]
check("the DD states the same prefix pattern on every administradora field",
      not ddnop, "%d administradora fields, missing=%s" % (len(adm), ddnop))

print("\n" + "=" * 62)
print("SUPPLEMENTARY RESULT: %d check(s) failed" % len(fails))
for f in fails:
    print("   FAILED:", f)
