# Port Killer 🧰

> Ein einfaches GUI-Tool, um Prozesse zu beenden, die einen bestimmten Port belegen.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-orange)
![Platform](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-informational)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧩 Übersicht

**Port Killer** ist ein kleines Python-Tool mit grafischer Oberfläche (PyQt6), das den Prozess identifiziert, der auf einem bestimmten Port lauscht, und ihn bei Bedarf beendet.  
Es nutzt dafür die Bibliothek **psutil**, um plattformübergreifend offene Verbindungen und Prozesse zu verwalten.

Ideal, wenn z. B. dein Webserver oder eine Entwicklungsumgebung sagt:  
> “Port already in use”

---

## ⚙️ Voraussetzungen

- **Python 3.10 oder höher**
- **PyQt6** (für die Benutzeroberfläche)
- **psutil** (zum Ermitteln und Beenden von Prozessen)

Installiere die Abhängigkeiten mit:

```bash
pip install -r requirements.txt
```

---

## 🚀 Verwendung

### Start

1. Lade das Repository herunter oder klone es:
   ```bash
   git clone https://github.com/cCFabi/PortProcess_killer.git
   cd PortProcess_killer
   ```
2. Starte das Programm:
   ```bash
   python port_killer.py
   ```
   *(Passe den Dateinamen an, falls deine Datei anders heißt.)*

### GUI-Bedienung

1. Gib eine Portnummer in das Eingabefeld ein (z. B. **8080**).  
2. Klicke auf **Kill** oder drücke **Enter**.  
3. Das Tool zeigt:
   - welche Prozesse auf dem Port lauschen  
   - deren PID, Name und Command Line  
   - ob sie erfolgreich beendet wurden  

---

## 🧠 Funktionsweise

1. Das Tool durchsucht mithilfe von **psutil.net_connections()** alle aktiven Internet-Verbindungen.
2. Es filtert Prozesse, die auf dem angegebenen Port lauschen (`CONN_LISTEN`).
3. Falls Prozesse gefunden werden:
   - wird zunächst versucht, sie **freundlich zu beenden** (`terminate()`),
   - falls nötig, wird der **Kill-Befehl** ausgeführt (`kill()`).
4. Das Ergebnis wird direkt im Textfeld angezeigt.

---

## ⚠️ Hinweise

- Manche Prozesse können nur mit **Administrator-/Root-Rechten** beendet werden.
- Systemprozesse oder Dienste bitte **nicht unbedacht** killen.
- Auf Windows kann das Tool ggf. UAC-Berechtigungen erfordern.

---

## 🧪 Entwicklung

### Lokales Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# oder
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### Tests & Codequalität (optional)

```bash
pip install pytest ruff
ruff check .
pytest
```

---

## 📦 Struktur

```
PortProcess_killer/
│
├── port_killer.py          # Hauptprogramm (PyQt6-GUI)
├── requirements.txt        # Abhängigkeiten
├── README.md               # Diese Datei
└── portkillericon.png      # (Optional) Programm-Icon
```

---


> 💡 *Ein kleines, aber nützliches Tool für alle, die öfter mal “Port already in use” sehen.*
