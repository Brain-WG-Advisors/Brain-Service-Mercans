import sys,openpyxl,re
sys.stdout.reconfigure(encoding='utf-8')
for f in sys.argv[1:]:
    ws=openpyxl.load_workbook(f,read_only=True)['Sample File']
    bad=0;n=0
    for i,r in enumerate(ws.iter_rows(values_only=True),1):
        v=r[0]
        if isinstance(v,str):
            m=re.match(r'\s*pos\s+(\d+)-(\d+)\s*\|(.*)\|\s*$',v)
            if m:
                n+=1; a,b=int(m.group(1)),int(m.group(2)); L=len(m.group(3))
                if L!=b-a+1: bad+=1; print(f[-40:],i,a,b,'len',L,'expected',b-a+1)
    print(f[-60:],'segments',n,'bad',bad)
