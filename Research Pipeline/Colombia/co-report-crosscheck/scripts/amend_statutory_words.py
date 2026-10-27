"""Appends to 04-output/final-prep/<SPEC>-cleanup-map.json one edit per cell (not already in the map) where a listed word
survives in a statutory sense, replacing it with neutral wording. Prints every replacement context. Usage: python3 scripts/amend_statutory_words.py <SPEC>"""
import sys,os,re,json,openpyxl
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); spec=sys.argv[1]
mp=os.path.join(ROOT,'04-output','final-prep',spec+'-cleanup-map.json'); cm=json.load(open(mp,encoding='utf-8'))
wb=openpyxl.load_workbook(os.path.join(ROOT,cm['draft']))
covered={(e['sheet'],e['cell']) for e in cm['edits']}
REPL=[(r'\bcorrected downward\b','adjusted downward'),(r'\bbeing corrected\b','being amended'),(r'\bcorrected return\b','amended return'),(r'\bcorrected\b','amended'),
      (r'\bcross-checks\b','checks'),(r'\bcross-checked\b','checked'),(r'\bcross-check\b','check'),(r'\bnot (\d[\d,.]*)\b',r'rather than \1'),(r'\bpreviously\b','earlier'),(r'\bno longer\b','not'),(r'\brevised\b','updated')]
added=0
for ws in wb:
    if ws.title=='Version Control': continue
    for row in ws.iter_rows():
        for c in row:
            if not isinstance(c.value,str) or (ws.title.endswith('Spec') and c.column in (20,21) and c.row>2): continue
            if (ws.title,c.coordinate) in covered: continue
            new=c.value
            for rx,rep in REPL: new=re.sub(rx,rep,new)
            if new!=c.value:
                for rx,rep in REPL:
                    for m in re.finditer(rx,c.value): print(f'{ws.title}!{c.coordinate}: ...{c.value[max(0,m.start()-60):m.end()+40]}...  ->  {rep}')
                cm['edits'].append({'sheet':ws.title,'cell':c.coordinate,'field_id':ws.cell(c.row,4).value if ws.title.endswith('Spec') else None,'current':c.value,'proposed':new,'why':'statutory wording neutralised (word list)'}); added+=1
json.dump(cm,open(mp,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print(f'{spec}: {added} cells appended to the cleanup map')
