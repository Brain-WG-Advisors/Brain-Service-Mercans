# -*- coding: utf-8 -*-
"""Testes mecânicos de apoio à v1.2.
Uso: python -I check_layout.py <v1.2.xlsx> <SNHI_sample.txt>
(a) soma dos comprimentos (col. D) por seção = 200;
(b) amostra oficial NHIA: totais da seção 3 = soma das linhas 2; amostras E36/E37/E38 da v1.2 batem com as posições;
(c) aba Testing: o que a saída atual violaria."""
import sys, re, openpyxl
sys.stdout.reconfigure(encoding="utf-8")
wb = openpyxl.load_workbook(sys.argv[1])
ws = wb["Spec(TXT)"]
sec, tot = None, {}
for r in range(3, 41):
    a, b, d = ws.cell(r, 1).value, ws.cell(r, 2).value, ws.cell(r, 4).value
    if a: sec = a
    if r in (24, 25, 26, 27):  # sub-campos do bloco 93-132 (linha 23 já conta 40)
        continue
    tot[sec] = tot.get(sec, 0) + int(d)
print("(a) comprimento por seção:", tot, "->", "OK" if all(v == 200 for v in tot.values()) else "ERRO")
sub = sum(int(ws.cell(r, 4).value) for r in (24, 25, 26, 27))
print("    bloco 93-132: sub-campos somam", sub, "->", "OK" if sub == 40 else "ERRO")

L = [l for l in open(sys.argv[2], encoding="utf-8").read().splitlines() if l]
det = [l for l in L if l[0] == "2"]
s3 = [l for l in L if l[0] == "3"][0]
amt = sum(int(l[68:82]) for l in det); fee = sum(int(l[82:92]) for l in det)
print("(b) amostra NHIA: %d linhas 2; soma 69-82 = %d; soma 83-92 = %d" % (len(det), amt, fee))
print("    seção 3: 12-20=%s 21-40=%s 41-56=%s 57-71=%r" % (s3[11:20], s3[20:40], s3[40:56], s3[56:71]))
ok = int(s3[11:20]) == len(det) and int(s3[20:40]) == amt and int(s3[40:56]) == fee
print("    totais = soma das linhas:", "OK" if ok else "ERRO")
for cell, val in (("E36", s3[20:40]), ("E37", s3[40:56]), ("E38", s3[56:71].rstrip())):
    print("    %s v1.2 = %r | amostra = %r -> %s" % (cell, ws[cell].value, val, "OK" if ws[cell].value == val else "ERRO"))
print("    E14 v1.2 = %r | amostra 2-9 = %r" % (ws["E14"].value, det[0][1:9]))

print("(c) aba Testing (saída da configuração, fev/2026):")
t = wb["Testing"]
for r in range(1, 15):
    v = t.cell(r, 1).value
    if v is None: continue
    v = str(v)
    probs = []
    if v[0] in "123" and v[9:11] != "62": probs.append("posições 10-11 = %r, não '62' (UBN 2-9 ausente: campos deslocados; tipo 62 está em 2-3 = %r)" % (v[9:11], v[1:3]))
    if "-" in v: probs.append("sinal negativo em campo")
    if v[0] == "2": probs.append("data de pagamento 22-28 = %r" % v[20:27])
    if "e+" in v: probs.append("valor gravado como número científico")
    print("    A%d: %s" % (r, "; ".join(probs) if probs else "sem violação detectada"))
