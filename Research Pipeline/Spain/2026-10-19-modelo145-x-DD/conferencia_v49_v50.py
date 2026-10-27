import openpyxl,sys
sys.stdout.reconfigure(encoding="utf-8")
A=openpyxl.load_workbook(sys.argv[1]); B=openpyxl.load_workbook(sys.argv[2])
def shift5(r): return r if r<=56 else r+5 if r<=72 else r+69 if r<=78 else r+71
def shift1(r): return r+1 if r>=34 else r
def sig(c): 
    f=c.font; al=c.alignment; b=c.border
    return (c.value, c.fill.fill_type, c.fill.fgColor.rgb, f.name, f.sz, f.b, f.i, f.color.rgb if f.color else None, c.number_format, al.horizontal, al.vertical, al.wrap_text, *[getattr(getattr(b,k),"style",None) for k in ("left","right","top","bottom")])
NEW5=set(range(57,62))|set(range(78,142))|{148,149}
out={}
assert A.sheetnames==B.sheetnames
for name in A.sheetnames:
    a,b=A[name],B[name]
    f=shift5 if name=="Country Fields" else shift1 if name=="Version Control" else (lambda r:r)
    for row in a.iter_rows():
        for c in row:
            d=b.cell(f(c.row),c.column); sa,sb=sig(c),sig(d)
            if sa!=sb:
                fields=[i for i in range(len(sa)) if sa[i]!=sb[i]]
                out.setdefault(name,[]).append((c.coordinate,d.coordinate,fields,sa[0],sb[0],sa[2],sb[2]))
    mapr=lambda s: s
    print(name,"rows A",a.max_row,"B",b.max_row,"diffs",len(out.get(name,[])),"merged A/B",len(a.merged_cells.ranges),len(b.merged_cells.ranges))
for n,l in out.items():
    for x in l: print(n,x)
cf=B["Country Fields"]
print("NEW ROWS")
for r in sorted(NEW5): print(r,[cf.cell(r,k).value for k in (3,4,5,8,10,11,13,17,18,20,21,22,24)], cf.cell(r,4).fill.fgColor.rgb)
print("VC34",[B["Version Control"].cell(34,k).value for k in range(2,7)],B["Version Control"].cell(34,4).fill.fgColor.rgb)
print("tables",[(t.name,t.ref) for t in cf.tables.values()],"vs",[(t.name,t.ref) for t in A["Country Fields"].tables.values()])
