"""D-12 - alleenstaandeouderenkorting: for every AOW-age IKV compare the monthly-table withholding with and without
the AOK column (Witte Maandloon-tabel 2026). Usage: python -I d12.py"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
NL = r"C:\Users\instituto\Documents\internal-certification\Netherlands"
ROWS = json.load(open(os.path.join(NL, "_references", "2026", "wit_mnd_nl_std_20260101.pdf.rows.json")))


def row_for(t):
    r = [x for x in ROWS if x[0] <= t]
    return r[-1] if r else None


out = {}
for folder in ("Excerpta Medica - 2026-09", "Quest Software - 2026-09", "Sherwin Williams - 2026-09"):
    d = json.load(open(os.path.join(NL, folder, "02 Validation", "_evidence", "checks.json"), encoding="utf-8"))
    res = []
    for k in d["ikv_rows"]:
        if not k.get("AOW") or k.get("tabelloon") is None:
            continue
        r = row_for(k["tabelloon"])
        lhk = bool(k.get("LHK"))
        excl, incl = (r[9], r[10]) if lhk else (r[8], r[8])
        withheld = k.get("IngLbPh")
        reg = k.get("exp_regular")
        if abs(excl - incl) < 0.005:
            verdict = "Pass - AOK immaterial at this tabelloon"
        elif withheld is not None and abs(float(withheld) - excl) <= 0.10:
            verdict = "Pass - withheld on the column without AOK"
        elif withheld is not None and abs(float(withheld) - incl) <= 0.10:
            verdict = "Observation - withheld on the AOK column; entitlement (single AOW pensioner) not evidenced"
        else:
            verdict = "Neither column (bb wage present - see D-03)" if k.get("LnTabBB") else "Neither column"
        res.append({"PersNr": k["PersNr"], "NumIV": k.get("NumIV"), "tabelloon": k["tabelloon"], "LHK": lhk,
                    "table excl AOK": excl, "table incl AOK": incl, "IngLbPh": withheld, "verdict": verdict})
    out[folder] = res
    print("==", folder, len(res), "AOW-age IKVs")
    for x in res:
        print("  ", x)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "d12_result.json"), "w", encoding="utf-8"), indent=1)
