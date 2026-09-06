# Cutover und Go-Live (Woche 8)

## Grundsätze

1. **Cutover auf die Monatsgrenze legen.** Der Wechsel erfolgt so, dass ein voller
   Abrechnungszeitraum sauber im neuen System beginnt. Das vermeidet doppelte oder fehlende
   Rechnungen – der häufigste und teuerste Fehler bei Systemwechseln.
2. **Ein System ist führend – ab dem Stichtag das neue.** Kein Parallelbetrieb bei der Erfassung.
   Das Altsystem bleibt ausschließlich lesend erreichbar.
3. **Rückfallebene definieren, bevor sie gebraucht wird.**

## Ablaufplan

### Vorbereitung (Freitag vor dem Cutover)

- [ ] Abnahme erteilt (M7), Go-Entscheidung der Geschäftsführung dokumentiert
- [ ] Kundenanschreiben versandfertig (neue Zahlungsweise, Portalzugang, Ansprechpartner)
- [ ] Team informiert: ab Montag keine Erfassung mehr im Altsystem
- [ ] Vollbackup/Export des Altsystems erstellt und geprüft
- [ ] Notfallkontakt beim Anbieter für den Cutover-Zeitraum bestätigt

### Tag 1 (Montag): Datenannahmestopp

- [ ] Altsystem auf lesend umgestellt bzw. Erfassung eingestellt
- [ ] Finaler Vollexport gezogen (Zeitstempel dokumentiert)
- [ ] Vorgänge des Tages werden auf einer Deltaliste geführt und später manuell nachgetragen

### Tag 2 (Dienstag): Produktive Migration

- [ ] Import in die Produktivumgebung
- [ ] Abgleich nach den Kriterien aus `datenmigration.md`
- [ ] Deltaliste nachgetragen
- [ ] Schriftliche Freigabe durch Fachverantwortung Finanzen
- [ ] **Entscheidungspunkt:** Freigabe erteilt → weiter; nicht erteilt → Rückfall (siehe unten)

### Tag 3 (Mittwoch): Go-Live

- [ ] Alle Neuvorgänge ausschließlich im neuen System
- [ ] Zutrittsberechtigungen geprüft (Stichprobe vor Ort)
- [ ] Kundeninformation versendet
- [ ] Website/Buchungsstrecke umgestellt (falls im Umfang)
- [ ] Kurzanleitung am Arbeitsplatz ausgehängt

### Tag 4 (Donnerstag): Erster Abrechnungslauf

- [ ] Lauf im Testmodus/Vorschau prüfen: Anzahl Rechnungen, Summe, Auffälligkeiten
- [ ] Vier-Augen-Prinzip: Freigabe durch zwei Personen
- [ ] Versand
- [ ] Stichprobe von 10 Rechnungen inhaltlich prüfen

### Tag 5 (Freitag): Zahlungslauf und Stabilisierung

- [ ] SEPA-Einzug ausgelöst, Vorabinformationsfristen eingehalten
- [ ] Rückläufer und Fehler beobachtet
- [ ] Offene Punkte gesammelt, Hypercare-Plan bestätigt

## Rückfallebene

| Auslöser | Reaktion |
| --- | --- |
| Migrationsabgleich scheitert (Tag 2) | Cutover abbrechen, Altsystem wieder produktiv setzen, Fehler beheben, Cutover auf den nächsten Monatswechsel verschieben |
| Abrechnungslauf liefert falsche Beträge | Versand stoppen, Ursache klären; im Notfall Fakturierung des Monats einmalig manuell, Systembetrieb parallel fortführen |
| Zahlungsanbindung funktioniert nicht | Einzug des Monats über die bisherige Methode; Systembetrieb läuft weiter |
| Zutritt funktioniert nicht | Übergangsweise manuelle Zutrittsverwaltung durch den Facility Manager |

Die Entscheidung über den Rückfall trifft die Geschäftsführung auf Empfehlung der Projektleitung
und wird im Entscheidungslog dokumentiert.

## Hypercare (2 Wochen nach Go-Live)

- Tägliches Kurz-Standup (15 Minuten): Was hat gestern nicht funktioniert?
- Zentrale Fehlerliste, tägliche Nachverfolgung mit dem Anbieter
- Tägliche Kontrolle: Zahlungseingänge, fehlgeschlagene Einzüge, offene Posten
- Nach 2 Wochen: Übergang in den Regelbetrieb, Restpunkte in eine Nachlaufliste

## Abschluss des Altsystems

- [ ] Revisionssicheres Archiv erstellt (Belege, Verträge, Buchungsdaten) und geprüft lesbar
- [ ] Aufbewahrungsfristen dokumentiert (Verweis: `20_anforderungen/rechtliche_rahmenbedingungen_at.md`)
- [ ] Zugriff auf das Archiv geregelt (wer, wie, wo)
- [ ] Kündigung des Altsystems ausgesprochen, Kündigungsbestätigung abgelegt
- [ ] Löschung der Daten beim Altanbieter beauftragt und bestätigt
