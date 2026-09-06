# Nicht-funktionale Anforderungen (NFA)

Diese Anforderungen sind nicht als Funktionsliste abfragbar, sondern werden über Nachweise,
Vertragszusagen und die Demo geprüft. Sie fließen in die Bewertungsdimensionen
„Anbieter & Betrieb" und „Einführbarkeit" ein.

## 1. Betrieb und Verfügbarkeit

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-01 | Verfügbarkeit der SaaS-Lösung | ≥ 99,5 % im Monatsmittel | SLA im Vertrag |
| NFA-02 | Geplante Wartungsfenster | außerhalb 08:00–18:00 MEZ, mit Vorankündigung | SLA |
| NFA-03 | Erreichbarkeit des Kundenportals und der Buchungsstrecke | 24/7 | Statusseite/Referenzen |
| NFA-04 | Antwortzeit im Tagesgeschäft (Suche, Kundenakte öffnen) | < 2 Sekunden | Demo mit realistischem Datenvolumen |
| NFA-05 | Bedienbarkeit auf Tablet/Smartphone (Facility Manager vor Ort) | Kernfunktionen mobil nutzbar | Demo am Gerät |

## 2. Support und Betreuung

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-06 | Supportsprache | Deutsch | Vertrag, Testanfrage |
| NFA-07 | Supportzeiten | mindestens Mo–Fr 08:00–17:00 MEZ | SLA |
| NFA-08 | Reaktionszeit bei Betriebsstillstand (z. B. keine Abrechnung möglich) | ≤ 4 Stunden | SLA |
| NFA-09 | Benannter Ansprechpartner in der Einführungsphase | ja | Angebot |
| NFA-10 | Selbsthilfe: deutschsprachige Dokumentation/Hilfecenter | vorhanden | Sichtprüfung |

## 3. Sicherheit und Datenschutz

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-11 | Hosting in der EU/EWR | ja | AVV, Angabe Rechenzentrum |
| NFA-12 | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO inkl. Unterauftragsverarbeiter-Liste | vorliegend | Vertragsdokument |
| NFA-13 | Verschlüsselung der Übertragung (TLS) und der Datenhaltung | Stand der Technik | Anbieterauskunft |
| NFA-14 | Rollenbasierte Rechte, Zwei-Faktor-Authentifizierung | verfügbar | Demo |
| NFA-15 | Backups mit definierter Wiederherstellungszeit | tägliches Backup, RPO ≤ 24 h, RTO ≤ 8 h | SLA |
| NFA-16 | Zertifizierungen (z. B. ISO 27001) beim Anbieter oder Hoster | vorhanden oder begründet nicht | Nachweis |
| NFA-17 | Zahlungsdaten: keine Speicherung von Kartendaten im System selbst (PCI-DSS-konformer Provider) | ja | Anbieterauskunft |

## 4. Datenhoheit und Ausstiegsfähigkeit

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-18 | Vollständiger Datenexport (Stammdaten, Verträge, Belege, Zahlungen) jederzeit durch den Kunden auslösbar | ja | Demo |
| NFA-19 | Exportformate maschinenlesbar (CSV/Excel, PDF für Belege) | ja | Demo |
| NFA-20 | Herausgabe der Daten bei Vertragsende, definierte Löschung danach | vertraglich geregelt | Vertrag |
| NFA-21 | Keine Zusatzkosten für den Datenexport | ja | Vertrag |

## 5. Einführbarkeit im 8-Wochen-Rahmen

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-22 | Einführung ohne Programmierung, reine Konfiguration | ja | Referenzen |
| NFA-23 | Anbieter kann innerhalb von 2 Wochen nach Beauftragung mit der Einrichtung starten | ja | schriftliche Zusage |
| NFA-24 | Migrationsunterstützung durch den Anbieter (Importvorlagen, Prüfläufe) | inkludiert oder als Festpreis | Angebot |
| NFA-25 | Schulungsaufwand für das Team | ≤ 2 × 2 Stunden bis zur Arbeitsfähigkeit | Referenzen |
| NFA-26 | Testumgebung/Sandbox vor Go-Live verfügbar | ja | Angebot |

## 6. Vertrag und Kosten

| ID | Anforderung | Zielwert | Nachweis |
| --- | --- | --- | --- |
| NFA-27 | Vertragslaufzeit maximal 12 Monate, danach kündbar | ja | Vertrag |
| NFA-28 | Preismodell transparent (je Einheit/Standort/Transaktion), keine versteckten Modulkosten | ja | Angebot |
| NFA-29 | Preisanpassungsklausel begrenzt (z. B. Indexbindung, Ankündigungsfrist) | ja | Vertrag |
| NFA-30 | Kosten für Zahlungsverkehr transparent ausgewiesen | ja | Angebot |
