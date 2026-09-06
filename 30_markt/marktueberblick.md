# Marktüberblick: Kernsysteme für Self-Storage

Desk Research, Stand 06.09.2026. Alle Anbieterangaben stammen aus öffentlich zugänglichen
Quellen (Anbieterseiten, Vergleichsportale, Branchenmedien) und sind in
[`../90_quellen/recherchequellen.md`](../90_quellen/recherchequellen.md) belegt.

> **Wichtig:** Preise und Funktionsumfänge von SaaS-Produkten ändern sich laufend und sind
> stark vom Vertriebsgespräch abhängig. Die Angaben hier dienen der Vorauswahl, **nicht** der
> Entscheidung. Verbindlich sind ausschließlich die schriftlichen Angebote aus Woche 4.

## 1. Drei Lösungswege

| Weg | Beschreibung | Stärken | Schwächen | Eignung für deinPlatz |
| --- | --- | --- | --- | --- |
| **A – Self-Storage-Fachsystem** | Branchensoftware, die Einheiten, Verträge, Abrechnung, Online-Buchung und Zutritt in einem Produkt abbildet | Prozesse sind bereits fertig gedacht; schnellste Einführung; Zutritts- und Zahlungsintegrationen vorhanden | Wenig Spielraum für Sonderwünsche; teils angelsächsisch geprägt (Sprache, Steuerlogik, Zahlungsarten) | **Hoch** – Standardprozesse eines Einzelstandorts |
| **B – Generischer Stack** (CRM + Abo-Abrechnung + Buchhaltung) | Kombination aus Standardbausteinen, z. B. CRM plus Subscription-Billing plus Buchhaltung | Sehr flexibel; deutschsprachig und AT-konform verfügbar; oft günstiger in der Lizenz | Belegungsplan, Zutritt und Buchungsstrecke müssen nachgebaut/integriert werden; höherer Einrichtungsaufwand | **Mittel** – Rückfalloption, falls Weg A an AT-Anforderungen scheitert |
| **C – Individualentwicklung / Low-Code** | Eigenbau auf einer Plattform | Passgenau | In 8 Wochen nicht mit vertretbarem Risiko produktiv zu bekommen; Wartung bleibt am Betrieb hängen | **Nicht empfohlen** (siehe Entscheidung E-02) |

## 2. Erkenntnisse aus der Recherche

1. **Der Markt ist klein, aber gut besetzt.** Für Einzelstandorte mit 100–400 Einheiten gibt es
   mehrere ausgereifte SaaS-Produkte; die Einführung ist bei diesen Anbietern ein
   Standardvorgang von wenigen Wochen – der 8-Wochen-Rahmen ist damit grundsätzlich realistisch.
2. **Die Sprach- und Rechtsraumfrage entscheidet die Vorauswahl.** Viele führende Produkte
   kommen aus dem angelsächsischen Raum (Storable/SiteLink, Stora). Für deinPlatz sind
   deutschsprachige Oberfläche und Kundentexte, österreichische Rechnungslogik, SEPA-Lastschrift
   und ein für die Steuerberatung brauchbarer Export die harten Kriterien.
3. **DACH-Relevanz ist konkret vorhanden.** Storeganise wird im deutschsprachigen Raum
   eingesetzt und verweist auf Support in Wien; Kinnovis ist ein europäischer Anbieter mit
   Fokus auf automatisierte Buchung, Abrechnung und Kundenportal; mit selfstorage.team existiert
   ein DACH-Angebot, das Software mit Marketing-, Telefon- und Buchhaltungsdiensten kombiniert.
4. **Zahlungsabwicklung ist der eigentliche Automatisierungshebel.** Marktüblich ist der
   monatliche automatische Einzug per Karte oder SEPA-Lastschrift mit automatischer
   Rücklastschrift-Behandlung und automatischem Mahnlauf. Genau hier liegt der größte
   Zeitgewinn gegenüber manueller Fakturierung.
5. **Zutrittskontrolle wird über Integrationen gelöst, nicht im Kernsystem.** Verbreitet sind
   Nokē Smart Entry (Janus), PTI, SpiderDoor, OpenTech sowie im DACH-Raum Sensorberg. Welche
   Integration möglich ist, hängt vom vorhandenen Anlagenhersteller ab – deshalb ist dessen
   Erhebung in Woche 1 ein kritischer Input.
6. **Buchhaltungsanbindung ist der typische Schwachpunkt internationaler Anbieter.**
   Angebunden sind meist Xero oder QuickBooks; für Österreich zählen BMD, RZL oder DATEV
   bzw. ein sauber definierter CSV-Export. Diese Frage gehört zwingend in den RFP (BUH-01).

## 3. Preisniveau (Orientierung, keine Angebote)

| Anbieter | Öffentlich genannte Größenordnung | Anmerkung |
| --- | --- | --- |
| Storeganise | ab ca. 90 USD/Monat (jährliche Zahlung) für 1–100 Einheiten, ca. +10 USD je weitere 10 Einheiten | skaliert mit Einheitenzahl |
| Stora | ca. 100–200 GBP/Monat je Standort | UK-Preisliste |
| Kinnovis | keine öffentliche Preisliste, Angebot nach Standort-/Einheitenzahl | Anfrage nötig |
| SiteLink / Storable | keine öffentliche Preisliste | eher auf Mehrstandortbetreiber ausgelegt |
| Generischer Stack (Weg B) | Lizenzkosten häufig niedriger, Einrichtungsaufwand höher | TCO erst nach Angebot vergleichbar |

Zusätzlich fallen in allen Fällen **transaktionsabhängige Zahlungsentgelte** an
(Kartenzahlung typischerweise deutlich teurer als SEPA-Lastschrift). Diese gehören in die
TCO-Betrachtung, weil sie bei laufenden Mieten monatlich anfallen.

## 4. Konsequenzen für das Vorgehen

- Die Longlist enthält bewusst beide Wege (A und B), damit die Entscheidung belastbar ist.
- Im RFP werden die AT-spezifischen Punkte (Sprache, USt./Rechnung, SEPA, Steuerberatungs-Export,
  Registrierkasse bei Barumsätzen) als K.o.-Kriterien vorangestellt – das reduziert die Longlist
  schnell und spart in der kurzen Projektlaufzeit Demo-Termine.
- Für jede Demo gilt: **Der Anbieter führt unsere Testfälle vor**, nicht seine Standardpräsentation
  (siehe `40_auswahl/demo_skript.md`).
