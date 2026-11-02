import sys; sys.stdout.reconfigure(encoding="utf-8",errors="replace")
import sys,re
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
parts=re.split(r'--- p\.(\d+) ---',t)
d={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for p in sys.argv[2].split(','):
    a,b=(p.split('-')+[p])[:2]
    for n in range(int(a),int(b)+1):
        print(f'=== p.{n} ==='); print(d.get(n,'')[:int(sys.argv[3]) if len(sys.argv)>3 else None])
