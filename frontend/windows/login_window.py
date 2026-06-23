"""
windows/login_window.py — Login screen

CONNECTION FLOW:
  User clicks Login
    → ApiWorker calls api.login(username, password)
    → Django authenticates and sets a session cookie in api.session
    → On success: LoginWindow emits 'logged_in' signal with role string
    → main.py opens MainWindow and closes LoginWindow
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


from api_client import api, ApiError
from assets.styles import PRIMARY, SIDEBAR_BG, CARD_BG, BORDER, TEXT_MUTED
from workers.api_worker import ApiWorker


class LoginWindow(QWidget):
    """
    Standalone login screen.
    Emits 'logged_in(role)' when authentication succeeds so the caller
    (main.py) can open the correct dashboard panel for that role.
    """
    logged_in = Signal(str)   # carries the user's role string

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optical Cabinet — Login")
        self.setFixedSize(420, 520)
        self._worker = None
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Top accent bar ──────────────────────────────────────────────
        accent = QFrame()
        accent.setFixedHeight(6)
        accent.setStyleSheet(f"background-color: {PRIMARY}; border: none;")
        root.addWidget(accent)

        # ── Main content ────────────────────────────────────────────────
        content = QVBoxLayout()
        content.setContentsMargins(48, 40, 48, 40)
        content.setSpacing(0)

        # Logo / title
        logo = QLabel("👁 Optical Cabinet")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        logo.setStyleSheet(f"color: {PRIMARY}; margin-bottom: 6px;")
        content.addWidget(logo)

        subtitle = QLabel("Management System")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px; margin-bottom: 36px;")
        content.addWidget(subtitle)

        # ── Form card ──────────────────────────────────────────────────
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background: {CARD_BG};
                border: 1px solid {BORDER};
                border-radius: 12px;
            }}
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(28, 28, 28, 28)
        card_layout.setSpacing(16)

        card_title = QLabel("Sign in to your account")
        card_title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        card_layout.addWidget(card_title)

        # Username
        card_layout.addWidget(self._field_label("Username"))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setFixedHeight(40)
        card_layout.addWidget(self.username_input)

        # Password
        card_layout.addWidget(self._field_label("Password"))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.returnPressed.connect(self._do_login)
        card_layout.addWidget(self.password_input)

        # Error message (hidden until login fails)
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: #d93025; font-size: 12px;")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setVisible(False)
        card_layout.addWidget(self.error_label)

        # Login button
        self.login_btn = QPushButton("Sign In")
        self.login_btn.setObjectName("primary_btn")
        self.login_btn.setFixedHeight(42)
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.clicked.connect(self._do_login)
        card_layout.addWidget(self.login_btn)

        content.addWidget(card)

        # Footer
        footer = QLabel("© 2025 Optical Cabinet")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px; margin-top: 20px;")
        content.addWidget(footer)

        wrapper = QWidget()
        wrapper.setLayout(content)
        wrapper.setStyleSheet(f"background-color: #f0f2f5;")
        root.addWidget(wrapper)

    def _field_label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setStyleSheet(f"color: #3c4043; font-weight: bold; font-size: 12px; border: none; background: transparent;")
        return lbl

    def _do_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            self._show_error("Please enter username and password")
            return

        self.login_btn.setEnabled(False)
        self.login_btn.setText("Signing in…")
        self.error_label.setVisible(False)

        # Run the API call on a background thread
        self._worker = ApiWorker(api.login, username, password)
        self._worker.success.connect(self._on_login_success)
        self._worker.error.connect(self._on_login_error)
        self._worker.start()

    def _on_login_success(self, data: dict):
        self.login_btn.setEnabled(True)
        self.login_btn.setText("Sign In")

        # data = { "redirect": "admin_dashboard" } or similar
        # We extract the role from the redirect key
        redirect = data.get("redirect", "Home_page")
        role_map = {
            "admin_dashboard":        "admin",
            "Home_page":              "secretary",
            "inventory_management":   "stockist",
            "patient_home":           "patient",
        }
        role = role_map.get(redirect, "secretary")
        self.logged_in.emit(role)

    def _on_login_error(self, message: str):
        self.login_btn.setEnabled(True)
        self.login_btn.setText("Sign In")
        self._show_error(f"Login failed: {message}")

    def _show_error(self, message: str):
        self.error_label.setText(message)
        self.error_label.setVisible(True)
