import glob,re,sys,os
sys.path.insert(0,'.'); from langdefs import FR,NL,EN
from openpyxl import load_workbook
HOM={'moment','minutes','date','zone','si','ce','au','entre','ne'}
for f in sorted(glob.glob(sys.argv[1]+'/*_v1.1.xlsx')):
  wb=load_workbook(f,read_only=True); core=[s for s in wb.sheetnames if s.endswith('Spec')][0]; bad=[]; acc=[]
  for i,r in enumerate(wb[core].iter_rows(values_only=True),start=1):
    if i==1: continue
    for col in 'GM':
      j=ord(col)-65; v=r[j] if j<len(r) else None
      if not isinstance(v,str): continue
      t=re.sub(r'\([^()]*\)','',v); t=re.sub(r'[«“"‘\'][^»”"’\']*[»”"’\']','',t)
      w=re.findall(r'[a-zàâçéèêëîïôûùüÿœ]+',t.lower())
      fw=[x for x in w if x in FR and x not in HOM]
      if fw: bad.append((col+str(i),fw,v[:110]))
      if re.search(r'[àâçéèêîôûœ]',t): acc.append((col+str(i),t[:140]))
  print(os.path.basename(f),'FR-words',len(bad)); [print('   W',b) for b in bad[:8]]
  print('   accents outside ()/quotes',len(acc)); [print('   A',a) for a in acc[:8]]
