# PortProcess_killer

> Identifiziert den Prozess, der einen angegebenen Port belegt, und beendet ihn auf Wunsch.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/OS-Windows%20%7C%20macOS%20%7C%20Linux-informational)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Inhalt
- [Überblick](#überblick)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Sicherheit & Hinweise](#sicherheit--hinweise)
- [Entwicklung](#entwicklung)

---

## Überblick

**PortProcess_killer** hilft dir, nervige „Port already in use“-Situationen schnell zu lösen: Gib eine Portnummer an, das Tool findet den zugehörigen Prozess (PID), zeigt Details an und kann ihn kontrolliert beenden. Das Repository ist in **Python** umgesetzt.

## Voraussetzungen

- **Python 3.8+**
- Je nach Plattform werden systemeigene Tools angesprochen:
  - **Linux/macOS:** `lsof` oder `ss`
  - **Windows:** `netstat`
- (Optional) **Administrator-/Root-Rechte**, um bestimmte Prozesse beenden zu können


## Installation

```bash
- Repository klonen
git clone https://github.com/cCFabi/PortProcess_killer.git
cd PortProcess_killer

```

> Die genaue Skriptdatei kann je nach Struktur `port_killer.py`, `main.py` o.ä. heißen. Passe den Pfad einfach an, falls dein Dateiname anders lautet.

## Sicherheit & Hinweise

- **Admin-/Root-Rechte:** Manche Prozesse (v. a. von anderen Benutzern oder Systemdienste) lassen sich nur mit erhöhten Rechten beenden.
- **Vorsicht beim Killen:** Achte darauf, keine Datenbanken, IDEs oder produktive Services ungewollt zu beenden.
- **Port-Freigabe ≠ Fehlerbehebung:** Wenn ein Prozess den Port belegt, hat das oft einen Grund. Prüfe Logs, bevor du killst.

## Entwicklung

Beiträge willkommen! Vorschläge:

- ✅ Einheitliche, plattformübergreifende Prozess-Ermittlung (Windows/macOS/Linux)
- ✅ „Dry-Run“-Modus
- ⏩ Optionale Python-API (als Funktion nutzbar, nicht nur CLI)
- ⏩ Tests (Mocking von Systembefehlen)
- ⏩ GitHub Actions für Linting/Tests
