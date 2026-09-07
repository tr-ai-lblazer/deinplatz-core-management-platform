# Risikoregister

Bewertung: Eintrittswahrscheinlichkeit (E) und Auswirkung (A) je 1–5, Risikowert = E × A.
Stand: 06.09.2026 · Aktualisierung im wöchentlichen Jour fixe.

| ID | Risiko | E | A | Wert | Maßnahme | Verantwortlich | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Datenqualität im Altsystem schlechter als erwartet (Dubletten, fehlende IBAN/SEPA-Mandate, unklare Vertragsstände) | 4 | 4 | 16 | Testexport bereits in Woche 1, Bereinigung parallel zur Auswahl, Bereinigungsverantwortliche benennen | Beratung | offen |
| R02 | Entscheidung in Woche 5 verzögert sich | 3 | 5 | 15 | Entscheidungstermin fix im Kalender, Entscheidungsvorlage 3 Tage vorher, Rückfallebene definiert | PL | offen |
| R03 | SEPA-Mandate müssen neu eingeholt werden | 2 | 4 | 8 | **Entschärft:** deinPlatz ist selbst Gläubiger mit eigener Gläubiger-ID, die Mandate bleiben gültig. Verbleibende Fälle: Mandate ohne Einzug in den letzten 36 Monaten und Verträge ohne Mandat | Finanzen | reduziert |
| R16 | **Gläubiger-ID wird in Stripe falsch konfiguriert** – nach der ersten Live-Zahlung nicht mehr änderbar | 3 | 5 | **15** | Konfiguration mit eigener Gläubiger-ID vor der ersten Live-Zahlung schriftlich bestätigen lassen (O-10) | PL | offen |
| R17 | Kein Kontoauszugsimport in beiden Systemen | 3 | 3 | 9 | In den Demos prüfen (O-11); Anteil der Überweiser durch Umstellungsaktion senken | Beratung | offen |
| R04 | Zutrittskontrolle lässt sich nicht (oder nur teuer) anbinden | 3 | 3 | 9 | Hersteller/Modell in Woche 1 erheben, Integrationsfrage in RFP, manueller Betrieb als Übergangslösung akzeptiert | Beratung | offen |
| R05 | Kein Anbieter erfüllt die österreichischen Anforderungen (USt., Belege, Steuerberatungs-Export) vollständig | 2 | 5 | 10 | K.o.-Kriterien früh prüfen, Alternative „Fachsystem + Buchhaltungs-/Kassensystem" als Kombination bewerten | Beratung | offen |
| R06 | Kapazität im Kleinbetrieb: Tagesgeschäft blockiert Projektmitarbeit | 4 | 3 | 12 | Feste Zeitfenster (halbtags/Woche) reservieren, Aufgaben so weit möglich an Beratung/Anbieter auslagern | GF | offen |
| R07 | Kundenakzeptanz: Umstellung auf Lastschrift/Portal irritiert Bestandskunden | 3 | 3 | 9 | Frühe, klare Kundenkommunikation; Zahlungsarten übergangsweise parallel zulassen | GF | offen |
| R08 | Doppelbelastung durch Altsystem (Kündigungsfrist nicht eingehalten) | 3 | 2 | 6 | Vertragsfristen in Woche 1 prüfen und Kündigung terminieren | PL | offen |
| R09 | Migration verzögert den ersten Abrechnungslauf, Umsatz wird zu spät fakturiert | 2 | 5 | 10 | Cutover auf Monatsgrenze legen, Testlauf 2 mit echten Daten, Fallback: Fakturierung einmalig manuell | Beratung | offen |
| R10 | Anbieter-Lock-in (kein vollständiger Datenexport) | 2 | 4 | 8 | Exportfähigkeit als K.o.-Kriterium und Vertragsklausel | GF | offen |
| R11 | Scope-Ausweitung („wenn wir schon dabei sind …": Website, Marketing, zweiter Standort) | 4 | 3 | 12 | Nicht-Ziele im Projektauftrag, Themen in Backlog für Phase 2 | PL | offen |
| R12 | Preis-/Kostenüberraschung durch transaktionsabhängige Gebühren | 3 | 3 | 9 | TCO über 3 Jahre mit realistischem Transaktionsvolumen rechnen, nicht mit Listenpreis je Modul; SEPA statt Karte als Standard | Beratung | offen |
| R13 | **Kein Anbieter liefert einen in RZL importierbaren Buchhaltungsexport** | 3 | 5 | **15** | Musterexport beider Anbieter vor der Entscheidung von der Steuerberatung testweise importieren lassen; Rückfallebene: Mapping-Datei oder monatlicher Sammelbeleg | Beratung + Steuerberatung | offen |
| R14 | Zuordnung Kunde ↔ Lagerabteil ist nicht strukturiert vorhanden (in Zoho kein Objektmodell) | 4 | 3 | 12 | Führende Einheitenliste in Woche 1 aufbauen und per Begehung vor Ort verifizieren | Fachverantwortung Betrieb | offen |
| R15 | Deutschsprachigkeit der Kundendokumente bei einem Shortlist-Anbieter nicht gegeben | 2 | 5 | 10 | K.o.-Prüfung in der Demo an echten Vorlagen; Rückfallebene Weg B aus der Longlist | Beratung | offen |
| R18 | **Gläubiger-ID und Mandate gehen beim Wechsel zur GmbH nicht über** – rund 250 Mandate müssten neu eingeholt werden | 3 | 5 | **15** | Klärung mit Bank und Steuerberatung in KW 38 (O-12); Systemfähigkeit zur Mandatsänderung als K.o.-Kriterium ABR-18; Kommunikation so terminieren, dass ein Schreiben genügt | Peter | offen |
| R19 | Parallelbetrieb wird zur Doppelpflege: beide Systeme fakturieren | 3 | 4 | 12 | Schattenbetrieb festlegen (O-14): ein führendes System ab 01.11., Zoho nur lesend; Abgleich zu drei festen Terminen | PL | offen |
| R20 | Preiserhöhung zum 01.01.2027 trifft mit der Systemumstellung zusammen und löst Kündigungen aus | 3 | 3 | 9 | Kommunikation trennen (O-15); Umstellungsinformation neutral halten, Preisanpassung mit eigener Frist und Begründung | GF | offen |
| R21 | Der Sieben-Tage-Auszahlungsrhythmus des Zahlungsdienstleisters erhöht den Buchhaltungsaufwand dauerhaft | 3 | 2 | 6 | Auflösung der Sammelauszahlungen im Buchhaltungsexport als Anforderung BUH-05; Einrichtung mit der Steuerberatung einmalig festlegen | Finanzen | offen |

## Top-3-Risiken zum Projektstart

1. **R18 Gläubigerwechsel zur GmbH** – entscheidet, ob rund 250 Mandate neu eingeholt werden
   müssen und ob eine einzige Kundeninformation genügt. Klärung in KW 38.
2. **R13 RZL-Export** – die wichtigste Einzelanforderung; der Nachweis muss vor der Entscheidung
   erbracht werden. Daneben bleibt R14 (Einheitenzuordnung) Voraussetzung jeder Migration.
3. **R02 Entscheidungsverzug** – der 8-Wochen-Plan hat auf dem kritischen Pfad keinen Puffer.
