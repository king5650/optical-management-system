import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from backend.person_service import PersonService


class EditPersonDialog(QDialog):
    def __init__(self, person_id: int, parent=None):
        super().__init__(parent)

        self.person_id = person_id
        self.setWindowTitle("Edit Person")
        self.setMinimumWidth(420)

        self.build_ui()
        self.load_person_data()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Edit Person")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # NAME
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")
        layout.addWidget(self.name)

        # EMAIL
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        email_regex = QRegularExpression(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        self.email.setValidator(QRegularExpressionValidator(email_regex))
        layout.addWidget(self.email)

        # GROUP
        self.group = QComboBox()
        self.group.addItems(["General", "Students", "Staff", "Administration"])
        layout.addWidget(self.group)

        # BUTTONS
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.update_person)

        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)
        layout.addLayout(btn_row)

    def load_person_data(self):
        """Load data from database into fields."""
        person = PersonService.get_person(self.person_id)

        if not person:
            QMessageBox.critical(self, "Error", "Person not found!")
            self.reject()
            return

        self.name.setText(person["name"])
        self.email.setText(person["email"])
        self.group.setCurrentText(person.get("group_name", "General"))

    def update_person(self):
        """Save updated information to the database."""
        name = self.name.text().strip()
        email = self.email.text().strip()
        group_name = self.group.currentText()

        if not name:
            QMessageBox.warning(self, "Error", "Name is required.")
            return

        if not email:
            QMessageBox.warning(self, "Error", "Email is required.")
            return

        if not PersonService.is_valid_email(email):
            QMessageBox.warning(self, "Error", "Invalid email format.")
            return

        # Ensure email is not duplicated
        if PersonService.email_exists(email, exclude_id=self.person_id):
            QMessageBox.warning(self, "Error", "Email already belongs to another person.")
            return

        try:
            PersonService.update_person(self.person_id, name, email, group_name)
            QMessageBox.information(self, "Success", "Person updated successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return
