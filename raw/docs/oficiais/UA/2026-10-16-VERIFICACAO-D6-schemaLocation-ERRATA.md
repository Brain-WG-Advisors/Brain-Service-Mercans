# Errata de 2026-10-16-VERIFICACAO-D6-schemaLocation.md (§2)

O §2 citou, como sendo do Format da ДПС (наказ Міндоходів № 729), a frase "Жодний з описаних вище елементів (крім елемента SOFTWARE)…". Essa redação é a do **Format 3.1 do Держстат**. O texto do Format da ДПС (`2026-10-13-DPS-nakaz729-2013-Format-standart-dodatok1.doc`, relido em 2026-10-16) é:

> "Жодний з описаних вище елементів (крім елементів LINKED_DOCS та SOFTWARE), що входять до заголовка документа (елемент DECLARHEAD), не може мати пусте значення."

A conclusão do §2 não muda: C_REG, C_RAJ e C_STI_ORIG (J0510611.xsd linhas 97, 98 e 102, sem `minOccurs="0"`) são obrigatórios e não podem ser vazios. LINKED_DOCS (linha 104) e SOFTWARE (linha 130) são `nillable`, `minOccurs="0"` e podem ser vazios.
