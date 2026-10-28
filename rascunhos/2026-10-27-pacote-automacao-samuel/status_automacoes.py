import sys
from PIL import Image, ImageDraw, ImageFont
ref, out = sys.argv[1], sys.argv[2]
W, H = 1588, 2800
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

d.rectangle([0,0,W,575], fill=NAVY)
logo = Image.open(ref).convert('RGB').crop((80,52,156,136)); img.paste(logo,(M,52))
d.text((M+100,72),'MERCANS · COMPLIANCE',font=f(BOLD,30),fill='white')
rt='Status · 28 October 2026'; ft=f(REG,24); d.text((W-M-d.textlength(rt,font=ft),78),rt,font=ft,fill='white')
d.text((M,163),'Compliance automations',font=f(BOLD,25),fill=ORANGE)
d.text((M,195),'Testing Status',font=f(BOLD,58),fill='white')
# progress block
d.text((M,300),'OVERALL PROGRESS',font=f(BOLD,22),fill=(170,200,210))
big=f(BOLD,88); d.text((M,326),'60%',font=big,fill=ORANGE)
bx0=M+230; bx1=W-M; by0=362; by1=402
d.rounded_rectangle([bx0,by0,bx1,by1],radius=20,fill=(20,75,92))
fx=bx0+int((bx1-bx0)*0.60)
d.rounded_rectangle([bx0,by0,fx,by1],radius=20,fill=ORANGE)
for pct in (25,50,75):
    tx=bx0+int((bx1-bx0)*pct/100); d.line([tx,by1+6,tx,by1+14],fill=(120,150,160),width=2)
    lb=f'{pct}%'; lf=f(REG,18); d.text((tx-d.textlength(lb,font=lf)/2,by1+16),lb,font=lf,fill=(150,175,185))
def pill(x,y,t,fill,txt,outline=None,bold=True):
    ft=f(BOLD if bold else REG,23); w=d.textlength(t,font=ft)+50
    d.rounded_rectangle([x,y,x+w,y+60],radius=30,fill=fill,outline=outline,width=2)
    d.text((x+25,y+14),t,font=ft,fill=txt); return x+w
x=pill(M,478,'Redline: full cycle tested on the test board',NAVY,'white',outline=(200,210,215),bold=False)
pill(x+20,478,'SCA: design done, build not started',NAVY,'white',outline=(200,210,215),bold=False)
y=625
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

section('1 · Ticket → Artifact Redline (Muhammad Muneeb Tahir)')
table([(24,'Stage',520),(580,'Status',180),(800,'Tested',590)],[
 ('Read the resolved YouTrack ticket, Skill File and routing','Tested','Against real services, 13 Oct','b'),
 ('Research in the official source','Tested','Canada test ticket, 14 Oct','b'),
 ('Find the live document through the Monday link','Tested','27 Oct','b'),
 ('Draft the change as tracked changes in a copy','Tested','Test document, 14 Oct','b'),
 ('Approval in the reviewer app (approver recorded)','Tested','13 and 21 Oct','b'),
 ('Publish: Drive, Archived, Monday, closing comment, ticket Resolved','Tested','Test board (HRBS-9), 21 and 27 Oct','b'),
 ('Clean published version; redlined copy kept in Archived','Tested','27 Oct','b'),
 ('Real tickets: HRBS-14331, 14055, 11806','Next test','Tickets sent to Muhammad on 14–15 Oct','o'),
],chipcol=1)
note('All runs so far used the Monday test board.')
section('2 · Statutory Change Alert (SCA)')
cards=[('Design',['BRD, user stories and flow shared on 31 Aug','Merged into the consolidated BRD shared on 11 Sep']),
       ('Build',['Not started','No developer assigned']),
       ('Today',['Alerts are produced manually with a prompt'])]
cw=(W-2*M-2*24)/3; ch=230
for i,(t,ls) in enumerate(cards):
    x=M+i*(cw+24); d.rounded_rectangle([x,y,x+cw,y+ch],radius=18,fill=HEADBG)
    d.text((x+24,y+22),t,font=f(BOLD,24),fill=NAVY); yy=y+66
    for l in ls:
        for w_ in wrap(l,f(REG,23),cw-48): d.text((x+24,yy),w_,font=f(REG,23),fill=INK); yy+=34
        yy+=8
y+=ch+16
note('The SCA has not reached testing yet.')
section('3 · Next steps')
table([(24,'Owner',300),(360,'Action',700),(1100,'Status',300)],[
 ('Muhammad','Run the three real tickets end to end','Next test','w'),
 ('Wallisson','Review the real-ticket results with Muhammad','After the run','n'),
 ('To be defined','Assign a developer for the SCA build','Open','w'),
],warmcol=2)
img.crop((0,0,W,y+20)).save(out); print(out, y+20)
