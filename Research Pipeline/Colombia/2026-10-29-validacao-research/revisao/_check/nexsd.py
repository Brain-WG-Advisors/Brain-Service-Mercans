import sys,openpyxl
from lxml import etree
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
ws=wb['Sample File']
rows=[r[0] for r in ws.iter_rows(values_only=True)]
# find xml start/end
s=next(i for i,v in enumerate(rows) if isinstance(v,str) and v.lstrip().startswith('<?xml'))
e=max(i for i,v in enumerate(rows) if isinstance(v,str) and '</NominaIndividual>' in v)
xml='\n'.join((rows[i] or '') for i in range(s,e+1))
open(sys.argv[3],'w',encoding='utf-8').write(xml)
print('rows',s+1,e+1)
schema=etree.XMLSchema(etree.parse(sys.argv[2]))
doc=etree.fromstring(xml.encode('utf-8'))
ok=schema.validate(doc); print('VALID' if ok else 'INVALID'); 
for er in list(schema.error_log)[:10]: print(er)
