# Migration: Zoho Subscriptions → neues Kernsystem

Ergänzt [`datenmigration.md`](datenmigration.md) um die Besonderheiten der Quelle.
Ausgangslage: [`../10_analyse/ist_zustand_zoho.md`](../10_analyse/ist_zustand_zoho.md).

## 1. Die eine Frage, die alles andere bestimmt

> **Können die bestehenden Lastschriftmandate übernommen werden – oder müssen sie bei rund
> 120 Kundinnen und Kunden neu eingeholt werden?**

Im Zoho-Export fehlen die IBANs. Das ist kein Fehler des Exports: In Zoho Subscriptions liegen
Bankdaten in aller Regel **nicht** im Abrechnungssystem, sondern beim dahinterliegenden
Zahlungsdienstleister. Zoho speichert nur eine Referenz.

Daraus folgen drei Szenarien:

| Szenario | Voraussetzung | Aufwand | Wahrscheinlichkeit |
| --- | --- | --- | --- |
| **S1 – Mandate wandern mit** | Zahlungsdienstleister bleibt derselbe (z. B. Stripe), das Zahlungskonto gehört **deinPlatz** (nicht Zoho), die Mandate liegen als PaymentMethod vor und die **Gläubiger-ID bleibt identisch** | gering: technische Übertragung, keine Kundenaktion | zu prüfen |
| **S2 – Mandate müssen neu eingeholt werden** | Wechsel des Dienstleisters, Mandate nur als veraltetes Objekt gespeichert, oder abweichende Gläubiger-ID | **hoch**: Kundenkommunikation, Rücklauf, Nachfassen, 3–4 Wochen Vorlauf | zu prüfen |
| **S3 – heute gar keine Lastschrift** | Zahlung heute per Überweisung/Karte | Lastschrift ist dann eine **Neueinführung**, kein Migrationsthema – mit demselben Vorlauf | zu prüfen |

**Belegte technische Randbedingung:** Ein Übertrag gespeicherter SEPA-Zahlungsmittel zwischen
Stripe-Konten ist möglich, aber nur für als *PaymentMethod* gespeicherte Mandate und nur, wenn
**Gläubiger-ID von Quell- und Zielkonto übereinstimmen**; Mandate von einem anderen Anbieter
lassen sich grundsätzlich zu Stripe portieren. Beides ist beim Anbieter und bei Stripe
schriftlich zu bestätigen – nicht auf Zuruf.

### Zu klären in Woche 1 (Reihenfolge)

1. Welcher Zahlungsdienstleister steht heute hinter Zoho?
2. Wem gehört das Konto beim Dienstleister – deinPlatz oder Zoho?
3. Gibt es eine eigene SEPA-Gläubiger-ID (Creditor Identifier)? Welche?
4. Wie viele aktive Verträge zahlen per Lastschrift, wie viele per Überweisung/Karte?
5. Bestätigung des Zielanbieters (Kinnovis/Stora), ob und wie er übernommene Mandate einbindet.

### Wenn S2 oder S3 eintritt: Ablauf Mandatsneueinholung

| Woche | Schritt |
| --- | --- |
| 1 | Entscheidung, Text und Formular/Online-Strecke vorbereiten (Rechtsprüfung des Mandatstexts) |
| 2 | Anschreiben an alle aktiven Kunden mit Frist und klarem Nutzen; digitale Erfassung bevorzugen |
| 3 | Erinnerung an alle ohne Rücklauf |
| 4 | Telefonisches Nachfassen; Restliche zunächst auf Überweisung stellen |
| ab Go-Live | Nacherfassung beim nächsten Kundenkontakt vor Ort |

Erfahrungswert: Der Rücklauf liegt nach dem ersten Anschreiben meist bei etwa der Hälfte, nach
Erinnerung und Telefonaten bei 80–90 %. Ein Rest zahlt dauerhaft per Überweisung – dafür braucht
es einen sauberen Prozess für den Zahlungsabgleich (Anforderung BUH-04).

## 2. Exportfähigkeit von Zoho

Zoho Subscriptions/Billing exportiert je Modul nach CSV, TSV oder XLS – Kunden, Abonnements,
Rechnungen, Zahlungen, Produkte/Pläne – wahlweise über frei definierbare **Exportvorlagen**
mit Feldauswahl, sowie als vollständige Datensicherung. Damit ist die Datenbeschaffung
unproblematisch; die Arbeit liegt in Zuordnung und Bereinigung.

**Anzufordern (Woche 1, jeweils als CSV, UTF-8):**

