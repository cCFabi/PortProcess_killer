import sys
from typing import Set
import os

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QIntValidator

import psutil

ICON_PATH = 'portkillericon.png'  # relative oder absolut

class PortKiller(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Port Killer")
        # <- Icon korrekt setzen (falls vorhanden)
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        self.setFixedSize(420, 280)

        # Widgets
        self.label = QLabel("Auf welchem Port soll der Prozess beendet werden?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("z. B. 8080")
        self.port_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.port_input.setMaxLength(5)
        self.port_input.setValidator(QIntValidator(1, 65535, self))  # nur gültige Ports zulassen
        self.port_input.returnPressed.connect(self.on_kill_clicked)   # Enter = Klick

        self.kill_button = QPushButton("Kill")
        self.kill_button.clicked.connect(self.on_kill_clicked)

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        # Layouts
        top = QVBoxLayout()
        top.addWidget(self.label)

        row = QHBoxLayout()
        row.addStretch(1)
        row.addWidget(self.port_input)
        row.addStretch(1)

        btn_row = QHBoxLayout()
        btn_row.addStretch(1)
        btn_row.addWidget(self.kill_button)
        btn_row.addStretch(1)

        top.addLayout(row)
        top.addLayout(btn_row)
        top.addWidget(self.output)

        self.setLayout(top)

    def log(self, text: str) -> None:
        self.output.append(text)
        self.output.verticalScrollBar().setValue(self.output.verticalScrollBar().maximum())

    def on_kill_clicked(self):
        port_text = self.port_input.text().strip()
        if not port_text:
            self.log("Bitte eine Portnummer eingeben.")
            return

        try:
            port = int(port_text)
            if not (1 <= port <= 65535):
                raise ValueError
        except ValueError:
            self.log(f"Ungültiger Port: {port_text}. Gültig sind 1–65535.")
            return

        self.kill_processes_on_port(port)

    def find_listening_pids(self, port: int) -> Set[int]:
        pids = set()
        # Schneller globaler Scan (kann erhöhte Rechte brauchen)
        try:
            for conn in psutil.net_connections(kind='inet'):
                try:
                    if (
                        conn.laddr
                        and getattr(conn.laddr, "port", None) == port
                        and conn.status == psutil.CONN_LISTEN
                        and conn.pid is not None
                    ):
                        pids.add(conn.pid)
                except Exception:
                    continue
        except psutil.AccessDenied:
            # Fallback: pro Prozess iterieren
            for proc in psutil.process_iter(attrs=["pid"]):
                try:
                    for c in proc.connections(kind='inet'):
                        if (
                            c.laddr
                            and getattr(c.laddr, "port", None) == port
                            and c.status == psutil.CONN_LISTEN
                        ):
                            pids.add(proc.pid)
                            break
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    continue
        return pids

    def kill_processes_on_port(self, port: int):
        pids = self.find_listening_pids(port)

        if not pids:
            self.log(f"Kein Prozess gefunden, der auf Port {port} lauscht.")
            return

        self.log(f"Gefundene PID(s) auf Port {port}: {', '.join(map(str, sorted(pids)))}")

        procs = []
        for pid in sorted(pids):
            try:
                proc = psutil.Process(pid)
                name = proc.name()
                try:
                    cmdline = " ".join(proc.cmdline())
                except Exception:
                    cmdline = ""
                self.log(f"Versuche PID {pid} ({name}) ordentlich zu beenden …{f'  [{cmdline}]' if cmdline else ''}")
                proc.terminate()
                procs.append(proc)
            except psutil.NoSuchProcess:
                self.log(f"PID {pid} existiert nicht mehr.")
            except psutil.AccessDenied:
                self.log(f"Zugriff verweigert für PID {pid} – ggf. als Administrator / mit sudo ausführen.")

        if procs:
            gone, alive = psutil.wait_procs(procs, timeout=3)
            for p in alive:
                try:
                    self.log(f"PID {p.pid} reagiert nicht – erzwinge Kill …")
                    p.kill()
                except psutil.NoSuchProcess:
                    pass
                except psutil.AccessDenied:
                    self.log(f"Zugriff verweigert beim Kill von PID {p.pid} – erhöhte Rechte nötig.")

            # Finalstatus
            final = []
            for pid in pids:
                final.append(f"{pid}: {'LEBT NOCH' if psutil.pid_exists(pid) else 'BEENDET'}")
            self.log("Ergebnis: " + ", ".join(final))


def main():
    app = QApplication(sys.argv)
    # Optional: App-weites Icon (falls vorhanden)
    if os.path.exists(ICON_PATH):
        app.setWindowIcon(QIcon(ICON_PATH))
    w = PortKiller()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

