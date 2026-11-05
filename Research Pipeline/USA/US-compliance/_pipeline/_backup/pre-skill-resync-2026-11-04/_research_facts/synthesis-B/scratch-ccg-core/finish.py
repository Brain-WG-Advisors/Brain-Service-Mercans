import json, os, sys, subprocess, glob
BASE=sys.argv[1]; R=os.path.join(BASE,'_research'); S=os.path.join(R,'synthesis-B','scratch-ccg-core')
units=['m01_foundational','m02_master_data','m03_gross_to_net','m04_compensation','m05_social_security','m06_tax','m07_deductions','m08_leave','m09_termination','m10_reporting','m11_advanced','m12_worked_examples','m13_practices','coverage']
consumed=json.load(open(os.path.join(S,'consumed.json')))
val=os.path.expanduser('~/mercans-pipeline/shared/schemas/validate_contract.py')
idx=['','---','','## Key index per unit (generated from the facts files)','']
oq=['','## Open questions (mirrors `unresolved[]`; same keys, same wording)','']
for u in units:
    p=os.path.join(R,f'CCG-{u}-facts.json'); d=json.load(open(p,encoding='utf-8'))
    own=[f"`{f['key']}` [{f['register_id']}]" for f in d['facts']]
    ann=d.get('_annex_keys_cited',{})
    idx.append(f'**{u}** — own facts ({len(own)}): '+(', '.join(own) if own else 'none')+'.')
    if ann: idx.append(f'  Annex keys cited ({len(ann)}): '+', '.join(f'`{k}` ({v})' for k,v in ann.items())+'.')
    if u=='coverage': idx.append('  coverage_matrix rows: '+', '.join(d['coverage_matrix'].keys())+'.')
    idx.append('')
    for e in d['unresolved']:
        oq.append(f"- **`{e['key']}`** ({u}; blocking={str(e.get('blocking',True)).lower()}). Why: {e['why']} What would close it: {e['what_would_close_it']}")
    out=subprocess.run([sys.executable,val,'facts',p],capture_output=True,text=True).stdout.strip().splitlines()[-1]
    ids=sorted(k for k,v in consumed.items() if f'CCG/{u}' in v)
    rep=[f'# CCG {u} - Synthesis B report (CCG core worker, 2026-11-02)','',
         f'- File: `_research/CCG-{u}-facts.json`',f'- Facts written: {len(d["facts"])}' + (f'; coverage_matrix rows: {len(d["coverage_matrix"])} (all answered)' if u=='coverage' else ''),
         f'- Annex-owned keys cited instead of duplicated: {len(ann)}',f'- Unresolved: {len(d["unresolved"])} (blocking: {sum(1 for e in d["unresolved"] if e.get("blocking",True))})',
         f'- Validator: `validate_contract.py facts` -> {out}',
         f'- Register ids consumed ({len(ids)}), to append `CCG/{u}` to consumed_by in the merge: '+', '.join(ids),
         '- Pack: `_research/CCG-research-pack.md` section for this unit.']
    open(os.path.join(R,'synthesis-B',f'CCG-{u}-report.md'),'w',encoding='utf-8',newline='\n').write('\n'.join(rep)+'\n')
pack=open(os.path.join(S,'pack-prose.md'),encoding='utf-8').read()+'\n'.join(idx)+'\n'.join(oq)+'\n'
open(os.path.join(R,'CCG-research-pack.md'),'w',encoding='utf-8',newline='\n').write(pack)
print('pack bytes',len(pack.encode()),'open questions',len(oq)-3)
