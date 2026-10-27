"""CCG v1.4: 40% test denominator per UGPP ABC Empleadores 2025 (PENDING #57), in place by XML surgery. Usage: python -I ccg_decisao57.py <docx>"""
import zipfile, sys, html, shutil, os, datetime
sys.stdout.reconfigure(encoding='utf-8')
src = sys.argv[1]
z = zipfile.ZipFile(src); data = {n: z.read(n) for n in z.namelist()}
d = data['word/document.xml'].decode('utf8')
OLD = ("UGPP's published guidance (2021, prior to the ruling) takes all salary and non-salary payments of the period, excluding the social benefits "
       "of CST titles VIII and IX, vacation pay and indemnities. Configure the denominator on that basis until UGPP or the Consejo de Estado says otherwise.")
NEW = ("UGPP's guidance for employers (ABC Empleadores, 2025) defines it as all salary payments plus the pacted non-salary payments plus paid leave, "
       "leaving out indemnities, unpaid leave, incapacities and social benefits. Payments that are non-salary by nature are therefore outside both the "
       "numerator and the total. Vacation pay is not part of the total: it is not in the 2025 formula, and UGPP's 2021 guidance excluded it expressly.")
VC_OLD = "general-illness incapacity - the incapacity value as the IBC, no occupational-risk contribution."
VC_NEW = VC_OLD + " Module 4: total remuneration of the 40% test of Law 1393 of 2010 art. 30 per UGPP ABC Empleadores 2025."
for o, n in ((OLD, NEW), (VC_OLD, VC_NEW)):
    e = html.escape(o, quote=False); assert d.count(e) == 1, (o[:50], d.count(e))
    d = d.replace(e, html.escape(n, quote=False), 1)
data['word/document.xml'] = d.encode('utf8')
prev = os.path.join(os.path.dirname(os.path.abspath(src)), '_previous'); os.makedirs(prev, exist_ok=True)
shutil.copy2(src, os.path.join(prev, os.path.basename(src)[:-5] + '.' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.docx'))
tmp = src + '.tmp'
with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as out:
    for info in z.infolist(): out.writestr(info, data[info.filename])
z.close(); os.replace(tmp, src); print('ok: S23 denominator, VC 1.4 line')
