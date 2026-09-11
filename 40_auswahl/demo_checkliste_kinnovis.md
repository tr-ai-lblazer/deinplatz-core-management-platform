# Fragenkatalog für die Kinnovis-Demo

Version 0.2 (Entwurf, Stand 11.09.2026) · Grundlage für Aufgabe A1 aus dem
[Stakeholder-Termin vom 07.09.2026](../00_management/protokolle/2026-09-07_stakeholder_termin.md)
· Issue [#3](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/3)

> **Zu ergänzen vor dem Versand:** Termin, Dauer, Teilnehmende auf beiden Seiten.

## 0. Vorbemerkung zum Vorgehen

**Grundsatz:** Was nicht live im System gezeigt oder schriftlich zugesagt wird, gilt als nicht
vorhanden. „Machbar", „auf der Roadmap" und „das lässt sich einrichten" werden im
Bewertungsbogen als *nicht erfüllt* geführt und im Nachgang schriftlich nachgefordert.

**Diese Unterlagen gehen vorab an Kinnovis**, damit die Demo vorbereitet ist:

- [ ] dieser Fragenkatalog
- [ ] das allgemeine Demo-Drehbuch [`demo_skript.md`](demo_skript.md) mit den acht Testfällen
- [ ] die Bitte um einen **Musterexport für die Buchhaltung** (ein voller Monat, echte Struktur) –
      wird von der Steuerberatung **vor** der Demo testweise in RZL importiert
- [ ] die Bitte um eine **Musterrechnung für einen österreichischen Firmenkunden**
- [ ] unsere Eckdaten: ein Standort, rund 250 aktive Verträge, Einheiten von 2,5 bis 50 m²,
      Mindestmietdauer ein Monat, heutiger Einzug per SEPA über die eigene Bank, Steuerberatung mit RZL

**Rollen im Termin:** eine Person führt durch den Katalog, eine protokolliert, eine achtet auf
die Zeit. Betrieb und Finanzen bewerten getrennt (Bewertungsbogen in Abschnitt 12).

## 1. Zeitplan für 90 Minuten

| Zeit | Block | Inhalt | Priorität |
| --- | --- | --- | --- |
| 0–5 | Einstieg | Kurzvorstellung, vergleichbare Kunden in Österreich | – |
| 5–20 | **K** | **K.o.-Fragen** – wenn hier etwas fehlt, erübrigt sich der Rest | P1 |
| 20–30 | A | Lizenzmodell, Preise, Bindungsdauer | P1 |
| 30–42 | B | SEPA über die eigene Bank, Mandate, Gläubigerwechsel zur GmbH | P1 |
| 42–50 | C | Bankdaten, Zahlungstexte, Abgleich | P1 |
| 50–57 | D | Zahlungsdienstleister (Stripe) | P2 |
| 57–67 | E | Buchhaltung und RZL | P1 |
| 67–75 | F | Österreichische Anforderungen und Sprache | P1 |
| 75–85 | G | Migration, Go-Live 01.11., Parallelbetrieb | P1 |
| 85–90 | H | Vertrag, Datenschutz, Ausstieg – und offene Punkte | P2 |

Reicht die Zeit nicht, werden D und H schriftlich nachgereicht. **K, B, E und G werden nicht gekürzt.**

## 2. Block K – K.o.-Fragen (bitte zuerst, live im System)

Diese acht Punkte entscheiden über die Eignung. Ein „nein" ist kein Beinbruch, aber es muss
sofort auf dem Tisch liegen.

| Nr. | Frage | Anforderung | Antwort | Erfüllt |
| --- | --- | --- | --- | --- |
| K1 | Erzeugt Kinnovis eine **SEPA-Einzugsdatei (pain.008)** für den Upload in unser Electronic Banking – unter **unserer eigenen Gläubiger-ID**? | ABR-15 | | ⬜ |
| K2 | Können wir **bestehende Mandate importieren** (IBAN, Mandatsreferenz, Datum der Erteilung)? | ABR-16 | | ⬜ |
| K3 | Unterstützt das System die **Mandatsänderung bei Gläubigerwechsel**, also die Mitgabe der bisherigen Gläubiger-ID und Mandatsreferenz im Einzug? | ABR-18 | | ⬜ |
| K4 | Liefert das System einen Buchhaltungsexport, der **in RZL importierbar** ist? Bitte die Datei zeigen. | BUH-01 | | ⬜ |
| K5 | Sind **Oberfläche und alle Kundendokumente auf Deutsch** und von uns selbst änderbar? Bitte einen Text live ändern. | ADM-07, KOM-03 | | ⬜ |
| K6 | Entspricht die Rechnung dem **österreichischen Umsatzsteuerrecht** (Pflichtangaben, USt.-Ausweis, fortlaufende Nummer)? | ABR-03 | | ⬜ |
| K7 | Läuft der **monatliche Abrechnungslauf automatisch**, inklusive taggenauer anteiliger Abrechnung? | ABR-01, ABR-02 | | ⬜ |
| K8 | Gibt es einen **Auftragsverarbeitungsvertrag nach Art. 28 DSGVO**, Hosting in der EU und einen vollständigen Datenexport durch uns? | ADM-03, ADM-05 | | ⬜ |

## 3. Block A – Lizenzmodell, Preise, Bindungsdauer

Der Punkt aus dem Stakeholder-Termin: Lizenzmodell, Preise und Bindungsdauer sind zu klären.

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| A1 | Wie ist das Lizenzmodell aufgebaut – je Standort, je Einheit, je Benutzer oder umsatzabhängig? | | P1 |
| A2 | Was kostet unser Fall konkret: ein Standort, rund 250 aktive Verträge? | | P1 |
| A3 | **Fällt zusätzlich zu den Zahlungsentgelten ein Prozentsatz auf den abgewickelten Umsatz an? Im Vorgespräch waren 0,7 % genannt – wofür genau, und ist der Satz verhandelbar?** | | P1 |
| A4 | Welche Funktionen sind enthalten, welche kosten extra: Kundenportal, Buchungsstrecke, Facility Map, Zutrittsintegration, E-Signatur, Identitätsprüfung? | | P1 |
| A5 | Mindestlaufzeit und Kündigungsfrist? | | P1 |
| A6 | Preisanpassungsklausel: Ankündigungsfrist, Obergrenze, Indexbindung, Sonderkündigungsrecht? | | P2 |
| A7 | Einmalige Kosten für Einrichtung, Migration, Schulung? | | P1 |
| A8 | Was kostet ein zweiter Standort, falls wir erweitern? | | P3 |
| A9 | Bitte Gesamtkosten über 36 Monate schriftlich und aufgeschlüsselt. | | P1 |

> **Hintergrund zu A3:** Stripe verrechnet SEPA-Lastschrift pauschal mit 0,35 € je Transaktion.
> Ein zusätzlicher Prozentsatz auf den Umsatz ist der Sache nach eine Plattformgebühr des
> Softwareanbieters und gehört damit zum Lizenzpreis. Bei rund 25.000 € Monatsumsatz entsprechen
> 0,7 % etwa **2.100 € im Jahr** – ein zweiter, mitwachsender Preisbestandteil.

## 4. Block B – SEPA über die eigene Bank und Mandate

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| B1 | Bitte den vollständigen Ablauf zeigen: Einzugslauf anstoßen, Datei erzeugen, Inhalt der Datei | | P1 |
| B2 | Wie werden **Rückläufer** erfasst, und lösen sie automatisch eine Mahnstufe aus? | | P1 |
| B3 | Wird die **Vorabinformation (Pre-Notification)** automatisch erzeugt und versendet? Welche Frist ist einstellbar? | | P1 |
| B4 | Wie werden Mandate verwaltet: Referenzbildung, Nachweis, Gültigkeit, Verfall nach 36 Monaten ohne Einzug? | | P2 |
| B5 | **Fall Rechtsformwechsel:** Wir wechseln vom Einzelunternehmen zur GmbH. Wie bilden Sie den Wechsel der Gläubiger-ID ab, ohne dass rund 250 Kundinnen und Kunden neu unterschreiben müssen? | | P1 |
| B6 | Können Bank-Lastschrift für den Bestand und Dienstleister-Einzug für Neukunden **dauerhaft parallel** laufen? | | P1 |
| B7 | Welche Felder brauchen Sie von uns, damit der erste Einzug funktioniert? | | P2 |

## 5. Block C – Bankdaten, Zahlungstexte, Abgleich

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| C1 | **Benötigt Kinnovis Bank-Feeds zur Konsolidierung?** Wenn ja, welche Formate – CAMT.053, MT940, Direktanbindung? | | P1 |
| C2 | Kann ein Kontoauszug eingelesen und automatisch der offenen Forderung zugeordnet werden? | | P1 |
| C3 | **Wie müssen Zahlungstexte, Verwendungszweck oder Referenz gestaltet sein, damit die Zuordnung automatisch gelingt?** | | P1 |
| C4 | Was passiert mit Zahlungen, die sich nicht zuordnen lassen? Wo sieht das Büro sie? | | P1 |
| C5 | Wie werden Teilzahlungen, Überzahlungen und Guthaben abgebildet? | | P2 |
| C6 | Wie sieht die Liste der offenen Posten aus – nach Alter und Mahnstufe? | | P2 |

## 6. Block D – Zahlungsdienstleister (Stripe)

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| D1 | Welche Zahlungsarten stehen zur Verfügung? | | P2 |
| D2 | Welche Entgelte fallen an – je Transaktion, je Rückläufer, prozentual? | | P1 |
| D3 | In welchem Rhythmus wird ausgezahlt, und **wie werden die Sammelauszahlungen samt Gebühren im Buchhaltungsexport aufgelöst**? | | P1 |
| D4 | Wird bei Stripe **unsere eigene Gläubiger-ID** verwendet? Wann muss diese Entscheidung fallen, und ist sie später änderbar? | | P1 |
| D5 | Kann die Kundin oder der Kunde die Zahlungsart selbst im Portal ändern? | | P2 |

## 7. Block E – Buchhaltung und RZL

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| E1 | **Bitte einen echten Buchhaltungsexport eines Monats erzeugen und die Datei öffnen** | | P1 |
| E2 | Welche Formate gibt es – DATEV-CSV, eigenes CSV, andere? Ist der Aufbau dokumentiert? | | P1 |
| E3 | Sind Konten und Steuerschlüssel frei konfigurierbar, auch für den **österreichischen** Kontenrahmen? | | P1 |
| E4 | Wie werden **Kautionen** geführt – als Erlös oder als durchlaufender Posten? | | P1 |
| E5 | Wie wird eine bereits versendete Rechnung korrigiert? Bleibt der Ursprungsbeleg unverändert? | | P1 |
| E6 | Wie oft und auf welchem Weg kann die Steuerberatung die Daten abholen? Gibt es einen lesenden Zugang? | | P2 |
| E7 | Unterstützen Sie strukturierte E-Rechnung (ebInterface, Peppol)? | | P3 |

## 8. Block F – Österreichische Anforderungen und Sprache

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| F1 | Musterrechnung für einen österreichischen Firmenkunden mit UID und USt.-Ausweis | | P1 |
| F2 | Vertragsvorlage: Wie ändern wir eine Klausel selbst, ohne Sie zu beauftragen? | | P1 |
| F3 | Wie wird eine Barzahlung mit Belegausgabe erfasst? | | P2 |
| F4 | Referenzkunden in Österreich, die wir kontaktieren dürfen | | P1 |
| F5 | Mahnwesen nach österreichischer Praxis: Stufen, Fristen, Mahnspesen, Verzugszinsen | | P1 |

## 9. Block G – Migration, Go-Live und Parallelbetrieb

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| G1 | **Ist der 1. November als Go-Live realistisch?** Wann könnten Sie nach Beauftragung beginnen? | | P1 |
| G2 | Wie läuft die Migration aus **Zoho Subscriptions** ab: Formate, Importvorlagen, Prüfläufe, wer macht was? | | P1 |
| G3 | Welche Objekte können übernommen werden: Kunden, Einheiten, Verträge, offene Posten, Kautionen, Mandate, Dokumente, Historie? | | P1 |
| G4 | Wie stellen Sie sicher, dass **die nächsten Abrechnungsstichtage** je Vertrag exakt übernommen werden? | | P1 |
| G5 | Gibt es eine Testumgebung vor dem Go-Live? | | P1 |
| G6 | Wie unterstützen Sie einen **Parallelbetrieb bis Januar** – etwa beim Abgleich von Summen und offenen Posten? | | P1 |
| G7 | Wie viel interner Aufwand ist einzuplanen, und wie wird geschult (Sprache, Umfang, Format)? | | P1 |
| G8 | Wer ist unser Ansprechpartner in der Einführungsphase, und wie sind die Supportzeiten und Reaktionszeiten? | | P2 |

## 10. Block H – Vertrag, Datenschutz, Ausstieg

| Nr. | Frage | Antwort | Prio |
| --- | --- | --- | --- |
| H1 | Wo liegen die Daten, und wer bei Ihnen kann auf unsere Produktivdaten zugreifen? Wird das protokolliert? | | P1 |
| H2 | Liegt ein AVV nach Art. 28 DSGVO samt Liste der Unterauftragsverarbeiter vor? | | P1 |
| H3 | Bitte den vollständigen Datenexport live zeigen. Welche Formate, welche Objekte? | | P1 |
| H4 | Was passiert mit unseren Daten bei Vertragsende – Herausgabe, Frist, Kosten, Löschung? | | P1 |
| H5 | Verfügbarkeit, Wartungsfenster, Backup und Wiederherstellungszeiten? | | P2 |
| H6 | Gibt es eine Zertifizierung (z. B. ISO 27001) beim Anbieter oder beim Hoster? | | P3 |

## 11. Live vorzuführende Fälle

Diese fünf Fälle werden im System durchgespielt – mit **unseren** Daten, nicht mit einer
Standardpräsentation. Die vollständige Fassung steht im [Demo-Drehbuch](demo_skript.md).

| Nr. | Fall | Worauf wir achten |
| --- | --- | --- |
| L1 | Neuer Vertrag über 12 m², Einzug am **17.** des Monats, Zahlung per Lastschrift | taggenaue anteilige Abrechnung, Mandatserfassung, Vertrags-PDF, Willkommensmail |
| L2 | Aktion „1 Monat gratis bei 12 Monaten Bindung" | Monat 1 = 0 €, automatisches Auslaufen der Aktion, Wirkung auf die ersten drei Rechnungen |
| L3 | Monatlicher Abrechnungslauf für alle Verträge, anschließend Einzugsdatei erzeugen | Anzahl der Klicks, Vorschau vor Versand, Inhalt der Datei |
| L4 | Rücklastschrift, Mahnstufen 1 und 2, Zahlungseingang, Aufhebung der Sperre | Automatik, Spesen, Zutrittssperre, Protokoll |
| L5 | Kündigung mit Frist zum Monatsende, Endabrechnung, Kaution, Rückgabe | Fristenrechnung, Anzeige „ab … verfügbar", Aufgabenliste bis zur Rückgabe |

## 12. Bewertungsbogen – unmittelbar nach der Demo ausfüllen

Je Teilnehmerin und Teilnehmer, Punkte 0 bis 5
(5 = im Standard gezeigt, 3 = mit Konfiguration, 1 = nur über Umweg, 0 = nicht möglich).

| Block | Punkte | Beobachtung, Beleg |
| --- | --- | --- |
| K K.o.-Fragen | | |
| A Lizenz und Preis | | |
| B SEPA und Mandate | | |
| C Zahlungsabgleich | | |
| D Zahlungsdienstleister | | |
| E Buchhaltung und RZL | | |
| F Österreich und Sprache | | |
| G Migration und Go-Live | | |
| H Vertrag und Datenschutz | | |
| Bedienbarkeit im Alltag | | |
| Verbindlichkeit des Anbieters | | |

**Nicht gezeigt oder ausgewichen bei:** ______________________________

**Würde ich damit arbeiten wollen?** ⬜ ja ⬜ mit Einschränkungen ⬜ nein

## 13. Nachbereitung

| Schritt | Verantwortlich | Frist |
| --- | --- | --- |
| Antworten in diesen Katalog eintragen und in `main` einchecken | Protokollführung | 1 Werktag nach der Demo |
| Offene Punkte schriftlich bei Kinnovis nachfordern | Martin | 2 Werktage |
| Bewertung in [`bewertungsmatrix.csv`](bewertungsmatrix.csv) übertragen | Beratung | 3 Werktage |
| Musterexport durch die Steuerberatung in RZL testen lassen (falls nicht vorab erfolgt) | Peter | 3 Werktage |
| Ergebnis im Entscheidungslog vermerken | Projektleitung | 3 Werktage |
