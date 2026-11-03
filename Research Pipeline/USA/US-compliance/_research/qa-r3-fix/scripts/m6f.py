import sys; sys.path.insert(0,r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from g import *
t=text_of('00-official-sources/ccg-sources/MA/MA_DFML-PFML-contribution-rates_2026-11-02.html')
t=re.sub(r'\s+',' ',t)
for m in re.finditer(r'2027 Contribution rate split for employers with 25',t): print('MA|',t[m.start():m.start()+1200])
