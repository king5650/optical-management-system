import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
#     QTextEdit, QPushButton, QComboBox, QFrame, QSpacerItem,
#     QSizePolicy, QMessageBox
# )
# from PySide6.QtCore import Qt, Signal
# from PySide6.QtGui import QRegularExpressionValidator
# from PySide6.QtCore import QRegularExpression

# from backend.person_service import PersonService



# class AddPersonDialog(QDialog):
#     person_added = Signal(dict)   # Emitted when Save is pressed

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Add Person")
#         self.setMinimumWidth(420)
#         self.setStyleSheet(self.load_styles())
#         self.build_ui()
#         self.person_service = PersonService()
        

#     def build_ui(self):
#         main_layout = QVBoxLayout(self)
#         main_layout.setSpacing(14)
#         main_layout.setContentsMargins(20, 20, 20, 20)

#         # ------------------------
#         # Title
#         # ------------------------
#         title = QLabel("Add Person")
#         title.setObjectName("dialogTitle")
#         main_layout.addWidget(title)

#         # ------------------------
#         # FORM FIELDS
#         # ------------------------

#         # First Name
#         # self.fname = QLineEdit()
#         # self.fname.setPlaceholderText("First Name")
#         # main_layout.addWidget(self.fname)

#         # Last Name
#         self.name = QLineEdit()
#         self.name.setPlaceholderText("Last Name")
#         main_layout.addWidget(self.name)

#         # Email
#         self.email = QLineEdit()
#         self.email.setPlaceholderText("Email")

#         # Email validation
#         email_regex = QRegularExpression(r"^[\w\.-]+@[\w\.-]+\.\w+$")
#         self.email.setValidator(QRegularExpressionValidator(email_regex))
#         main_layout.addWidget(self.email)

#         # Phone
#         self.phone = QLineEdit()
#         self.phone.setPlaceholderText("Phone (optional)")
#         main_layout.addWidget(self.phone)

#         # Group dropdown
#         self.group = QComboBox()
#         self.group.addItems(["General", "Students", "Staff", "Administration"])
#         self.group.setPlaceholderText("Select Group")
#         main_layout.addWidget(self.group)

#         # Status dropdown
#         self.status = QComboBox()
#         self.status.addItems(["Active", "Inactive"])
#         main_layout.addWidget(self.status)

#         # Notes
#         self.notes = QTextEdit()
#         self.notes.setPlaceholderText("Notes (optional)")
#         self.notes.setFixedHeight(100)
#         main_layout.addWidget(self.notes)

#         # ------------------------
#         # BUTTONS (Cancel / Save)
#         # ------------------------
#         btn_row = QHBoxLayout()
#         btn_row.addStretch()

#         cancel_btn = QPushButton("Cancel")
#         cancel_btn.setObjectName("secondaryBtn")
#         cancel_btn.clicked.connect(self.reject)

#         save_btn = QPushButton("Save")
#         save_btn.setObjectName("primaryBtn")
#         save_btn.clicked.connect(self.save_person)

#         btn_row.addWidget(cancel_btn)
#         btn_row.addWidget(save_btn)

#         main_layout.addLayout(btn_row)

#     # -------------------------
#     # SAVE ACTION
#     # -------------------------
    

#     def save_person(self):
#         data = {
#             "name": self.name.text().strip(),
#             "email": self.email.text().strip(),
#             "phone": self.phone.text().strip(),
#             "group": self.group.currentText(),
#             "status": self.status.currentText(),
#             "notes": self.notes.toPlainText().strip(),
#         }
#         # name = self.name.text().strip()
#         # email = self.email.text().strip()
#         # phone_number = self.phone.text().strip()
#         # group = self.group.currentText()
#         # status = self.status.currentText()
#         # notes = self.notes.toPlainText().strip()

#         # if not name or not email:
#         #     QMessageBox.warning(self, "Missing info", "Name and Email are required.")
#         #     return

#         self.person_service.add_person(data)

#         QMessageBox.information(self, "Success", "Person added successfully.")
#         self.accept()   # Close dialog and return success  
          
#     # def save_person(self):
#     #     if not self.email.hasAcceptableInput():
#     #         self.email.setStyleSheet("border: 1px solid #E02424;")
#     #         return

#     #     data = {
#     #         "first_name": self.fname.text(),
#     #         "last_name": self.lname.text(),
#     #         "email": self.email.text(),
#     #         "phone": self.phone.text(),
#     #         "group": self.group.currentText(),
#     #         "status": self.status.currentText(),
#     #         "notes": self.notes.toPlainText(),
#     #     }

#     #     self.person_added.emit(data)
#     #     self.accept()


from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from backend.person_service import PersonService


class AddPersonDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Person")
        self.setMinimumWidth(420)

        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(14)
        main_layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Add Person")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(title)

        # Name
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")
        main_layout.addWidget(self.name)

        # Email
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        email_regex = QRegularExpression(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        self.email.setValidator(QRegularExpressionValidator(email_regex))

        main_layout.addWidget(self.email)

        # Group
        self.group = QComboBox()
        self.group.addItems(["General", "Students", "Staff", "Administration"])
        main_layout.addWidget(self.group)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_person)

        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)
        main_layout.addLayout(btn_row)

    # -------------------------
    # SAVE LOGIC (FIXED)
    # -------------------------
    def save_person(self):
        name = self.name.text().strip()
        email = self.email.text().strip()
        group_name = self.group.currentText()

        # VALIDATION
        if not name:
            QMessageBox.warning(self, "Error", "Name is required.")
            return

        if not email:
            QMessageBox.warning(self, "Error", "Email is required.")
            return

        if not PersonService.is_valid_email(email):
            QMessageBox.warning(self, "Error", "Invalid email format.")
            return

        if PersonService.email_exists(email):
            QMessageBox.warning(self, "Error", "Email already exists in the system.")
            return

        # INSERT INTO DATABASE
        try:
            PersonService.add_person(name, email, group_name)
            QMessageBox.information(self, "Success", "Person added successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

    # -------------------------
    # QSS Styling
    # -------------------------
    def load_styles(self):
        return """
        QDialog {
            background: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
            border-radius: 12px;
        }

        #dialogTitle {
            font-size: 20px;
            font-weight: 900;
            color: white;
            margin-bottom: 10px;
        }

        QLineEdit, QComboBox, QTextEdit {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            padding: 8px;
            color: black;
        }
        QLineEdit:focus, QComboBox:focus, QTextEdit:focus {
            border: 1px solid #1363DF;
        }

        #primaryBtn {
            background: #1363DF;
            color: white;
            padding: 8px 18px;
            border-radius: 6px;
        }
        #primaryBtn:hover {
            background: #0F52B3;
        }

        #secondaryBtn {
            background: #EEF4FF;
            color: #1363DF;
            padding: 8px 18px;
            border-radius: 6px;
            border: 1px solid rgba(19,99,223,0.12);
        }
        """

