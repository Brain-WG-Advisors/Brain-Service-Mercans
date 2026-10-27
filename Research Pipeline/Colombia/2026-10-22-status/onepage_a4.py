import sys
from PIL import Image, ImageDraw, ImageFont
ref, out = sys.argv[1], sys.argv[2]
W, H = 1588, 2600
F = 'C:/Windows/Fonts/'
def f(n, s): return ImageFont.truetype(F + n, s)
BOLD, REG, SEMI = 'segoeuib.ttf', 'segoeui.ttf', 'seguisb.ttf'
try: ImageFont.truetype(F + SEMI, 10)
except OSError: SEMI = 'segoeuib.ttf'
NAVY=(0,47,63); TEAL=(0,122,164); ORANGE=(255,153,0); INK=(26,31,34); MUTED=(61,71,77)
HEADBG=(238,243,245); BORDER=(204,210,213); CHIPB=((214,237,244),(0,90,122)); CHIPO=((255,231,209),(138,51,0)); WARM=(138,51,0)
img = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(img)
M = 80
def wrap(t, font, w):
    out, cur = [], ''
    for x in t.split():
        tt = (cur + ' ' + x).strip()
        if d.textlength(tt, font=font) <= w: cur = tt
        else: out.append(cur); cur = x
    out.append(cur); return out
# header
d.rectangle([0,0,W,405], fill=NAVY)
logo = Image.open(ref).convert('RGB').crop((80,52,156,136)); img.paste(logo,(M,52))
d.text((M+100,72),'MERCANS · COMPLIANCE',font=f(BOLD,30),fill='white')
rt='PMI Review · 22 October 2026'; ft=f(REG,24); d.text((W-M-d.textlength(rt,font=ft),78),rt,font=ft,fill='white')
d.text((M,163),'Colombia · PMI',font=f(BOLD,25),fill=ORANGE)
d.text((M,195),'Artifact Review Status and Next Steps',font=f(BOLD,58),fill='white')
def pill(x,y,t,fill,txt,outline=None,bold=True):
    ft=f(BOLD if bold else REG,23); w=d.textlength(t,font=ft)+50
    d.rounded_rectangle([x,y,x+w,y+60],radius=30,fill=fill,outline=outline,width=2)
    d.text((x+25,y+14),t,font=ft,fill=txt); return x+w
x=pill(M,300,'Research completion: end of Oct 2026',ORANGE,INK)
pill(x+20,300,'Design start (estimate): 20 Nov',NAVY,'white',outline=(200,210,215),bold=False)
y=455
def section(t):
    global y
    d.text((M,y),t,font=f(BOLD,33),fill=TEAL); y+=62
def table(cols, rows, chipcol=None, warmcol=None):
    global y
    x0,x1=M,W-M; top=y
    hf,bf=f(SEMI,23),f(REG,23); bb=f(SEMI,23)
    d.rectangle([x0,y,x1,y+62],fill=HEADBG)
    for cx,h,_ in cols: d.text((x0+cx,y+16),h,font=hf,fill=MUTED)
    y+=62
    for r in rows:
        lines=[wrap(r[i],bb if i==0 else bf,cols[i][2]) for i in range(len(cols))]
        if chipcol is not None: lines[chipcol]=[r[chipcol]]
        rh=max(len(l) for l in lines)*34+30
        d.line([x0,y,x1,y],fill=BORDER,width=1)
        for i,(cx,_,cw) in enumerate(cols):
            if i==chipcol:
                kind=r[-1]; bg,tx=CHIPO if kind=='o' else CHIPB
                cf=f(BOLD,21); tw=d.textlength(r[i],font=cf)
                d.rounded_rectangle([x0+cx,y+14,x0+cx+tw+30,y+52],radius=19,fill=bg); d.text((x0+cx+15,y+19),r[i],font=cf,fill=tx)
            else:
                ft=bb if i==0 else bf; col=WARM if (i==warmcol and r[-1]=='w') else INK
                if i==warmcol and r[-1]=='w': ft=bb
                for k,l in enumerate(lines[i]): d.text((x0+cx,y+15+k*34),l,font=ft,fill=col)
        y+=rh
    d.rounded_rectangle([x0,top,x1,y],radius=16,outline=BORDER,width=2)
    y+=14
def note(t, size=22):
    global y
    for l in wrap(t,f(REG,size),W-2*M): d.text((M,y),l,font=f(REG,size),fill=MUTED); y+=32
    y+=30
section('1 · Artifact review status')
table([(24,'Artifact',320),(380,'Status',160),(600,'Notes',790)],[
 ('SS and income tax logic','Confirmed','BAU answers of 16, 21 and 22 Oct reflected in the specs','b'),
 ('Wage Type Catalogue v1.5','Updated','Citations updated to Res. DIAN 000227 de 2025; client wage-type mapping points forwarded by BAU to the mapping team','b'),
 ('Country Configuration Guide v1.3','Updated','BAU suggestions resolved; pensioners\' health 4 / 10 / 12 %; vacation rules in the social security bases','b'),
 ('Statutory Integration (CO-SIR-001) v1.1','Updated','Res. DIAN 000013 de 2021 replaced by Res. 000227 de 2025, as BAU pointed out','b'),
 ('Data Dictionary v1.2','Updated','Termination date taken from the system Termination record; citations updated','b'),
 ('Statutory report specs','Final','7 specs (v1.0) on Drive, incl. new CO-PILA-007 (PILA for pensioners paid by the employer). September electronic payroll files under review','b'),
],chipcol=1)
note('All artifacts are on the Compliance Team Drive; the Monday links point to the current versions.')
section('2 · BAU answers of 22 Oct')
cards=[('Electronic payroll',['871 September files received (one zip)','Review by 28 Oct']),
       ('Pensioners',['No shared pensions with Colpensiones','No CCF contributions paid']),
       ('Wage-type mapping',['Conceptos CIR points forwarded to the mapping team'])]
cw=(W-2*M-2*24)/3; ch=200
for i,(t,ls) in enumerate(cards):
    x=M+i*(cw+24); d.rounded_rectangle([x,y,x+cw,y+ch],radius=18,fill=HEADBG)
    d.text((x+24,y+22),t,font=f(BOLD,24),fill=NAVY); yy=y+66
    for l in ls:
        for w_ in wrap(l,f(REG,23),cw-48): d.text((x+24,yy),w_,font=f(REG,23),fill=INK); yy+=34
        yy+=8
y+=ch+16
note('With these answers, the pension and CCF parts of CO-PILA-007 do not apply today.')
section('3 · Actions')
table([(24,'Owner',260),(320,'Action',640),(1010,'When',380)],[
 ('Wallisson','Review the September electronic payroll files; send any delta to Mohit\'s team','By 28 Oct','w'),
 ('Mohit\'s team','Confirm the new design start (estimate 20 Nov)','Requested 22 Oct','w'),
 ('Mapping team (via BAU)','Review the Conceptos CIR points: WT 21330 / 25834, 21644, 65820, 62839, 23552; FSP on pensions','Forwarded 22 Oct','n'),
 ('Cinthya','Testing plan on a new clean entity (consult Nabil)','-','n'),
 ('Andy / Wallisson','Update the plan dates from design onward','After Mohit\'s reply','n'),
 ('Wallisson','Bonus and interest reports assessment (plan row 12)','To be scheduled','n'),
],warmcol=2)
note("Plan dates from design onward will be updated after Mohit's confirmation." ' Open, no official source located: electronic payroll worker-type code for pensioners paid by the employer (DIAN); denominator of the 40% non-salary limit.')
img.crop((0,0,W,y+20)).save(out); print(out, y+20)
