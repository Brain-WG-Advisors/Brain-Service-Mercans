import re,sys,html
sys.stdout.reconfigure(encoding='utf-8')
P='x/word/document.xml'
x=open(P,encoding='utf-8').read()
DATE='2026-10-29T00:00:00Z'; AUTH='Claude'
nid=[9000]
def a():
    nid[0]+=1; return f'w:author="{AUTH}" w:id="{nid[0]}" w:date="{DATE}"'
esc=lambda s: html.escape(s,quote=False)
RPR='<w:rPr><w:rFonts w:ascii="Google Sans" w:cs="Google Sans" w:eastAsia="Google Sans" w:hAnsi="Google Sans"/><w:color w:val="1f1f1f"/><w:rtl w:val="0"/></w:rPr>'
def ins_run(text,rpr=RPR): return f'<w:ins {a()}><w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:ins>'
def to_del(runs_xml):
    # wrap each plain run (not already inside ins/del) in w:del, w:t -> w:delText
    def f(m):
        r=m.group(0)
        if '<w:t' not in r: return r
        r=re.sub(r'<w:t( [^>]*)?>',lambda k:'<w:delText xml:space="preserve">',r).replace('</w:t>','</w:delText>')
        return f'<w:del {a()}>{r}</w:del>'
    return re.sub(r'<w:r\b(?:(?!<w:r\b).)*?</w:r>',f,runs_xml,flags=re.S)
paras=list(re.finditer(r'<w:p\b[^>]*>(?:(?!<w:p\b).)*?</w:p>',x,flags=re.S))
def ptxt(p): return ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>',p))
edits={}
def replace_para(i,expect,new):
    p=paras[i].group(0); t=html.unescape(ptxt(p))
    assert t.strip()==expect, (i,t)
    head,body=p.split('</w:pPr>',1) if '</w:pPr>' in p else (None,p)
    body=body[:-len('</w:p>')]
    nb=to_del(body)+ins_run(new)
    edits[i]=(head+'</w:pPr>' if head else '')+nb+'</w:p>'
# Scenario 3 (12.1)
replace_para(4692,'Health Insurance: Exempt up to €500/year per person. (Here €2,400/year > €500).',
 'Health Insurance: Exempt up to €500 per year for each covered person (€1,500 with a disability), Art. 42.3.c LIRPF and Art. 46 RIRPF. Luis is the only person covered, so his annual limit is €500 (here €2,400/year > €500).')
replace_para(4693,'Exempt part: €41.66/mo (500/12).',
 'Exempt part: the limit is annual, not €41.66 a month. Use the bucket logic of 7.2 (2. Health Insurance - Corrected): the premiums are exempt until the YTD premium reaches €500. January €200 and February €200 are exempt (YTD €400); in March €100 is exempt and €100 taxable; from April the full €200 is taxable (€500 exempt and €1,900 taxable in the year). The full €500 also applies to an employee who joins or leaves during the year (DGT binding ruling V1967-17).')
replace_para(4694,'Taxable part: €158.34/mo.','Taxable part (January): €0.00.')
replace_para(4697,'Taxable Base: €2,650 (Cash) + €158.34 (Taxable Health) = €2,808.34. (Note the reduction in tax base compared to standard €3,000).',
 'Taxable Base (January): €2,650 (Cash) + €0.00 (Taxable Health) = €2,650.00. (Note the reduction in tax base compared to standard €3,000). From April: €2,650 + €200 = €2,850.00.')
replace_para(4698,'Rate (Approx 15%): $2,808.34 × 0.15 = €421.25','Rate (Approx 15%), January: €2,650.00 × 0.15 = €397.50')
replace_para(4702,'Less Tax: €421.25.','Less Tax: €397.50.')
replace_para(4703,'Net Transfer: €2,033.755. (Plus he has the insurance and food card coverage).',
 'Net Transfer (January): €2,057.50. (Plus he has the insurance and food card coverage).')
