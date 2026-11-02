import sys,re,openpyxl
sys.stdout.reconfigure(encoding='utf-8')
from lxml import etree
wb=openpyxl.load_workbook(sys.argv[1],data_only=True); ws=wb['Sample File']
lines=[]
for r in range(55,200):
    v=ws.cell(r,1).value
    if v is None: continue
    lines.append(str(v))
    if '</NominaIndividual>' in str(v): break
xml='\n'.join(lines)
open('ne_sample_v2.xml','w',encoding='utf-8').write(xml)
sch=etree.XMLSchema(etree.parse('xsd/XSD/NominaIndividualElectronicaXSDV1.0.6.xsd'))
def val(s,label):
    try:
        d=etree.fromstring(s.encode('utf-8'))
    except Exception as e:
        print(label,'PARSE',e); return
    ok=sch.validate(d); print(label,'VALID' if ok else 'INVALID')
    for e in list(sch.error_log)[:6]: print('  ',e.line,e.message[:200])
val(xml.split('?>',1)[1] if xml.startswith('<?xml') else xml,'as-is')
fx=xml.replace('<NominaIndividual>','<NominaIndividual xmlns="dian:gov:co:facturaelectronica:NominaIndividual" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" SchemaLocation="">',1)
fx=re.sub(r'<(/?)UBLExtensions>',r'<\1ext:UBLExtensions>',fx); fx=re.sub(r'<(/?)UBLExtension>',r'<\1ext:UBLExtension>',fx); fx=re.sub(r'<(/?)ExtensionContent>',r'<\1ext:ExtensionContent>',fx)
pass
val(fx.split('?>',1)[1],'fixed')
m=re.search(r'TiempoLaborado="([^"]+)"',xml); print('TiempoLaborado',m and m.group(1))
