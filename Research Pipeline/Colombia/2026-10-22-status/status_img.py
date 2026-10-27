import sys
from PIL import Image, ImageDraw, ImageFont
out=sys.argv[1]
F='C:/Windows/Fonts/'
f=lambda n,s: ImageFont.truetype(F+n,s)
T,H,B,BB,S=f('segoeuib.ttf',30),f('segoeuib.ttf',19),f('segoeui.ttf',16),f('segoeuib.ttf',16),f('segoeui.ttf',13)
W=1500
NAVY=(31,56,100); GREEN=(46,125,50); AMBER=(230,145,0); BLUE=(25,118,210); GREY=(110,110,110); RED=(183,28,28)
rows=[
 ('Done', GREEN, [
  ('Compliance','7 report specs final (v1.0) on Drive, incl. new CO-PILA-007 (PILA for pensioners paid by the employer)','22 Oct','Done'),
  ('Compliance','BAU answers of 16, 21 and 22 Oct reflected in the specs','22 Oct','Done'),
  ('Compliance','SIR v1.1, CCG v1.3, WTC v1.5, DD v1.2 on Drive; Monday links updated','22 Oct','Done'),
  ('BAU','Pensioners: no shared pensions with Colpensiones; no CCF contributions paid for pensioners','22 Oct','Answered'),
  ('BAU','871 electronic payroll files of September shared in one zip','22 Oct','Shared'),
  ('Andy','Non-statutory reports moved to a separate tab of the plan','22 Oct','Done'),
 ]),
 ('Waiting on others', AMBER, [
  ('BAU -> mapping team','Conceptos CIR points: WT 21330 / 25834, 21644, 65820, 62839, 23552; FSP on pensions','-','Forwarded by BAU 22 Oct'),
  ("Mohit's team",'Confirm Colombia design start and completion date (31 Oct no longer holds)','-','Requested 22 Oct'),
  ('Cinthya','Testing plan on a new clean entity (consult Nabil); rows 44-45 of the plan','-','Open'),
 ]),
 ('Compliance next steps', BLUE, [
  ('Compliance','Review the September electronic payroll files; send any delta to Mohit','28 Oct','Files received'),
  ('Compliance','Update the plan dates from design onward','-',"After Mohit's reply"),
  ('Compliance','Bonus and interest reports assessment (plan row 12)','tbc','Not started'),
 ]),
 ('Open - no official source located', GREY, [
  ('DIAN','Electronic payroll: no worker-type code for pensioners paid by the employer (Anexo Tecnico v1.0)','-','Recorded'),
  ('UGPP / case law','Denominator of the 40% non-salary limit','-','Recorded'),
 ]),
]
cols=[(30,'Owner',230),(270,'Item',860),(1140,'Due',90),(1240,'Status',230)]
def wrap(d,t,font,w):
    words=t.split(); lines=[]; cur=''
    for x in words:
        tt=(cur+' '+x).strip()
        if d.textlength(tt,font=font)<=w: cur=tt
        else: lines.append(cur); cur=x
    lines.append(cur); return lines
img=Image.new('RGB',(W,3000),'white'); d=ImageDraw.Draw(img)
y=25
d.text((30,y),'Colombia (PMI) - status 22 Oct 2026',font=T,fill=NAVY); y+=48
d.text((30,y),'Plan milestones: compliance fixes 20 Nov  |  regression 4 Dec  |  parallel run / UAT sign-off 18 Dec',font=B,fill=GREY); y+=40
for title,color,items in rows:
    d.rectangle([30,y,W-30,y+34],fill=color); d.text((42,y+5),title,font=H,fill='white'); y+=40
    d.rectangle([30,y,W-30,y+26],fill=(240,242,245))
    for x,h,w in cols: d.text((x+8,y+3),h,font=BB,fill=(60,60,60))
    y+=30
    for i,(o,it,du,st) in enumerate(items):
        ls=wrap(d,it,B,cols[1][2]-16); lo=wrap(d,o,B,cols[0][2]-16); rh=max(len(ls),len(lo))*22+10
        if i%2: d.rectangle([30,y,W-30,y+rh],fill=(250,250,252))
        for k,l in enumerate(lo): d.text((cols[0][0]+8,y+5+k*22),l,font=B,fill=(30,30,30))
        for k,l in enumerate(ls): d.text((cols[1][0]+8,y+5+k*22),l,font=B,fill=(30,30,30))
        d.text((cols[2][0]+8,y+5),du,font=B,fill=(30,30,30))
        d.text((cols[3][0]+8,y+5),st,font=BB,fill=color if color!=GREY else (80,80,80))
        y+=rh; d.line([30,y,W-30,y],fill=(225,225,225))
    y+=18
d.text((30,y),'Source: Columbia Regulation Plan (updated 22 Oct) and e-mails of 22 Oct in the PMI Review thread.',font=S,fill=GREY); y+=30
img.crop((0,0,W,y)).save(out); print(out, y)
