"""XML / package validation of a v1.1 spec against its base.
Usage: validate.py <base.xlsx> <new.xlsx>
Checks: every XML/rels part well-formed; [Content_Types] overrides all resolve; every .rels target exists;
media/drawing/comment part counts vs base (minus removed sheet parts); openpyxl loads; images per sheet;
Version Control row 14 (1.1 / 2026-10-27 date / status in the E13:E23 list / Wallisson Gomes); data-validation lists respected."""
import re
import sys
import zipfile
import posixpath
import warnings
import xml.etree.ElementTree as ET

import openpyxl

warnings.filterwarnings("ignore")
sys.stdout.reconfigure(encoding="utf-8")


def main(base, new):
    ok = True
    z, zb = zipfile.ZipFile(new), zipfile.ZipFile(base)
    names = set(z.namelist())
    for n in sorted(names):
        if n.endswith((".xml", ".rels", ".vml")):
            try:
                ET.fromstring(z.read(n))
            except ET.ParseError as e:
                if n.endswith(".vml"):
                    print("  (vml não-XML estrito, igual à base)" if z.read(n) == zb.read(n) else "  VML ERRO " + n)
                else:
                    ok = False; print("XML INVÁLIDO", n, e)
    ct = z.read("[Content_Types].xml").decode()
    for p in re.findall(r'PartName="/([^"]+)"', ct):
        if p not in names:
            ok = False; print("Content_Types aponta parte inexistente:", p)
    for n in names:
        if n.endswith(".rels"):
            folder = posixpath.dirname(posixpath.dirname(n))
            for t, mode in re.findall(r'Target="([^"]+)"(?: TargetMode="(\w+)")?', z.read(n).decode()):
                if mode == "External":
                    continue
                tp = t.lstrip("/") if t.startswith("/") else posixpath.normpath(posixpath.join(folder, t))
                if tp not in names:
                    ok = False; print("rels alvo inexistente:", n, "->", t)
    cnt = lambda ns, pat: len([x for x in ns if re.search(pat, x)])
    for lab, pat in [("media", r"^xl/media/"), ("drawings", r"^xl/drawings/drawing\d+\.xml$"),
                     ("comments", r"^xl/comments\d+\.xml$"), ("vml", r"\.vml$"), ("threaded", r"threadedComment")]:
        print("  %-9s base=%d nova=%d" % (lab, cnt(zb.namelist(), pat), cnt(names, pat)))
    wb = openpyxl.load_workbook(new)
    print("  abas:", wb.sheetnames)
    for ws in wb.worksheets:
        if ws._images:
            print("  imagens em", ws.title, len(ws._images))
    vc = wb["Version Control"]
    row = [vc["B14"].value, vc["C14"].value, vc["D14"].value, vc["E14"].value, vc["F14"].value]
    print("  Version Control 14:", row[0], row[1], "|", row[3], "|", row[4], "| date?", vc["C14"].is_date)
    if not (row[0] == 1.1 and str(row[1]).startswith("2026-10-27") and row[3] in ("In Progress", "Under Review", "Approved") and row[4] == "Wallisson Gomes"):
        ok = False; print("  VERSION CONTROL INCORRETO")
    rm = wb["Report Matrix"]; opt = wb["Options"]
    opts = {r: [opt["A%d" % i].value for i in rng] for r, rng in
            {"B6": range(1, 8), "B7": range(9, 14), "B11": range(15, 19)}.items()}
    for r, vals in opts.items():
        print("  %s=%r em lista: %s" % (r, rm[r].value, rm[r].value in vals))
        ok &= rm[r].value in vals
    print("RESULTADO:", "OK" if ok else "FALHA")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
