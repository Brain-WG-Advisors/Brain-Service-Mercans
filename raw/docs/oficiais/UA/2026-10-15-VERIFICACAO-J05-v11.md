# Verificação 2026-10-15: pacote J05 versão 11 (ДПС) e vigência

Feita pelo Chrome do usuário (tax.gov.ua bloqueia acesso direto desta máquina). Só leitura; nada baixado além do que está abaixo.

## 1. Pacote oficial j0500111.arj = arquivos em `j0500111-extraido/`
- URL: `https://tax.gov.ua/data/material/000/357/453385/j0500111.arj` — HTTP 200, `Last-Modified: Thu, 01 Oct 2026 06:12:50 GMT`, 881.813 bytes.
- Cabeçalhos ARJ lidos no navegador (tamanho original e CRC32 de cada arquivo) comparados com os arquivos locais: **14 de 14 idênticos**.

| Arquivo | Tamanho | CRC32 (oficial = local) |
|---|---|---|
| J0500111.pdf | 157817 | f20f12a5 |
| J0500111.xsd | 14584 | bbb2651a |
| J0510111.pdf | 107873 | e05faf1d |
| J0510111.xsd | 10329 | bdcd6556 |
| J0510211.pdf | 146957 | 328ace15 |
| J0510211.xsd | 11423 | caf1af2e |
| J0510311.pdf | 119624 | fe35782a |
| J0510311.xsd | 7018 | 68cdc03c |
| J0510411.pdf | 117009 | 1f60b273 |
| J0510411.xsd | 14249 | e3f06b1e |
| J0510511.pdf | 115865 | b3d4f5ea |
| J0510511.xsd | 9460 | 8f01913b |
| J0510611.pdf | 103557 | df61b1a2 |
| J0510611.xsd | 8050 | 50b96c15 |

- `common_types.xsd` (mesma pasta oficial): `Last-Modified: 16 Oct 2025`, 126.531 bytes, CRC32 a4284ec3 = `2026-10-09-common_types-DPS.xsd` local.

## 2. SPR_VER oficial (довідник версій)
- URL: `https://tax.gov.ua/data/material/000/006/58777/SPR_VER.ZIP` — `Last-Modified: Tue, 06 Oct 2026 14:02:45 GMT`.
- J05, C_DOC_SUB 001/101/102/103/104/105/106: versão **10** com `D_BEGIN 01012014`, **`D_END 30062026`** (Накази Мінфіну 24.01.2025 № 39 та 30.01.2025 № 53); versão **11** com `D_BEGIN 01012014`, `D_END` vazio — "Наказ Міністерства фінансів України від 13.01.2015 № 4 (у редакції наказу Міністерства фінансів України від 07.05.2026 № 243)".

## 3. Notícia oficial da ДПС (14/07/2026 13:58)
URL: `https://tax.gov.ua/nove-pro-podatki--novini-/1031674.html` — "Затверджено нові форми Податкового розрахунку: коли і за які періоди звітувати". Texto original (ucraniano), trechos:
> Міністерство фінансів України затвердило нові форми Податкового розрахунку … Вони набирають чинності 17 липня 2026 року.
> Застосування форм починається із 1 серпня для звітування: - податкових агентів (крім ФОП та осіб, які провадять незалежну професійну діяльність) – за липень 2026 року;
> Довідково: Відповідні зміни внесено наказами Мінфіну від 07.05.2026 № 243 та від 26.05.2026 № 284, які набирають чинності 17 липня 2026 року.

## Conclusão
- C_DOC_VER = **11** para períodos de relatório a partir de **julho de 2026** (agentes fiscais); versão 10 para períodos até 30.06.2026 (SPR_VER D_END).
- O pacote local `j0500111-extraido/` é o oficial. Substitui a ressalva do `LEIA-ME.md` (09/10: "não há captura de j0500111") e da `2026-10-13-VERIFICACAO.md` (v11 "não confirmada").
