# Migration: Zoho Subscriptions → neues Kernsystem

Ergänzt [`datenmigration.md`](datenmigration.md) um die Besonderheiten der Quelle.
Ausgangslage: [`../10_analyse/ist_zustand_zoho.md`](../10_analyse/ist_zustand_zoho.md).

## 1. Mandate und IBAN – Sachstand nach Klärung

**Ausgangslage (bestätigt durch den Auftraggeber, 06.09.2026):** Die Einzüge erfolgen heute als
SEPA-Lastschrift über das **eigene Bankkonto** von deinPlatz, unter **eigener Gläubiger-ID**;
ein Teil der Kunden zahlt per Überweisung. Die Konsolidierung in Zoho erfolgt weitgehend von Hand.

Damit entfällt das zuvor größte Migrationsrisiko: **deinPlatz ist selbst Gläubiger der Mandate.**
Ein Mandat wird durch die Kombination aus Gläubiger-ID und Mandatsreferenz identifiziert; solange
beide unverändert bleiben, bleibt es gültig – unabhängig davon, welche Software die Einzugsdatei
erzeugt. Eine Neueinholung ist also **nicht** erforderlich, solange die Einzüge weiterhin unter
derselben Gläubiger-ID laufen.

Die fehlende IBAN ist kein Datenverlust, sondern eine Beschaffungsaufgabe: Sie steht in den
Mandatsunterlagen und im Electronic Banking der Hausbank.

### Was daraus für die Zielsysteme folgt

| Zielmodell | Wirkung auf die Mandate | Voraussetzung im System |
| --- | --- | --- |
| **A – Einzug über die eigene Bank** | bleiben unverändert gültig, keine Kundenaktion | SEPA-Einzugsdatei (pain.008) erzeugbar – belegt nur bei Kinnovis (ABR-15) |
| **B – Einzug über Stripe mit eigener Gläubiger-ID** | Bestandsmandate werden zu Stripe portiert, keine Kundenaktion | **Die eigene Gläubiger-ID muss vor der ersten Live-Zahlung in Stripe hinterlegt werden – danach ist sie nicht mehr änderbar** |
| **B – Einzug über Stripe mit Stripe-Gläubiger-ID** | neue Mandate bei allen Kunden erforderlich | vermeidbar, siehe oben – dieser Fall darf nicht versehentlich eintreten |
| **C – Hybrid (Empfehlung)** | Bestand bleibt bei der Bank, Neukunden über Stripe | System muss beide Wege parallel führen (ABR-17) |

### Aufgaben in Woche 1

1. **Mandatsliste aufbauen**: Kunde, IBAN, Mandatsreferenz, Datum der Erteilung, Datum des
   letzten erfolgreichen Einzugs – aus Mandatsunterlagen und Electronic Banking.
2. Gläubiger-ID dokumentieren; prüfen, ob mehrere im Einsatz sind.
3. Verträge **ohne** gültiges Mandat identifizieren – nur hier ist eine Neueinholung nötig.
4. Mandate prüfen, deren letzter Einzug mehr als **36 Monate** zurückliegt: Diese sind verfallen
   und müssen neu erteilt werden.
5. Liste der Überweiser erstellen – Zielgruppe der Umstellungsaktion (Abschnitt 1a).

## 1a. Umstellung der Überweiser auf Lastschrift

Unabhängig vom gewählten System und Modell ist dies die wirksamste Einzelmaßnahme gegen den
manuellen Aufwand: Jeder Wechsel von Überweisung auf Lastschrift entfernt einen manuellen
Abgleich pro Monat. Reine Überweisungen bleiben in beiden Shortlist-Systemen Handarbeit, solange
kein Kontoauszugsimport besteht (Anforderung BUH-04).

| Schritt | Maßnahme | Erfahrungswert |
| --- | --- | --- |
| 1 | Liste der Überweiser aus Zoho-Export und Kontoauszug | – |
| 2 | Anschreiben mit einfachem Weg zur Mandatserteilung (digital bevorzugt) | rund die Hälfte reagiert |
| 3 | Erinnerung nach zwei Wochen | – |
| 4 | Telefonisches Nachfassen | hebt die Quote auf 80–90 % |
| 5 | Rest bei Überweisung belassen, sauberer manueller Prozess | – |

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
| Zahlungsmittel/Mandat | Zahlungsart und Mandat | Quelle ist **nicht** Zoho, sondern die Mandatsunterlagen und das Electronic Banking – siehe Abschnitt 1 |

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
W1  Exporte anfordern · Mandatsliste aus Bank und Unterlagen aufbauen · Einheitenliste aufbauen
W2  Datenqualität bewerten · Betriebsmodell festlegen (A/B/C) · Anschreiben für Überweiser vorbereiten
W3  Bereinigung · Begehung/Abgleich vor Ort · Umstellungsaktion Überweiser starten
W4  Mapping mit dem favorisierten Anbieter abstimmen (Importvorlagen)
W6  Testlauf 1 · Abgleich
W7  Testlauf 2 mit aktuellem Stand · Abgleich · Freigabe
W8  Produktive Migration · Cutover
```

Die Mandatsliste (Abschnitt 1) und die Einheitenliste (Abschnitt 3) sind die einzigen Stränge, die
**nicht** auf die Anbieterentscheidung warten können. Beide starten in Woche 1.
