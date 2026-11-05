import sys; sys.path.insert(0,r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from g import *
import pymupdf
d=pymupdf.open('00-official-sources/pdfs/DE/DE-wilm-doc462.bin',filetype='pdf')
t='\n'.join(f'[[PAGE {i+1}]]\n'+pg.get_text() for i,pg in enumerate(d)); print('DE pages',len(d))
for m in list(re.finditer(r'1\.25|one and one-quarter|1-1/4|1 1/4',t))[:5]: print('  DE p',page_at(t,m.start()),'|',snippet(t,m.start(),160))
t=text_of('00-official-sources/ccg-sources/MA/MA_DFML-PFML-contribution-rates_2026-11-02.html'); i=t.find('2027 Contribution rate split'); print('MA2027|',re.sub(r'\s+',' ',t[i:i+900]))
t=text_of(files_of(R['US-WVS5-015'])[0]); i=t.find('TABLE II'); print('WV|',re.sub(r'\s+',' ',t[i:i+2500]))
print('OH 5747.02 rows'); [print('  ',r['id'],r['instrument_name'][:90],r['local_file'][:80]) for r in rows if r['id'].startswith('US-OH') and '5747.02' in (r['instrument_name']+r['article_or_section'])]
print('OH 2.75'); grepall('OH',r'2\.75',6)
print('AR 250'); grepall('AR',r'(?<![\d,.])250(?![\d])|two hundred fifty',6)
