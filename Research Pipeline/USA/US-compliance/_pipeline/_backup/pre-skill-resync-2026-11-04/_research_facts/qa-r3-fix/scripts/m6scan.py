import json,glob,sys
sys.path.insert(0,'.')
from lib import *
keys=['ar.report.sui.efile_threshold_employees','co.famli.employee.rate','co.famli.employer.rate','de.local.wilmington.eit.rate','ma.pfml.family.rate','ma.pfml.medical.rate','ms.oracle.weekly_460_0ex.withholding','nc.overtime.premium.multiplier','pa.overtime.premium.multiplier','nd.data.breach.ag_threshold','sd.data.breach.ag_threshold','oh.pit.municipal.count_in_force','oh.wh.supplemental.rate','wa.pit.high_income_tax.agi_threshold','wv.sui.employer.rate.max']
fields,rows=load_reg(); R={r['id']:r for r in rows}
for fn in facts_files():
    d=json.load(open(fn,encoding='utf-8'))
    for f in d['facts']:
        if f['key'] in keys or (f['register_id']=='US-SCS5-004' and 'band' in f['key']):
            r=R.get(f['register_id'],{})
            print('##',fn.split('/')[-1],f['key'],repr(f['value']),f.get('effective_from'),f['register_id'],'|',r.get('local_file','')[:90],'|',(f.get('note') or '')[:150])
