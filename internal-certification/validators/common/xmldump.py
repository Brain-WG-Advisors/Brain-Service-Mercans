"""Print an XML file compactly: one line per leaf, path=value (namespaces stripped).
Usage: python -I xmldump.py file.xml [maxlines]"""
import sys

from lxml import etree


def main(p, maxl=100000):
    t = etree.parse(p)
    n = 0
    for el in t.iter():
        if not isinstance(el.tag, str):
            continue
        if len(el) == 0:
            path = []
            e = el
            while e is not None:
                path.append(etree.QName(e).localname)
                e = e.getparent()
            print("/".join(reversed(path[:4])), "=", (el.text or "").strip())
            n += 1
            if n >= maxl:
                break


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100000)
