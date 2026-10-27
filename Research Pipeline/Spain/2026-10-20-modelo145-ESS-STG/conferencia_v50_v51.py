"""Cell-by-cell check V5.0 x V5.1: value + format of every cell in every sheet."""
import openpyxl, sys, zipfile, collections
sys.stdout.reconfigure(encoding="utf-8")
A = openpyxl.load_workbook(sys.argv[1]); B = openpyxl.load_workbook(sys.argv[2])
assert zipfile.ZipFile(sys.argv[2]).testzip() is None
assert A.sheetnames == B.sheetnames
def sig(c):
    f, al, b = c.font, c.alignment, c.border
    return (f.name, f.sz, f.b, f.i, f.color.rgb if f.color else None, c.number_format, al.horizontal, al.vertical, al.wrap_text,
            *[getattr(getattr(b, k), "style", None) for k in ("left", "right", "top", "bottom")])
tot = collections.Counter(); bad = []
for name in A.sheetnames:
    a, b = A[name], B[name]
    sh = (lambda r: r + 1 if r >= 35 else r) if name == "Version Control" else (lambda r: r)
    for row in a.iter_rows():
        for c in row:
            d = b.cell(sh(c.row), c.column)
            if sig(c) != sig(d): bad.append((name, c.coordinate, "format", sig(c), sig(d)))
            fa, fb = c.fill.fgColor.rgb, d.fill.fgColor.rgb
            if c.value != d.value:
                tot[name] += 1
                if fb != "FFFCE4D6": bad.append((name, c.coordinate, "changed but not orange", fb))
                if c.column == 3 and name == "Country Fields":
                    pass
            elif fa != fb or c.fill.fill_type != d.fill.fill_type:
                bad.append((name, c.coordinate, "fill changed without value change", fa, fb))
    print(f"{name}: rows {a.max_row} -> {b.max_row}, changed cells {tot[name]}, merged {len(a.merged_cells.ranges)} -> {len(b.merged_cells.ranges)}")
vc = B["Version Control"]
print("VC35:", [vc.cell(35, k).value for k in range(2, 7)], vc.cell(35, 4).fill.fgColor.rgb, "| VC36:", vc.cell(36, 2).value)
# ordinal checks
cf = B["Country Fields"]; ords = collections.defaultdict(list)
for r in range(1, cf.max_row + 1):
    if cf.cell(r, 16).value == "employee_tax_relief_declaration":
        ords[cf.cell(r, 19).value].append((cf.cell(r, 3).value, cf.cell(r, 5).value))
for sub, l in ords.items():
    o = sorted(x[0] for x in l)
    print(sub, "n =", len(l), "ordinals unique:", len(set(o)) == len(o), "min/max", o[0], o[-1])
for sub in ("descendants", "ascendants"):
    l = sorted(ords[sub])
    print(" ", sub, [f"{int(x[0])}:{x[1][4:]}" for x in l[:10]], "...")
print("PROBLEMS:", len(bad))
for x in bad[:30]: print(" ", x)
