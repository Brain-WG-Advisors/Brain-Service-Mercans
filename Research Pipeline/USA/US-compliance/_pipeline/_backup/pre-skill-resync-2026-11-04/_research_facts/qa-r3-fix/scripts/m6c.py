import sys; sys.path.insert(0,r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from g import *
print('MA2027'); grep('US-MAS5-012',r'2027 Contribution rate split',2,700)
print('PA'); grep('US-PAS5-001',r'overtime|one-half|1 1/2|one and',4)
print('WV'); grep('US-WVS5-015',r'per centum|percent',12,120)
print('DE'); grep('US-DEP52-001',r'per ?cent|%',6)
print('OH 5747.02 rows'); [print('  ',r['id'],r['instrument_name'][:90],r['local_file'][:80]) for r in rows if r['id'].startswith('US-OH') and '5747.02' in (r['instrument_name']+r['article_or_section'])]
print('OH 2.75'); grepall('OH',r'2\.75',6)
print('AR 250'); grepall('AR',r'(?<![\d,.])250(?![\d])|two hundred fifty',6)
