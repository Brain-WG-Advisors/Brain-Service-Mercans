# -*- coding: utf-8 -*-
"""Read-only inventory of the approved Report Specs (Report Matrix): one record per report row, with the channel
class, portal, status and accuracy statement the spec carries (the SIR carries the same statement, F27)."""
import glob
import os
import re

from openpyxl import load_workbook

import sir_common as S

CH = re.compile(r"Channel:\s*(.*?)\s*\|\s*Portal:\s*(.*?)\s*\|\s*Source:\s*(.*?)\s*\|\s*((?:CONFIRMED|TO CONFIRM)[^.]*)\.\s*"
                r"Accuracy\s+(\d+)%(?:\s*\((.*?)\))?\.\s*Closes with:\s*(.*)$", re.S)
NORET = re.compile(r"^No return for this jurisdiction:.*?(CONFIRMED)\.\s*$", re.S)
GAPTAG = re.compile(r"\s*\[\[GAP:[^\]]*\]\]")
_CACHE = {}


def specs():
    if _CACHE:
        return _CACHE["v"]
    out = []
    for p in sorted(glob.glob(os.path.join(S.SPECS, "*-Spec.xlsx"))):
        sid = re.match(r"(US-[A-Z0-9]+-\d{3})", os.path.basename(p)).group(1)
        wb = load_workbook(p, read_only=True, data_only=True)
        top, rows, inm = {}, [], False
        for row in wb["Report Matrix"].iter_rows(values_only=True):
            if not any(x is not None for x in row):
                continue
            a = str(row[0] or "")
            if a.startswith("═══ REPORT MATRIX"):
                inm = True
                continue
            if a.startswith("═══"):
                inm = False
                continue
            if inm:
                if a == "Report ID":
                    continue
                rows.append([("" if x is None else str(x)) for x in row[:10]])
            elif len(row) > 1 and row[1] is not None:
                top[a] = str(row[1])
        recs = []
        for r in rows:
            m = CH.search(r[9])
            nr = NORET.search(r[9])
            rec = dict(row_id=r[0], name=r[1], authority=r[3], frequency=r[4], due=r[5], method=r[6], fileformat=r[7],
                       legal=r[8], acc_text=r[9])
            if m:
                rec.update(channel=m.group(1), portal=m.group(2), source=m.group(3), status=m.group(4),
                           accuracy=int(m.group(5)), basis=m.group(6) or "", closes=GAPTAG.sub("", m.group(7)).strip())
            elif nr:
                rec.update(channel="none (no return for this jurisdiction)", portal="Not applicable", source="", status="CONFIRMED",
                           accuracy=None, basis="", closes="")
            else:
                rec.update(channel=None, portal=None, source=None, status=None, accuracy=None, basis=None, closes=None)
            sfx = r[0][len(sid) + 1:] if r[0].startswith(sid + "-") else ""
            rec["jur"] = sfx
            recs.append(rec)
        out.append(dict(id=sid, file=os.path.basename(p), title=top.get("Document Title", sid), authority=top.get("Authority", ""),
                        rtype=top.get("Report Type", ""), rows=recs, sheets=wb.sheetnames))
    _CACHE["v"] = out
    return out


def by_id():
    return {s["id"]: s for s in specs()}
