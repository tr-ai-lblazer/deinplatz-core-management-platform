# Datenmigration

Die Migration ist das größte Einzelrisiko des Projekts (R01, R09). Grundregel:
**zwei Testläufe vor dem produktiven Lauf**, jeder mit dokumentiertem Abgleich.

## 1. Umfang

| Objekt | Migration | Begründung |
| --- | --- | --- |
| Kunden (aktiv) | vollständig | Betriebsnotwendig |
| Kunden (inaktiv, letzte 7 Jahre) | nur Stammdaten oder Archiv | Aufbewahrungspflicht, aber keine Betriebsrelevanz |
| Einheiten | vollständig, Neuanlage nach Flächenplan | Chance zur Bereinigung der Bezeichnungen |
| Aktive Mietverträge | vollständig inkl. Preis, Rabatt, Stichtag, Kaution | betriebskritisch |
| Beendete Verträge | Archiv (PDF/Export), nicht als Datensätze | Aufwandsreduktion |
| Offene Posten | vollständig zum Stichtag | betriebskritisch, Summenabgleich zwingend |
| Rechnungshistorie | als PDF-Archiv, nicht als Belegdaten | Aufbewahrungspflicht erfüllbar, Migrationsaufwand vermeidbar |
| SEPA-Mandate | vollständig (falls übernehmbar) | sonst Neueinholung – Kundenkommunikation nötig |
| Dokumente | selektiv: aktueller Vertrag je aktivem Kunden | Rest bleibt im Archiv |
| Zutrittsberechtigungen | Neuanlage im Zielsystem | sauberer Stand, geringes Risiko |
| Leads/Notizen | optional | nur wenn ohne Aufwand möglich |

## 2. Ablauf je Durchlauf

```
Export (Alt) → Bereinigung → Mapping → Import (Neu) → Abgleich → Protokoll → Fehlerkorrektur
```

| Schritt | Ergebnis | Verantwortlich |
| --- | --- | --- |
| Export | Rohdateien mit Zeitstempel, unverändert archiviert | Beratung |
| Bereinigung | Dubletten, fehlende Pflichtfelder, Formatfehler (IBAN, PLZ, E-Mail) bereinigt | Fachverantwortung |
| Mapping | Feldzuordnung Alt → Neu, dokumentiert je Objekt | Beratung + Anbieter |
| Import | Import in die Testumgebung mit Importprotokoll | Anbieter |
| Abgleich | Summen- und Stichprobenprüfung (siehe unten) | Fachverantwortung Finanzen |
| Protokoll | Ergebnis, Abweichungen, Maßnahmen | Beratung |

## 3. Abgleichregeln (Abnahmekriterien der Migration)

| Prüfung | Kriterium |
| --- | --- |
| Anzahl aktiver Kunden | alt = neu |
| Anzahl aktiver Verträge | alt = neu |
| Summe monatlicher Sollmieten | Abweichung 0,00 € |
| Summe offener Posten | Abweichung 0,00 € |
| Summe Kautionen | Abweichung 0,00 € |
| Nächster Abrechnungsstichtag | bei 100 % der Verträge korrekt (Stichprobe 20 + alle Sonderfälle) |
| Rabatte/Aktionen | alle laufenden Aktionen mit korrektem Enddatum |
| SEPA-Mandate | Anzahl und Mandatsreferenzen identisch |
| Stichprobe Einzelverträge | 50 zufällige Verträge Feld für Feld geprüft |
| Sonderfälle | alle Verträge mit mehreren Einheiten, Teilzahlungen, Guthaben, Ratenvereinbarungen |

Die Migration gilt erst als abgenommen, wenn **alle** Kriterien erfüllt sind. Die Freigabe
erteilt die Fachverantwortung Finanzen schriftlich (Eintrag im Protokoll).

## 4. Migrationsprotokoll (Vorlage je Durchlauf)

| Feld | Eintrag |
| --- | --- |
| Durchlauf | Test 1 / Test 2 / Produktiv |
| Datum, Uhrzeit | |
| Exportstand (Stichtag) | |
| Importierte Datensätze je Objekt | |
| Fehlerhafte Datensätze | |
| Abweichungen im Summenabgleich | |
| Maßnahmen | |
| Freigabe (Name, Datum) | |

## 5. Typische Fallstricke

| Fallstrick | Gegenmaßnahme |
| --- | --- |
| Abrechnungsstichtage verschieben sich, Kunden werden doppelt oder gar nicht belastet | Stichtag je Vertrag explizit prüfen; ersten Lauf im Vier-Augen-Prinzip |
| Rabatte laufen im Neusystem unbegrenzt weiter | Enddatum je Aktion kontrollieren (Stichprobe 100 % der Aktionsverträge) |
| SEPA-Mandate nicht übertragbar → Einzüge scheitern | frühzeitig mit Bank/Provider klären (O-06), sonst Neueinholung mit Vorlauf |
| IBAN-/Adressfehler blockieren den Import | Formatprüfung bereits in der Bereinigungsphase |
| Kautionen gehen verloren | eigene Prüfsumme, getrennte Position |
| Historie fehlt bei Kundenrückfragen | Archivexport des Altsystems griffbereit, Zugriff geregelt |
| Umlaute/Zeichensatz zerschossen | Export und Import konsequent UTF-8, Stichprobe auf Umlaute |

## 6. Datenschutz bei der Migration

- Exporte enthalten personenbezogene Daten: Ablage ausschließlich in der geschützten Ablage,
  **niemals in diesem Repository** (siehe `.gitignore`).
- Weitergabe an den Anbieter nur auf Basis des Auftragsverarbeitungsvertrags.
- Nach Abschluss der Migration: Testdaten und Zwischenkopien nachweislich löschen.
- Anlass zur Bereinigung nutzen: Daten, die nicht mehr benötigt werden, werden nicht migriert.
