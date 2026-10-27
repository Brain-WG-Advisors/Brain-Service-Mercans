"""Print words of a PDF page with positions (x0, top) to design position-based readers.
Usage: python -I pdfwords.py file.pdf page_no(1-based) [min_top] [max_top]"""
import sys

import pdfplumber


def main(p, pg, lo=0, hi=10000):
    with pdfplumber.open(p) as pdf:
        page = pdf.pages[pg - 1]
        print("page size", page.width, page.height, "pages", len(pdf.pages))
        lines = {}
        for w in page.extract_words(keep_blank_chars=False, use_text_flow=False):
            if lo <= w["top"] <= hi:
                lines.setdefault(round(w["top"]), []).append(w)
        for t in sorted(lines):
            print(f"{t:4d}: " + "  ".join(f"[{w['x0']:.0f}]{w['text']}" for w in sorted(lines[t], key=lambda w: w['x0'])))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv
    main(a[1], int(a[2]), float(a[3]) if len(a) > 3 else 0, float(a[4]) if len(a) > 4 else 10000)
