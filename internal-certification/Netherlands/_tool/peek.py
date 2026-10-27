"""Compact structural summary of every file in a pack (SEPA, xlsx/xls)."""
import sys, os, re, glob, xml.etree.ElementTree as ET
import pandas as pd, warnings
warnings.filterwarnings("ignore")
def s(t): return t.split('}')[-1]
for f in sorted(glob.glob(os.path.join(sys.argv[1], "**", "*"), recursive=True)):
    if os.path.isdir(f): continue
    b = os.path.basename(f); low = b.lower()
    if low.endswith(".xml") and "L01" not in b:
        r = ET.parse(f).getroot()
        if "pain" not in r.tag: print("=== XML (non-SEPA)", b, s(r.tag)); continue
        g = {s(e.tag): e.text for e in r.iter() if s(e.tag) in ("MsgId","CreDtTm","NbOfTxs","CtrlSum","ReqdExctnDt")}
        tx = []
        for t in r.iter():
            if s(t.tag) == "CdtTrfTxInf":
                d = {s(e.tag): (e.text or "").strip() for e in t.iter()}
                tx.append((d.get("Nm"), d.get("InstdAmt"), d.get("Ustrd"), d.get("EndToEndId")))
        print("=== SEPA", b, g, "txs", len(tx), "sum", round(sum(float(str(x[1]).replace(",","")) for x in tx),2))
        for x in tx: print("    ", x)
    elif low.endswith((".xlsx", ".xls")):
        eng = "xlrd" if low.endswith(".xls") else None
        for sh, x in pd.read_excel(f, header=None, sheet_name=None, engine=eng).items():
            print("=== XLS", b, "|", sh, x.shape)
            for i in range(min(len(x), int(sys.argv[2]) if len(sys.argv) > 2 else 12)):
                v = [str(c)[:22] for c in x.iloc[i].tolist() if str(c) != "nan"]
                if v: print("    ", i, v[:14])
