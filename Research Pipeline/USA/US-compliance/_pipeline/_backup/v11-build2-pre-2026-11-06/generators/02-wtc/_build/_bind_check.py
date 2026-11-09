import csv,sys
sys.path.insert(0,'02-wtc/_build')
import wtc_common as W
bad=0;n=0
for r in csv.DictReader(open('_pipeline/WTC-bindings.csv',encoding='utf-8')):
    n+=1
    if r['register_id'] not in W.rids(r['key']): bad+=1; print(r)
print('bindings',n,'not matching facts',bad)
