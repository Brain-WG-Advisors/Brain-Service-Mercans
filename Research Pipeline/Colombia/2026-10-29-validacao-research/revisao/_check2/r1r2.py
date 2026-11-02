import sys,json
sys.stdout.reconfigure(encoding='utf-8')
a=json.load(open(sys.argv[1],encoding='utf-8')); b=json.load(open(sys.argv[2],encoding='utf-8'))
A={x['sheet']+'!'+x['cell']:x for x in a['cells']}; B={x['sheet']+'!'+x['cell']:x for x in b['cells']}
n=int(sys.argv[3]) if len(sys.argv)>3 else 600
print('r1',len(A),'r2',len(B))
for k in sorted(set(A)|set(B)):
    va=A.get(k,{}).get('new','<base>') if k in A else '<=base>'
    vb=B[k]['new'] if k in B else '<=base>'
    if va!=vb:
        print('##',k,'| base:',str(B.get(k,A.get(k))['old'])[:n])
        print('   R1:',str(va)[:n]); print('   R2:',str(vb)[:n])
