# smtp_settings.py
from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QCheckBox,
    QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout,
    QMessageBox
)

from backend.database import get_connection
from backend.mail_service import mail_service


class SMTPSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("SMTP Settings")
        self.setMinimumWidth(420)

        # -----------------------------
        # Widgets
        # -----------------------------
        self.smtp_host = QLineEdit()
        self.smtp_port = QSpinBox()
        self.smtp_port.setRange(1, 99999)
        self.email = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.use_tls = QCheckBox("Enable TLS (Recommended)")
        self.use_ssl = QCheckBox("Enable SSL")

        # Buttons
        self.btnSave = QPushButton("Save Settings")
        self.btnCancel = QPushButton("Cancel")

        # -----------------------------
        # Layouts
        # -----------------------------
        form = QFormLayout()
        form.addRow("SMTP Host:", self.smtp_host)
        form.addRow("SMTP Port:", self.smtp_port)
        form.addRow("Email Address:", self.email)
        form.addRow("Password:", self.password)
        form.addRow(self.use_tls)
        form.addRow(self.use_ssl)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.btnSave)
        btn_layout.addWidget(self.btnCancel)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(form)
        main_layout.addSpacing(10)
        main_layout.addLayout(btn_layout)

        # -----------------------------
        # Load saved settings
        # -----------------------------
        self.load_settings()

        # -----------------------------
        # Signals
        # -----------------------------
        self.use_tls.stateChanged.connect(self.on_tls_toggle)
        self.use_ssl.stateChanged.connect(self.on_ssl_toggle)
        self.btnSave.clicked.connect(self.save_settings)
        self.btnCancel.clicked.connect(self.reject)

    # -------------------------------------------------------------
    # Load SMTP settings from database
    # -------------------------------------------------------------
    def load_settings(self):
        s = mail_service.settings  # Loaded from DB on startup

        self.smtp_host.setText(s["smtp_host"])
        self.smtp_port.setValue(s["smtp_port"])
        self.email.setText(s["email"])
        self.password.setText(s["password"])
        self.use_tls.setChecked(s["use_tls"])
        self.use_ssl.setChecked(s["use_ssl"])

    # -------------------------------------------------------------
    # Auto-switch TLS/SSL ports
    # -------------------------------------------------------------
    def on_tls_toggle(self):
        if self.use_tls.isChecked():
            self.use_ssl.setChecked(False)
            self.smtp_port.setValue(587)

    def on_ssl_toggle(self):
        if self.use_ssl.isChecked():
            self.use_tls.setChecked(False)
            self.smtp_port.setValue(465)

    # -------------------------------------------------------------
    # Save settings back to database
    # -------------------------------------------------------------
    def save_settings(self):
        smtp_host = self.smtp_host.text().strip()
        smtp_port = self.smtp_port.value()
        email = self.email.text().strip()
        password = self.password.text().strip()
        use_tls = self.use_tls.isChecked()
        use_ssl = self.use_ssl.isChecked()

        if not smtp_host or not email or not password:
            QMessageBox.warning(self, "Missing Fields", "All fields are required!")
            return

        conn = get_connection()
        cursor = conn.cursor()

        # clear previous settings
        cursor.execute("DELETE FROM settings")

        # Insert settings into DB
        settings_data = [
            ("smtp_host", smtp_host),
            ("smtp_port", str(smtp_port)),
            ("email", email),
            ("password", password),
            ("use_tls", "1" if use_tls else "0"),
            ("use_ssl", "1" if use_ssl else "0"),
        ]

        cursor.executemany(
            "INSERT INTO settings (key, value) VALUES (?, ?)",
            settings_data
        )

        conn.commit()
        conn.close()

        # Reload settings into mail_service immediately
        mail_service.settings = mail_service.load_settings()

        QMessageBox.information(self, "Saved", "SMTP settings saved successfully.")
        self.accept()
