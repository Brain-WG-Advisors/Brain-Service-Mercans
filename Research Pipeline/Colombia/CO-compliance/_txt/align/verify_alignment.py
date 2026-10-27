# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - VERIFIER. Re-runs all six checks against the
rebuilt CO-DD-001-v1.0.xlsx and 04-reports-spec/*.xlsx."""
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
    "CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx": ("Consignacion Cesantias Spec", "CO-CESANTIAS-006"),
}
COLS = ["EN", "ES", "RecType", "FieldPos", "PayrollYN", "Mand", "CondReason", "PosFile",
        "Len", "Format", "Example", "SysMap", "Explanation", "RelPayroll", "OptionValues",
        "Rounding", "Neg", "ValType", "Freq", "QueryRA", "RAComments"]

spec, opts, short = {}, {}, {}
for b, (sh, sid) in SPEC_SHEET.items():
    wb = openpyxl.load_workbook(os.path.join(SP, b), read_only=True)
    recs = []
    ws = wb[sh]
    for i, r in enumerate(ws.iter_rows(min_row=3, max_row=ws.max_row, max_col=21,
                                       values_only=True), start=3):
        v = ["" if c is None else str(c).strip() for c in r]
        if not any(v):
            continue
        if v[0].startswith("====") or (v[0] and not any(v[1:])):
            continue
        d = {"row": i}
        d.update(dict(zip(COLS, v)))
        recs.append(d)
    spec[b] = recs
    short[b] = sid
    ws = wb["Field Options"]
    cur, d = None, {}
    for r in list(ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=4, values_only=True))[2:]:
        a, c, vv, n = ["" if x is None else str(x).strip() for x in (r + (None,) * 4)[:4]]
        if a.startswith("==="):
            cur = a.strip("= ").strip()
            d.setdefault(cur, [])
            continue
        if not any([a, c, vv, n]):
            continue
        d.setdefault(cur or "(none)", []).append([a, c, vv, n])
    opts[b] = d
    wb.close()

wb = openpyxl.load_workbook(DDF, read_only=True)
ws = wb["Country Option Mappers"]
mappers, cur = {}, None
for r in ws.iter_rows(min_row=3, max_row=ws.max_row, max_col=7, values_only=True):
    v = ["" if c is None else str(c).strip() for c in r]
    if v[1]:
        cur = v[1]
        mappers.setdefault(cur, {"codes": [], "note": v[6]})
    if cur and v[2]:
        mappers[cur]["codes"].append((v[2], v[3], v[4], v[5]))
ddrows = []
for sh, ncol, fcol, ncol_notes in (("ID Information", 22, 2, 21),
                                   ("Country Fields", 33, 3, 22)):
    w = wb[sh]
    for i, r in enumerate(w.iter_rows(min_row=5, max_row=w.max_row, max_col=ncol,
                                      values_only=True), start=5):
        v = ["" if c is None else str(c).strip() for c in r]
        if not any(v):
            continue
        ddrows.append({"sheet": sh, "row": i, "name": v[fcol],
                       "notes": v[ncol_notes], "mapper": v[fcol + 8]})
wb.close()

fails = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("  " + detail) if detail else ""))
    if not ok:
        fails.append(name)


print("\n=== CHECK 1  OPTION MAPPER CODE ALIGNMENT (F1) ===")
# Worker Type must be a strict subset of Anexo table 5.5.3
T553 = {"01", "02", "04", "12", "18", "19", "21", "22", "23", "30", "31", "47",
        "51", "54", "56", "58"}
wt = {c for c, _, _, _ in mappers["Worker Type"]["codes"]}
check("DD Worker Type is a subset of Anexo table 5.5.3", wt <= T553,
      "extra=%s" % sorted(wt - T553))
T554 = {"00", "01"}
wst = {c for c, _, _, _ in mappers["Worker Sub-Type"]["codes"]}
check("DD Worker Sub-Type documents the 5.5.4 / PILA dual catalogue",
      "table 5.5.4" in mappers["Worker Sub-Type"]["note"]
      and "single digit" in mappers["Worker Sub-Type"]["note"],
      "codes=%s (5.5.4 admits %s)" % (sorted(wst), sorted(T554)))
# code 47 abbreviation must match Anexo table 5.2.1 verbatim label
a47 = [a for c, a, _, _ in mappers["Employee Document Type"]["codes"] if c == "47"]
check("DD Employee Document Type 47 abbreviation = PEP (table 5.2.1)", a47 == ["PEP"], str(a47))
# the PILA letter catalogue exists and is complete
pila_letters = {c for c, _, _, _ in
                mappers.get("Employee Document Type (PILA / Cesantias)", {"codes": []})["codes"]}
check("DD carries the PILA/cesantias letter catalogue (AT2 campo 3)",
      {"CC", "CE", "TI", "PA", "CD", "SC", "RC", "PE"} <= pila_letters,
      "missing=%s" % sorted({"CC", "CE", "TI", "PA", "CD", "SC", "RC", "PE"} - pila_letters))

# spec Sheet 6 vs DD mapper, for the tables that exist on both sides
PAIRS = [
    ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "TIPO DE DOCUMENTO DE IDENTIFICACION",
     "Employee Document Type"),
    ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "PERIODO DE NOMINA", "Pay Frequency"),
    ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "TIPO DE CONTRATO", "Contract Type"),
    ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "MEDIO DE PAGO", "Payment Method"),
    ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "CLASE DE APORTANTE", "Class of Contributor"),
    ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "TIPO DOCUMENTO COTIZANTE",
     "Employee Document Type (PILA / Cesantias)"),
    ("CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx", "CODIGO DEL FONDO DE CESANTIAS",
     "Severance-Savings Fund"),
    ("CO-DIAN-004-Formulario220-Spec.xlsx", "PARENTESCO", "Dependant Relationship"),
]
for b, secpfx, mname in PAIRS:
    sec = next((k for k in opts[b] if k.startswith(secpfx)), None)
    if sec is None:
        check("Sheet 6 section %r exists in %s" % (secpfx, short[b]), False)
        continue
    scodes = {r[0] for r in opts[b][sec] if not r[0].startswith("(")}
    dcodes = {c for c, _, _, _ in mappers[mname]["codes"]}
    sabb = {r[0]: r[1] for r in opts[b][sec] if not r[0].startswith("(")}
    dabb = {c: a for c, a, _, _ in mappers[mname]["codes"]}
    # a DD code whose own English Description scopes it to a DIFFERENT channel
    # ("... ONLY") is not expected in this artefact's Sheet 6 table
    scoped_out = {c for c, _, _, eng in mappers[mname]["codes"]
                  if " ONLY" in eng.upper()}
    dcodes = dcodes - scoped_out
    common = scodes & dcodes
    mismatch = [c for c in common if sabb.get(c) and dabb.get(c)
                and sabb[c] != dabb[c] and not sabb[c].isdigit() and not dabb[c].isdigit()]
    check("%s %r codes reconcile with DD %r" % (short[b], secpfx[:26], mname),
          dcodes <= scodes and not mismatch,
          "dd_only=%s abbrev_mismatch=%s" % (sorted(dcodes - scodes), mismatch))

print("\n=== CHECK 2  FIELD CLASSIFICATION (F3) ===")
bad = []
for b, recs in spec.items():
    for r in recs:
        sm = r["SysMap"]
        if r["PayrollYN"] == "N" and re.match(r"^(Employee|Company|Contract)\.", sm):
            bad.append("%s %s N/%s" % (short[b], r["FieldPos"], sm))
        if r["PayrollYN"] == "Y" and re.match(
                r"^(Payroll|SUM|Mercans|System|PayPeriod|Constant)", sm):
            bad.append("%s %s Y/%s" % (short[b], r["FieldPos"], sm))
check("col E agrees with the System Mapping namespace on every field", not bad, str(bad[:6]))
# every Payroll=Y master-data mapping must exist in the DD
ddtok = set()
for r in ddrows:
    ddtok |= set(re.findall(r"(?:Employee|Company|Contract|Payroll)\.[A-Za-z0-9_]+", r["notes"]))
miss = set()
for b, recs in spec.items():
    for r in recs:
        if r["PayrollYN"] != "Y":
            continue
        m = re.match(r"^((?:Employee|Company|Contract)\.[A-Za-z0-9_]+)", r["SysMap"])
        if m and m.group(1) not in ddtok:
            miss.add(m.group(1))
check("every Payroll-Field=Y mapping has a Data Dictionary row", not miss, str(sorted(miss)))

print("\n=== CHECK 3  MANDATORY / CONDITIONAL + C16 BIDIRECTIONAL REFS (F13) ===")
noc = [(short[b], r["FieldPos"]) for b, recs in spec.items() for r in recs
       if r["Mand"] == "C" and not r["CondReason"]]
check("every Mandatory=C field carries a conditional reason", not noc, str(noc[:6]))
byid = {}
for b, recs in spec.items():
    for r in recs:
        if r["FieldPos"]:
            byid[(short[b], r["FieldPos"])] = r
bymap = {}
for b, recs in spec.items():
    for r in recs:
        m = re.match(r"^([A-Za-z]+\.[A-Za-z0-9_]+)", r["SysMap"])
        if m:
            bymap.setdefault(m.group(1), []).append((short[b], r["FieldPos"]))
PATS = {"CO-DIAN-001": r"NI[A]?E\d+", "CO-PILA-003": r"(?:A1-\d+|T2R\d-\d+)",
        "CO-CESANTIAS-006": r"(?<![A-Z])(?:T\d{2}|E\d{2}|MA\d{2})(?![0-9])",
        "CO-DIAN-005": r"(?:N\d{2}|ENV-\d+)"}
stale, incomplete = [], []
allnotes = list(ddrows) + [{"sheet": "Country Option Mappers", "row": 0, "name": k,
                            "notes": v["note"]} for k, v in mappers.items()]
for r in allnotes:
    note = r["notes"]
    m = re.search(r"Spec ref:\s*([A-Za-z]+\.[A-Za-z0-9_]+)", note)
    truth = bymap.get(m.group(1), []) if m else []
    for sid, pat in PATS.items():
        t = {i for s, i in truth if s == sid}
        cited = set(re.findall(pat, note))
        if not m:
            for c in cited:
                if (sid, c) not in byid:
                    stale.append("%s r%s %s: %s %s does not exist" %
                                 (r["sheet"][:2], r["row"], r["name"][:26], sid, c))
            continue
        for c in cited - t:
            if (sid, c) not in byid:
                stale.append("%s r%s %s: %s %s does not exist" %
                             (r["sheet"][:2], r["row"], r["name"][:26], sid, c))
        if t and not (t & cited) and truth:
            incomplete.append("%s r%s %s: %s missing %s" %
                              (r["sheet"][:2], r["row"], r["name"][:26], sid, sorted(t)))
check("no DD note cites a spec field ID that does not exist", not stale, str(stale[:5]))
check("every DD 'Spec ref' names the correct field on every artefact",
      not incomplete, str(incomplete[:5]))

print("\n=== CHECK 4  OPTION VALUE COMPLETENESS (F14) ===")
unres = []
def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())
for b, recs in spec.items():
    secs = [norm(k) for k in opts[b]]
    for r in recs:
        ov = r["OptionValues"]
        if not ov.startswith("-> Sheet 6:"):
            continue
        core = norm(re.sub(r"\(.*?\)", "", ov.split(":", 1)[1]))
        if not any(core in s for s in secs):
            unres.append("%s %s -> %s" % (short[b], r["FieldPos"], ov))
check("every column-O reference resolves to a Sheet 6 section", not unres, str(unres[:5]))
thin = []
for b, d in opts.items():
    for sec, rows in d.items():
        real = [r for r in rows if not r[0].startswith("(")]
        if len(real) == 0 and "TIPO" in sec.upper():
            thin.append("%s :: %s" % (short[b], sec[:50]))
check("no code-table section is left as a bare placeholder", not thin, str(thin))

print("\n=== CHECK 5  COMPOSITE KEY DOCUMENTATION (F12) ===")
COMP = [("CO-DIAN-001-NominaElectronica-Spec.xlsx", "NIE012"),
        ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "NIE024"),
        ("CO-DIAN-004-Formulario220-Spec.xlsx", "4"),
        ("CO-DIAN-005-Formato2276-Spec.xlsx", "N02"),
        ("CO-DIAN-005-Formato2276-Spec.xlsx", "N34"),
        ("CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx", "E01"),
        ("CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx", "T04")]
missing = [(short[b], f) for b, f in COMP
           if "composite" not in byid[(short[b], f)]["Explanation"].lower()]
check("every concatenated identifier documents its Composite Key Structure",
      not missing, str(missing))

print("\n=== CHECK 6  CODE PREFIX VERIFICATION (F14) ===")
PFX = [("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R1-014"),
       ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R2-031"),
       ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R2-032"),
       ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R2-033"),
       ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R2-034"),
       ("CO-PILA-003-AportesSeguridadSocial-Spec.xlsx", "T2R2-035"),
       ("CO-DIAN-001-NominaElectronica-Spec.xlsx", "NIE010"),
       ("CO-DIAN-002-Formulario350-Spec.xlsx", "983")]
nop = [(short[b], f) for b, f in PFX if "attern" not in byid[(short[b], f)]["Format"]]
check("every coded identifier states its prefix pattern in column J", not nop, str(nop))
# and the examples must satisfy the stated pattern
bad = []
for b, f in PFX[:6]:
    ex = byid[(short[b], f)]["Example"]
    if ex and not re.match(r"^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$", ex):
        bad.append((f, ex))
check("every administradora example matches the stated prefix pattern", not bad, str(bad))

print("\n" + "=" * 62)
print("RESULT: %d check(s) failed" % len(fails))
for f in fails:
    print("   FAILED:", f)
