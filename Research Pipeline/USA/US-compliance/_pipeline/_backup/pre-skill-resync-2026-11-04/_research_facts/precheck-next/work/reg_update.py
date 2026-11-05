import os,csv,json,time,re,sys
BASE='.'
d=os.path.join(BASE,'00-official-sources/precheck-copies')
upd={}
for f in os.listdir(d):
    if not f.endswith('.raw'): continue
    p=os.path.join(d,f); b=open(p,'rb').read()
    rid=f[:-4]
    if len(b)<2000 or b[:200].lower().count(b'access denied')>0 or b'<title>429' in b[:600].lower():
        os.remove(p);continue
    ext='.pdf' if b[:4]==b'%PDF' else '.html'
    os.replace(p,os.path.join(d,rid+ext)); upd[rid]='00-official-sources/precheck-copies/'+rid+ext
print(len(upd),'copies kept')
REG=os.path.join(BASE,'00-official-sources/legal-basis-register.csv')
LOCK=os.path.join(BASE,'_research/facts.lock')
for i in range(300):
    try: fd=os.open(LOCK,os.O_CREAT|os.O_EXCL|os.O_WRONLY);break
    except FileExistsError: time.sleep(1)
else: sys.exit('lock busy')
try:
    raw=open(REG,encoding='utf-8',newline='').read()
    rows=list(csv.reader(raw.splitlines(True) and __import__('io').StringIO(raw)))
    h=rows[0];ci=h.index('local_file');ii=h.index('id');vi=h.index('verified_on')
    n=0
    for r in rows[1:]:
        if r and r[ii] in upd and not r[ci].strip(): r[ci]=upd[r[ii]];n+=1
    open(REG+'.precheck-bak','w',encoding='utf-8',newline='').write(raw)
    import io;o=io.StringIO();csv.writer(o,lineterminator='\n' if '\r\n' not in raw else '\r\n').writerows(rows)
    open(REG,'w',encoding='utf-8',newline='').write(o.getvalue())
    print('register rows updated',n)
finally:
    os.close(fd);os.remove(LOCK)
json.dump(upd,open('_research/precheck-next/work/upd.json','w'))
