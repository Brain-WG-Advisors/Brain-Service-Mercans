# Verificação 2026-10-16: schemaLocation do root (D6 / J05) e outros pontos do Format da ДПС

Feita pela janela Suporte, a pedido da janela geral. Fonte primária já baixada: `2026-10-13-DPS-nakaz729-2013-Format-standart-dodatok1.doc` (Наказ Міндоходів 29.11.2013 № 729, "Формат (стандарт) електронного документа звітності суб'єктів господарювання"), lido como texto UTF-16 do .doc.

## 1. Root DECLAR referencia o arquivo do schema

- Texto do Format: "Кореневим елементом є елемент з іменем DECLAR, при оголошенні цього елемента вказується посилання на схему контролю даних (XML схему). Наприклад: `<DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J0100112.xsd">`".
- Nome do arquivo do schema: "Файл з XML-схемою іменується за таким принципом: позиції з 1 по 3 … C_DOC; позиції з 4 по 6 … C_DOC_SUB; позиції з 7 по 8 … C_DOC_VER, доповненого зліва нулем до 2 символів; файл має розширення xsd. Наприклад: J0100112.xsd".
- Додаток 1 (пункт 6), "Структура електронного документа звітності": `xsi:noNamespaceSchemaLocation="ім'я файла, що містить XML-схему"`.
- Додаток 2 (exemplo): `J0100112.xsd` com `<C_DOC>J01</C_DOC> <C_DOC_SUB>001</C_DOC_SUB> <C_DOC_VER>12</C_DOC_VER>`, ou seja, nome do schema = C_DOC + C_DOC_SUB + C_DOC_VER.
- **Conclusão:** com `C_DOC=J05`, `C_DOC_SUB=106`, `C_DOC_VER=11`, o root deve referenciar **`J0510611.xsd`** (é o arquivo do pacote oficial v11: `j0500111-extraido/J0510611.xsd`, fixed C_DOC_SUB=106 e C_DOC_VER=11, linhas 93–94).
- **Anexo do Dev (SR-163):** `raw/tickets/api/anexos/SR-163/20261016-0832 - special_seniority new template.xml`, linha 2: `xsi:noNamespaceSchemaLocation="J0510610.xsd"`, linha 7: `<C_DOC_VER>11</C_DOC_VER>`. Diverge da regra.
- Não verificado: se a ДПС rejeita o arquivo por essa divergência (a regra existe; o efeito na recepção não está documentado aqui).

## 2. C_REG, C_RAJ e C_STI_ORIG obrigatórios no J0510611

- `J0510611.xsd`, DECLARHEAD: `C_REG` (DGsti), `C_RAJ` (DGsti) e `C_STI_ORIG` sem `minOccurs="0"` (obrigatórios). Validação lxml da amostra do Dev de 16/10 08:32: "Element 'PERIOD_MONTH': This element is not expected. Expected is ( C_REG )".
- Format (mesmo documento): "Жодний з описаних вище елементів (крім елемента SOFTWARE), що входять до заголовка документа (елемент DECLARHEAD), не може мати пусте значення" (citado também no Format 3.1 do Держстат).

## 3. Vazio × ausente (para o SR-160)

- Format: "елементи, що мають пусте значення, записуються у вигляді `<Код показника xsi:nil="true"/>` … причому атрибут xsi:nil="true" є обов'язковим … Якщо елемент відсутній у тілі документа (елемента DECLARBODY), то його значення теж вважається пустим".
- `J0510111.xsd` (D1 v11), linhas 191–211: `T1RXXXXG12` a `T1RXXXXG26` e `R01G16` a `R01G20` todos `nillable="true" minOccurs="0"`.
- Consequência: tag vazia sem `xsi:nil` não é forma prevista; elemento omitido = valor vazio. O XSD não obriga nenhuma dessas colunas.

## 4. Achado lateral (não comunicado)

- Format: "Між елементами не допускаються знаки пробілів, табуляцій тощо." Os templates do Dev são indentados (espaços entre elementos). Não verificado se o gerador final remove a indentação.
