import csv,sys,re
r={x['id']:x for x in csv.DictReader(open(sys.argv[1],encoding='utf-8'))}
pat=sys.argv[2]
for i,x in r.items():
  if re.search(pat,i): print(i,x['status'],x['tier'],'|',x['figure_or_rule_carried'][:int(sys.argv[3]) if len(sys.argv)>3 else 110].replace('\n',' '))
