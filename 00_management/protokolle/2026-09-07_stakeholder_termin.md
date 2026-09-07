# Protokoll: Stakeholder-Termin am 07.09.2026

Grundlage: Notizen des Facilitators. Beschlüsse und Aufgaben sind in dieses Repository überführt;
die Aufgaben werden als GitHub-Issues geführt (siehe [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)).

Beteiligte laut Notizen: Peter, Martin, Martina, „Papa"; extern erwähnt: Pickerle bzw. Frau Tarmann
(Steuerberatung), Sepp (Buchhaltung).

## 1. Beschlüsse

| Nr. | Beschluss | Folge im Repository |
| --- | --- | --- |
| B1 | **Kinnovis wird als erster Kandidat in die Demo geführt.** Zu klären sind dort Lizenzmodell, Preise und Bindungsdauer | Entscheidung E-10, Demo-Checkliste `40_auswahl/demo_checkliste_kinnovis.md` |
| B2 | **Go-Live am 1. November 2026.** Das operative Geschäft läuft zunächst mit Zoho weiter | Entscheidung E-11, Projektplan angepasst |
| B3 | **Parallelbetrieb bis zum Jahreswechsel, längstens bis in den Januar**, um Abweichungen zu vergleichen und den Übergang abzusichern | Entscheidung E-11, `50_umsetzung/parallelbetrieb_und_sundown.md` |
| B4 | **Zahlungsabwicklung über Stripe zunächst nur für künftige Kunden**, nicht ohne Weiteres für den Bestand | Entscheidung E-12, bestätigt das Hybridmodell |
| B5 | **Den rund 250 Kunden soll nur einmal geschrieben werden**, möglichst als reine Info-Mail ohne neue Unterschrift | Entscheidung E-13, `50_umsetzung/schulung_und_change.md` |
| B6 | Für 1. Januar 2027 ist eine **Preiserhöhung** vorgesehen; der zusätzliche Aufwand ist einzuplanen | Meilenstein M9/M10, Risiko R20 |

## 2. Zahlungsabwicklung – besprochene Konditionen

Im Termin genannt: **0,35 € je SEPA-Zahlung zuzüglich 0,7 % des über die Plattform abgewickelten
Umsatzes**; Auszahlung alle sieben Tage als Sammelzahlung auf das Firmenkonto.
Als Zahlungsarten wurden SEPA, Kreditkarte, Apple Pay und Bitcoin genannt.

### Einordnung der Beratung

1. **Die 0,7 % sind vermutlich keine Stripe-Kondition.** Stripe verrechnet für SEPA-Lastschrift
   in Österreich 0,35 € pauschal. Ein zusätzlicher Prozentsatz auf den Plattformumsatz ist
   typischerweise eine **Plattformgebühr des Softwareanbieters**, der Stripe im Hintergrund
   einsetzt. Das gehört in die Klärung des Lizenzmodells (B1) – es ist faktisch ein zweiter,
   umsatzabhängiger Preisbestandteil.
2. **Kostenwirkung** bei rund 250 Verträgen und `ANNAHME:` 100 € Durchschnittsmiete
   (25.000 € Monatsumsatz):

   | Weg | Kosten pro Monat | Kosten pro Jahr |
   | --- | --- | --- |
   | Einzug über die eigene Hausbank | Bankentgelt, meist unter 60 € | rund 300 bis 900 € |
   | Über die Plattform: 250 × 0,35 € + 0,7 % von 25.000 € | 87,50 € + 175,00 € = **262,50 €** | **rund 3.150 €** |

   Die Differenz von rund 2.000 bis 2.800 € pro Jahr entspricht der Größenordnung der
   Softwarekosten. Sie ist kein Argument gegen Stripe, aber ein starkes Argument dafür, den
   **Bestand über die Bank zu belassen** – genau wie im Termin besprochen (B4).
3. **Die Sammelauszahlung im Sieben-Tage-Rhythmus** erzeugt den genannten Zusatzaufwand:
   Auf dem Konto erscheint eine Summe, in der Buchhaltung müssen Einzelforderungen und
   Gebühren aufgelöst werden. Das ist einmalig einzurichten (Anforderung BUH-05) und mit der
   Steuerberatung abzustimmen – danach ist es Routine, aber es muss im Buchhaltungsexport
   sauber abgebildet sein.
4. **Bitcoin** ist für wiederkehrende Mieten nicht geeignet: kein Einzug, Kursrisiko und
   zusätzlicher Bewertungs- und Dokumentationsaufwand in der Buchhaltung. Empfehlung: nicht in
   Phase 1 betrachten; bei Bedarf später als reine Einmalzahlungsoption prüfen.

## 3. SEPA und Bankintegration – zu klärende Punkte

Aus dem Termin, gerichtet an Kinnovis:

- Kann Kinnovis **Zahlungsdatenträger beziehungsweise XML-Dateien (pain.008)** für den Einzug
  über die eigene Bank erzeugen? (Anforderung ABR-15)
- Benötigt Kinnovis **Bank-Feeds** zur Konsolidierung, und welche Formate? (Anforderung BUH-04)
- Wie müssen **Zahlungstexte und Verwendungszwecke** gestaltet sein, damit eingehende Zahlungen
  automatisch der richtigen Forderung zugeordnet werden? (neue Anforderung ABR-19)

## 4. Rechtsformwechsel: Einzelunternehmen zur GmbH

Offen ist, ob die bestehenden SEPA-Mandate beziehungsweise die **Gläubiger-ID (Creditor ID)** auf
die GmbH übergehen oder neu eingerichtet werden müssen. Peter klärt das mit Pickerle
beziehungsweise der Bank. Ziel: die rund 250 Kundinnen und Kunden nicht mehrfach anschreiben
oder um neue Unterschriften bitten zu müssen.

