import re,sys,html
sys.stdout.reconfigure(encoding='utf-8')
P='x/word/document.xml'
x=open(P,encoding='utf-8').read()
DATE='2026-11-02T00:00:00Z'; AUTH='Claude'
nid=[9100]
def a():
    nid[0]+=1; return f'w:author="{AUTH}" w:id="{nid[0]}" w:date="{DATE}"'
esc=lambda s: html.escape(s,quote=False)
def ins_run(text,rpr): return f'<w:ins {a()}><w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:ins>'
def to_del(runs_xml):
    def f(m):
        r=m.group(0)
        if '<w:t' not in r: return r
        r=re.sub(r'<w:t( [^>]*)?>',lambda k:'<w:delText xml:space="preserve">',r).replace('</w:t>','</w:delText>')
        return f'<w:del {a()}>{r}</w:del>'
    return re.sub(r'<w:r\b(?:(?!<w:r\b).)*?</w:r>',f,runs_xml,flags=re.S)
paras=list(re.finditer(r'<w:p\b[^>]*>(?:(?!<w:p\b).)*?</w:p>',x,flags=re.S))
def ptxt(p): return html.unescape(''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>',p)))
def rpr_of(p):
    m=re.search(r'<w:r\b[^>]*>(<w:rPr>.*?</w:rPr>)',p,flags=re.S); return m.group(1) if m else '<w:rPr/>'
edits={}
def split(p):
    head,body=p.split('</w:pPr>',1) if '</w:pPr>' in p else (None,p)
    return (head+'</w:pPr>' if head else ''), body[:-len('</w:p>')]
def replace_para(i,expect,new):
    p=paras[i].group(0); assert ptxt(p).strip()==expect,(i,ptxt(p))
    h,b=split(p); edits[i]=h+to_del(b)+ins_run(new,rpr_of(p))+'</w:p>'
def append_para(i,expect,extra):
    p=paras[i].group(0); assert ptxt(p).strip()==expect,(i,ptxt(p))
    h,b=split(p); edits[i]=h+b+ins_run(extra,rpr_of(p))+'</w:p>'
def new_para_after(i,expect_start,text):
    p=paras[i].group(0); assert ptxt(p).startswith(expect_start),(i,ptxt(p))
    ppr=re.search(r'<w:pPr>.*?</w:pPr>',p,flags=re.S).group(0)
    if '<w:rPr/>' in ppr: ppr2=ppr.replace('<w:rPr/>',f'<w:rPr><w:ins {a()}/></w:rPr>')
    elif '<w:rPr>' in ppr: ppr2=ppr.replace('<w:rPr>',f'<w:rPr><w:ins {a()}/>',1)
    else: ppr2=ppr.replace('</w:pPr>',f'<w:rPr><w:ins {a()}/></w:rPr></w:pPr>')
    rp=re.sub(r'<w:b/>|<w:bCs/>','',rpr_of(p))
    edits[i]=edits.get(i,p)+f'<w:p>{ppr2}'+ins_run(text,rp)+'</w:p>'

# 7.1 Family Minimums summary
append_para(1440,'Descendants: €2,400 (1st), €2,700 (2nd), €4,000 (3rd), €4,500 (4th+) per child.',
 ' For the withholding rate, each descendant counts by half unless the employee is exclusively entitled to the whole minimum (Art. 84.2.º RIRPF; Art. 61.1.ª LIRPF).')
# 7.1 table, Descendant Minimum notes
append_para(3238,'Must be < 25 years old or disabled, & living with employee.',
 ' For withholding, counted by half unless the employee is exclusively entitled (Art. 84.2.º RIRPF).')
# 9.1 Treatment of Excess
replace_para(4074,'Social Security: Severance pay (both exempt and non-exempt) is generally excluded from the Social Security contribution base (Art. 147 LGSS), provided it does not exceed the statutory limits. Excess amounts may be included in the contribution base if they are deemed "remuneration" rather than "indemnity," though typically, pure severance is excluded.',
 'Social Security: Severance is excluded from the contribution base only up to the statutory (compulsory) amount. When the contract ends before the conciliation act, the exempt amount is the one that would apply to an unfair dismissal, except mutual-agreement exits under collective incentive schemes. In collective dismissals (Art. 51 ET) and dismissals under Art. 52.c ET, when due to economic, technical, organisational or production reasons or force majeure, the part up to the compulsory unfair-dismissal limit is exempt. Any excess is included and prorated over the 12 months before the month of termination, whatever the termination date (Art. 147.2.c LGSS; Art. 23.2.B RD 2064/1995).')
# ETP table, ETP-002
replace_para(4099,'Excluded (generally)','Included only for the part above the exempt amount of Art. 147.2.c LGSS (see Treatment of Excess; no €180,000 cap), prorated over the 12 months before the termination month')
# Worked example table, Ex-Gratia Severance, SS base
assert ptxt(paras[4186].group(0)).strip()=='Ex-Gratia Severance'
replace_para(4190,'€0.00 (Excluded)','€36,712.60 (Included, prorated: €3,059.38 a month, Dec 2024 to Nov 2025)')
# Worked example, new step after Step 7
new_para_after(4214,'Employee Cost (6.50%)',
 'Step 8: Social Security on the Severance Excess: the €36,712.60 excess (Ex-gratia) is included in the contribution base and prorated over the 12 months before the month of termination, December 2024 to November 2025: €36,712.60 ÷ 12 = €3,059.38 a month (Art. 147.2.c LGSS; Art. 23.2.B RD 2064/1995). The statutory €63,287.40 stays excluded. In this example the monthly pay (€70,000 ÷ 12 = €5,833.33) is above the 2025 maximum base (€4,909.50 a month), so the common contingencies base of January to November 2025 does not increase; the part above the maximum base is subject to the solidarity contribution (Art. 19 bis and DT 42.ª LGSS, from 2025). For December 2024, apply the 2024 maximum base.')

# version table: clone row 1.7
rows=list(re.finditer(r'<w:tr\b.*?</w:tr>',x,flags=re.S))
r17=rows[6].group(0); assert ptxt(r17).startswith('1.729-Oct-26')
cells=re.findall(r'<w:tc\b.*?</w:tc>',r17,flags=re.S)
vals=['1.8','02-Nov-26','6.1.1 and 7.1: for the withholding rate, each descendant counts by half unless the employee is exclusively entitled (art. 84.2.º RIRPF; art. 61.1.ª LIRPF), in the Family Minimums summary (6.1.1) and in the Descendant Minimum row (7.1). 9.1: severance excess included in the Social Security base and prorated over the 12 months before the termination month (art. 147.2.c LGSS; art. 23.2.B RD 2064/1995), in Treatment of Excess, ETP-002 and the worked example (Ex-Gratia row and new Step 8), in line with the Social Security base table.','Updated','Wallisson Gomes']
newcells=[]
for c,v in zip(cells,vals):
    tcpr=re.search(r'<w:tcPr>.*?</w:tcPr>',c,flags=re.S).group(0) if '<w:tcPr>' in c else ''
    pm=re.search(r'<w:p\b.*?</w:p>',c,flags=re.S).group(0)
    pp=re.search(r'<w:pPr>.*?</w:pPr>',pm,flags=re.S); pp=pp.group(0) if pp else '<w:pPr></w:pPr>'
    pp=re.sub(r'<w:rPr>.*?</w:rPr>','',pp,flags=re.S)
    rp=re.search(r'<w:r\b[^>]*>(<w:rPr>.*?</w:rPr>)',pm,flags=re.S); rp=rp.group(1) if rp else '<w:rPr/>'
    pp2=pp.replace('</w:pPr>',f'<w:rPr><w:ins {a()}/></w:rPr></w:pPr>')
    newcells.append(f'<w:tc>{tcpr}<w:p>{pp2}{ins_run(v,rp)}</w:p></w:tc>')
trpr=re.search(r'<w:trPr>.*?</w:trPr>',r17,flags=re.S)
trpr_s=re.sub(r'<w:ins [^>]*/>','',trpr.group(0)) if trpr else ''
trpr_new=(trpr_s.replace('</w:trPr>',f'<w:ins {a()}/></w:trPr>') if trpr_s else f'<w:trPr><w:ins {a()}/></w:trPr>')
newrow='<w:tr>'+trpr_new+''.join(newcells)+'</w:tr>'
spans=[(paras[i].start(),paras[i].end(),v) for i,v in edits.items()]+[(rows[6].end(),rows[6].end(),newrow)]
for s,e,v in sorted(spans,key=lambda t:-t[0]): x=x[:s]+v+x[e:]
open(P,'w',encoding='utf-8').write(x)
print('ok edits',len(edits),'ids up to',nid[0])
