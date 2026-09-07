# Labelschema

Vier Ebenen, frei kombinierbar. Die Labels werden einmalig angelegt; danach gilt: keine neuen
Labels ohne Abstimmung, sonst zerfasert die Auswertung.

## Typ – was ist es?

| Label | Farbe | Bedeutung |
| --- | --- | --- |
| `aufgabe` | `#1D76DB` | Konkrete Arbeit mit Ergebnis und Termin |
| `entscheidung` | `#5319E7` | Eine Frage, die entschieden werden muss |
| `risiko` | `#D93F0B` | Gefährdet Termin, Kosten oder Qualität |
| `anbieterfrage` | `#0E8A16` | Frage an Kinnovis, Stora oder Store365 |
| `dokumentation` | `#C2E0C6` | Pflege der Projektdokumente |

## Bereich – worum geht es?

| Label | Farbe |
| --- | --- |
| `bereich:zahlungen` | `#FBCA04` |
| `bereich:buchhaltung` | `#FBCA04` |
| `bereich:migration` | `#FBCA04` |
| `bereich:anforderungen` | `#FBCA04` |
| `bereich:auswahl` | `#FBCA04` |
| `bereich:betrieb` | `#FBCA04` |
| `bereich:kommunikation` | `#FBCA04` |
| `bereich:recht` | `#FBCA04` |

## Steuerung – wie dringend?

| Label | Farbe | Bedeutung |
| --- | --- | --- |
| `kritischer-pfad` | `#B60205` | Verzug verschiebt den Go-Live unmittelbar |
| `blockiert` | `#000000` | Wartet auf eine Zuarbeit – Grund steht im Issue |
| `prio:hoch` | `#E99695` | |
| `prio:mittel` | `#F9D0C4` | |
| `prio:niedrig` | `#FEF2C0` | |

## Anbieter

| Label | Farbe |
| --- | --- |
| `anbieter:kinnovis` | `#BFD4F2` |
| `anbieter:stora` | `#BFD4F2` |
| `anbieter:store365` | `#BFD4F2` |

## Einmalig anlegen

Mit der GitHub-CLI (`gh`) im geklonten Repository:

```bash
gh label create "aufgabe"            --color 1D76DB --description "Konkrete Arbeit mit Ergebnis und Termin"
gh label create "entscheidung"       --color 5319E7 --description "Frage, die entschieden werden muss"
gh label create "risiko"             --color D93F0B --description "Gefaehrdet Termin, Kosten oder Qualitaet"
gh label create "anbieterfrage"      --color 0E8A16 --description "Frage an einen Anbieter"
gh label create "dokumentation"      --color C2E0C6 --description "Pflege der Projektdokumente"
gh label create "bereich:zahlungen"     --color FBCA04
gh label create "bereich:buchhaltung"   --color FBCA04
gh label create "bereich:migration"     --color FBCA04
gh label create "bereich:anforderungen" --color FBCA04
gh label create "bereich:auswahl"       --color FBCA04
gh label create "bereich:betrieb"       --color FBCA04
gh label create "bereich:kommunikation" --color FBCA04
gh label create "bereich:recht"         --color FBCA04
gh label create "kritischer-pfad"    --color B60205 --description "Verzug verschiebt den Go-Live"
gh label create "blockiert"          --color 000000 --description "Wartet auf Zuarbeit"
gh label create "prio:hoch"          --color E99695
gh label create "prio:mittel"        --color F9D0C4
gh label create "prio:niedrig"       --color FEF2C0
gh label create "anbieter:kinnovis"  --color BFD4F2
gh label create "anbieter:stora"     --color BFD4F2
gh label create "anbieter:store365"  --color BFD4F2
```

Alternativ über die Weboberfläche unter **Issues → Labels → New label**.

## Meilensteine anlegen

```bash
gh api repos/:owner/:repo/milestones -f title="M1 Ist-Bild und Projektauftrag"      -f due_on="2026-09-11T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M2 Anforderungen und Anbieteransprache" -f due_on="2026-09-18T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M3 Demos und RZL-Test"                -f due_on="2026-09-25T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M4 Angebote bewertet"                 -f due_on="2026-10-02T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M5 Anbieter beauftragt"               -f due_on="2026-10-09T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M6 Konfiguration und Migrationstest 1" -f due_on="2026-10-16T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M7 Abnahme und Go-/No-Go"             -f due_on="2026-10-23T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M8 Go-Live"                           -f due_on="2026-11-01T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M9 Parallelbetrieb und Abgleich"      -f due_on="2026-12-31T12:00:00Z"
gh api repos/:owner/:repo/milestones -f title="M10 Sundown Zoho und Archivierung"    -f due_on="2027-01-31T12:00:00Z"
```
