import sys; sys.path.insert(0,r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from g import *
t=text_of('00-official-sources/ccg-sources/MA/MA_DFML-PFML-contribution-rates_2026-11-02.html'); i=t.find('2027 Contribution'); print('MA2027|',re.sub(r'\s+',' ',t[i:i+1000]))
t=text_of('00-official-sources/ccg-sources/OH/ORC-5747.02_codes-ohio_2026-11-02.html')
for m in list(re.finditer(r'2026|two and three|2\.75|per cent',t))[:8]: print('OH|',snippet(t,m.start(),200))
t=text_of(files_of(R['US-WVS5-015'])[0])
for m in list(re.finditer(r'seven and five-tenths|six and five-tenths|surtax',t))[:4]: print('WV|',snippet(t,m.start(),200))
