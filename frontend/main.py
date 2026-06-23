"""
main.py — Application entry point

STARTUP FLOW:
  1. Create QApplication
  2. Apply global stylesheet from assets/styles.py
  3. Show LoginWindow
  4. On successful login → open MainWindow with the user's role
  5. On MainWindow close → show LoginWindow again (re-login)
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from assets.styles import APP_STYLE
from windows.login_window import LoginWindow
from windows.main_window  import MainWindow


class App:
    """
    Manages the lifecycle between LoginWindow and MainWindow.

    Why a class instead of plain functions?
    ─────────────────────────────────────────
    We need to hold references to both windows so they don't get
    garbage-collected by Python before Qt is done with them.
    A class keeps those references alive as instance attributes.
    """

    def __init__(self, qt_app: QApplication):
        self.qt_app = qt_app
        self.login_window = None
        self.main_window  = None

    def start(self):
        self._show_login()

    def _show_login(self):
        self.main_window = None   # allow old main window to be GC'd

        self.login_window = LoginWindow()

        # When the user successfully logs in, open the main window
        self.login_window.logged_in.connect(self._on_logged_in)

        self.login_window.show()

    def _on_logged_in(self, role: str):
        """Called when LoginWindow emits its 'logged_in' signal."""
        self.login_window.close()

        self.main_window = MainWindow(role=role)

        # When the user logs out (closes MainWindow), go back to login
        self.main_window.destroyed.connect(self._show_login)

        self.main_window.show()


def main():
    app = QApplication(sys.argv)

    # Global font
    app.setFont(QFont("Segoe UI", 13))

    # Apply stylesheet to every widget in the application
    app.setStyleSheet(APP_STYLE)

    controller = App(app)
    controller.start()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
