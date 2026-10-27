"""Cell-by-cell diff between the source spec (01-specs) and its DRAFT (02-specs-out), against the apply log.

usage: python3 scripts/diff_specs.py 02-specs-out/<SPEC>-apply-log.json

Checks: same sheets; no row lost (max row and row count per sheet); merged ranges identical; zero formula cells in the draft;
images per sheet identical; every changed cell is in the intended set (edits + column U marks + Version Control rows +
formula conversions); nothing else changed. Exit code 1 on any failure.
"""
import sys,os,json,zipfile,re,openpyxl
log=json.load(open(sys.argv[1],encoding='utf-8')); src,dst=log['source'],log['draft']
wo=openpyxl.load_workbook(src); wd=openpyxl.load_workbook(dst)
fail=[]; info=[]
if wo.sheetnames!=wd.sheetnames: fail.append(f'sheet list differs: {wo.sheetnames} vs {wd.sheetnames}')
# zip-level row count and merges
def rows_merges(path):
    z=zipfile.ZipFile(path); out={}
    for n in z.namelist():
        if n.startswith('xl/worksheets/sheet') and n.endswith('.xml'):
            x=z.read(n).decode('utf-8'); out[n]=(len(re.findall(r'<row\b',x)),sorted(re.findall(r'<mergeCell ref="([^"]+)"',x)),len(re.findall(r'<f\b',x)))
    return out
ro,rd=rows_merges(src),rows_merges(dst)
# zip-level: every part that is not an edited worksheet must be byte-identical (drawings, media, styles, rels, sharedStrings)
zs,zd=zipfile.ZipFile(src),zipfile.ZipFile(dst)
if zs.namelist()!=zd.namelist(): fail.append('zip entry list differs')
edited_parts=set()
for n in zs.namelist():
    if zs.read(n)!=zd.read(n): edited_parts.add(n)
non_ws=[n for n in edited_parts if not (n.startswith('xl/worksheets/sheet') and n.endswith('.xml'))]
if non_ws: fail.append('non-worksheet parts changed: '+', '.join(non_ws))
drawings=[n for n in zs.namelist() if 'drawings/' in n or 'media/' in n]
info.append(f'{len(drawings)} drawing/media parts byte-identical; worksheet parts rewritten: {sorted(edited_parts)}')
for n in ro:
    if ro[n][0]!=rd[n][0]: fail.append(f'{n}: row count {ro[n][0]} -> {rd[n][0]}')
    if ro[n][1]!=rd[n][1]: fail.append(f'{n}: merged ranges changed')
    if rd[n][2]!=0: fail.append(f'{n}: {rd[n][2]} formula cell(s) remain in the draft')
intended=set()
for sn,ref in log['edits']: intended.add((sn,ref))
spec_sheet=None
for sn in wo.sheetnames:
    if sn.endswith('Spec'): spec_sheet=sn
for r in log['corrected_rows']: intended.add((spec_sheet,f'U{r}'))
for sn,ref in log['formula_cells_converted']: intended.add((sn,ref))
for r in log['vc_rows']:
    for c in 'BCDEF': intended.add(('Version Control',f'{c}{r}'))
# map part names to sheet names for the intended edits (edits are logged by part)
z=zipfile.ZipFile(src); wbx=z.read('xl/workbook.xml').decode(); rels=z.read('xl/_rels/workbook.xml.rels').decode()
rid2t={re.search(r'Id="([^"]+)"',m).group(1):re.search(r'Target="([^"]+)"',m).group(1) for m in re.findall(r'<Relationship\b[^>]*/>',rels)}
part2name={}
for name,rid in re.findall(r'<sheet\b[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wbx):
    t=rid2t[rid].lstrip('/'); t=t if t.startswith('xl/') else 'xl/'+t; part2name[t]=name.replace('&amp;','&')
intended={(part2name.get(sn,sn),ref) for sn,ref in intended}
changed=[]
for sn in wo.sheetnames:
    a,b=wo[sn],wd[sn]
    if a.max_row!=b.max_row or a.max_column!=b.max_column: fail.append(f'{sn}: dimensions {a.max_row}x{a.max_column} -> {b.max_row}x{b.max_column}')
    if len(a._images)!=len(b._images): fail.append(f'{sn}: images {len(a._images)} -> {len(b._images)}')
    for row in a.iter_rows():
        for c in row:
            v1=c.value; v2=b[c.coordinate].value
            if v1!=v2: changed.append((sn,c.coordinate,v1,v2))
    for row in b.iter_rows():
        for c in row:
            if isinstance(c.value,str) and c.value.startswith('=') and c.data_type=='f': fail.append(f'{sn}!{c.coordinate}: still a formula')
unexpected=[(sn,ref) for sn,ref,_,_ in changed if (sn,ref) not in intended]
missing=[(sn,ref) for sn,ref in intended if (sn,ref) not in {(s,r) for s,r,_,_ in changed}]
if unexpected: fail.append('unexpected changed cells: '+', '.join(f'{s}!{r}' for s,r in unexpected[:30]))
print(f"{log['spec']}: {len(changed)} changed cells, {len(intended)} intended, {len(unexpected)} unexpected, {len(missing)} intended-but-identical")
if missing: print('  intended but identical (text equal to current, or Corrected already set):',', '.join(f'{s}!{r}' for s,r in missing[:20]))
print('  '+info[0]) if info else None
print('  rows per sheet identical:',all(ro[n][0]==rd[n][0] for n in ro),'| merges identical:',all(ro[n][1]==rd[n][1] for n in ro),'| formula cells in draft:',sum(rd[n][2] for n in rd),'| images:',{sn:len(wd[sn]._images) for sn in wd.sheetnames if wd[sn]._images})
if fail:
    print('FAIL'); print('\n'.join(' - '+f for f in fail)); sys.exit(1)
print('PASS')
