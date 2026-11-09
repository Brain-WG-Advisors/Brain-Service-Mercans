import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sir_common as S
miss=0
for k in S.SIR_KEYS:
    f=S.fact(k)
    m,hc=S.f44_miss(f)
    if m: miss+=1; print(k,m[:4],'nocopy' if not hc else '')
print(miss,len(S.SIR_KEYS))
