# Governance, Rollen und Zusammenarbeit

## Rollen

| Rolle | Aufgabe | Besetzung |
| --- | --- | --- |
| Auftraggeber (GF) | Entscheidungen zu Scope, Budget, Anbieterwahl; Freigabe Vertrag | *(zu benennen)* |
| Projektleitung (PL) | Termine, Aufgabenverfolgung, Eskalation, Ansprechpartner Anbieter | *(zu benennen)* |
| Fachverantwortung Betrieb | Ist-Prozesse, Testfälle, Abnahme aus Sicht Tagesgeschäft (Facility Manager) | *(zu benennen)* |
| Fachverantwortung Finanzen | Fakturierung, Zahlungen, Mahnwesen, Schnittstelle Steuerberatung | *(zu benennen)* |
| Beratung/Umsetzung | Analyse, Anforderungen, Marktansprache, Bewertung, Migrationssteuerung | accilium |
| Steuerberatung (extern) | Klärung RKSV/Belege, Kontenrahmen, Exportformat | *(Kanzlei)* |
| Anbieter | Konfiguration, Migrationsunterstützung, Schulung, Support | ab Woche 5 |

## Entscheidungsregeln

| Entscheidungstyp | Entscheidet | Vorbereitung |
| --- | --- | --- |
| Anforderung Muss/Soll | PL, im Zweifel GF | Beratung |
| Anbieterauswahl | GF | Entscheidungsvorlage der Beratung |
| Budgetabweichung > 10 % | GF | PL |
| Scope-Reduktion für Go-Live | GF | PL |
| Go-/No-Go Cutover | GF auf Empfehlung PL | Testprotokoll |

## Termine

| Termin | Rhythmus | Teilnehmende | Dauer |
| --- | --- | --- | --- |
| Jour fixe Projekt | wöchentlich, fixer Slot | GF, PL, Beratung | 45 min |
| Kurz-Standup | in Woche 6–8 täglich | PL, Fachverantwortliche | 15 min |
| Steuerungstermin/Meilenstein | zu M1–M8 | GF, PL, Beratung | 60 min |

## Dokumentation

- Dieses Repository ist die **einzige gültige Projektablage**. Entscheidungen, die nur mündlich
  oder per E-Mail fallen, werden von der PL im Entscheidungslog nachgezogen.
- Vertrauliche Unterlagen (Angebote mit Preisen, Kundendaten, Verträge) gehören **nicht** ins
  Repository, sondern in die vereinbarte geschützte Ablage; hier wird nur darauf verwiesen.
- Statusberichte wöchentlich nach `00_management/statusbericht_vorlage.md`.

## Eskalationsweg

1. Fachliche Klärung im Jour fixe.
2. Bei Terminrisiko > 3 Tage auf dem kritischen Pfad: sofortige Information an GF durch PL.
3. Bei Anbieterproblemen: schriftliche Eskalation an den benannten Ansprechpartner mit Frist.
