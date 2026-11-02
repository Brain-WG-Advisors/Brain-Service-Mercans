"""Zip payroll-compliance-colombia/ (SKILL.md + references/) with the same layout as the France skill zip."""
import os, zipfile
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(S, 'payroll-compliance-colombia')
Z = os.path.join(S, 'payroll-compliance-colombia.zip')
files = ['SKILL.md'] + ['references/' + f for f in sorted(os.listdir(os.path.join(SK, 'references')))]
with zipfile.ZipFile(Z, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(os.path.join(SK, *f.split('/')), 'payroll-compliance-colombia/' + f)
with zipfile.ZipFile(Z) as z:
    assert z.testzip() is None
    for i in z.infolist(): print(i.filename, i.file_size)
