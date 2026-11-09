import sys, openpyxl, collections
a=openpyxl.load_workbook(sys.argv[1]); b=openpyxl.load_workbook(sys.argv[2])
print("sheets", a.sheetnames==b.sheetnames)
cnt=collections.Counter(); ex={}
for n in a.sheetnames:
    if n not in b.sheetnames: print("missing",n); continue
    A,B=a[n],b[n]
    for r in range(1,max(A.max_row,B.max_row)+1):
        for c in range(1,max(A.max_column,B.max_column)+1):
            x,y=A.cell(r,c).value,B.cell(r,c).value
            if x!=y:
                k=(n,openpyxl.utils.get_column_letter(c)); cnt[k]+=1; ex.setdefault(k,[]).append(r)
for k,v in sorted(cnt.items()): print(k,v,ex[k][:12])
