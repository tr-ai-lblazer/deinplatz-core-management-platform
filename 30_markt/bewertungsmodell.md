# Bewertungsmodell

Ziel: eine nachvollziehbare, dokumentierte Entscheidung – nicht die höchste Punktzahl um jeden
Preis. Die Punktbewertung strukturiert die Diskussion; die Entscheidung trifft die
Geschäftsführung und begründet sie im Entscheidungslog.

## 1. Zweistufiges Verfahren

**Stufe 1 – K.o.-Prüfung (Ja/Nein).** Alle als K.o. markierten Anforderungen müssen erfüllt sein.
Kein Ausgleich durch Punkte in anderen Bereichen.

**Stufe 2 – Gewichtete Bewertung** in vier Dimensionen:

| Dimension | Gewicht | Inhalt |
| --- | --- | --- |
| D1 Funktionale Abdeckung | 45 % | Erfüllungsgrad des Anforderungskatalogs, gewichtet nach Domänen |
| D2 Kosten (TCO 3 Jahre) | 25 % | Lizenz, Einrichtung, Migration, Zahlungsentgelte, interner Aufwand |
| D3 Einführbarkeit in 8 Wochen | 20 % | Startfähigkeit, Migrationsunterstützung, Konfigurationsaufwand, Schulungsbedarf |
| D4 Anbieter & Betrieb | 10 % | Sprache/Support, Referenzen im DACH-Raum, Stabilität, Datenschutz, Ausstiegsfähigkeit |

## 2. Punkteskala je Einzelkriterium

| Punkte | Bedeutung |
| --- | --- |
| 5 | Vollständig im Standard erfüllt, in der Demo gezeigt |
| 4 | Im Standard erfüllt, kleinere Einschränkungen |
| 3 | Mit Konfiguration erfüllbar, Aufwand vertretbar |
| 2 | Nur mit Zusatzmodul, Zusatzkosten oder Workaround |
| 1 | Nur über Individualanpassung/Drittsystem |
| 0 | Nicht erfüllbar |

**Beleggrundsatz:** Nur was in der Demo gezeigt oder schriftlich zugesagt wurde, zählt als
erfüllt. Aussagen wie „steht auf der Roadmap" werden mit maximal 1 Punkt bewertet und im
Kommentarfeld vermerkt.

## 3. Berechnung der funktionalen Abdeckung (D1)

Je Domäne wird der Erfüllungsgrad ermittelt und mit dem Domänengewicht aus dem
Anforderungskatalog multipliziert:

```
Domänenwert   = Σ(Punkte je Anforderung × Prioritätsfaktor) / Σ(5 × Prioritätsfaktor)
Prioritätsfaktor: Muss = 3, Soll = 2, Kann = 1
D1            = Σ(Domänenwert × Domänengewicht) × 100
```

## 4. Kostenbewertung (D2)

Verglichen wird die **TCO über 3 Jahre**, nicht der Monatspreis:

| Position | Erhebung |
| --- | --- |
| SaaS-Lizenz (36 Monate, inkl. angekündigter Preissteigerung) | Angebot |
| Einmalige Einrichtung, Vorlagen, Schulung | Angebot |
| Datenmigration (Anbieter + eigener Aufwand) | Angebot + Schätzung |
| Zahlungsentgelte (Annahme: monatliches Volumen × Gebührensatz × 36) | Angebot Provider |
| Zusatzmodule (Portal, Buchungsstrecke, Zutrittsintegration, E-Signatur) | Angebot |
| Interner Betriebsaufwand (Stunden/Monat × Stundensatz) | Schätzung |

Punktvergabe: günstigstes Angebot = 5 Punkte; je angefangene 15 % Mehrkosten ein Punkt Abzug
(Minimum 0).

## 5. Einführbarkeit (D3)

| Kriterium | Punkte-Anker |
| --- | --- |
| Startzusage nach Beauftragung | 5 = innerhalb 1 Woche · 3 = 2–3 Wochen · 0 = > 4 Wochen |
| Migrationsunterstützung | 5 = Import inkl. Prüflauf durch Anbieter · 3 = Importvorlagen + Support · 1 = reine Selbstbedienung |
| Konfigurationsaufwand bis Produktivbetrieb | 5 = wenige Tage · 3 = 1–2 Wochen · 1 = mehrere Wochen |
| Schulungsbedarf | 5 = ≤ 4 Stunden · 3 = 1 Tag · 1 = mehrtägig |
| Testumgebung vor Go-Live | 5 = ja · 0 = nein |

## 6. Anbieter & Betrieb (D4)

Sprache und Erreichbarkeit des Supports, Referenzkunden im DACH-Raum (idealerweise Österreich),
Unternehmensstabilität und Kundenanzahl, Datenschutz-/Hostingnachweise, Vertragskonditionen
(Laufzeit, Kündigung, Preisanpassung), Ausstiegsfähigkeit (Datenexport).

## 7. Ergebnisdarstellung

Die Werte werden in [`../40_auswahl/bewertungsmatrix.csv`](../40_auswahl/bewertungsmatrix.csv)
je Anbieter erfasst. Die Entscheidungsvorlage enthält zusätzlich:

- Gesamtpunktzahl und Rangfolge,
- die zwei bis drei entscheidenden Unterschiede in Klartext,
- den ausdrücklichen Hinweis, wenn der punktbeste Anbieter **nicht** empfohlen wird, samt Begründung,
- Risiken der Empfehlung und deren Absicherung im Vertrag.

## 8. Sensitivitätsprüfung

Vor der Entscheidung wird geprüft, ob sich die Rangfolge ändert, wenn
(a) das Kostengewicht auf 35 % steigt oder (b) die Online-Buchungsstrecke aus der Bewertung
genommen wird (Phase-2-Szenario). Bleibt die Rangfolge stabil, ist die Entscheidung robust;
kippt sie, muss die Geschäftsführung die Gewichtung ausdrücklich bestätigen.
