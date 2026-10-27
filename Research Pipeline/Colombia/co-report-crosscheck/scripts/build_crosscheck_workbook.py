"""Consolidates <dir>/*-crosscheck<suffix>.json and *-verification<suffix>.json into <dir>/<name>.xlsx.
Usage: python3 scripts/build_crosscheck_workbook.py [dir] [suffix] [name]   (defaults: 04-output, "", CO-SPECS-vs-CLIENT-REPORTS-CROSSCHECK)"""
import os,glob,json,sys
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'04-output'); SUF=sys.argv[2] if len(sys.argv)>2 else ''; NAME=sys.argv[3] if len(sys.argv)>3 else 'CO-SPECS-vs-CLIENT-REPORTS-CROSSCHECK'
F=lambda **k: Font(**{'name':'Arial','size':10,**k}); HF=Font(name='Arial',size=10,bold=True,color='FFFFFF'); HB=PatternFill('solid',fgColor='1F3864')
COL={'Aligned':'C6EFCE','Explanation to improve':'FFF2CC','Format mismatch':'FFE699','Conflict':'F8CBAD','Not evidenced':'EDEDED','Missing in spec':'F8CBAD','Client-specific':'DDEBF7'}
wb=Workbook(); S=wb.active; S.title='Summary'
def hdr(ws,vals,w):
    for i,v in enumerate(vals,1):
        c=ws.cell(1,i,v); c.font=HF; c.fill=HB; c.alignment=Alignment(wrap_text=True)
        ws.column_dimensions[c.column_letter].width=w[i-1]
hdr(S,['Spec','Aligned','Explanation to improve','Format mismatch','Conflict','Not evidenced','Report columns missing in spec','Verifier agreement'],[18,10,12,10,10,10,14,12])
r=2
for f in sorted(glob.glob(os.path.join(O,f'*-crosscheck{SUF}.json'))):
    d=json.load(open(f)); code=d['spec']; cnt={}
    for x in d['fields']: cnt[x['verdict']]=cnt.get(x['verdict'],0)+1
    miss=sum(1 for x in d.get('uncovered_report_columns',[]) if x.get('classification')=='Missing in spec')
    vf=os.path.join(O,f'{code}-verification{SUF}.json'); agr=json.load(open(vf)).get('agreement_rate') if os.path.exists(vf) else None
    for j,v in enumerate([code,cnt.get('Aligned',0),cnt.get('Explanation to improve',0),cnt.get('Format mismatch',0),cnt.get('Conflict',0),cnt.get('Not evidenced',0),miss,agr],1): S.cell(r,j,v).font=F()
    ws=wb.create_sheet(code[:31]); hdr(ws,['Field ID','Field','Verdict','Client evidence (masked)','Finding','Proposed Field Explanation','Official source'],[12,30,18,45,55,60,30])
    rr=2
    for x in d['fields']:
        ev='; '.join(f"{e.get('file')}/{e.get('sheet')}/{e.get('column')} = {e.get('example_masked')}" for e in x.get('report_evidence',[]))
        for j,v in enumerate([x.get('id'),x.get('name'),x.get('verdict'),ev,x.get('finding'),x.get('proposed_explanation'),x.get('official_source')],1):
            c=ws.cell(rr,j,v); c.font=F(); c.alignment=Alignment(wrap_text=True,vertical='top')
        ws.cell(rr,3).fill=PatternFill('solid',fgColor=COL.get(x.get('verdict'),'FFFFFF')); rr+=1
    ws.freeze_panes='A2'
    if d.get('uncovered_report_columns'):
        u=wb.create_sheet((code+' uncovered')[:31]); hdr(u,['File','Sheet','Column','Classification','Note'],[40,20,30,18,70])
        for i,x in enumerate(d['uncovered_report_columns'],2):
            for j,k in enumerate(['file','sheet','column','classification','note'],1): u.cell(i,j,x.get(k)).font=F()
    r+=1
mp=os.path.join(O,'report-spec-map.json')
if os.path.exists(mp):
    m=json.load(open(mp)); ws=wb.create_sheet('Report map'); hdr(ws,['Client report','Sheet','Role','Specs','Confidence','Rationale'],[50,20,12,30,10,80])
    for i,x in enumerate(m.get('reports',[]),2):
        for j,v in enumerate([x.get('file'),x.get('sheet'),x.get('role'),', '.join(x.get('specs',[])),x.get('confidence'),x.get('rationale')],1): ws.cell(i,j,v).font=F()
out=os.path.join(O,NAME+'.xlsx'); wb.save(out); print('written',out)
