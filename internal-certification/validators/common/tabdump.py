"""Dump every sheet of an xls/xlsx/xlsm/ods/csv as non-empty rows (cell values joined by ' | ').
Usage: python -I tabdump.py file [maxrows] [transpose]"""
import sys

import pandas as pd


def main(p, maxr=400, transpose=False):
    pl = p.lower()
    if pl.endswith(".csv"):
        for enc in ("utf-8-sig", "cp1252"):
            try:
                sheets = {"csv": pd.read_csv(p, header=None, dtype=str, sep=None, engine="python", encoding=enc)}
                break
            except UnicodeDecodeError:
                continue
    else:
        eng = "odf" if pl.endswith(".ods") else ("xlrd" if pl.endswith(".xls") else "openpyxl")
        sheets = pd.read_excel(p, sheet_name=None, header=None, dtype=object, engine=eng)
    for name, df in sheets.items():
        df = df.dropna(how="all").dropna(axis=1, how="all")
        if transpose:
            df = df.T
        print(f"##### sheet '{name}' shape={df.shape}")
        for i, (idx, row) in enumerate(df.iterrows()):
            if i >= maxr:
                print("...")
                break
            vals = ["" if pd.isna(v) else str(v) for v in row.tolist()]
            print(f"{idx}: " + " | ".join(vals))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 400,
         len(sys.argv) > 3 and sys.argv[3] == "T")
