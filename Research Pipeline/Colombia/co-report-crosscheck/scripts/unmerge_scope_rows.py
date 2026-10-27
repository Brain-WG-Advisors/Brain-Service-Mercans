"""Builds <SPEC>-pass3b-map.json that unmerges the Payroll Scope Summary scenario rows merged A:C which carry values in B/C
in the XML (written by an earlier pass but hidden by the merge), declaring those B/C cells as touched. Usage: python3 scripts/unmerge_scope_rows.py <SPEC> <final file name>"""
import sys,os,re,json,zipfile,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); spec,fname=sys.argv[1],sys.argv[2]
f=os.path.join(ROOT,'05-final',fname); z=zipfile.ZipFile(f)
wbx=z.read('xl/workbook.xml').decode(); rels=z.read('xl/_rels/workbook.xml.rels').decode()
rid2t={re.search(r'Id="([^"]+)"',m).group(1):re.search(r'Target="([^"]+)"',m).group(1) for m in re.findall(r'<Relationship\b[^>]*/>',rels)}
part=None
for name,rid in re.findall(r'<sheet\b[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wbx):
    if html.unescape(name)=='Payroll Scope Summary': t=rid2t[rid].lstrip('/'); part=t if t.startswith('xl/') else 'xl/'+t
xml=z.read(part).decode()
sst=[html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))) for si in re.findall(r'<si>(.*?)</si>',z.read('xl/sharedStrings.xml').decode(),re.S)] if 'xl/sharedStrings.xml' in z.namelist() else []
def val(ref):
    m=re.search(r'<c r="%s"(?: [^>]*)?(?<!/)>(.*?)</c>'%ref,xml,re.S)
    if not m: return None
    c=m.group(0)
    if 't="s"' in c: v=re.search(r'<v>(.*?)</v>',c); return sst[int(v.group(1))] if v else None
    if 'inlineStr' in c: return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',c,re.S)))
    v=re.search(r'<v>(.*?)</v>',c); return html.unescape(v.group(1)) if v else None
edits=[]; unm=[]
for rng in re.findall(r'<mergeCell ref="(A(\d+):C\2)"/>',xml):
    rng,row=rng[0],int(rng[1])
    if row<=3: continue
    b,c=val(f'B{row}'),val(f'C{row}')
    if b or c:
        unm.append({'sheet':'Payroll Scope Summary','range':rng})
        for col,v in (('B',b),('C',c)):
            if v: edits.append({'sheet':'Payroll Scope Summary','cell':f'{col}{row}','current':v,'proposed':v,'rule':'unmerge-reveal'})
cm={'spec':spec,'final':'05-final/'+fname,'edits':edits,'pre_apply':{'unmerge':unm,'reason':'scenario rows merged A:C hide the REPORT?/NOTES values written in B/C'},'moved_to_open_points':[]}
json.dump(cm,open(os.path.join(ROOT,'04-output','final-prep',spec+'-pass3b-map.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(spec,'rows to unmerge:',[u['range'] for u in unm],'| B/C cells declared:',len(edits))
