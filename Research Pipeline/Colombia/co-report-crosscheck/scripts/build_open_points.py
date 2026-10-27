"""Regenerates 04-output/OPEN-POINTS-2026-10-16.md with what is still open after the 16 Oct rules:
 (1) questions to the client, taken from the column-T queries added in rounds 1 and 2 (approved change maps) whose text is
     addressed to the client (client to confirm / provide / explain ...), de-duplicated per spec and field;
 (2) the configuration points left open by the 16 Oct rules maps ("still_open" lists) incl. Form 220 casilla 56;
 (3) an appendix: RA / compliance queries of the specs the 16 Oct rules did not cover (PILA, cesantías), kept for a
     decision on whether they are closed.
The previous full T/U export is kept as 04-output/OPEN-POINTS-2026-10-16-draft-export.md.
Usage: python3 scripts/build_open_points.py"""
import os,re,json,glob,shutil
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O=os.path.join(ROOT,'04-output')
full=os.path.join(O,'OPEN-POINTS-2026-10-16.md'); keep=os.path.join(O,'OPEN-POINTS-2026-10-16-draft-export.md')
if os.path.exists(full) and not os.path.exists(keep): shutil.move(full,keep)
CLIENT=re.compile(r'\b(?:client|Client|Cinthya|employer) (?:to|must|should) (?:confirm|provide|explain|name|classify|state|supply|say|give|approve|qualify)|\bconfirm with the client\b|\bclient (?:confirms|confirmation)\b|\bClient/provider\b|\bclient validation\b|\bask the client\b',re.I)
RA=re.compile(r'\bRA (?:to|must|should)\b|\bconfirm (?:under|against|from)\b|\bRA confirmation\b|\bRA to confirm\b|\bto RA\b|\bwith RA\b|\bRA answers?\b',re.I)
def added(cur,prop):
    cur=cur or ''
    return prop[len(cur):].lstrip('\n ') if prop.startswith(cur) else prop
def sentences(t):
    t=re.sub(r'\s+',' ',t)
    return [s.strip() for s in re.split(r'(?<=[.;])\s+(?=[A-Z(\[])',t) if s.strip()]
specs=['CO-PILA-003','CO-DIAN-001','CO-DIAN-002','CO-DIAN-004','CO-DIAN-005','CO-CESANTIAS-006']
NAMES={'CO-PILA-003':'PILA','CO-DIAN-001':'Nómina Electrónica','CO-DIAN-002':'Formulario 350','CO-DIAN-004':'Formulario 220','CO-DIAN-005':'Formato 2276','CO-CESANTIAS-006':'Consignación de cesantías'}
RULED={'CO-DIAN-001','CO-DIAN-002','CO-DIAN-004','CO-DIAN-005'}
CLOSED={('CO-PILA-003','T2R2-076'),('CO-PILA-003','T2R2-045'),('CO-CESANTIAS-006','T14'),('CO-CESANTIAS-006','E92')}  # settled by Wallisson's rules of 16 Oct 2026 (second batch)
client={s:{} for s in specs}; ra={s:{} for s in specs}
for s in specs:
    for f in [os.path.join(O,f'{s}-changemap-APPROVED.json'),os.path.join(O,'round2',f'{s}-changemap-r2-APPROVED.json')]:
        if not os.path.exists(f): continue
        cm=json.load(open(f,encoding='utf-8'))
        for e in cm['edits']:
            if e['column_letter']!='T': continue
            key=f"{e.get('field_id') or ''} (row {e['row']})"
            for sent in sentences(added(e.get('current'),e['proposed'])):
                if re.search(r'\d{8}',sent) and re.search(r'employee \d{8}',sent): continue
                if CLIENT.search(sent): client[s].setdefault(key,[]).append(sent)
                elif RA.search(sent) and s not in RULED and (s,(e.get('field_id') or '')) not in CLOSED: ra[s].setdefault(key,[]).append(sent)
