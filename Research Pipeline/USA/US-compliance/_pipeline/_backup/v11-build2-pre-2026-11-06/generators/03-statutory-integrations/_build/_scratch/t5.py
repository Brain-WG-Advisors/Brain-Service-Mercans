import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding='utf-8')
import sir_common as S
import collections
print(collections.Counter((r['tier'],r['status']) for r in S.REG.values()).most_common(12))
w=[]
for f in S.C.FACTS.values():
    pass
for k in S.SIR_KEYS:
    f=S.fact(k)
    if not S.reg_ok(f['register_id']) and re.search(r'\d',str(f['value'])): w.append((k,f['register_id'],S.REG.get(f['register_id'],{}).get('tier'),S.REG.get(f['register_id'],{}).get('status')))
print(len(w),w[:20])
# existence of candidate keys
for k in ['fed.form1042s.channel','rspec.fed.form940.due','rspec.fed.form944.due','rspec.fed.schedule_h.due','rspec.fed.aca.ty2026_due','fed.aca.efile_threshold','multi.iwo.governing_law','multi.iwo.remittance_business_days','fed.iwo.omb_expiry','fed.iwo.priority','fed.levy.exempt.single_0dep.monthly','rspec.fed.reporting_agent.form','rspec.fed.new_hire.electronic_interval','fed.w2.due_date','rspec.fed.form941x.deadlines','rspec.fed.form941.frequency','rspec.nm.wh_qtr_report.form','rspec.wa.wc_report.frequency','rspec.wy.wc_report.frequency','rspec.or.wc_report.frequency']:
    print(k, S.has(k), S.fact(k)['_file'] if S.has(k) else '')
