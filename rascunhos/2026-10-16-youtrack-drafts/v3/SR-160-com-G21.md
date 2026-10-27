Hi @lli,

1. Yes: Mandatory (Y) is always written, including 0 / 0.00.
2. Yes: Conditional (C) is written only when the condition is met; otherwise the element is omitted (no 0, no empty tag). Spec v3.4 removes the two exceptions: rows 32–33 (G23, G24) are now Y, because form J0510111 defines columns 23 and 24 as 1/0 indicators ("1 - так, 0 - ні"); row 27 (G18) stays C, and the XML sample no longer writes it.
3. Optional (N): omitted when there is no value. In D1 the N rows are only LINKED_DOCS and SOFTWARE (header), sent with xsi:nil="true".

Omitting is valid: under the ДПС format an element absent from DECLARBODY is read as empty (Format, наказ Міндоходів № 729 of 29.11.2013), and XSD J0510111 makes every table column optional.

Row 30 (G21) is corrected in v3.4: column 21 is "Ознака основного місця роботи" (main place of work, 1/0), not a labour book indicator (form J0510111).
