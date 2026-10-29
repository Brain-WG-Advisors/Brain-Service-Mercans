"""Final step for LT-SIR-001-v1.1.docx, after Word refreshed the TOC (update_toc_word.ps1).

Word drops w:updateFields and writes its own user into lastModifiedBy on save, so this
script puts back the document settings the build requires:
  - w:updateFields = true (TOC and PAGE fields refreshed when the file is opened)
  - core properties: author / last modified by "Mercans Compliance", title, subject,
    no python-docx description, created/modified = now (UTC)
"""
import datetime
import os
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "LT-SIR-001-v1.1.docx")

doc = Document(PATH)
settings = doc.settings.element
for old in settings.findall(qn("w:updateFields")):
    settings.remove(old)
uf = OxmlElement("w:updateFields")
uf.set(qn("w:val"), "true")
settings.append(uf)

now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
cp = doc.core_properties
cp.author = "Mercans Compliance"
cp.last_modified_by = "Mercans Compliance"
cp.title = "Lithuania Statutory Integration Register (LT-SIR-001 v1.1)"
cp.subject = "Statutory Integration Register, Lithuania, tax year 2026"
cp.comments = ""
cp.created = now
cp.modified = now
doc.save(PATH)
print("finalized:", PATH)
