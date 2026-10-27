"""Etapa 0 - inventory 01 Received (size, sha256), extract zips into 02 Validation/_extracted.
Usage: python -I intake.py "<package folder>"
Never writes into 01 Received."""
import hashlib
import os
import shutil
import sys
import zipfile


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main(pkg):
    rec = os.path.join(pkg, "01 Received")
    val = os.path.join(pkg, "02 Validation")
    ext = os.path.join(val, "_extracted")
    os.makedirs(ext, exist_ok=True)
    lines = ["file\tbytes\tsha256"]
    for n in sorted(os.listdir(rec)):
        p = os.path.join(rec, n)
        if not os.path.isfile(p) or n == "received.txt":
            continue
        lines.append(f"{n}\t{os.path.getsize(p)}\t{sha(p)}")
        if n.lower().endswith(".zip"):
            with zipfile.ZipFile(p) as z:
                for i, info in enumerate(z.infolist()):
                    if info.is_dir():
                        continue
                    name = info.filename
                    try:
                        name = name.encode("cp437").decode("cp866") if info.flag_bits & 0x800 == 0 and any(ord(c) > 127 for c in name) else name
                    except Exception:
                        pass
                    out = os.path.join(ext, f"z{i:02d}_" + os.path.basename(name))
                    with z.open(info) as src, open(out, "wb") as dst:
                        shutil.copyfileobj(src, dst)
                    lines.append(f"  [{n}] {name}\t{info.file_size}\t{sha(out)}\t-> {os.path.basename(out)}")
        else:
            out = os.path.join(ext, n)
            shutil.copyfile(p, out)
    for root, _, files in os.walk(val):
        for f in files:
            fp = os.path.join(os.path.abspath(root), f)
            if len(fp) > 240:
                lines.append(f"WARNING long path ({len(fp)}): {fp}")
    with open(os.path.join(val, "_inventory.tsv"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1])