still={}
for s in specs:
    f=os.path.join(O,'final-prep',f'{s}-rules-map.json')
    if os.path.exists(f): still[s]=json.load(open(f,encoding='utf-8')).get('still_open',[])
    p3=os.path.join(O,'final-prep',f'{s}-pass3-map.json')
    if os.path.exists(p3) and s in still:
        m3=json.load(open(p3,encoding='utf-8')); touched3={f"{e['sheet']}!{e['cell']}" for e in m3.get('edits',[])}|{f"{x.get('sheet')}!{x.get('cell')}" for x in m3.get('moved_to_open_points',[])}
        still[s]=[x for x in still[s] if not any(ref in x for ref in touched3)]
out=['# Open points after the 16 Oct 2026 rules - internal control (not for the development team)','',
'What stays open: (1) questions to the client (via Cinthya); (2) configuration points the 16 Oct rules left open, including Form 220 casilla 56 (employer contributions to institutional plans); (3) items removed from the specs in the third pass because no rule exists; appendix: RA / compliance queries of the specs the 16 Oct rules did not address (PILA, cesantías), to be confirmed as closed or kept. The full column T/U export of the v1.1 drafts is kept in OPEN-POINTS-2026-10-16-draft-export.md.','',
'## 1. Questions to the client (via Cinthya)','']
n1=0
for s in specs:
    if not client[s]: continue
    out.append(f'### {s} ({NAMES[s]})')
    for key,sl in client[s].items():
        seen=[]
        for x in sl:
            if x not in seen: seen.append(x)
        out.append(f'- **{key}**: '+' '.join(seen)); n1+=1
    out.append('')
out+=['## 2. Configuration points left open by the 16 Oct rules','']
n2=0
for s in specs:
    if s not in still or not still[s]: continue
    out.append(f'### {s} ({NAMES[s]})')
    for x in still[s]: out.append('- '+x.replace('\n',' ')); n2+=1
    out.append('')
moved={}
for s_ in specs:
    f=os.path.join(O,'final-prep',f'{s_}-pass3-map.json')
    if os.path.exists(f): moved[s_]=json.load(open(f,encoding='utf-8')).get('moved_to_open_points',[])
out+=['## 3. Items removed from the specs on 16 Oct 2026 (no defined rule) - owner in brackets','']
n4=0
for s_ in specs:
    if not moved.get(s_): continue
    out.append(f'### {s_} ({NAMES[s_]})')
    for x in moved[s_]: out.append(f"- [{x.get('owner','?')}] {x.get('sheet')}!{x.get('cell')} ({x.get('field_id') or '-'}): {x.get('question','').strip()}"); n4+=1
    out.append('')
out+=['## Appendix. RA / compliance queries not covered by the 16 Oct rules (PILA, cesantías) - confirm closed or keep','']
n3=0
for s in specs:
    if s in RULED or not ra[s]: continue
    out.append(f'### {s} ({NAMES[s]})')
    for key,sl in ra[s].items():
        seen=[]
        for x in sl:
            if x not in seen: seen.append(x)
        out.append(f'- **{key}**: '+' '.join(seen)); n3+=1
    out.append('')
open(full,'w',encoding='utf-8').write('\n'.join(out))
nc=n1+sum(1 for s_ in specs for x in moved.get(s_,[]) if str(x.get('owner','')).lower().startswith('client')); nr=n3+sum(1 for s_ in specs for x in moved.get(s_,[]) if str(x.get('owner','')).lower().startswith('ra'))
out.append(f'\nTotals: client {nc} (section 1 + section 3 client items), RA {nr} (section 3 RA items + appendix), configuration notes {n2}.')
open(full,'w',encoding='utf-8').write('\n'.join(out))
print(f'written {full}: {n1} client items, {n2} configuration points, {n4} removed items, {n3} appendix items | totals client {nc}, RA {nr}')