### Einordnung der Beratung

Das SEPA-Verfahren kennt den Fall des **Gläubigerwechsels**. Wenn der Mandatsbestand im Zuge
einer Rechtsnachfolge auf die GmbH übergeht, wird die Änderung üblicherweise **nicht durch neue
Unterschriften**, sondern durch eine **Änderungsmitteilung im Einzug** abgebildet: Beim ersten
Einzug unter der neuen Gläubiger-ID werden die bisherige Gläubiger-ID und die bisherige
Mandatsreferenz als Änderungsangaben mitgegeben, und die Zahlungspflichtigen werden vorab
informiert. Ob dieser Weg im konkreten Fall greift, entscheidet die Bank gemeinsam mit der
Steuerberatung – nicht dieses Dokument.

**Zwei Konsequenzen für das Projekt:**

1. Der Prüfauftrag an Bank und Steuerberatung ist terminkritisch, weil er die Kundenkommunikation
   und den Zeitpunkt des Wechsels bestimmt (Issue mit Label `kritischer-pfad`).
2. Das neue System muss diese Änderungsangaben in der Einzugsdatei abbilden können. Das ist als
   **Anforderung ABR-18** aufgenommen und gehört in die Kinnovis-Demo. Kann das System es nicht,
   müssten die Mandate tatsächlich neu eingeholt werden – der Fall, den alle vermeiden wollen.

## 5. Kundenkommunikation

Vereinbart: möglichst **ein** Schreiben, reine Information, keine zusätzlichen Unterschriften,
um keine Verlängerungs- oder Kündigungsentscheidungen auszulösen.

**Empfehlung:** Systemwechsel und Gläubigerwechsel gehören in dasselbe Schreiben – beides ist
für die Kundin oder den Kunden dieselbe Nachricht: „Ihre Zahlung läuft weiter, Sie müssen nichts
tun." Die **Preisanpassung zum 1. Januar** sollte davon getrennt bleiben: Sie braucht eine eigene
Frist und eine eigene Begründung, und ein Schreiben, das Preiserhöhung und Systemumstellung
mischt, lädt zur Kündigung ein. Diese Abwägung ist als offene Frage O-15 im Entscheidungslog
vermerkt.

## 6. Aufgaben aus dem Termin

Werden als GitHub-Issues geführt; die Verantwortlichen sind aus den Notizen übernommen.

| Nr. | Aufgabe | Verantwortlich | Termin | Issue |
| --- | --- | --- | --- | --- |
| A1 | Checkliste mit Fragen und Demo-Inhalten für die Kinnovis-Demo abstimmen | Team | vor dem Demotermin | [#3](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/3) |
| A2 | Cutover-Szenario einschließlich Langzeitarchivierung nach dem Sundown von Zoho entwerfen | Martina | bis M7 | [#4](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/4) |
| A3 | Demotermin mit Kinnovis organisieren – **nicht innerhalb der nächsten zwei Tage** | „Papa", Martin | KW 38 | [#2](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/2) |
| A4 | E-Mail an Sepp mit den Spezifikationsanforderungen für den Datenaustausch mit der Buchhaltung | Peter | KW 38 | [#5](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/5) |
| A5 | Übergang der SEPA-Mandate und der Gläubiger-ID auf die GmbH mit Pickerle bzw. der Bank klären | Peter | KW 38 | [#1](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/1) |
| A6 | Lizenzmodell, Preise und Bindungsdauer von Kinnovis klären | Martin | mit der Demo | [#6](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/6) |

> Zu A1: Eine erste Fassung der Checkliste liegt bereits vor:
> [`../../40_auswahl/demo_checkliste_kinnovis.md`](../../40_auswahl/demo_checkliste_kinnovis.md).
> Sie ist als Arbeitsgrundlage gedacht und im Team zu ergänzen.

## 7. Was im Termin nicht besprochen wurde, aber entschieden werden muss

| Nr. | Punkt | Warum |
| --- | --- | --- |
| 1 | Was „Parallelbetrieb" genau bedeutet – siehe Abschnitt 8 | bestimmt, ob Doppelarbeit oder Absicherung entsteht |
| 2 | Ob Stora und Store365 weiterhin verglichen werden oder Kinnovis gesetzt ist | beeinflusst Aufwand und Verhandlungsposition |
| 3 | Wann genau der Rechtsformwechsel wirksam wird | bestimmt die Reihenfolge von System- und Gläubigerwechsel |

## 8. Präzisierung des Parallelbetriebs (Vorschlag)

„Beide Systeme laufen parallel" kann zweierlei heißen. Der Unterschied ist erheblich:

| Variante | Beschreibung | Bewertung |
| --- | --- | --- |
| **Schattenbetrieb (empfohlen)** | Ab 1.11. ist Kinnovis führend: Verträge, Rechnungen und Zahlungen entstehen dort. Zoho wird nicht mehr bespielt, bleibt aber lesend verfügbar und dient dem Abgleich | eine Wahrheit, kein Doppelaufwand, Rückfall bleibt möglich |
| **Echter Parallelbetrieb** | Beide Systeme werden gepflegt und fakturieren | doppelte Erfassung, Gefahr doppelter oder fehlender Rechnungen, hoher Aufwand über zwei Monate |

Empfehlung: **Schattenbetrieb**, mit monatlichem Abgleich (Sollmieten, offene Posten, Zahlungseingänge)
zum 30.11. und 31.12. sowie einem festen Sundown-Termin im Januar. Details in
[`../../50_umsetzung/parallelbetrieb_und_sundown.md`](../../50_umsetzung/parallelbetrieb_und_sundown.md).