# 6.1.2 pseudo-code: delete the v1.6 ROUND insertion, insert TRUNCATE
p=paras[1588].group(0)
m=re.search(r'(<w:ins [^>]*>)(<w:r\b.*?</w:r>)(</w:ins>)',p,flags=re.S)
assert 'ROUND(New_Rate, 2)' in m.group(2)
oldins=m.group(1)+to_del(m.group(2))+m.group(3)
rpr=re.search(r'<w:rPr>.*?</w:rPr>',m.group(2),flags=re.S).group(0)
newp=p[:m.start()]+oldins+ins_run('    Final_Rate = TRUNCATE(New_Rate, 2)   # Arts. 86.1 and 87.3.c: two decimals, truncated (AEAT algorithm: TRUNCAR (TIPO)); never round up',rpr)+p[m.end():]
edits[1588]=newp
# 7.3.2 section 8: note after paragraph 3693
p=paras[3693].group(0)
assert ptxt(p).startswith('Reading the example')
ppr=re.search(r'<w:pPr>.*?</w:pPr>',p,flags=re.S).group(0)
ppr_ins=ppr.replace('<w:rPr/>',f'<w:rPr><w:ins {a()}/></w:rPr>') if '<w:rPr/>' in ppr else re.sub(r'</w:pPr>$',f'<w:rPr><w:ins {a()}/></w:rPr></w:pPr>',ppr) if '<w:rPr>' not in ppr else ppr.replace('<w:rPr>',f'<w:rPr><w:ins {a()}/>',1)
note=f'<w:p>{ppr_ins}'+ins_run('Note: 41.67 is the figure shown in the HRBS-11310 payslip (500 / 12). It is not a monthly limit. The exemption is €500 per year for each covered person (€1,500 with a disability), Art. 42.3.c LIRPF and Art. 46 RIRPF, applied with the bucket logic of 7.2 (2. Health Insurance - Corrected).')+'</w:p>'
edits[3693]=p+note
# version table: clone row 1.6
rows=list(re.finditer(r'<w:tr\b.*?</w:tr>',x,flags=re.S))
r16=rows[5].group(0); assert ptxt(r16).startswith('1.617-Sep-26')
cells=re.findall(r'<w:tc\b.*?</w:tc>',r16,flags=re.S)
vals=['1.7','29-Oct-26','HRBS-16407. 6.1.2: final rate in the pseudo-code truncated to two decimals, Final_Rate = TRUNCATE(New_Rate, 2), replacing CEILING(TRUNCATE(...)) and ROUND (arts. 86.1 and 87.3.c RIRPF; AEAT algorithm, TRUNCAR (TIPO)), in line with the rounding rule of 6.1 (6. Final Withholding Rate). 12.1 Scenario 3: health insurance exemption applied per year and per covered person with the bucket logic of 7.2 (art. 42.3.c LIRPF; art. 46 RIRPF; DGT V1967-17), replacing the fixed €41.66 a month; tax and net pay recalculated. 7.3.2 (8. Worked Example): note that 41.67 is the HRBS-11310 payslip figure, not a monthly limit.','Updated','Wallisson Gomes']
newcells=[]
for c,v in zip(cells,vals):
    tcpr=re.search(r'<w:tcPr>.*?</w:tcPr>',c,flags=re.S).group(0) if '<w:tcPr>' in c else ''
    pm=re.search(r'<w:p\b.*?</w:p>',c,flags=re.S).group(0)
    pp=re.search(r'<w:pPr>.*?</w:pPr>',pm,flags=re.S); pp=pp.group(0) if pp else '<w:pPr></w:pPr>'
    rp=re.search(r'<w:r\b[^>]*>(<w:rPr>.*?</w:rPr>)',pm,flags=re.S); rp=rp.group(1) if rp else '<w:rPr/>'
    pp2=pp.replace('</w:pPr>',f'<w:rPr><w:ins {a()}/></w:rPr></w:pPr>') if '<w:rPr' not in pp else pp
    newcells.append(f'<w:tc>{tcpr}<w:p>{pp2}{ins_run(v,rp)}</w:p></w:tc>')
trpr=re.search(r'<w:trPr>.*?</w:trPr>',r16,flags=re.S)
trpr_new=(trpr.group(0).replace('</w:trPr>',f'<w:ins {a()}/></w:trPr>') if trpr else f'<w:trPr><w:ins {a()}/></w:trPr>')
newrow='<w:tr>'+trpr_new+''.join(newcells)+'</w:tr>'
# apply edits from end to start
spans=[(paras[i].start(),paras[i].end(),v) for i,v in edits.items()]+[(rows[5].end(),rows[5].end(),newrow)]
for s,e,v in sorted(spans,key=lambda t:-t[0]): x=x[:s]+v+x[e:]
open(P,'w',encoding='utf-8').write(x)
print('ok edits',len(edits),'ids up to',nid[0])
