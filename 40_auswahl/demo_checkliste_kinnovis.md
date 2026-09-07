# Demo-Checkliste Kinnovis

Aufgabe A1 aus dem Stakeholder-Termin vom 07.09.2026. Diese Liste geht **vor** dem Termin an
Kinnovis, damit die Punkte vorbereitet vorgeführt werden. Grundsatz: Was nicht live gezeigt oder
schriftlich zugesagt wird, gilt als nicht vorhanden.

Ergänzend gilt das allgemeine Demo-Drehbuch [`demo_skript.md`](demo_skript.md) mit den acht
Testfällen. Diese Checkliste ergänzt die Punkte, die im Termin ausdrücklich benannt wurden.

## A  Lizenzmodell, Preise, Bindung

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| A1 | Wie ist das Lizenzmodell aufgebaut – je Standort, je Einheit, je Benutzer oder umsatzabhängig? | | ⬜ |
| A2 | Wie hoch sind die Kosten für unseren Fall: ein Standort, rund 250 aktive Verträge? | | ⬜ |
| A3 | **Fällt zusätzlich zu den Zahlungsentgelten ein Prozentsatz auf den abgewickelten Umsatz an? Wenn ja, wie hoch und wofür?** | | ⬜ |
| A4 | Welche Funktionen sind im Preis enthalten, welche kosten extra (Kundenportal, Buchungsstrecke, Facility Map, Zutrittsintegration, E-Signatur)? | | ⬜ |
| A5 | Wie lang ist die Mindestlaufzeit, wie lang die Kündigungsfrist? | | ⬜ |
| A6 | Wie werden Preise angepasst – Ankündigungsfrist, Obergrenze, Indexbindung? | | ⬜ |
| A7 | Was kostet ein zweiter Standort? | | ⬜ |
| A8 | Gibt es einmalige Kosten für Einrichtung, Migration oder Schulung? | | ⬜ |
| A9 | Gesamtkosten über 36 Monate, schriftlich und aufgeschlüsselt | | ⬜ |

## B  Zahlungsabwicklung über die eigene Bank

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| B1 | **Erzeugt Kinnovis eine SEPA-Einzugsdatei (pain.008) zum Upload in unser Electronic Banking?** | | ⬜ |
| B2 | Können wir dabei unter **unserer eigenen Gläubiger-ID** einziehen? | | ⬜ |
| B3 | Können bestehende Mandate mit IBAN, Mandatsreferenz und Erteilungsdatum importiert werden? | | ⬜ |
| B4 | **Unterstützt das System eine Mandatsänderung bei Gläubigerwechsel** – also die Angabe der bisherigen Gläubiger-ID und Mandatsreferenz im Einzug (Anforderung ABR-18)? | | ⬜ |
| B5 | Wie werden Rückläufer erfasst, und lösen sie automatisch eine Mahnstufe aus? | | ⬜ |
| B6 | Wird die Vorabinformation (Pre-Notification) automatisch erzeugt und versendet? Welche Frist ist einstellbar? | | ⬜ |

## C  Bankdaten und Zuordnung von Zahlungen

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| C1 | **Benötigt Kinnovis Bank-Feeds zur Konsolidierung?** Wenn ja, welche Formate (CAMT.053, MT940, Direktanbindung)? | | ⬜ |
| C2 | Kann ein Kontoauszug eingelesen und automatisch der offenen Forderung zugeordnet werden? | | ⬜ |
| C3 | **Wie müssen Zahlungstexte, Verwendungszweck oder Referenz gestaltet sein, damit die Zuordnung automatisch gelingt** (Anforderung ABR-19)? | | ⬜ |
| C4 | Wie werden Überweisungen behandelt, die nicht zuordenbar sind? | | ⬜ |
| C5 | Wie werden Teilzahlungen und Guthaben abgebildet? | | ⬜ |

## D  Zahlungsabwicklung über Stripe

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| D1 | Welche Zahlungsarten stehen zur Verfügung (SEPA, Karte, Apple Pay, weitere)? | | ⬜ |
| D2 | Welche Entgelte fallen an – je Transaktion, je Rückläufer, prozentual? | | ⬜ |
| D3 | In welchem Rhythmus zahlt Stripe aus, und **wie werden die Sammelauszahlungen samt Gebühren im Buchhaltungsexport aufgelöst** (Anforderung BUH-05)? | | ⬜ |
| D4 | **Können Bank-Lastschrift für den Bestand und Stripe für Neukunden dauerhaft parallel laufen** (Anforderung ABR-17)? | | ⬜ |
| D5 | Wird bei Stripe unsere eigene Gläubiger-ID verwendet? Wann muss diese Entscheidung fallen? | | ⬜ |

## E  Buchhaltung und Steuerberatung

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| E1 | **Bitte einen echten Buchhaltungsexport eines Monats erzeugen und die Datei zeigen** | | ⬜ |
| E2 | Welche Formate stehen zur Verfügung (DATEV-CSV, eigenes CSV, andere)? Ist der Export in RZL importierbar? | | ⬜ |
| E3 | Sind Konten und Steuerschlüssel frei konfigurierbar, auch für den österreichischen Kontenrahmen? | | ⬜ |
| E4 | Wie werden Kautionen abgebildet – Erlös oder durchlaufender Posten? | | ⬜ |
| E5 | Wie wird eine bereits versendete Rechnung korrigiert? | | ⬜ |

## F  Österreichische Anforderungen

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| F1 | Musterrechnung für einen österreichischen Firmenkunden mit UID und Umsatzsteuerausweis | | ⬜ |
| F2 | Sind Oberfläche **und** alle Kundendokumente auf Deutsch und von uns selbst änderbar? Bitte einen Text live ändern | | ⬜ |
| F3 | Wie wird eine Barzahlung mit Belegausgabe erfasst? | | ⬜ |
| F4 | Gibt es Referenzkunden in Österreich? | | ⬜ |

## G  Umstellung und Betrieb

| Nr. | Frage | Antwort | Status |
| --- | --- | --- | --- |
| G1 | Wann können Sie nach Beauftragung mit der Einrichtung beginnen? Ist der **1. November** als Go-Live realistisch? | | ⬜ |
| G2 | Wie läuft die Migration ab: Formate, Importvorlagen, Prüfläufe, wer macht was? | | ⬜ |
| G3 | Gibt es eine Testumgebung vor dem Go-Live? | | ⬜ |
| G4 | Wie viel interner Aufwand ist einzuplanen, und wie wird geschult? | | ⬜ |
| G5 | Wie unterstützen Sie einen **Parallelbetrieb bis Januar** – etwa beim Abgleich der Summen? | | ⬜ |
| G6 | Wie erfolgt der vollständige Datenexport, falls wir das System wieder verlassen? | | ⬜ |

## H  Nach der Demo auszufüllen

| Punkt | Ergebnis |
| --- | --- |
| Nicht gezeigt oder ausgewichen bei | |
| Schriftlich zugesagt | |
| Offene Punkte mit Termin | |
| Gesamteindruck Betrieb (Bedienbarkeit im Alltag) | |
| Gesamteindruck Finanzen (Abrechnung, Buchhaltung) | |
| Empfehlung | |
