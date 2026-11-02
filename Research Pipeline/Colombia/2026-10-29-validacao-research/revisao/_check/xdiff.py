import sys, zipfile, hashlib, openpyxl, json
sys.stdout.reconfigure(encoding='utf-8')
base, draft, out = sys.argv[1], sys.argv[2], sys.argv[3]
zb, zd = zipfile.ZipFile(base), zipfile.ZipFile(draft)
nb, nd = set(zb.namelist()), set(zd.namelist())
res = {'only_base': sorted(nb-nd), 'only_draft': sorted(nd-nb), 'changed_entries': [], 'protected_changed': []}
for n in sorted(nb & nd):
    if zb.read(n) != zd.read(n):
        res['changed_entries'].append(n)
        if any(k in n for k in ('drawing', 'media', 'comments', 'vmlDrawing', 'threadedComment')):
            res['protected_changed'].append(n)
# read-only open test
try:
    w = openpyxl.load_workbook(draft, read_only=True); _ = [ws.title for ws in w.worksheets]; w.close(); res['ro_open'] = 'OK'
except Exception as e:
    res['ro_open'] = 'FAIL ' + repr(e)
wb = openpyxl.load_workbook(base); wd = openpyxl.load_workbook(draft)
res['sheets_base'] = wb.sheetnames; res['sheets_draft'] = wd.sheetnames
cells = []
for sn in wd.sheetnames:
    sd = wd[sn]; sb = wb[sn] if sn in wb.sheetnames else None
    mr = max(sd.max_row, sb.max_row if sb else 0); mc = max(sd.max_column, sb.max_column if sb else 0)
    for r in range(1, mr+1):
        for c in range(1, mc+1):
            vd = sd.cell(r, c).value
            vb = sb.cell(r, c).value if sb else None
            if vd != vb:
                cl = sd.cell(r, c)
                fill = cl.fill.fgColor.rgb if cl.fill and cl.fill.fill_type else None
                cells.append({'sheet': sn, 'cell': cl.coordinate, 'old': vb, 'new': vd, 'fill': fill})
res['cells'] = cells
res['n_changed_cells'] = len(cells)
res['nonblue'] = [x['sheet']+'!'+x['cell'] for x in cells if x['fill'] != 'FFDDEBF7']
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k != 'cells'}, ensure_ascii=False, default=str)[:3000])
