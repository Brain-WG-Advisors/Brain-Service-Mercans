# Code lists — belastingjaar 2025

Transcribed from `codes-aangifte-2025.pdf` (Belastingdienst, "Codes voor de
aangifte loonheffingen 2025", LH 998-1Z51KE), bundled in this folder. The full
ISO country table and nationality table are in that PDF — grep it rather than
duplicating them here.

**These are 2025 values.** See `../2026/codes-aangifte-2026.pdf` for 2026;
several lists changed on 1 January 2026.

## Code loonbelastingtabel

Three digits, composed as follows.

**First digit — soort tabel (herleidingsregels)**

| Code | Meaning |
|---|---|
| 0 | No herleidingsregels; employee both belasting- and premieplichtig |
| 3 | Only premieplichtig for the volksverzekeringen (AOW/Anw/Wlz) |
| 5 | Only belastingplichtig |
| 6 | Belastingplichtig, not premieplichtig for the Wlz |
| 7 | Belastingplichtig, only premieplichtig for the Wlz |

**Second digit — kleur tabel**

| Code | Meaning |
|---|---|
| 1 | Wit (loon uit tegenwoordige dienstbetrekking) |
| 2 | Groen (loon uit vroegere dienstbetrekking) |

**Third digit — soort loontijdvak**

| Code | Meaning |
|---|---|
| 1 | Kwartaal |
| 2 | Maand |
| 3 | Week |
| 4 | 4 weken |
| 5 | Dag |
| 0 | Only the bijzondere beloningen table applied |

So **014** = no herleiding, wit, four-weekly. **012** = no herleiding, wit,
monthly. **024** = no herleiding, groen, four-weekly. **010** = no herleiding,
wit, bijzondere beloningen only.

This composition makes the payroll system's own tax-method field directly
testable against the declared code. Where master data says "white table,
monthly" and the XML declares 014, the declaration and the withholding basis
disagree.

**Standalone codes (not composed)**

| Code | Meaning |
|---|---|
| 210 | Aannemers van werk, thuiswerkers, sekswerkers en gelijkgestelden |
| 220 | Binnenlandse artiesten |
| 221 | Buitenlandse artiesten/beroepssporters (verlaagd tarief) |
| 224 | Buitenlandse artiestengezelschappen en sportploegen |
| 225 | Buitenlandse beroepssporters, verlaagd tarief per ministerieel besluit |
| 226 | Niet belastingplichtig, alleen premieplichtig Wlz |
| 227 | Niet belastingplichtig, alleen premieplichtig Anw |
| 228 | Niet belastingplichtig, alleen premieplichtig AOW/Anw |
| 250 | Percentagetarief bijstand |
| 940 | 52%-tarief, anonieme werknemers |
| 950 | 52%-tarief, negatieve uitgaven bij afkoop inkomensvoorzieningen |
| 999 | Overige gevallen waarin geen tabel is toegepast |

## Code soort inkomstenverhouding / inkomenscode (SrtIv)

Employment income (the codes that carry contract indicators and contractloon):

| Code | Meaning |
|---|---|
| 11 | Loon/salaris ambtenaren in de zin van de Ambtenarenwet |
| 13 | Loon/salaris directeuren nv/bv, **wel** verzekerd voor de WV |
| 15 | Loon/salaris niet onder te brengen onder 11, 13 of 17 |
| 17 | Loon/salaris DGA nv/bv, **niet** verzekerd voor de WV |
| 18 | Wachtgeld van een overheidsinstelling |

Benefits (SrtIv values that force AWf/Aof laag aanwas to zero — see L2201,
L2336, L2340): 31 ZW/WAZO · 32 WAO · 33 nWW · 34 IOAW · 36 Waz · 37 Wajong ·
38 samenloop Wajong · 39 IVA · 40 WGA · 42 Bbz · 43 Participatiewet ·
45 IOAZ · 46 Toeslagenwet · 50 overige sociale verzekeringswetten · 52 IOW ·
53 vervroegde uittreding · 55 APPA.

Pensions and post-employment: 22 AOW · 23 oorlogs- en verzetspensioenen ·
24 Anw · 56 ouderdomspensioen · 57 nabestaandenpensioen ·
58 arbeidsongeschiktheidspensioen · 59/60 lijfrenten · 61 aanvulling werkgever
op een WV-uitkering na einde dienstbetrekking · **62 ontslagvergoeding /
transitievergoeding** · 63 overige pensioenen of betaling na einde
dienstbetrekking.

**62 is the leaver code.** An ontslagvergoeding is green-table income and must
sit in its own inkomstenverhouding (its own `NumIV`), separate from the
white-table wage — whether it is paid alongside the final salary or in a later
tijdvak. See the gegevensspecificaties, "Samenloop of wijziging van
loonbelastingtabelkleur in de loop van het jaar".

## Code aard arbeidsverhouding

| Code | Meaning |
|---|---|
| 1 | Arbeidsovereenkomst (exclusief BBL) |
| 4 | Deelvisser |
| 6 | Musicus/artiest |
| 7 | Stagiair |
| 11 | Uitzendkracht |
| 18 | Publiekrechtelijke aanstelling |
| 21 | WSW beschut werk |
| 22 | WSW detachering bij reguliere werkgever |
| 23 | WSW begeleid werk |
| 24 | Participatiewet beschut werk |
| 79 | Opting-inregeling |
| 81 | Overige fictieve dienstbetrekkingen |
| 82 | Payrolling |
| 83 | Beroepspraktijkopleiding BBL |

## Code reden einde arbeidsverhouding

| Code | Meaning |
|---|---|
| 01 | Opzegging/ontslag door werkgever binnen de proeftijd |
| 03 | Ontbinding door rechter op verzoek van de werkgever |
| 04 | Beëindiging met wederzijds goedvinden, initiatief werkgever |
| 05 | Opzegging/ontslag wegens langdurige arbeidsongeschiktheid |
| 06 | Opzegging/ontslag wegens bedrijfseconomische redenen |
| 20 | Einde door opzegging werknemer of op initiatief van de werknemer |
| 21 | Ontslag op staande voet (dringende reden) |
| 30 | Einde van rechtswege, verstrijken duur bepaalde tijd |
| **31** | **Einde van rechtswege, andere reden (ontbindende voorwaarde, pensionering, overlijden e.d.)** |
| 40 | Einde uitzendovereenkomst, uitzendbeding, ziekte uitzendkracht |
| 41 | Einde uitzendovereenkomst, uitzendbeding, andere reden |
| 50 | Ontslag publiekrechtelijke aanstelling, onbekwaamheid/ongeschiktheid |
| 51 | Ontslag publiekrechtelijke aanstelling, leeftijd/pensionering |
| 90 | Arbeidsverhouding loopt door, IKV administratief beëindigd |
| 91 | Arbeidsverhouding loopt door bij een nieuwe werkgever |
| 92 | Zonder onderbreking opgevolgd door nieuwe arbeidsverhouding, zelfde werkgever |
| 99 | Een andere, hiervoor niet genoemde reden |

**Code 31 is valid in 2025.** It was withdrawn on 1 January 2026 and split into
32 (pensionering), 33 and 34. Corrections over 2025 must continue to use 31.

## Code verzekeringssituatie Zvw

| Code | Meaning |
|---|---|
| A | Niet verzekeringsplichtig, ook niet verzekerd voor de Wlz |
| B | Niet verzekeringsplichtig, militair ambtenaar in werkelijke dienst |
| G | Niet verzekeringsplichtig, buitenlands artiest/beroepssporter (tabelcode 221/224/225) |
| H | Wel verzekeringsplichtig, geen tarief, binnenlands artiest (tabelcode 220) |
| I | Niet verzekeringsplichtig, wel pseudobijdrage (art. 69 Zvw) |
| **K** | Wel verzekeringsplichtig, normaal tarief werkgeversheffing |
| L | Wel verzekeringsplichtig, 0%-tarief werkgeversheffing (zeelieden) |
| **M** | Wel verzekeringsplichtig, **ingehouden bijdrage** |
| N | Wel verzekeringsplichtig, meer tarieven werkgeversheffing (K en L) |

K is the ordinary case for wage from current employment. M is the only code
under which `IngBijdrZvw` may be non-zero (L1310).

## Code invloed verzekeringsplicht (IVP)

| Code | Meaning |
|---|---|
| A | Geen gezagsverhouding met echtgenoot of familie van de eigenaar/DGA |
| B | Geen gezagsverhouding met vorige eigenaar |
| D | Oproep-/invalkracht zonder verplichting om te komen |
| E | Oproep-/invalkracht met verplichting om te komen |

## Code fase indeling F&Z

1 Fase 1-2 met uitzendbeding · 3 Fase 3 · 4 Fase 4 · 5 Wettelijk regime ·
6 Ketensysteem · 17 Fase A met uitzendbeding · 18 Fase B · 19 Fase C ·
38 Fase A zonder uitzendbeding, met uitsluiting loondoorbetaling ·
40 Fase A zonder uitzendbeding · 41 Fase 1-2 zonder uitzendbeding ·
43 Fase 1-2 zonder uitzendbeding, met uitsluiting loondoorbetaling.

## Code incidentele inkomstenvermindering

K Kindverlof · O Onbetaald verlof · S Stakingsdagen · Z Ziekte.

## Code reden geen bijtelling auto

1 Afspraak werkgever met de Belastingdienst · 2 Verklaring geen privégebruik
auto · 3 Ander bewijs personen- en bestelauto · 5 Doorlopend afwisselend
gebruik bestelauto · 7 Verklaring uitsluitend zakelijk gebruik bestelauto.

## Geslacht

0 Onbekend · 1 Mannelijk · 2 Vrouwelijk · 9 Niet gespecificeerd.

## Tijdvakcodes, aangifte- en betaaldatums 2025

From `tijdvakcodes-2025.pdf` (LH 210-1T51FD).

**Vierwekenaangiften 2025**

| Tijdvak | Code | Ingangsdatum | Einddatum | Uiterste aangifte- en betaaldatum |
|---|---|---|---|---|
| Periode 1 | 5710 | 01-01-2025 | 26-01-2025 | 26-02-2025 |
| Periode 2 | 5720 | 27-01-2025 | 23-02-2025 | 23-03-2025 |
| Periode 3 | 5730 | 24-02-2025 | 23-03-2025 | 23-04-2025 |
| Periode 4 | 5740 | 24-03-2025 | 20-04-2025 | 20-05-2025 |
| Periode 5 | 5750 | 21-04-2025 | 18-05-2025 | 18-06-2025 |
| Periode 6 | 5760 | 19-05-2025 | 15-06-2025 | 15-07-2025 |
| Periode 7 | 5770 | 16-06-2025 | 13-07-2025 | 13-08-2025 |
| Periode 8 | 5780 | 14-07-2025 | 10-08-2025 | 10-09-2025 |
| **Periode 9** | **5790** | **11-08-2025** | **07-09-2025** | **07-10-2025** |
| Periode 10 | 5800 | 08-09-2025 | 05-10-2025 | 05-11-2025 |
| Periode 11 | 5810 | 06-10-2025 | 02-11-2025 | 02-12-2025 |
| Periode 12 | 5820 | 03-11-2025 | 30-11-2025 | 30-12-2025 |
| Periode 13 | 5830 | 01-12-2025 | 31-12-2025 | 31-01-2026 |

**Maandaangiften 2025** — codes 5010 (januari) through 5120 (december), each
running the calendar month with the deadline on the last day of the following
month. **Overige** — 5310 1e halfjaar, 5320 2e halfjaar, 5400 jaar.

Use this table to test that `DatAanvTv` and `DatEindTv` are genuine period
boundaries, that `SaldoCorrectiesVoorgaandTijdvak` ranges are real earlier
periods of the same year, and that the filing date falls inside the window.

## XML namespace and berichtversie

A 2025 loonaangifte declares:

```
xmlns="http://xml.belastingdienst.nl/schemas/Loonaangifte/2025/01" version="2.0"
```

The `version` attribute is the **berichtversie** (berichtspecificatie lineage),
not the gegevensspecificaties document version, which is 3.0 for 2025. Two
separate numbering schemes for the same filing year — record both, or a later
reader will conclude the pack was built against a superseded spec.

Check the namespace year before trusting any structural result. A year mismatch
between file and validator produces a silent clean pass.
