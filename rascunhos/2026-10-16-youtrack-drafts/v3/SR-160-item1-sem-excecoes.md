Hi @lli,

1. Yes: Y is always written, including 0 / 0.00.
2. Yes: C is written only when its condition is met; otherwise the element is omitted (no 0, no empty tag). An element absent from DECLARBODY is read as empty (ДПС Format, наказ № 729). Spec v3.4 aligns the two exceptions: rows 32–33 (G23, G24) are now Y, as form J0510111 defines columns 23 and 24 as 1/0 indicators ("1 - так, 0 - ні"); row 27 (G18) stays C and is no longer written in the XML sample.
3. In D1 the N rows are only LINKED_DOCS and SOFTWARE (header text, no 0 case); when blank they are sent with xsi:nil="true", as in the XML sample.

Changes highlighted in light purple.