- [ ] Kunden (alle Felder, inkl. benutzerdefinierter Felder)
- [ ] Abonnements (aktiv **und** beendet, mit Plan, Preis, Startdatum, nächstem Abrechnungsdatum)
- [ ] Rechnungen (offen und bezahlt, letzte 7 Jahre)
- [ ] Zahlungen und Gutschriften
- [ ] Produkte/Pläne/Zusatzartikel
- [ ] Kundenkontoauszüge (Statements) als PDF-Archiv
- [ ] Vollsicherung („Data Backup") als Sicherheitskopie

## 3. Der zweite kritische Punkt: die Zuordnung zum Lagerabteil

Zoho kennt Abonnements, aber kein Mietobjekt. Die Information, **welcher Kunde welches Abteil
mietet**, steht daher vermutlich nicht strukturiert im System, sondern im Plannamen, in einem
Freitextfeld oder in der OneDrive-Liste.

Das neue System baut aber genau auf dieser Zuordnung auf. Vorgehen:

1. Prüfen, wo die Zuordnung heute steht (Woche 1).
2. **Führende Liste erstellen:** Einheit → Fläche → Kunde → Vertragsbeginn → Preis → Zahlungsart.
   Diese Liste ist das Herzstück der Migration und wird einmal vollständig verifiziert –
   idealerweise durch eine **Begehung mit Abgleich vor Ort** (Türnummer gegen Liste).
3. Abweichungen zwischen Liste, Zoho und Realität sind normal. Sie jetzt zu bereinigen ist
   deutlich billiger als nach dem Go-Live.

Nebeneffekt: Diese Liste ist zugleich die Grundlage für den Anlageplan (Phase 2) und für die
Preisliste je Größenklasse.

## 4. Feldzuordnung (Grobmapping)

| Zoho-Objekt | Zielobjekt | Hinweise |
| --- | --- | --- |
| Customer | Kunde/Kontakt | Privat/Firma trennen; UID prüfen; Dubletten bereinigen |
| Customer → Billing Address | Rechnungsanschrift | Format- und Ländercode-Prüfung |
| Subscription | Mietvertrag | Preis, Startdatum, Intervall, **nächstes Abrechnungsdatum** (stichtagskritisch) |
| Plan / Add-on | Preis/Tarif bzw. Zusatzleistung | Auf Größenklassen des neuen Systems abbilden |
| – | **Einheit** | **existiert in Zoho nicht** – aus der Liste nach Abschnitt 3 |
| Invoice (offen) | Offener Posten | Summenabgleich zwingend |
| Invoice (bezahlt) | Archiv (PDF) | keine Belegmigration |
| Payment | Zahlung | nur soweit für offene Posten nötig |
| Credit Note | Gutschrift/Guthaben | Guthaben müssen im Zielsystem sichtbar bleiben |
| Kaution | Kaution | in Zoho oft als normale Rechnung erfasst → **manuelle Liste erforderlich** |
| Zahlungsmittel/Mandat | Zahlungsart | siehe Abschnitt 1 |

## 5. Kautionen – gesonderte Behandlung

Kautionen sind in einem Abo-System selten sauber abgebildet. Vor der Migration ist eine
**eigene Kautionsliste** zu erstellen (Kunde, Betrag, Datum, Status) und mit der Buchhaltung
abzugleichen. Steuerlich ist eine Kaution ein durchlaufender Posten, kein Erlös – wie das
Zielsystem das abbildet, ist Prüffrage F5 im Benchmark, und die Behandlung ist mit der
Steuerberatung zu bestätigen (Prüfauftrag P2).

## 6. Zusätzliche Prüfsummen für diese Migration

Ergänzend zu den Kriterien in [`datenmigration.md`](datenmigration.md):

| Prüfung | Kriterium |
| --- | --- |
| Summe der monatlichen Abo-Beträge in Zoho | = Summe der Sollmieten im Zielsystem |
| Anzahl aktiver Abonnements | = Anzahl aktiver Verträge |
| Nächstes Abrechnungsdatum je Abo | 1:1 übernommen, keine Verschiebung |
| Summe offener Rechnungen | Abweichung 0,00 € |
| Summe Kautionen laut gesonderter Liste | im Zielsystem wiederauffindbar |
| Zuordnung Vertrag ↔ Einheit | 100 % geprüft, keine Einheit doppelt belegt |
| Kunden ohne E-Mail | Liste erstellt, vor Go-Live geklärt |
| Kunden ohne gültige Zahlungsart | Liste erstellt, in Nacherfassung überführt |

## 7. Abschluss von Zoho

- [ ] Vollständige Datensicherung **vor** der Kündigung erstellen und Lesbarkeit prüfen
- [ ] Rechnungs- und Belegarchiv (7 Jahre, § 132 BAO) gesichert und dokumentiert abgelegt
- [ ] Kündigungsfrist des Zoho-Abonnements geprüft und Kündigung terminiert
- [ ] Zahlungsdienstleister-Konto: klären, ob es bestehen bleibt (bei Weiterverwendung von Stripe)
      oder zu schließen ist
- [ ] Löschung der Daten bei Zoho nach Ablauf der Aufbewahrungspflicht beauftragen
- [ ] Zugriff auf das Archiv geregelt (wer, wie, wo)

## 8. Reihenfolge der Arbeitspakete

```
W1  Exporte anfordern · Zahlungsdienstleister klären · Einheitenliste aufbauen
W2  Datenqualität bewerten · Entscheidung Mandate (S1/S2/S3) · ggf. Kundenanschreiben vorbereiten
W3  Bereinigung · Begehung/Abgleich vor Ort · ggf. Mandatsaktion starten
W4  Mapping mit dem favorisierten Anbieter abstimmen (Importvorlagen)
W6  Testlauf 1 · Abgleich
W7  Testlauf 2 mit aktuellem Stand · Abgleich · Freigabe
W8  Produktive Migration · Cutover
```

Die Mandatsklärung (Abschnitt 1) ist der einzige Strang, der **nicht** auf die Anbieterentscheidung
warten kann. Er startet in Woche 1.
