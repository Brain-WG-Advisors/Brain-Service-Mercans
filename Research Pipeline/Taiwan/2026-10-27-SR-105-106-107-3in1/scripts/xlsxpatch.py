"""XML-level patcher for Mercans .xlsx specs (methodology skill section 4).

- Never uses openpyxl.save(): edits sheet XML / styles.xml as text and repacks the zip,
  copying every untouched part unchanged (same decompressed bytes, same order, same ZipInfo).
- Every written cell gets a clone of its own style with a solid FFDDEBF7 fill (light blue).
- Text is written as inline strings (sharedStrings.xml is left untouched).
"""
import json
import re
import zipfile
from xml.sax.saxutils import escape

BLUE = "FFDDEBF7"


def col2num(col):
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n


def split_ref(ref):
    m = re.match(r"([A-Z]+)(\d+)$", ref)
    return m.group(1), int(m.group(2))


class Book:
    def __init__(self, path):
        self.zin = zipfile.ZipFile(path)
        self.infos = self.zin.infolist()
        self.data = {i.filename: self.zin.read(i.filename) for i in self.infos}
        self.text = {}          # part name -> edited text
        self.removed = set()
        self.log = []           # list of dicts: sheet, cell, value
        self._fill_id = None
        self._xf_clone = {}
        wb = self.data["xl/workbook.xml"].decode("utf-8")
        rels = self.data["xl/_rels/workbook.xml.rels"].decode("utf-8")
        relmap = {}
        for m in re.finditer(r"<Relationship ([^>]*?)/>", rels):
            a = m.group(1)
            rid = re.search(r'Id="([^"]+)"', a).group(1)
            tgt = re.search(r'Target="([^"]+)"', a).group(1)
            relmap[rid] = tgt
        self.sheets = {}
        for m in re.finditer(r'<sheet [^>]*?name="([^"]+)"[^>]*?r:id="([^"]+)"', wb):
            self.sheets[m.group(1)] = "xl/" + relmap[m.group(2)].lstrip("/").replace("xl/", "", 1) \
                if relmap[m.group(2)].startswith("/xl/") else "xl/" + relmap[m.group(2)]

    # ---------- text access ----------
    def get(self, part):
        if part not in self.text:
            self.text[part] = self.data[part].decode("utf-8")
        return self.text[part]

    def put(self, part, txt):
        self.text[part] = txt

    # ---------- styles ----------
    def _blue_fill_id(self):
        if self._fill_id is not None:
            return self._fill_id
        st = self.get("xl/styles.xml")
        m = re.search(r'<fills count="(\d+)">(.*?)</fills>', st, re.S)
        n = int(m.group(1))
        new_fill = ('<fill><patternFill patternType="solid"><fgColor rgb="%s"/>'
                    '<bgColor rgb="%s"/></patternFill></fill>' % (BLUE, BLUE))
        st = st[:m.start()] + '<fills count="%d">%s%s</fills>' % (n + 1, m.group(2), new_fill) + st[m.end():]
        self.put("xl/styles.xml", st)
        self._fill_id = n
        return n

    def _numfmt_id(self, code):
        st = self.get("xl/styles.xml")
        m = re.search(r'<numFmt numFmtId="(\d+)" formatCode="%s"/>' % re.escape(code), st)
        if m:
            return int(m.group(1))
        m = re.search(r'<numFmts count="(\d+)">(.*?)</numFmts>', st, re.S)
        ids = [int(i) for i in re.findall(r'numFmtId="(\d+)"', m.group(2))]
        nid = max(ids + [163]) + 1
        st = st[:m.start()] + '<numFmts count="%d">%s<numFmt numFmtId="%d" formatCode="%s"/></numFmts>' % (
            int(m.group(1)) + 1, m.group(2), nid, code) + st[m.end():]
        self.put("xl/styles.xml", st)
        return nid

    def blue_style(self, s, numfmt=None):
        s = int(s)
        key = (s, numfmt)
        if key in self._xf_clone:
            return self._xf_clone[key]
        nf = self._numfmt_id(numfmt) if numfmt else None
        fid = self._blue_fill_id()
        st = self.get("xl/styles.xml")
        m = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
        n = int(m.group(1))
        xfs = re.findall(r"<xf [^>]*?/>|<xf [^>]*?>.*?</xf>", m.group(2), re.S)
        assert len(xfs) == n, (len(xfs), n)
        src = xfs[s]
        head = re.match(r"<xf [^>]*?/?>", src).group(0)
        newhead = re.sub(r'fillId="\d+"', 'fillId="%d"' % fid, head) if "fillId=" in head \
            else head.replace("<xf ", '<xf fillId="%d" ' % fid, 1)
        if nf is not None:
            newhead = re.sub(r'numFmtId="\d+"', 'numFmtId="%d"' % nf, newhead) if "numFmtId=" in newhead                 else newhead.replace("<xf ", '<xf numFmtId="%d" ' % nf, 1)
            newhead = re.sub(r'applyNumberFormat="\d"', 'applyNumberFormat="1"', newhead) if "applyNumberFormat=" in newhead                 else newhead.replace("<xf ", '<xf applyNumberFormat="1" ', 1)
        if "applyFill=" in newhead:
            newhead = re.sub(r'applyFill="\d"', 'applyFill="1"', newhead)
        else:
            newhead = newhead.replace("<xf ", '<xf applyFill="1" ', 1)
        newxf = newhead + src[len(head):]
        st = st[:m.start()] + '<cellXfs count="%d">%s%s</cellXfs>' % (n + 1, m.group(2), newxf) + st[m.end():]
        self.put("xl/styles.xml", st)
        self._xf_clone[key] = n
        return n

    # ---------- cells ----------
    def set(self, sheet, ref, value, num=False, style_from=None, numfmt=None):
        part = self.sheets[sheet]
        x = self.get(part)
        col, row = split_ref(ref)
        cell_re = re.compile(r'<c r="%s"(?: [^>]*?)?(?:/>|>.*?</c>)' % ref, re.S)
        m = cell_re.search(x)

        def style_of(cref):
            mm = re.search(r'<c r="%s"( [^>]*?)?(?:/>|>)' % cref, x)
            if not mm or not mm.group(1):
                return 0
            ss = re.search(r's="(\d+)"', mm.group(1))
            return int(ss.group(1)) if ss else 0

        s = style_of(style_from) if style_from else (style_of(ref) if m else 0)
        ns = self.blue_style(s, numfmt)
        if value is None or value == "":
            newc = '<c r="%s" s="%d"/>' % (ref, ns)
        elif num:
            newc = '<c r="%s" s="%d"><v>%s</v></c>' % (ref, ns, value)
        else:
            newc = '<c r="%s" s="%d" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (
                ref, ns, escape(str(value)))
        if m:
            x = x[:m.start()] + newc + x[m.end():]
        else:
            rm = re.search(r'<row r="%d"([^>]*?)(/>|>(.*?)</row>)' % row, x, re.S)
            if rm:
                inner = rm.group(3) or ""
                cells = list(re.finditer(r'<c r="([A-Z]+)\d+"(?: [^>]*?)?(?:/>|>.*?</c>)', inner, re.S))
                pos = len(inner)
                for c in cells:
                    if col2num(c.group(1)) > col2num(col):
                        pos = c.start()
                        break
                inner = inner[:pos] + newc + inner[pos:]
                attrs = rm.group(1)
                x = x[:rm.start()] + '<row r="%d"%s>%s</row>' % (row, attrs, inner) + x[rm.end():]
            else:
                rows = list(re.finditer(r'<row r="(\d+)"', x))
                pos = None
                for r in rows:
                    if int(r.group(1)) > row:
                        pos = r.start()
                        break
                if pos is None:
                    pos = x.index("</sheetData>")
                x = x[:pos] + '<row r="%d">%s</row>' % (row, newc) + x[pos:]
        self.put(part, x)
        self.log.append({"sheet": sheet, "cell": ref, "value": value, "num": num})

    # ---------- sheet removal ----------
    def remove_sheet(self, sheet):
        part = self.sheets[sheet]
        wb = self.get("xl/workbook.xml")
        m = re.search(r'<sheet [^>]*?name="%s"[^>]*?r:id="([^"]+)"[^>]*?/>' % re.escape(sheet), wb)
        rid = m.group(1)
        idx = list(self.sheets).index(sheet)
        wb = wb[:m.start()] + wb[m.end():]
        # shift localSheetId of later sheets
        def fix(mm):
            v = int(mm.group(1))
            assert v != idx, "definedName bound to removed sheet"
            return 'localSheetId="%d"' % (v - 1 if v > idx else v)
        wb = re.sub(r'localSheetId="(\d+)"', fix, wb)
        self.put("xl/workbook.xml", wb)
        rels = self.get("xl/_rels/workbook.xml.rels")
        rels = re.sub(r'<Relationship Id="%s" [^>]*?/>' % rid, "", rels)
        self.put("xl/_rels/workbook.xml.rels", rels)
        # parts owned by the sheet (via its rels)
        relpart = part.replace("worksheets/", "worksheets/_rels/") + ".rels"
        owned = []
        if relpart in self.data:
            for t in re.findall(r'Target="([^"]+)"', self.data[relpart].decode("utf-8")):
                if t.startswith("../"):
                    owned.append("xl/" + t[3:])
        for p in owned:
            sub_rel = p.rsplit("/", 1)[0] + "/_rels/" + p.rsplit("/", 1)[1] + ".rels"
            assert sub_rel not in self.data, "owned part has its own rels: " + p
        for p in [part, relpart] + owned:
            self.removed.add(p)
        ct = self.get("[Content_Types].xml")
        for p in list(self.removed):
            ct = re.sub(r'<Override [^>]*?PartName="/%s"[^>]*?/>' % re.escape(p), "", ct)
        self.put("[Content_Types].xml", ct)
        del self.sheets[sheet]
        self.log.append({"sheet": sheet, "cell": "*", "value": "SHEET REMOVED", "removed_parts": sorted(self.removed)})

    # ---------- save ----------
    def save(self, out, log_json=None):
        with zipfile.ZipFile(out, "w") as z:
            for info in self.infos:
                name = info.filename
                if name in self.removed:
                    continue
                data = self.text[name].encode("utf-8") if name in self.text else self.data[name]
                zi = zipfile.ZipInfo(name, date_time=info.date_time)
                zi.compress_type = info.compress_type
                zi.external_attr = info.external_attr
                z.writestr(zi, data)
        if log_json:
            with open(log_json, "w", encoding="utf-8") as f:
                json.dump({"edits": self.log, "modified_parts": sorted(self.text), "removed_parts": sorted(self.removed)},
                          f, ensure_ascii=False, indent=1)
